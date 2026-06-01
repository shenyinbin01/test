#!/usr/bin/env python3
"""
run_book_architect.py — Phase 8 Step 3: Book Architect 全书故事工程资产反推

用法:
    python tools/phase8/run_book_architect.py --book-id dachengqi --real

策略:
    1. 读取 774 张 chapter_card，做机械聚合（字符统计、频率、模式）
    2. 将聚合数据 + prompt 传给 DeepSeek
    3. 逐个生成 5 个核心交付物
"""

import os, sys, yaml, json, time, subprocess
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict

_THIS_FILE = Path(__file__).resolve()
for _p in [_THIS_FILE.parent.parent.parent, *_THIS_FILE.parents]:
    if (_p / "tools" / "phase8").exists():
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))
        break

from tools.phase8.common import resolve_project_root


def _extract_yaml(text: str) -> str:
    if "```yaml" in text:
        parts = text.split("```yaml", 1)
        inner = parts[1].split("```", 1)
        return inner[0] if inner else text
    if "```" in text:
        parts = text.split("```", 1)
        inner = parts[1].split("```", 1)
        return inner[0] if inner else text
    return text


def load_all_cards(cards_dir: Path, total: int) -> list:
    """加载全部 chapter_card"""
    cards = []
    for cn in range(1, total + 1):
        fpath = cards_dir / f"chapter_{cn:04d}.yaml"
        if not fpath.exists():
            cards.append({"chapter_number": cn, "_missing": True})
            continue
        try:
            data = yaml.safe_load(_extract_yaml(fpath.read_text()))
            if not isinstance(data, dict):
                data = {"chapter_number": cn, "_parse_error": "not_dict"}
        except Exception as e:
            data = {"chapter_number": cn, "_parse_error": str(e)[:100]}
        cards.append(data)
    return cards


def aggregate_stats(cards: list) -> dict:
    """机械聚合：统计、频率、模式（不进 LLM）"""
    total = len(cards)

    # chapter_function 分布
    func_counter = Counter()
    conf_counter = Counter()
    chars_counter = Counter()
    all_hooks = []
    all_debts = []
    char_appearances = defaultdict(list)  # char_name -> [chapter_numbers]

    for card in cards:
        if card.get("_missing") or card.get("_parse_error"):
            continue
        cn = card.get("chapter_number", 0)
        func_counter[card.get("chapter_function", "unknown")] += 1
        conf_counter[card.get("confidence", "unknown")] += 1

        chars = card.get("characters_present", [])
        for c in chars:
            if isinstance(c, dict):
                name = c.get("name", "")
            elif isinstance(c, str):
                name = c
            else:
                continue
            chars_counter[name] += 1
            char_appearances[name].append(cn)

        # hooks
        for h in card.get("hook_opened", []):
            all_hooks.append({"chapter": cn, "data": h, "type": "opened"})
        for h in card.get("hook_paid", []):
            all_hooks.append({"chapter": cn, "data": h, "type": "paid"})

        for d in card.get("reader_debts_opened", []):
            all_debts.append({"chapter": cn, "data": d, "type": "opened"})
        for d in card.get("reader_debts_paid", []):
            all_debts.append({"chapter": cn, "data": d, "type": "paid"})

    # 角色出现频率排序
    top_chars = chars_counter.most_common(40)

    # hook/debt 统计
    hooks_opened = [h for h in all_hooks if h["type"] == "opened"]
    hooks_paid = [h for h in all_hooks if h["type"] == "paid"]
    debts_opened = [d for d in all_debts if d["type"] == "opened"]
    debts_paid = [d for d in all_debts if d["type"] == "paid"]

    # 章节区间取样（头/中/尾）
    sample_chapters = []
    ranges = [(1, 20), (total//3-10, total//3+10), (total*2//3-10, total*2//3+10), (total-20, total)]
    for start, end in ranges:
        start, end = max(1, start), min(total, end)
        for card in cards:
            cn = card.get("chapter_number", 0)
            if start <= cn <= end and not card.get("_missing") and not card.get("_parse_error"):
                sample_chapters.append({
                    "chapter_number": cn,
                    "title": card.get("title", ""),
                    "one_sentence": card.get("one_sentence", ""),
                    "chapter_function": card.get("chapter_function", ""),
                    "main_events": card.get("main_events", [])[:3],
                    "ending_pull": str(card.get("ending_pull", ""))[:80],
                })

    return {
        "total_chapters": total,
        "chapter_function_distribution": dict(func_counter.most_common()),
        "confidence_distribution": dict(conf_counter),
        "top_characters": [{"name": name, "appearances": cnt, "chapters": char_appearances[name][:5] + ["..."] + char_appearances[name][-5:]}
                          for name, cnt in top_chars],
        "hooks_opened_count": len(hooks_opened),
        "hooks_paid_count": len(hooks_paid),
        "debts_opened_count": len(debts_opened),
        "debts_paid_count": len(debts_paid),
        "sample_chapters": sample_chapters,
        # 关键 hook/debt 取样（每100章取一个）
        "sampled_hooks": [{"chapter": h["chapter"], "data": str(h["data"])[:100]}
                         for h in hooks_opened[::50]][:20],
        "sampled_debts": [{"chapter": d["chapter"], "data": str(d["data"])[:100]}
                         for d in debts_opened[::50]][:20],
    }


def call_llm(system_prompt: str, user_content: str, output_path: Path,
             task_name: str, project_root: Path, real: bool = False,
             max_tokens: int = 8000, timeout: int = 300) -> dict:
    """调用 DeepSeek"""
    tmp_input = output_path.parent / f"{output_path.stem}_input.txt"
    tmp_input.write_text(user_content, encoding="utf-8")

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

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 60, cwd=str(project_root))
        if result.returncode == 0:
            return {"success": True}
        return {"success": False, "error": result.stderr[:300]}
    except subprocess.TimeoutExpired:
        return {"success": False, "error": "timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)[:300]}


def generate_bible(stats: dict, prompt: str, output_dir: Path, project_root: Path, real: bool) -> dict:
    """生成 reverse_story_bible.md"""
    # 构建角色表
    chars_table = ""
    for c in stats["top_characters"][:30]:
        chars_table += f"- {c['name']}: 出场 {c['appearances']} 次\n"

    user = f"""## 聚合数据

全书 774 章已全部完成 chapter_card 压缩。

### 章节功能分布
{json.dumps(stats['chapter_function_distribution'], ensure_ascii=False, indent=2)}

### 置信度分布
{json.dumps(stats['confidence_distribution'], ensure_ascii=False, indent=2)}

### 主要角色出场频率（Top 30）
{chars_table}

### 取样章节（头/1/3/2/3/尾）
{json.dumps(stats['sample_chapters'], ensure_ascii=False, indent=2)}

### Hook 取样
{json.dumps(stats['sampled_hooks'], ensure_ascii=False, indent=2)}

### Debt 取样
{json.dumps(stats['sampled_debts'], ensure_ascii=False, indent=2)}

{mermaid_diagram_placeholder}

请基于以上聚合数据生成 reverse_story_bible.md。每个核心判断必须附带 supporting_chapters、evidence_refs、confidence。
输出必须是 Markdown，严格使用模板格式（见 templates/reverse_story_bible.template.md）。
不要编造数据，不确定的地方标 unknown 或 low confidence。
"""
    output_path = output_dir / "reverse_story_bible.md"
    return call_llm(prompt, user, output_path, "book_architect_bible", project_root, real, max_tokens=8000, timeout=300)


def generate_characters(stats: dict, prompt: str, output_dir: Path, project_root: Path, real: bool) -> dict:
    """生成 character_cards/"""
    char_dir = output_dir / "character_cards"
    char_dir.mkdir(parents=True, exist_ok=True)

    # 取 Top 15 角色
    top_chars = stats["top_characters"][:15]
    
    results = []
    for c in top_chars:
        name = c["name"]
        chapters_data = c.get("chapters", [])
        first_ch = chapters_data[0] if chapters_data else "?"
        last_ch = chapters_data[-1] if chapters_data else "?"

        user = f"""## 角色信息
- 角色名: {name}
- 出场次数: {c['appearances']}
- 首次出场: 第 {first_ch} 章
- 最后出场: 第 {last_ch} 章

基于以上信息，生成 character_card。包含：
- 故事功能（压力源/资源入口/价值观对照/阶段反派/情感牵引）
- 与主角关系变化
- 核心欲望、关键行为、转折点
- 声口特征、最终状态
- 证据索引、低置信度判断

输出严格 Markdown，不要 YAML wrapping。
"""
        safe_name = name.replace("/", "_").replace(" ", "_")[:50]
        output_path = char_dir / f"{safe_name}.md"
        r = call_llm(prompt, user, output_path,
                     f"book_architect_character_{safe_name[:20]}",
                     project_root, real, max_tokens=2000, timeout=180)
        r["character"] = name
        results.append(r)
    
    return {"success": all(r["success"] for r in results), "results": results}


def generate_volume_structure(stats: dict, prompt: str, output_dir: Path, project_root: Path, real: bool) -> dict:
    """生成 volume_structure_report.md"""
    user = f"""## 聚合数据

全书 {stats['total_chapters']} 章。

### 章节功能分布
{json.dumps(stats['chapter_function_distribution'], ensure_ascii=False, indent=2)}

### 取样章节（分四段取样）
{json.dumps(stats['sample_chapters'][:30], ensure_ascii=False, indent=2)}

请基于以上数据，按照 模板（templates/volume_structure_report.template.md）生成 volume_structure_report.md。
核心要求：
- 不能只按固定 100 章切段
- 必须基于主线目标、敌人升级、地图/圈层变化、能力变化、读者债变化来分
- 每阶段包含：章范围、主角目标、主要压力源、核心爽点、高潮、阶段末尾获得
- 标记 low/unknown 判断
"""
    output_path = output_dir / "volume_structure_report.md"
    return call_llm(prompt, user, output_path, "book_architect_volume", project_root, real, max_tokens=8000, timeout=300)


def generate_debt_lifecycle(stats: dict, prompt: str, output_dir: Path, project_root: Path, real: bool) -> dict:
    """生成 reader_debt_lifecycle.md"""
    user = f"""## 聚合数据

全书 {stats['total_chapters']} 章。
总债务开启: {stats['debts_opened_count']}
总债务兑现: {stats['debts_paid_count']}

### Debt 取样（每 50 章取 1 个）
{json.dumps(stats['sampled_debts'], ensure_ascii=False, indent=2)}

### 取样章节
{json.dumps(stats['sample_chapters'][:20], ensure_ascii=False, indent=2)}

请生成 reader_debt_lifecycle.md。追踪主要读者债：
- 长期主线问题、能力边界、身份承诺、爽点承诺、情感承诺、反派压迫、伏笔
- 每条债：debt_id、debt_type、opened_in_chapter、promise、paid_in_chapter、payoff_type、confidence
- legacy debts 保留但标记 legacy_source: true
"""
    output_path = output_dir / "reader_debt_lifecycle.md"
    return call_llm(prompt, user, output_path, "book_architect_debts", project_root, real, max_tokens=8000, timeout=300)


def generate_hook_map(stats: dict, prompt: str, output_dir: Path, project_root: Path, real: bool) -> dict:
    """生成 hook_payoff_map.md"""
    user = f"""## 聚合数据

全书 {stats['total_chapters']} 章。
总钩子开启: {stats['hooks_opened_count']}
总钩子兑现: {stats['hooks_paid_count']}

### Hook 取样（每 50 章取 1 个）
{json.dumps(stats['sampled_hooks'], ensure_ascii=False, indent=2)}

### 章节功能分布
{json.dumps(stats['chapter_function_distribution'], ensure_ascii=False, indent=2)}

请生成 hook_payoff_map.md。优先提取对追读有持续贡献的关键 hook：
- hook_id、opened_in_chapter、hook_text、paid_in_chapter、payoff_text
- status: opened/escalated/paid/unresolved
- 不要把每章所有疑问都列入
"""
    output_path = output_dir / "hook_payoff_map.md"
    return call_llm(prompt, user, output_path, "book_architect_hooks", project_root, real, max_tokens=8000, timeout=300)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Book Architect — 全书故事工程资产反推")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--real", action="store_true", help="使用真实 API")
    parser.add_argument("--skip-bible", action="store_true")
    parser.add_argument("--skip-characters", action="store_true")
    parser.add_argument("--skip-volume", action="store_true")
    parser.add_argument("--skip-debts", action="store_true")
    parser.add_argument("--skip-hooks", action="store_true")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"
    book_id = args.book_id
    cards_dir = phase8 / "corpus" / book_id / "chapter_cards"
    output_dir = phase8 / "reverse_assets" / book_id
    output_dir.mkdir(parents=True, exist_ok=True)

    # 读取 manifest
    manifest_path = phase8 / "corpus" / book_id / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    total = manifest.get("chapter_count", 0)

    # 读取 prompt
    prompt_path = phase8 / "prompts" / "book_architect.prompt.md"
    architect_prompt = prompt_path.read_text(encoding="utf-8")

    print(f"{'='*60}")
    print(f"  Book Architect: {book_id} ({total} chapters)")
    print(f"  Mode: {'REAL' if args.real else 'MOCK'}")
    print(f"{'='*60}")

    # 步骤 1: 加载全量 cards + 聚合
    print("\n[1/7] Loading and aggregating {total} chapter cards...")
    cards = load_all_cards(cards_dir, total)
    stats = aggregate_stats(cards)
    print(f"  Aggregated: {len(stats['top_characters'])} chars, {stats['hooks_opened_count']} hooks, {stats['debts_opened_count']} debts")

    results = {}

    # 步骤 2: reverse_story_bible
    if not args.skip_bible:
        print("\n[2/7] Generating reverse_story_bible.md...")
        results["bible"] = generate_bible(stats, architect_prompt, output_dir, project_root, args.real)
        print(f"  {'✅' if results['bible']['success'] else '❌'} reverse_story_bible.md")
    else:
        results["bible"] = {"success": True, "skipped": True}

    # 步骤 3: character_cards
    if not args.skip_characters:
        print("\n[3/7] Generating character_cards/...")
        results["characters"] = generate_characters(stats, architect_prompt, output_dir, project_root, args.real)
        if isinstance(results["characters"], dict) and "results" in results["characters"]:
            ok = sum(1 for r in results["characters"]["results"] if r.get("success"))
            total_chars = len(results["characters"]["results"])
            print(f"  {ok}/{total_chars} character cards generated")
        else:
            print(f"  {'✅' if results['characters'].get('success') else '❌'}")
    else:
        results["characters"] = {"success": True, "skipped": True}

    # 步骤 4: volume_structure_report
    if not args.skip_volume:
        print("\n[4/7] Generating volume_structure_report.md...")
        results["volume"] = generate_volume_structure(stats, architect_prompt, output_dir, project_root, args.real)
        print(f"  {'✅' if results['volume']['success'] else '❌'} volume_structure_report.md")
    else:
        results["volume"] = {"success": True, "skipped": True}

    # 步骤 5: reader_debt_lifecycle
    if not args.skip_debts:
        print("\n[5/7] Generating reader_debt_lifecycle.md...")
        results["debts"] = generate_debt_lifecycle(stats, architect_prompt, output_dir, project_root, args.real)
        print(f"  {'✅' if results['debts']['success'] else '❌'} reader_debt_lifecycle.md")
    else:
        results["debts"] = {"success": True, "skipped": True}

    # 步骤 6: hook_payoff_map
    if not args.skip_hooks:
        print("\n[6/7] Generating hook_payoff_map.md...")
        results["hooks"] = generate_hook_map(stats, architect_prompt, output_dir, project_root, args.real)
        print(f"  {'✅' if results['hooks']['success'] else '❌'} hook_payoff_map.md")
    else:
        results["hooks"] = {"success": True, "skipped": True}

    # 步骤 7: summary
    print(f"\n[7/7] Generating summary...")
    summary_lines = [
        f"# Book Architect Summary: {book_id}",
        f"> Generated: {datetime.now().isoformat()}",
        f"",
        f"## Deliverables",
        f"| File | Status |",
        f"|------|--------|",
        f"| reverse_story_bible.md | {'✅' if results.get('bible',{}).get('success') else '❌'} |",
        f"| character_cards/ | {'✅' if results.get('characters',{}).get('success') else '❌'} |",
        f"| volume_structure_report.md | {'✅' if results.get('volume',{}).get('success') else '❌'} |",
        f"| reader_debt_lifecycle.md | {'✅' if results.get('debts',{}).get('success') else '❌'} |",
        f"| hook_payoff_map.md | {'✅' if results.get('hooks',{}).get('success') else '❌'} |",
    ]
    (output_dir / "book_architect_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    all_ok = all(r.get("success") for r in results.values())
    print(f"\n{'='*60}")
    print(f"  {'✅ ALL DELIVERABLES READY' if all_ok else '⚠️ SOME FAILED'}")
    print(f"{'='*60}")

    return 0 if all_ok else 1


mermaid_diagram_placeholder = """
请利用以上数据生成一份完整的故事工程分析文档，不要省略。
注意：这 774 章基于 data，不是虚构。所有结论必须有 evidence 支撑。
"""


if __name__ == "__main__":
    sys.exit(main())
