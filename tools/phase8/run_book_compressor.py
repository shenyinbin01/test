#!/usr/bin/env python3
"""
run_book_compressor.py — 批处理生成 chapter_card

用法:
    # 小批量测试
    python tools/phase8/run_book_compressor.py --book-id dachengqi --start 1 --end 5 --real
    
    # 全量运行
    python tools/phase8/run_book_compressor.py --book-id dachengqi --real --resume
    
    # 仅重试失败
    python tools/phase8/run_book_compressor.py --book-id dachengqi --real --retry-failed

依赖:
    - scripts/call_deepseek.py (真实 API 或 mock)
    - production/phase8/prompts/book_compressor.prompt.md
    - production/phase8/templates/chapter_card.template.yaml
"""

import os, sys, yaml, json, time, subprocess, shutil
from pathlib import Path
from datetime import datetime

# 自动注入 project root
_THIS_FILE = Path(__file__).resolve()
for _p in [_THIS_FILE.parent.parent.parent, *_THIS_FILE.parents]:
    if (_p / "tools" / "phase8").exists():
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))
        break

from tools.phase8.common import resolve_project_root


def build_user_prompt(chapter_text: str, chapter_num: int, ch_title: str) -> str:
    """构造 LLM user prompt：模板 + 章节正文"""
    lines = [
        f"## 章节信息",
        f"- 章节号: {chapter_num}",
        f"- 标题: {ch_title}",
        f"",
        f"## chapter_card 模板",
        f"请按照以下 YAML 模板结构输出，严格 YAML，不带解释：",
    ]
    return "\n".join(lines)


def call_llm(system_prompt: str, user_content: str, output_path: Path,
             task_name: str, project_root: Path, real: bool = False,
             log_path: Path = None, max_tokens: int = 4000, timeout: int = 120) -> dict:
    """调用 DeepSeek，返回结果字典"""
    
    # 写临时输入文件
    tmp_input = output_path.parent / f"{output_path.stem}_input.txt"
    full_user = system_prompt + "\n\n" + user_content
    tmp_input.write_text(full_user, encoding="utf-8")

    cmd = [
        sys.executable,
        str(project_root / "scripts" / "call_deepseek.py"),
        "--input", str(tmp_input),
        "--output", str(output_path),
        "--task-name", task_name,
        "--max-tokens", str(max_tokens),
        "--timeout", str(timeout),
        "--retries", "1",
    ]
    if real:
        cmd.append("--real")
    else:
        cmd.append("--mock")
    if log_path:
        cmd.extend(["--log", str(log_path)])
        log_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 30, cwd=str(project_root))
        if result.returncode == 0:
            return {"success": True, "output": str(output_path)}
        else:
            return {"success": False, "error": result.stderr[:500] if result.stderr else "unknown"}
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def validate_yaml_card(card_path: Path) -> dict:
    """校验 chapter_card YAML 格式"""
    result = {"valid": False, "errors": [], "data": None}
    if not card_path.exists():
        result["errors"].append("文件不存在")
        return result

    text = card_path.read_text(encoding="utf-8")
    
    # 尝试提取 YAML（LLM 可能在前后包裹了其他文本）
    yaml_text = text
    if "```yaml" in text:
        parts = text.split("```yaml", 1)
        if len(parts) > 1:
            inner = parts[1].split("```", 1)
            yaml_text = inner[0] if inner else text
    elif "```" in text:
        parts = text.split("```", 1)
        if len(parts) > 1:
            inner = parts[1].split("```", 1)
            yaml_text = inner[0] if inner else text

    try:
        data = yaml.safe_load(yaml_text)
        if not isinstance(data, dict):
            result["errors"].append("YAML 解析结果不是 dict")
            return result
        result["data"] = data
        result["valid"] = True
        
        # 必填字段检查
        required = ["book_id", "chapter_number", "title", "one_sentence", 
                    "chapter_function", "main_events", "characters_present", "confidence"]
        for field in required:
            if field not in data:
                result["errors"].append(f"缺必填字段: {field}")
                result["valid"] = False
        
        # evidence check
        evidence = data.get("evidence", [])
        if not evidence:
            result["errors"].append("evidence 为空")
        
        # confidence check
        if data.get("confidence", "") not in ("high", "medium", "low"):
            result["errors"].append(f"confidence 值异常: {data.get('confidence')}")

    except yaml.YAMLError as e:
        result["errors"].append(f"YAML 解析失败: {e}")
    
    return result


def load_status(status_path: Path, book_id: str, total: int) -> dict:
    """加载或初始化状态文件"""
    if status_path.exists():
        status = yaml.safe_load(status_path.read_text()) or {}
        # 确保所有章节都有条目
        chapters = status.get("chapters", [])
        existing = {c["chapter_number"] for c in chapters}
        for cn in range(1, total + 1):
            if cn not in existing:
                chapters.append({
                    "chapter_number": cn,
                    "source_file": f"chapters/chapter_{cn:04d}.md",
                    "output_file": f"chapter_cards/chapter_{cn:04d}.yaml",
                    "status": "pending",
                    "attempts": 0,
                    "last_error": "",
                    "confidence": "unknown",
                    "evidence_count": 0,
                })
        chapters.sort(key=lambda x: x["chapter_number"])
        status["chapters"] = chapters
        status["book_id"] = book_id
        status["total_chapters"] = total
        return status
    
    return {
        "book_id": book_id,
        "total_chapters": total,
        "completed": 0,
        "failed": 0,
        "skipped_existing": 0,
        "last_updated": "",
        "chapters": [
            {
                "chapter_number": cn,
                "source_file": f"chapters/chapter_{cn:04d}.md",
                "output_file": f"chapter_cards/chapter_{cn:04d}.yaml",
                "status": "pending",
                "attempts": 0,
                "last_error": "",
                "confidence": "unknown",
                "evidence_count": 0,
            }
            for cn in range(1, total + 1)
        ],
    }


def save_status(status: dict, status_path: Path):
    status["last_updated"] = datetime.now().isoformat()
    # 更新统计
    chapters = status["chapters"]
    status["completed"] = sum(1 for c in chapters if c["status"] == "completed")
    status["failed"] = sum(1 for c in chapters if c["status"] == "failed")
    status["skipped_existing"] = sum(1 for c in chapters if c["status"] == "skipped")
    status_path.write_text(yaml.dump(status, allow_unicode=True, default_flow_style=False, sort_keys=False))


def main():
    import argparse
    parser = argparse.ArgumentParser(description="批处理生成 chapter_card")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None, help="项目根目录，默认自动查找")
    parser.add_argument("--start", type=int, default=None, help="起始章节号（含）")
    parser.add_argument("--end", type=int, default=None, help="结束章节号（含）")
    parser.add_argument("--real", action="store_true", help="使用真实 API（否则 mock）")
    parser.add_argument("--resume", action="store_true", help="跳过已完成章节")
    parser.add_argument("--force", action="store_true", help="强制覆盖已完成章节")
    parser.add_argument("--retry-failed", action="store_true", help="仅重试失败章节")
    parser.add_argument("--batch-size", type=int, default=20, help="每批章节数")
    parser.add_argument("--batch-delay", type=int, default=5, help="批次间延迟秒数")
    parser.add_argument("--max-tokens", type=int, default=4000, help="每章最大 token")
    parser.add_argument("--timeout", type=int, default=120, help="单章超时秒数")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"
    book_id = args.book_id
    corpus = phase8 / "corpus" / book_id
    audit_dir = phase8 / "audit" / book_id
    cards_dir = corpus / "chapter_cards"
    cards_dir.mkdir(exist_ok=True)
    audit_dir.mkdir(parents=True, exist_ok=True)

    # 读取 manifest
    manifest = yaml.safe_load((corpus / "manifest.yaml").read_text()) or {}
    total = manifest.get("chapter_count", 0)
    if total == 0:
        print("❌ manifest chapter_count = 0")
        sys.exit(1)

    # 读取 prompt
    prompt_path = phase8 / "prompts" / "book_compressor.prompt.md"
    if not prompt_path.exists():
        print(f"❌ Prompt 不存在: {prompt_path}")
        sys.exit(1)
    compressor_prompt = prompt_path.read_text(encoding="utf-8")

    # 读取 template
    template_path = phase8 / "templates" / "chapter_card.template.yaml"
    if not template_path.exists():
        print(f"❌ Template 不存在: {template_path}")
        sys.exit(1)
    card_template = template_path.read_text(encoding="utf-8")

    # 状态文件
    status_path = corpus / "compressor_status.yaml"
    status = load_status(status_path, book_id, total)

    # 确定处理范围
    if args.retry_failed:
        target_chapters = [
            c for c in status["chapters"]
            if c["status"] == "failed"
        ]
    elif args.start and args.end:
        target_chapters = [
            c for c in status["chapters"]
            if args.start <= c["chapter_number"] <= args.end
        ]
    else:
        target_chapters = list(status["chapters"])

    # 过滤已完成的（resume 模式）
    if args.resume and not args.force:
        target_chapters = [
            c for c in target_chapters
            if c["status"] not in ("completed", "skipped")
        ]

    if not target_chapters:
        print("✅ 没有需要处理的章节")
        return 0

    log_path = audit_dir / "compressor_log.jsonl"

    print(f"{'='*60}")
    print(f"  Book Compressor: {book_id}")
    print(f"  总章节: {total} | 本次处理: {len(target_chapters)}")
    print(f"  模式: {'REAL' if args.real else 'MOCK'}")
    print(f"  已完成: {status['completed']} | 失败: {status['failed']}")
    print(f"{'='*60}\n")

    success_count = 0
    fail_count = 0

    for i, ch_entry in enumerate(target_chapters):
        cn = ch_entry["chapter_number"]
        src_file = corpus / ch_entry["source_file"]
        out_file = cards_dir / f"chapter_{cn:04d}.yaml"

        # 如果已存在且校验通过且非 --force，跳过
        if out_file.exists() and not args.force:
            vr = validate_yaml_card(out_file)
            if vr["valid"]:
                ch_entry["status"] = "completed"
                ch_entry["confidence"] = vr["data"].get("confidence", "unknown") if vr["data"] else "unknown"
                ch_entry["evidence_count"] = len(vr["data"].get("evidence", [])) if vr["data"] else 0
                continue

        if not src_file.exists():
            ch_entry["status"] = "failed"
            ch_entry["last_error"] = f"源文件不存在: {src_file}"
            fail_count += 1
            continue

        chapter_text = src_file.read_text(encoding="utf-8")
        ch_title = manifest.get("chapter_index", [{}])[cn-1].get("title", f"第{cn}章") if cn <= len(manifest.get("chapter_index", [])) else f"第{cn}章"

        # 构造 user prompt
        user_prompt = f"""## 模板
{card_template}

## 章节正文
{chapter_text}

请输出 chapter_card YAML。只输出 YAML，不带任何解释。"""
        
        task_name = f"book_compressor_{book_id}_ch{cn:04d}"

        if i % 20 == 0:
            print(f"  [{i+1}/{len(target_chapters)}] 处理 ch{cn:04d}...")

        ch_entry["attempts"] += 1
        result = call_llm(
            system_prompt=compressor_prompt,
            user_content=user_prompt,
            output_path=out_file,
            task_name=task_name,
            project_root=project_root,
            real=args.real,
            log_path=log_path,
            max_tokens=args.max_tokens,
            timeout=args.timeout,
        )

        if result["success"]:
            # 校验输出
            vr = validate_yaml_card(out_file)
            if vr["valid"]:
                ch_entry["status"] = "completed"
                ch_entry["confidence"] = vr["data"].get("confidence", "unknown") if vr["data"] else "unknown"
                ch_entry["evidence_count"] = len(vr["data"].get("evidence", [])) if vr["data"] else 0
                ch_entry["last_error"] = ""
                success_count += 1
            else:
                ch_entry["status"] = "failed"
                ch_entry["last_error"] = "; ".join(vr["errors"])
                fail_count += 1
        else:
            ch_entry["status"] = "failed"
            ch_entry["last_error"] = result.get("error", "unknown")
            fail_count += 1

        # 每 10 章保存状态
        if (i + 1) % 10 == 0:
            save_status(status, status_path)
            print(f"  [{i+1}/{len(target_chapters)}] 进度: {success_count} 成功, {fail_count} 失败")

        # 批次间延迟
        if args.batch_delay > 0 and (i + 1) % args.batch_size == 0:
            time.sleep(args.batch_delay)

    # 最终保存
    save_status(status, status_path)

    print(f"\n{'='*60}")
    print(f"  完成！成功: {success_count} | 失败: {fail_count}")
    print(f"  status: {status_path}")
    print(f"{'='*60}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
