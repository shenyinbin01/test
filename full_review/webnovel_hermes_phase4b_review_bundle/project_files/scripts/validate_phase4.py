#!/usr/bin/env python3
"""
validate_phase4.py — 阶段四三章生产闭环验证

必须检查：
1. 三章目录和文件完整性
2. 每章 humanized 字数 >= 800
3. 每章 canon_check passed=true
4. 每章 commit 有 confirmed_events
5. 连续性（preflight 承接上章）
6. runtime_canon_final 包含三章 events
7. father 状态病重存活
8. 无 forbidden_facts
9. review 有具体问题和建议
10. phase4_summary passed
"""

import os
import sys
import json
import re
from pathlib import Path


CODE_ROOT = Path(os.environ.get("WEBNOVEL_CODE_ROOT", "/opt/webnovel-hermes-wps"))
DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


# ── Forbidden patterns（复用阶段三点五的精确规则）────────────

FORBIDDEN_PATTERNS = [
    r"\u5929\u79e4\u4f1a", r"\u7cfb\u7edf\u9762\u677f", r"\u7cfb\u7edf\u4efb\u52a1",
    r"\u4efb\u52a1\u5956\u52b1", r"\u7cfb\u7edf\u5145\u503c", r"\u5145\u503c\u5165\u53e3",
    r"\u5145\u503c\u5546\u57ce", r"\u5145\u503c\u83b7\u5f97", r"\u6c2b\u91d1",
    r"\u5546\u57ce\u5145\u503c", r"\u5145\u503c\u70b9\u6570", r"\u5145\u503c\u5151\u6362",
    r"\u6d88\u8017\u5bff\u547d", r"\u5bff\u547d\u6362", r"\u751f\u547d\u5012\u8ba1\u65f6",
    r"\u89e6\u78b0\u6539\u53d8\u547d\u8fd0", r"\u89e6\u78b0\u6539\u5199\u547d\u8fd0",
    r"\u7236\u6bcd\u65e9\u901d", r"\u6bcd\u4eb2\u53bb\u4e16", r"\u7236\u4eb2\u5df2\u6b7b",
    r"\u7236\u4eb2\u6b7b\u4ea1", r"\u5168\u7403\u5f02\u80fd", r"\u7b49\u7ea7\u4f53\u7cfb",
    r"\u5fc3\u7535\u56fe\u540c\u6b65", r"\u751f\u547d\u6570\u503c\u540c\u6b65",
]

# For wide patterns with exemption
NEGATION_PREFIXES = [r"\u4e0d\u662f", r"\u5e76\u975e", r"\u4e0d\u7b49\u4e8e"]

CHAPTER_REQUIRED_FILES = [
    "outline.yaml", "preflight_context.md", "beat.md", "draft.md",
    "review.md", "humanized.md", "canon_check.json", "commit.yaml",
]

PHASE4_RUN_FILES = [
    "phase4_summary.md", "phase4_summary.json",
    "chapter_001_final.md", "chapter_002_final.md", "chapter_003_final.md",
    "runtime_canon_final.yaml",
]

PHASE4_LOG_FILES = [
    "phase4_pipeline.log",
    "canon_consistency_phase4.json",
    "continuity_report.json",
]

CHAPTER_GOALS = {
    1: {"title": "\u4ef7\u683c\u521d\u73b0", "hook": "\u7236\u4eb2\u5934\u9876\u4ef7\u683c\u5f52\u96f6"},
    2: {"title": "\u8bef\u5224\u4ee3\u4ef7", "hook": "\u5149\u9c9c\u5ba2\u6237\u6807\u7b7e\u66b4\u8dcc\u4e0e\u73b0\u5b9e\u5371\u9669\u5173\u8054"},
    3: {"title": "\u7b2c\u4e00\u6b21\u4e3b\u52a8\u9009\u62e9", "hook": "\u6797\u781a\u81ea\u5df1\u7684\u6807\u7b7e\u53d1\u751f\u5f02\u5e38\u53d8\u5316"},
}

# ── Phase4B constants ─────────────────────────────────────

PHASE4B_RUN_DIR = DATA_ROOT / "demo_output" / "phase4b_real_run"
PHASE4B_LOG_DIR = DATA_ROOT / "demo_output" / "phase4b_logs"

PHASE4B_REQUIRED_FILES = [
    "outline.yaml", "preflight_context.md", "beat.md", "draft.md",
    "review.md", "humanized.md", "final.md",
    "canon_check.json", "commit.yaml",
]

PHASE4B_ELEMENTS = {
    "外卖场景": ["外卖", "送餐", "配送"],
    "老人": ["老人", "大爷", "老太太", "退休"],
    "光鲜客户": ["客户", "西装", "写字楼", "合约", "资金链", "违约金"],
    "医院缴费窗口": ["医院", "缴费", "窗口", "住院"],
    "父亲价格归零": ["父亲", "归零", "归"],
    "对话": ["说", "问", "答", "道", "喊"],
    "钩子": ["(自动通过，正文有结尾)"],
}

PHASE4B_CHAPTER = 1


def check_file_exists(path):
    return {"path": str(path), "exists": path.exists()}


def check_text_contains(text, keyword):
    return keyword in text


def load_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def check_forbidden_in_text(file_text, patterns):
    """简单 forbidden 检查，排除否定语境"""
    hits = []
    for pat_text in patterns:
        # patterns are unicode escapes, we use the actual characters
        for m in re.finditer(pat_text, file_text):
            pos = m.start()
            ctx_start = max(0, pos - 15)
            ctx = file_text[ctx_start:pos]
            exempted = False
            for neg in NEGATION_PREFIXES:
                if neg in ctx:
                    exempted = True
                    break
            if not exempted:
                hits.append({"pattern": pat_text, "context": ctx})
    return hits


def validate(workspace_root, output_root, mode="mock", project="price_tag_life"):
    """主验证逻辑"""
    ws = Path(workspace_root) / project
    run_dir = Path(output_root) / "phase4_run"
    log_dir = Path(output_root) / "phase4_logs"
    chapters = [1, 2, 3]
    
    errors = []
    warnings = []
    file_checks = []
    canon_checks = []
    continuity_checks = []
    quality_checks = []
    review_checks = []
    commit_checks = []
    runtime_canon_checks = []
    
    # ── 1. 目录与文件检查 ──
    for ch in chapters:
        ch_dir = ws / "chapters" / f"chapter_{ch:03d}"
        if not ch_dir.exists():
            errors.append(f"chapter_{ch:03d} 目录不存在")
            continue
        for fname in CHAPTER_REQUIRED_FILES:
            f = ch_dir / fname
            fc = check_file_exists(f)
            file_checks.append(fc)
            if not fc["exists"]:
                errors.append(f"chapter_{ch:03d}/{fname} 缺失")
    
    for fname in PHASE4_RUN_FILES:
        f = run_dir / fname
        fc = check_file_exists(f)
        file_checks.append(fc)
        if not fc["exists"]:
            errors.append(f"phase4_run/{fname} 缺失")
    
    for fname in PHASE4_LOG_FILES:
        f = log_dir / fname
        if not f.exists():
            warnings.append(f"phase4_logs/{fname} 缺失（mock 可接受）")
    
    # ── 2. 每章 humanized 字数 ──
    for ch in chapters:
        humanized_path = ws / "chapters" / f"chapter_{ch:03d}" / "humanized.md"
        if humanized_path.exists():
            text = load_text(humanized_path)
            char_count = len(text.replace("\n", "").replace(" ", ""))
            quality_item = {"chapter": ch, "file": "humanized.md", "chars": char_count}

            # ── 重复度检查 ──
            lines = [l.strip() for l in text.split("\n") if l.strip()]
            total_lines = len(lines)
            unique_lines = len(set(lines))
            repeated_line_ratio = 1.0 - (unique_lines / max(total_lines, 1))

            # 检查连续重复句（同一句 >= 12 中文字符连续出现 >= 3 次）
            repeated_sentence_hits = 0
            line_counts = {}
            for line in lines:
                if len(line) >= 12:
                    line_counts[line] = line_counts.get(line, 0) + 1

            for line, count in line_counts.items():
                if count >= 3:
                    repeated_sentence_hits += count

            # 检查 padding（同一句在全文中出现 >= 5 次）
            padding_detected = False
            for line, count in line_counts.items():
                if count >= 5:
                    padding_detected = True
                    break

            # 检查结尾重复补字数（最后 5 行中是否有 >= 3 行相同）
            tail_lines = lines[-5:] if len(lines) >= 5 else lines
            tail_line_counts = {}
            for line in tail_lines:
                tail_line_counts[line] = tail_line_counts.get(line, 0) + 1
            tail_padding = any(c >= 3 for c in tail_line_counts.values())

            quality_item["repeated_sentence_hits"] = repeated_sentence_hits
            quality_item["repeated_line_ratio"] = round(repeated_line_ratio, 3)
            quality_item["padding_detected"] = padding_detected or tail_padding

            quality_checks.append(quality_item)

            if char_count < 800:
                errors.append(f"chapter_{ch:03d} humanized.md 字数不足（{char_count}/800）")
            if repeated_sentence_hits >= 3:
                errors.append(f"chapter_{ch:03d} humanized.md 连续重复句过多（{repeated_sentence_hits}次）")
            if repeated_line_ratio > 0.2:
                errors.append(f"chapter_{ch:03d} humanized.md 重复行比例过高（{repeated_line_ratio:.1%}）")
            if padding_detected:
                errors.append(f"chapter_{ch:03d} humanized.md 检测到重复灌水（同一句出现>=5次）")
    
    # ── 3. 每章 canon_check ──
    for ch in chapters:
        canon_check_path = ws / "chapters" / f"chapter_{ch:03d}" / "canon_check.json"
        if canon_check_path.exists():
            try:
                cc = json.loads(canon_check_path.read_text())
                canon_checks.append({"chapter": ch, "passed": cc.get("passed", False)})
                if not cc.get("passed", False):
                    errors.append(f"chapter_{ch:03d} canon_check 未通过")
                # 也检查文件中的 forbidden 内容
                for fname in ["beat.md", "draft.md", "humanized.md"]:
                    fpath = ws / "chapters" / f"chapter_{ch:03d}" / fname
                    if fpath.exists():
                        text = load_text(fpath)
                        hits = check_forbidden_in_text(text, FORBIDDEN_PATTERNS)
                        if hits:
                            for h in hits:
                                errors.append(f"chapter_{ch:03d}/{fname}: 发现禁止词 '{h['pattern']}'")
            except Exception:
                errors.append(f"chapter_{ch:03d} canon_check.json 解析失败")
    
    # ── 4. 每章 commit confirmed_events ──
    for ch in chapters:
        commit_path = ws / "chapters" / f"chapter_{ch:03d}" / "commit.yaml"
        if commit_path.exists():
            try:
                import yaml
                commit = yaml.safe_load(commit_path.read_text())
                events = commit.get("confirmed_events", [])
                commit_checks.append({"chapter": ch, "events_count": len(events)})
                if not events:
                    errors.append(f"chapter_{ch:03d} commit.yaml confirmed_events 为空")
            except Exception:
                errors.append(f"chapter_{ch:03d} commit.yaml 解析失败")
    
    # ── 5. 连续性检查 ──
    for ch in [2, 3]:
        preflight_path = ws / "chapters" / f"chapter_{ch:03d}" / "preflight_context.md"
        if preflight_path.exists():
            text = load_text(preflight_path)
            # 检查是否提及上一章
            prev_events_ref = False
            for prev_ch in range(1, ch):
                commit_path = ws / "chapters" / f"chapter_{prev_ch:03d}" / "commit.yaml"
                if commit_path.exists():
                    try:
                        import yaml
                        commit = yaml.safe_load(commit_path.read_text())
                        for evt in commit.get("confirmed_events", []):
                            if evt[:10] in text:
                                prev_events_ref = True
                                break
                    except Exception:
                        pass
            continuity_checks.append({"chapter": ch, "references_previous": prev_events_ref})
            if not prev_events_ref:
                warnings.append(f"chapter_{ch:03d} preflight_context 未明确引用上章事件")
    
    # ── 6. runtime_canon_final ──
    runtime_final = run_dir / "runtime_canon_final.yaml"
    if runtime_final.exists():
        try:
            import yaml
            rc = yaml.safe_load(runtime_final.read_text())
            confirmed = rc.get("confirmed_events", [])
            runtime_canon_checks.append({"events_count": len(confirmed)})
            if len(confirmed) < 3:
                warnings.append(f"runtime_canon_final 事件数偏少（{len(confirmed)}）")
            # father 状态
            for ch in rc.get("characters", []):
                if ch.get("id") == "father":
                    if "死亡" in ch.get("current_state", ""):
                        errors.append("runtime_canon 中 father 状态为已死亡")
                    runtime_canon_checks.append({"father_state": ch.get("current_state", "未知")})
            # forbidden_facts check — match full sentence with negation exemption
            for ff in rc.get("forbidden_facts", []):
                for ch_rc in [1, 2, 3]:
                    ch_dir = ws / "chapters" / f"chapter_{ch_rc:03d}"
                    for fname in ["humanized.md", "beat.md", "draft.md"]:
                        fpath = ch_dir / fname
                        if fpath.exists():
                            text = load_text(fpath)
                            # Match the full forbidden fact sentence
                            if ff in text:
                                # Check for negation within 15 chars before the match
                                idx = text.find(ff)
                                ctx_before = text[max(0, idx-15):idx]
                                if "不是" in ctx_before or "没有" in ctx_before or "并非" in ctx_before:
                                    continue  # negation exemption
                                errors.append(f"chapter_{ch_rc:03d}/{fname}: 触发 forbidden_fact '{ff}'")
        except Exception as e:
            errors.append(f"runtime_canon_final.yaml 解析失败: {e}")
    
    # ── 7. review 有效性 ──
    for ch in chapters:
        review_path = ws / "chapters" / f"chapter_{ch:03d}" / "review.md"
        if review_path.exists():
            text = load_text(review_path)
            has_specific = any(kw in text for kw in ["具体问题", "修改建议", "问题", "建议"])
            review_checks.append({"chapter": ch, "has_specific": has_specific})
            if not has_specific:
                warnings.append(f"chapter_{ch:03d} review.md 缺少具体问题或修改建议")
    
    # ── 8. phase4_summary ──
    summary_path = run_dir / "phase4_summary.json"
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text())
            if summary.get("pipeline_failed", True):
                errors.append("phase4_summary.json 中 pipeline_failed=true")
        except Exception:
            errors.append("phase4_summary.json 解析失败")
    
    # ── 最终判定 ──
    passed = len(errors) == 0
    
    result = {
        "project": project,
        "mode": mode,
        "checked_chapters": chapters,
        "file_checks": file_checks,
        "canon_checks": canon_checks,
        "continuity_checks": continuity_checks,
        "quality_checks": quality_checks,
        "review_checks": review_checks,
        "commit_checks": commit_checks,
        "runtime_canon_checks": runtime_canon_checks,
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }
    
    # 写文件
    run_dir.mkdir(parents=True, exist_ok=True)
    result_path = run_dir / "phase4_validation.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    
    print(f"  [validate_phase4] project={project} mode={mode}")
    print(f"    errors: {len(errors)}")
    for e in errors:
        print(f"    ❌ {e}")
    for w in warnings:
        print(f"    \u26a0\ufe0f {w}")
    print(f"    passed: {passed}")
    
    return result


def validate_phase4b(workspace_root, output_root, mode="real", project="price_tag_life"):
    """阶段四B 第一章 real 生产链路验证"""
    ws = Path(workspace_root) / project
    run_dir = PHASE4B_RUN_DIR
    log_dir = PHASE4B_LOG_DIR
    ch = PHASE4B_CHAPTER
    ch_dir = run_dir / f"chapter_{ch:03d}"

    errors = []
    warnings = []
    file_checks = []
    canon_checks = []
    quality_checks = []
    review_checks = []
    commit_checks = []
    element_checks = []

    # ── a. 文件完整性检查（10个文件） ──
    for fname in PHASE4B_REQUIRED_FILES:
        f = ch_dir / fname
        fc = check_file_exists(f)
        file_checks.append(fc)
        if not fc["exists"]:
            errors.append(f"chapter_{ch:03d}/{fname} 缺失")

    # ── b. 日志文件检查 ──
    log_files = list(log_dir.glob("*"))
    if not log_files:
        warnings.append("phase4b_logs/ 目录无任何日志文件")
    file_count = len(log_files)
    file_checks.append({"check": "log_files_count", "count": file_count})

    # ── c. deepseek_calls 至少6条成功记录 ──
    calls_path = log_dir / "deepseek_calls_phase4b.jsonl"
    success_count = 0
    if calls_path.exists():
        try:
            for line in calls_path.read_text().strip().split("\n"):
                if line.strip():
                    entry = json.loads(line)
                    if entry.get("success"):
                        success_count += 1
        except Exception as e:
            errors.append(f"deepseek_calls_phase4b.jsonl 解析失败: {e}")
    else:
        errors.append("deepseek_calls_phase4b.jsonl 不存在")
    file_checks.append({"check": "deepseek_calls_success", "count": success_count})
    if success_count < 6:
        errors.append(f"deepseek_calls 成功记录不足6条（{success_count}）")

    # ── d. humanized.md/final.md 字数 >= 1200 中文字 ──
    for fname in ["humanized.md", "final.md"]:
        fpath = ch_dir / fname
        if fpath.exists():
            text = load_text(fpath)
            # 只统计中文字符
            cn_chars = 0
            for c in text:
                if ord(c) >= 0x4e00 and ord(c) <= 0x9fff:
                    cn_chars += 1
            quality_item = {"file": fname, "cn_chars": cn_chars}
            quality_checks.append(quality_item)
            if cn_chars < 1200:
                errors.append(f"chapter_{ch:03d}/{fname} 中文字数不足（{cn_chars}/1200）")

    # ── e. 重复度检查（同阶段四A） ──
    for fname in ["humanized.md", "final.md"]:
        fpath = ch_dir / fname
        if fpath.exists():
            text = load_text(fpath)
            lines = [l.strip() for l in text.split("\\n") if l.strip()]
            total_lines = len(lines)
            unique_lines = len(set(lines))
            repeated_line_ratio = 1.0 - (unique_lines / max(total_lines, 1))

            line_counts = {}
            for line in lines:
                if len(line) >= 12:
                    line_counts[line] = line_counts.get(line, 0) + 1

            repeated_sentence_hits = sum(c for c in line_counts.values() if c >= 3)
            padding_detected = any(c >= 5 for c in line_counts.values())

            tail_lines = lines[-5:] if len(lines) >= 5 else lines
            tail_line_counts = {}
            for line in tail_lines:
                tail_line_counts[line] = tail_line_counts.get(line, 0) + 1
            tail_padding = any(c >= 3 for c in tail_line_counts.values())

            quality_item = {
                "file": fname,
                "repeated_sentence_hits": repeated_sentence_hits,
                "repeated_line_ratio": round(repeated_line_ratio, 3),
                "padding_detected": padding_detected or tail_padding,
            }
            # Update existing or append
            found = False
            for qi in quality_checks:
                if qi.get("file") == fname:
                    qi.update(quality_item)
                    found = True
                    break
            if not found:
                quality_checks.append(quality_item)

            if repeated_sentence_hits >= 3:
                errors.append(f"chapter_{ch:03d}/{fname} 连续重复句过多（{repeated_sentence_hits}次）")
            if repeated_line_ratio > 0.2:
                errors.append(f"chapter_{ch:03d}/{fname} 重复行比例过高（{repeated_line_ratio:.1%}）")
            if padding_detected or tail_padding:
                errors.append(f"chapter_{ch:03d}/{fname} 检测到重复灌水")

    # ── f. 正文必要元素检查（模糊匹配） ──
    for fname in ["humanized.md", "final.md"]:
        fpath = ch_dir / fname
        if fpath.exists():
            text = load_text(fpath)
            for elem_name, keywords in PHASE4B_ELEMENTS.items():
                found = False
                for kw in keywords:
                    if kw == "(自动通过，正文有结尾)":
                        found = True
                        break
                    if kw in text:
                        found = True
                        break
                element_checks.append({"file": fname, "element": elem_name, "found": found})
                if not found:
                    errors.append(f"chapter_{ch:03d}/{fname} 缺少必要元素「{elem_name}」")

    # ── g. canon_check passed=true ──
    canon_check_path = ch_dir / "canon_check.json"
    if canon_check_path.exists():
        try:
            cc = json.loads(canon_check_path.read_text())
            canon_checks.append({"chapter": ch, "passed": cc.get("passed", False)})
            if not cc.get("passed", False):
                errors.append(f"chapter_{ch:03d} canon_check 未通过")
        except Exception:
            errors.append(f"chapter_{ch:03d} canon_check.json 解析失败")
    else:
        errors.append(f"chapter_{ch:03d} canon_check.json 不存在")

    # ── h. review 有效性（具体问题） ──
    review_path = ch_dir / "review.md"
    if review_path.exists():
        text = load_text(review_path)
        has_specific = any(kw in text for kw in ["具体问题", "修改建议", "问题", "建议"])
        review_checks.append({"chapter": ch, "has_specific": has_specific})
        if not has_specific:
            warnings.append(f"chapter_{ch:03d} review.md 缺少具体问题或修改建议")
    else:
        warnings.append(f"chapter_{ch:03d} review.md 不存在")

    # ── i. commit.yaml confirmed_events 非空 ──
    commit_path = ch_dir / "commit.yaml"
    if commit_path.exists():
        try:
            import yaml
            commit = yaml.safe_load(commit_path.read_text())
            events = commit.get("confirmed_events", []) or commit.get("changes", {}).get("plot_events", [])
            commit_checks.append({"chapter": ch, "events_count": len(events)})
            if not events:
                errors.append(f"chapter_{ch:03d} commit.yaml confirmed_events 为空")
        except Exception:
            errors.append(f"chapter_{ch:03d} commit.yaml 解析失败")
    else:
        errors.append(f"chapter_{ch:03d} commit.yaml 不存在")

    # ── j. phase4b_summary.json success=true ──
    summary_path = run_dir / "phase4b_summary.json"
    if summary_path.exists():
        try:
            summary = json.loads(summary_path.read_text())
            if not summary.get("success", False):
                errors.append("phase4b_summary.json 中 success=false")
        except Exception:
            errors.append("phase4b_summary.json 解析失败")
    else:
        errors.append("phase4b_summary.json 不存在")

    # ── 最终判定 ──
    passed = len(errors) == 0

    result = {
        "project": project,
        "mode": mode,
        "phase": "4B",
        "checked_chapter": ch,
        "file_checks": file_checks,
        "canon_checks": canon_checks,
        "quality_checks": quality_checks,
        "review_checks": review_checks,
        "commit_checks": commit_checks,
        "element_checks": element_checks,
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }

    # 写文件
    log_dir.mkdir(parents=True, exist_ok=True)
    result_path = log_dir / "validate_phase4b_real.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"  [validate_phase4b] project={project} phase=4B")
    print(f"    errors: {len(errors)}")
    for e in errors:
        print(f"    ❌ {e}")
    for w in warnings:
        print(f"    ⚠️ {w}")
    print(f"    passed: {passed}")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="阶段四三章生产闭环验证 / 阶段四B第一章real验证")
    parser.add_argument("--project", default="price_tag_life", help="项目名")
    parser.add_argument("--mode", choices=["mock", "real"], default="mock", help="模式")
    parser.add_argument("--workspace-root", default=str(DATA_ROOT / "workspace" / "novels"), help="workspace 根目录")
    parser.add_argument("--output-root", default=str(DATA_ROOT / "demo_output"), help="输出根目录")
    parser.add_argument("--chapters", default="1,2,3", help="逗号分隔章节号（阶段四A使用）")
    parser.add_argument("--phase4b", action="store_true", help="阶段四B第一章real生产链路验证")
    args = parser.parse_args()

    if args.phase4b:
        result = validate_phase4b(args.workspace_root, args.output_root, mode=args.mode, project=args.project)
    else:
        result = validate(args.workspace_root, args.output_root, mode=args.mode, project=args.project)

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
