#!/usr/bin/env python3
"""
validate_phase8.py — 校验 Phase 8 目录、schema、模板、核心交付物是否齐全。

用法:
  python tools/phase8/validate_phase8.py --book-id toy_book

检查内容：
  - 目录是否存在
  - source_meta 是否存在
  - manifest 是否存在及必需字段
  - chapters 是否存在
  - chapter_cards 是否存在
  - 核心报告是否存在
  - candidate / approved / rejected 目录是否存在
  - 必要字段是否为空
  - Writer 禁止项是否在 skill_injection_plan 中声明
"""

import os, sys, yaml
from pathlib import Path
from datetime import datetime

PROJECT = Path("/opt/webnovel-hermes-wps")
PHASE8 = PROJECT / "production" / "phase8"


def check(val, label, detail=""):
    status = "✅" if val else "❌"
    d = f" — {detail}" if detail else ""
    print(f"  {status} {label}{d}")
    return val


def main():
    import argparse
    parser = argparse.ArgumentParser(description="校验 Phase 8 交付物完整性")
    parser.add_argument("--book-id", required=True)
    args = parser.parse_args()

    book_id = args.book_id
    corpus = PHASE8 / "corpus" / book_id
    audit_dir = PHASE8 / "audit" / book_id
    # reverse_assets: 优先用 book_id 子目录，否则用根目录
    reverse_book = PHASE8 / "reverse_assets" / book_id
    reverse_root = PHASE8 / "reverse_assets"
    reverse = reverse_book if reverse_book.exists() else reverse_root
    craft = PHASE8 / "craft_assets"
    skill = PHASE8 / "skill_injection"
    valid_dir = PHASE8 / "validation"

    errors = []
    warnings = []
    now = datetime.now().isoformat()

    print(f"\n{'=' * 50}")
    print(f"  Phase 8 校验: {book_id}")
    print(f"{'=' * 50}\n")

    # 1. 目录检查
    dirs = {
        "production/phase8": PHASE8,
        f"corpus/{book_id}": corpus,
        f"corpus/{book_id}/chapters": corpus / "chapters",
        f"corpus/{book_id}/chapter_cards": corpus / "chapter_cards",
        "audit": PHASE8 / "audit",
        "reverse_assets": PHASE8 / "reverse_assets",
        "craft_assets/candidate": craft / "candidate",
        "craft_assets/approved": craft / "approved",
        "craft_assets/rejected": craft / "rejected",
        "skill_injection": skill,
        "validation": valid_dir,
        "schemas": PHASE8 / "schemas",
        "templates": PHASE8 / "templates",
        "prompts": PHASE8 / "prompts",
    }
    missing_dirs = []
    for name, p in dirs.items():
        if not p.exists():
            missing_dirs.append(name)
            errors.append(f"缺失目录: {name}")
    if not missing_dirs:
        check(True, "目录完整性", "所有必需目录存在")

    # 2. source_meta
    sm_path = corpus / "source_meta.yaml"
    if sm_path.exists():
        sm = yaml.safe_load(sm_path.read_text()) or {}
        sm_ok = all(k in sm for k in ["source_id", "title", "author", "source_type", "permission_status", "allowed_operations", "do_not_copy"])
        if not sm_ok:
            errors.append("source_meta.yaml 缺少必需字段")
        check(sm_ok, "source_meta.yaml", f"{len(sm)} 字段")
    else:
        errors.append("source_meta.yaml 缺失")
        check(False, "source_meta.yaml", "缺失")

    # 3. manifest
    man_path = corpus / "manifest.yaml"
    manifest = {}
    if man_path.exists():
        manifest = yaml.safe_load(man_path.read_text()) or {}
        req = ["book_id", "title", "chapter_count", "chapter_index", "status"]
        man_ok = all(k in manifest for k in req)
        if not man_ok:
            errors.append("manifest.yaml 缺少必需字段")
        check(man_ok, "manifest.yaml", f"章节数: {manifest.get('chapter_count', '?')}")
    else:
        errors.append("manifest.yaml 缺失")
        check(False, "manifest.yaml", "缺失")

    # 4. chapters
    ch_dir = corpus / "chapters"
    expected_chapters = manifest.get("chapter_count", 0)
    if ch_dir.exists():
        ch_files = sorted(ch_dir.glob("*.md"))
        ch_ok = len(ch_files) >= expected_chapters
        if not ch_ok:
            errors.append(f"章节文件数不足: 期望 {expected_chapters}, 实际 {len(ch_files)}")
        check(ch_ok, f"章节文件", f"{len(ch_files)}/{expected_chapters}")
    else:
        errors.append("chapters/ 目录缺失")
        check(False, "章节文件", "缺失")

    # 5. chapter_cards
    cc_dir = corpus / "chapter_cards"
    if cc_dir.exists():
        cc_files = sorted(cc_dir.glob("*.yaml"))
        low_conf_cards = []
        for cf in cc_files:
            try:
                cc = yaml.safe_load(cf.read_text()) or {}
                if cc.get("confidence") == "low":
                    low_conf_cards.append(cf.name)
            except Exception:
                pass
        check(True, "chapter_cards", f"{len(cc_files)} 张, 低置信度: {len(low_conf_cards)}")
        if low_conf_cards:
            warnings.append(f"低置信度 chapter_cards: {low_conf_cards}")
    else:
        check(False, "chapter_cards", "缺失")

    # 6. 核心报告 — 在 reverse_assets/{book_id}/ 和 reverse_assets/ 根目录中查找
    reports = {}
    core_report_names = [
        "chapter_fact_audit_report.md",
        "reverse_story_bible.md",
        "volume_structure_report.md",
        "reader_debt_lifecycle.md",
        "hook_payoff_map.md",
    ]
    for rname in core_report_names:
        rpath = reverse / rname
        rfound = rpath.exists()
        reports[rname] = rfound

    # character_cards 目录检查
    cc_dir_check = reverse / "character_cards"
    reports["character_cards_dir"] = cc_dir_check.exists()
    # chapter_fact_audit_report 在 audit 目录下
    reports["chapter_fact_audit_report.md"] = (audit_dir / "chapter_fact_audit_report.md").exists() if audit_dir.exists() else False

    for rname, rexists in reports.items():
        if not rexists:
            warnings.append(f"核心报告未就绪: {rname}")
    check(True, "核心报告状态", f"就绪: {sum(1 for v in reports.values() if v)}/{len(reports)}")

    # 7. 技法资产
    ca_ok = all((craft / d).exists() for d in ["candidate", "approved", "rejected"])
    check(ca_ok, "技法资产目录", "candidate / approved / rejected")

    # 8. Skill injection
    si_ok = skill.exists()
    plan_paths = list(skill.glob("*.yaml")) + list(skill.glob("*.md"))
    si_has_plan = len(plan_paths) > 0
    # 检查 Writer 禁止声明
    writer_forbidden_declared = False
    for pp in plan_paths:
        text = pp.read_text()
        if "Writer 禁止" in text or "writer_forbidden" in text or "Writer 不能" in text:
            writer_forbidden_declared = True
            break
    if not writer_forbidden_declared:
        warnings.append("skill_injection_plan 未声明 Writer 禁止项")
    check(si_ok, "Skill 反哺目录", f"计划文件: {len(plan_paths)}, Writer禁止声明: {'✅' if writer_forbidden_declared else '⚠️'}")

    # 9. Schemas
    schema_dir = PHASE8 / "schemas"
    expected_schemas = [
        "source_meta.schema.yaml", "manifest.schema.yaml", "chapter_card.schema.yaml",
        "chapter_fact_audit_report.schema.yaml", "reverse_story_bible.schema.yaml",
        "character_card.schema.yaml", "volume_structure_report.schema.yaml",
        "reader_debt_lifecycle.schema.yaml", "hook_payoff_map.schema.yaml",
        "craft_asset.schema.yaml", "skill_injection_plan.schema.yaml", "validation_report.schema.yaml",
    ]
    schema_ok = all((schema_dir / s).exists() for s in expected_schemas)
    check(schema_ok, "Schema 文件", f"{len(expected_schemas)} 个")

    # 10. Templates
    tmpl_dir = PHASE8 / "templates"
    expected_templates = [
        "source_meta.template.yaml", "manifest.template.yaml", "chapter_card.template.yaml",
        "chapter_fact_audit_report.template.md", "reverse_story_bible.template.md",
        "character_card.template.md", "volume_structure_report.template.md",
        "reader_debt_lifecycle.template.md", "hook_payoff_map.template.md",
        "craft_asset_card.template.md", "skill_injection_plan.template.md", "validation_report.template.md",
    ]
    tmpl_ok = all((tmpl_dir / t).exists() for t in expected_templates)
    check(tmpl_ok, "Template 文件", f"{len(expected_templates)} 个")

    # 11. Prompts
    prompt_dir = PHASE8 / "prompts"
    expected_prompts = [
        "book_compressor.prompt.md", "book_architect.prompt.md",
        "craft_distiller.prompt.md", "asset_curator.prompt.md", "skill_injection.prompt.md",
    ]
    prompt_ok = all((prompt_dir / p).exists() for p in expected_prompts)
    check(prompt_ok, "Prompt 文件", f"{len(expected_prompts)} 个")

    # ── 结果 ──
    passed = len(errors) == 0
    print(f"\n{'=' * 50}")
    print(f"  结果: {'✅ PASS' if passed else '❌ FAIL'}")
    print(f"  错误: {len(errors)}")
    for e in errors:
        print(f"    ❌ {e}")
    print(f"  警告: {len(warnings)}")
    for w in warnings:
        print(f"    ⚠️ {w}")
    print(f"{'=' * 50}\n")

    # 生成校验报告
    report = {
        "book_id": book_id,
        "validated_at": now,
        "directory_check": {"exists": not missing_dirs, "missing_dirs": missing_dirs},
        "source_meta_check": {"exists": sm_path.exists(), "required_fields_present": sm_ok if sm_path.exists() else False},
        "manifest_check": {"exists": man_path.exists(), "required_fields_present": man_ok if man_path.exists() else False},
        "chapters_check": {"chapter_count": len(ch_files) if ch_dir.exists() else 0, "expected_count": expected_chapters},
        "chapter_cards_check": {"card_count": len(cc_files) if cc_dir.exists() else 0, "expected_count": expected_chapters},
        "core_reports_check": reports,
        "reverse_assets_path": str(reverse),
        "craft_assets_check": {"candidate_exists": (craft / "candidate").exists(), "approved_exists": (craft / "approved").exists(), "rejected_exists": (craft / "rejected").exists()},
        "skill_injection_check": {"plan_exists": si_has_plan, "writer_forbidden_declared": writer_forbidden_declared},
        "schema_check": {"exists": schema_ok, "count": len(expected_schemas) if schema_ok else 0},
        "template_check": {"exists": tmpl_ok, "count": len(expected_templates) if tmpl_ok else 0},
        "prompt_check": {"exists": prompt_ok, "count": len(expected_prompts) if prompt_ok else 0},
        "missing_files": errors,
        "risks": warnings,
        "passed": passed,
    }

    valid_dir.mkdir(parents=True, exist_ok=True)
    report_path = valid_dir / f"{book_id}_validation_report.json"
    import json
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"  报告: {report_path}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
