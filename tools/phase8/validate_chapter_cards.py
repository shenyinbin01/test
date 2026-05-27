#!/usr/bin/env python3
"""
validate_chapter_cards.py — 校验 chapter_card YAML 质量

用法:
    python tools/phase8/validate_chapter_cards.py --book-id dachengqi --project-root .

输出:
    production/phase8/audit/{book_id}/chapter_card_quality_report.md
    production/phase8/audit/{book_id}/chapter_card_quality_report.json
"""

import os, sys, yaml, json
from pathlib import Path
from datetime import datetime

_THIS_FILE = Path(__file__).resolve()
for _p in [_THIS_FILE.parent.parent.parent, *_THIS_FILE.parents]:
    if (_p / "tools" / "phase8").exists():
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))
        break

from tools.phase8.common import resolve_project_root


def validate_single_card(card_path: Path) -> dict:
    """校验单张 chapter_card"""
    result = {
        "file": str(card_path.name),
        "chapter_number": None,
        "valid_yaml": False,
        "parse_error": None,
        "missing_fields": [],
        "evidence_empty": False,
        "confidence_missing": False,
        "confidence_value": None,
        "unknown_fields_present": True,
        "hook_format": "unknown",
        "debt_format": "unknown",
        "warnings": [],
    }

    if not card_path.exists():
        result["parse_error"] = "FILE_MISSING"
        return result

    text = card_path.read_text(encoding="utf-8")

    # 提取 YAML
    yaml_text = text
    if "```yaml" in text:
        parts = text.split("```yaml", 1)
        if len(parts) > 1:
            yaml_text = parts[1].split("```", 1)[0]
    elif "```" in text:
        parts = text.split("```", 1)
        if len(parts) > 1:
            yaml_text = parts[1].split("```", 1)[0]

    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as e:
        result["parse_error"] = str(e)[:200]
        return result

    if not isinstance(data, dict):
        result["parse_error"] = "NOT_A_DICT"
        return result

    result["valid_yaml"] = True
    result["chapter_number"] = data.get("chapter_number")

    # 必填字段
    required = ["book_id", "chapter_number", "title", "one_sentence",
                "chapter_function", "main_events", "characters_present", "confidence"]
    for f in required:
        if f not in data or data[f] is None:
            result["missing_fields"].append(f)

    # evidence
    evidence = data.get("evidence", [])
    if not evidence:
        result["evidence_empty"] = True
    else:
        # 检查证据质量
        for ev in evidence:
            if isinstance(ev, dict):
                summary = ev.get("summary", "")
                if len(summary) > 120:
                    result["warnings"].append(f"evidence summary 过长 ({len(summary)} chars): {summary[:50]}...")

    # confidence
    conf = data.get("confidence")
    if conf is None:
        result["confidence_missing"] = True
    else:
        result["confidence_value"] = conf
        if conf not in ("high", "medium", "low"):
            result["warnings"].append(f"confidence 值非标准: {conf}")

    # unknown_fields
    if "unknown_fields" not in data:
        result["unknown_fields_present"] = False
        result["warnings"].append("缺少 unknown_fields 字段")

    # hook format detection
    hooks = data.get("hook_opened", [])
    if hooks:
        if all(isinstance(h, dict) for h in hooks):
            result["hook_format"] = "structured"
        elif all(isinstance(h, str) for h in hooks):
            result["hook_format"] = "legacy"
        else:
            result["hook_format"] = "mixed"

    # debt format detection
    debts = data.get("reader_debts_opened", [])
    if debts:
        if all(isinstance(d, dict) for d in debts):
            result["debt_format"] = "structured"
        elif all(isinstance(d, str) for d in debts):
            result["debt_format"] = "legacy"
        else:
            result["debt_format"] = "mixed"

    # one_sentence length check
    one_sent = data.get("one_sentence", "")
    if len(one_sent) > 150:
        result["warnings"].append(f"one_sentence 过长 ({len(one_sent)} chars)")

    # LLM nonsense check
    nonsense_markers = ["作为一个AI", "我不能", "我无法", "根据您的要求", "以下是", "请注意"]
    for marker in nonsense_markers:
        if marker in text:
            result["warnings"].append(f"可能包含 LLM 废话: '{marker}'")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="校验 chapter_card 质量")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None)
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"
    book_id = args.book_id
    cards_dir = phase8 / "corpus" / book_id / "chapter_cards"
    audit_dir = phase8 / "audit" / book_id
    audit_dir.mkdir(parents=True, exist_ok=True)

    # 读取 manifest
    manifest_path = phase8 / "corpus" / book_id / "manifest.yaml"
    if not manifest_path.exists():
        print(f"❌ manifest 不存在")
        sys.exit(1)
    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    expected = manifest.get("chapter_count", 0)

    if not cards_dir.exists():
        print(f"❌ chapter_cards 目录不存在: {cards_dir}")
        sys.exit(1)

    card_files = sorted(cards_dir.glob("chapter_*.yaml"))
    print(f"  校验 {len(card_files)}/{expected} 张 chapter_card...")

    results = []
    errors_list = []
    warnings_list = []

    # 检查覆盖
    present_nums = set()
    for cf in card_files:
        r = validate_single_card(cf)
        results.append(r)
        if r["chapter_number"]:
            present_nums.add(r["chapter_number"])
        
        if r["parse_error"]:
            errors_list.append(f"ch{r['chapter_number'] or cf.stem}: YAML 解析失败 — {r['parse_error']}")
        if r["missing_fields"]:
            errors_list.append(f"ch{r['chapter_number']}: 缺字段 {r['missing_fields']}")
        if r["evidence_empty"]:
            errors_list.append(f"ch{r['chapter_number']}: evidence 为空")
        if r["confidence_missing"]:
            errors_list.append(f"ch{r['chapter_number']}: confidence 缺失")

    # 章节覆盖检查
    missing_nums = set(range(1, expected + 1)) - present_nums
    if missing_nums:
        errors_list.append(f"缺失章节: {sorted(missing_nums)}")

    yaml_ok = sum(1 for r in results if r["valid_yaml"])
    yaml_err = sum(1 for r in results if r["parse_error"])
    evidence_ok = sum(1 for r in results if not r["evidence_empty"])
    evidence_missing = sum(1 for r in results if r["evidence_empty"])
    low_conf = sum(1 for r in results if r["confidence_value"] == "low")
    legacy_hooks = sum(1 for r in results if r["hook_format"] == "legacy")
    legacy_debts = sum(1 for r in results if r["debt_format"] == "legacy")
    structured_hooks = sum(1 for r in results if r["hook_format"] == "structured")
    structured_debts = sum(1 for r in results if r["debt_format"] == "structured")

    # 收集所有 warnings
    for r in results:
        for w in r.get("warnings", []):
            warnings_list.append(f"ch{r.get('chapter_number', '?')}: {w}")

    passed = len(errors_list) == 0

    # 生成 Markdown 报告
    md_lines = [
        f"# Chapter Card 质量报告: {book_id}",
        f"",
        f"> 生成时间: {datetime.now().isoformat()}",
        f"> 总章节: {expected} | 现有 card: {len(card_files)} | 缺失: {len(missing_nums)}",
        f"",
        f"## 摘要",
        f"",
        f"| 指标 | 值 |",
        f"|------|-----|",
        f"| YAML 可解析 | {yaml_ok}/{len(card_files)} |",
        f"| YAML 解析失败 | {yaml_err} |",
        f"| 字段完整 | {sum(1 for r in results if not r['missing_fields'])}/{len(card_files)} |",
        f"| 有 evidence | {evidence_ok}/{len(card_files)} |",
        f"| evidence 为空 | {evidence_missing} |",
        f"| low confidence | {low_conf} |",
        f"| structured hooks | {structured_hooks} |",
        f"| legacy hooks | {legacy_hooks} |",
        f"| structured debts | {structured_debts} |",
        f"| legacy debts | {legacy_debts} |",
        f"",
        f"## 结论",
        f"",
    ]

    if passed:
        md_lines.append(f"✅ **通过** — 允许进入 Step 2F")
    else:
        md_lines.append(f"❌ **不通过** — {len(errors_list)} 个错误，禁止进入 Step 2F")

    if errors_list:
        md_lines.append(f"\n### 错误 ({len(errors_list)})")
        for e in errors_list:
            md_lines.append(f"- {e}")

    if warnings_list:
        md_lines.append(f"\n### 警告 ({len(warnings_list)})")
        for w in warnings_list[:100]:  # 截断
            md_lines.append(f"- {w}")
        if len(warnings_list) > 100:
            md_lines.append(f"- ... ({len(warnings_list) - 100} 更多)")

    # 缺失 evidence 章节
    no_evidence_chs = [r for r in results if r["evidence_empty"]]
    if no_evidence_chs:
        md_lines.append(f"\n### 无 evidence 章节 ({len(no_evidence_chs)})")
        for r in no_evidence_chs:
            md_lines.append(f"- ch{r.get('chapter_number', '?')}")

    report_path = audit_dir / "chapter_card_quality_report.md"
    report_path.write_text("\n".join(md_lines), encoding="utf-8")

    # 生成 JSON
    json_report = {
        "book_id": book_id,
        "generated_at": datetime.now().isoformat(),
        "passed": passed,
        "summary": {
            "total_expected": expected,
            "total_existing": len(card_files),
            "missing": len(missing_nums),
            "yaml_parse_ok": yaml_ok,
            "yaml_parse_error": yaml_err,
            "fields_complete": sum(1 for r in results if not r["missing_fields"]),
            "evidence_ok": evidence_ok,
            "evidence_missing": evidence_missing,
            "low_confidence": low_conf,
            "structured_hooks": structured_hooks,
            "legacy_hooks": legacy_hooks,
        },
        "errors": errors_list,
        "warnings": warnings_list[:100],
    }
    json_path = audit_dir / "chapter_card_quality_report.json"
    json_path.write_text(json.dumps(json_report, ensure_ascii=False, indent=2))

    print(f"\n  报告: {report_path}")
    print(f"  JSON:  {json_path}")
    print(f"  结果: {'✅ PASS' if passed else '❌ FAIL'}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
