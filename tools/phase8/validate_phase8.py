#!/usr/bin/env python3
"""
validate_phase8.py — 校验 Phase 8 目录、schema、模板、核心交付物是否齐全。

用法:
  python tools/phase8/validate_phase8.py --book-id toy_book --mode scaffold
  python tools/phase8/validate_phase8.py --book-id toy_book --mode delivery

--mode scaffold (默认): 工程骨架验收，核心交付物缺失可 warning，只要骨架完整就 PASS。
--mode delivery: 真实书交付验收，7 个核心交付物缺失必须 FAIL。
"""

import os, sys, yaml, json
from pathlib import Path
from datetime import datetime

from tools.phase8.common import resolve_project_root


def check(val, label, detail=""):
    status = "✅" if val else "❌"
    d = f" — {detail}" if detail else ""
    print(f"  {status} {label}{d}")
    return val


def main():
    import argparse
    parser = argparse.ArgumentParser(description="校验 Phase 8 交付物完整性")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--mode", choices=["scaffold", "delivery"], default="scaffold",
                        help="scaffold: 工程骨架验收; delivery: 真实交付验收")
    parser.add_argument("--project-root", default=None, help="项目根目录，默认自动查找")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"
    book_id = args.book_id
    mode = args.mode

    corpus = phase8 / "corpus" / book_id
    audit_dir = phase8 / "audit" / book_id
    reverse_book = phase8 / "reverse_assets" / book_id
    reverse_root = phase8 / "reverse_assets"
    reverse = reverse_book if reverse_book.exists() else reverse_root
    craft = phase8 / "craft_assets"
    craft_book = craft / book_id
    skill = phase8 / "skill_injection"
    valid_dir = phase8 / "validation" / book_id
    valid_dir.mkdir(parents=True, exist_ok=True)

    errors = []
    warnings = []
    now = datetime.now().isoformat()

    print(f"\n{'=' * 50}")
    print(f"  Phase 8 校验: {book_id}  mode={mode}")
    print(f"{'=' * 50}\n")

    # ── 1. 目录检查 (scaffold + delivery) ──
    required_dirs = {
        "production/phase8": phase8,
        f"corpus/{book_id}": corpus,
        f"corpus/{book_id}/chapters": corpus / "chapters",
        f"corpus/{book_id}/chapter_cards": corpus / "chapter_cards",
        "audit": phase8 / "audit",
        "reverse_assets": phase8 / "reverse_assets",
        "craft_assets/candidate": craft / "candidate",
        "craft_assets/approved": craft / "approved",
        "craft_assets/rejected": craft / "rejected",
        "skill_injection": skill,
        "validation": phase8 / "validation",
        "schemas": phase8 / "schemas",
        "templates": phase8 / "templates",
        "prompts": phase8 / "prompts",
    }
    missing_dirs = []
    for name, p in required_dirs.items():
        if not p.exists():
            missing_dirs.append(name)
            errors.append(f"缺失目录: {name}")
    if not missing_dirs:
        check(True, "目录完整性", "所有必需目录存在")

    # ── 2. source_meta (scaffold + delivery) ──
    sm_path = corpus / "source_meta.yaml"
    if sm_path.exists():
        sm = yaml.safe_load(sm_path.read_text()) or {}
        required_meta = ["source_id", "title", "author", "source_type", "permission_status", "allowed_operations", "do_not_copy"]
        sm_ok = all(k in sm for k in required_meta)
        if not sm_ok:
            errors.append("source_meta.yaml 缺少必需字段")
        # 检查 allowed_operations 是否为 object (dict)
        ao = sm.get("allowed_operations", [])
        if isinstance(ao, list):
            errors.append("source_meta.yaml: allowed_operations 是 list，必须是 object (dict)")
            sm_ok = False
        elif isinstance(ao, dict):
            for key in ["ingest", "compress", "distill_craft", "quote", "train_model"]:
                if key not in ao:
                    warnings.append(f"source_meta.yaml: allowed_operations 缺 {key}")
        check(sm_ok, "source_meta.yaml", f"{len(sm)} 字段, allowed_operations={'object' if isinstance(ao, dict) else 'list'}")
    else:
        errors.append("source_meta.yaml 缺失")
        check(False, "source_meta.yaml", "缺失")

    # ── 3. manifest (scaffold + delivery) ──
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

    # ── 4. chapters (scaffold + delivery) ──
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

    # ── 5. chapter_cards (scaffold + delivery) ──
    cc_dir = corpus / "chapter_cards"
    if cc_dir.exists():
        cc_files = sorted(cc_dir.glob("*.yaml"))
        low_conf_cards = []
        for cf in cc_files:
            try:
                cc_data = yaml.safe_load(cf.read_text()) or {}
                if cc_data.get("confidence") == "low":
                    low_conf_cards.append(cf.name)
            except Exception:
                pass
        check(True, "chapter_cards", f"{len(cc_files)} 张, 低置信度: {len(low_conf_cards)}")
        if low_conf_cards:
            warnings.append(f"低置信度 chapter_cards: {low_conf_cards}")
    else:
        check(False, "chapter_cards", "缺失")
        if mode == "delivery":
            errors.append("chapter_cards/ 缺失")

    # ── 6. 核心报告 / 7 个老板可审计交付物 ──
    core_deliverables = {
        "chapter_fact_audit_report.md": audit_dir / "chapter_fact_audit_report.md",
        "reverse_story_bible.md": reverse / "reverse_story_bible.md",
        "character_cards": reverse / "character_cards",
        "volume_structure_report.md": reverse / "volume_structure_report.md",
        "reader_debt_lifecycle.md": reverse / "reader_debt_lifecycle.md",
        "hook_payoff_map.md": reverse / "hook_payoff_map.md",
        "skill_injection_plan": None,  # handled separately
    }
    # skill injection plan: check skill/ directory with book_id file
    skill_plan_paths = list(skill.glob(f"{book_id}*.yaml")) + list(skill.glob(f"{book_id}*.md")) + list(skill.glob("*.yaml")) + list(skill.glob("*.md"))
    core_results = {}
    for name, path in core_deliverables.items():
        if name == "skill_injection_plan":
            found = len(skill_plan_paths) > 0 and any("skill_injection" in p.stem for p in skill_plan_paths)
            core_results[name] = found
            if found:
                check(True, f"核心交付物: {name}", f"{skill_plan_paths[0].name if skill_plan_paths else '?'}")
            else:
                check(False, f"核心交付物: {name}", "缺失")
                if mode == "delivery":
                    errors.append(f"核心交付物缺失: {name}")
                else:
                    warnings.append(f"核心交付物未就绪: {name}")
        elif name == "character_cards":
            if path.exists():
                card_files = sorted(path.glob("*.md"))
                if len(card_files) >= 1:
                    core_results[name] = True
                    check(True, f"核心交付物: {name}", f"{len(card_files)} 张卡")
                else:
                    core_results[name] = False
                    check(False, f"核心交付物: {name}", "目录为空")
                    if mode == "delivery":
                        errors.append(f"核心交付物缺失: {name} 目录为空")
                    else:
                        warnings.append(f"核心交付物未就绪: {name}")
            else:
                core_results[name] = False
                check(False, f"核心交付物: {name}", "缺失")
                if mode == "delivery":
                    errors.append(f"核心交付物缺失: {name}")
                else:
                    warnings.append(f"核心交付物未就绪: {name}")
        else:
            found = path.exists()
            core_results[name] = found
            if found:
                check(True, f"核心交付物: {name}", f"{path.stat().st_size} bytes")
            else:
                check(False, f"核心交付物: {name}", "缺失")
                if mode == "delivery":
                    errors.append(f"核心交付物缺失: {name}")
                else:
                    warnings.append(f"核心交付物未就绪: {name}")

    # ── 7. craft_assets (scaffold + delivery) ──
    # candidate: check both root and book_id subdir
    candidate_dirs = [craft / "candidate"]
    if craft_book.exists():
        candidate_dirs.append(craft_book / "candidate")
    candidate_files = []
    for d in candidate_dirs:
        if d.exists():
            candidate_files.extend(sorted(d.glob("*")))
    # remove .gitkeep
    candidate_files = [f for f in candidate_files if f.name != ".gitkeep"]

    approved_dirs = [craft / "approved"]
    if craft_book.exists():
        approved_dirs.append(craft_book / "approved")
    approved_files = []
    for d in approved_dirs:
        if d.exists():
            approved_files.extend(sorted(d.glob("*")))
    approved_files = [f for f in approved_files if f.name != ".gitkeep"]

    rejected_dirs = [craft / "rejected"]
    if craft_book.exists():
        rejected_dirs.append(craft_book / "rejected")
    rejected_files = []
    for d in rejected_dirs:
        if d.exists():
            rejected_files.extend(sorted(d.glob("*")))
    rejected_files = [f for f in rejected_files if f.name != ".gitkeep"]

    ca_ok = True
    if mode == "delivery" and len(candidate_files) == 0:
        errors.append("candidate 技法卡为 0")
        ca_ok = False
    check(len(candidate_files) >= 0, "技法资产 candidate", f"{len(candidate_files)} 张")
    check(len(approved_files) >= 0, "技法资产 approved", f"{len(approved_files)} 张")
    check(len(rejected_files) >= 0, "技法资产 rejected", f"{len(rejected_files)} 张")

    # delivery: check approved cards have contamination_risk and do_not_copy
    approved_issues = []
    for af in approved_files:
        try:
            ac = yaml.safe_load(af.read_text()) or {}
            if "contamination_risk" not in ac and "原作污染风险" not in af.read_text():
                approved_issues.append(f"{af.name}: 缺污染风险")
            if "do_not_copy" not in ac and "禁止复制" not in af.read_text():
                approved_issues.append(f"{af.name}: 缺禁止复制声明")
        except Exception:
            pass
    if approved_issues:
        for issue in approved_issues:
            if mode == "delivery":
                errors.append(f"approved 技法缺项: {issue}")
            else:
                warnings.append(f"approved 技法缺项: {issue}")

    # ── 8. Skill injection plan (Writer safety) ──
    si_has_plan = len(skill_plan_paths) > 0
    if si_has_plan:
        ppt = skill_plan_paths[0].read_text()
        writer_safety = {
            "forbids_raw_text": "Writer 禁止" in ppt or "writer_forbidden" in ppt or "Writer 不能" in ppt,
            "forbids_source_evidence": "source evidence" in ppt or "原文" in ppt,
            "forbids_candidate_assets": "candidate 技法" in ppt or "candidate" in ppt.lower(),
            "approved_only": "approved" in ppt.lower(),
            "all_four": False,
        }
        writer_safety["all_four"] = all([writer_safety["forbids_raw_text"], writer_safety["forbids_source_evidence"],
                                          writer_safety["forbids_candidate_assets"], writer_safety["approved_only"]])
        if mode == "delivery" and not writer_safety["all_four"]:
            missing_safety = [k for k, v in writer_safety.items() if not v and k != "all_four"]
            errors.append(f"Writer 安全声明不完整: 缺 {missing_safety}")
        check(writer_safety["all_four"], "Writer 安全声明",
              f"原文禁止={'✅' if writer_safety['forbids_raw_text'] else '❌'}, "
              f"evidence禁止={'✅' if writer_safety['forbids_source_evidence'] else '❌'}, "
              f"candidate禁止={'✅' if writer_safety['forbids_candidate_assets'] else '❌'}, "
              f"approved_only={'✅' if writer_safety['approved_only'] else '❌'}")
    else:
        if mode == "delivery":
            errors.append("skill_injection_plan 缺失")
        check(False, "Writer 安全声明", "无 plan 文件")

    # ── 9. Schemas ──
    schema_dir = phase8 / "schemas"
    expected_schemas = [
        "source_meta.schema.yaml", "manifest.schema.yaml", "chapter_card.schema.yaml",
        "chapter_fact_audit_report.schema.yaml", "reverse_story_bible.schema.yaml",
        "character_card.schema.yaml", "volume_structure_report.schema.yaml",
        "reader_debt_lifecycle.schema.yaml", "hook_payoff_map.schema.yaml",
        "craft_asset.schema.yaml", "skill_injection_plan.schema.yaml", "validation_report.schema.yaml",
    ]
    schema_ok = all((schema_dir / s).exists() for s in expected_schemas)
    check(schema_ok, "Schema 文件", f"{len(expected_schemas)} 个")

    # ── 10. Templates ──
    tmpl_dir = phase8 / "templates"
    expected_templates = [
        "source_meta.template.yaml", "manifest.template.yaml", "chapter_card.template.yaml",
        "chapter_fact_audit_report.template.md", "reverse_story_bible.template.md",
        "character_card.template.md", "volume_structure_report.template.md",
        "reader_debt_lifecycle.template.md", "hook_payoff_map.template.md",
        "craft_asset_card.template.md", "skill_injection_plan.template.md", "validation_report.template.md",
    ]
    tmpl_ok = all((tmpl_dir / t).exists() for t in expected_templates)
    check(tmpl_ok, "Template 文件", f"{len(expected_templates)} 个")

    # ── 11. Prompts ──
    prompt_dir = phase8 / "prompts"
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
    print(f"  模式: {mode}")
    print(f"  错误: {len(errors)}")
    for e in errors:
        print(f"    ❌ {e}")
    print(f"  警告: {len(warnings)}")
    for w in warnings:
        print(f"    ⚠️ {w}")
    print(f"{'=' * 50}\n")

    # ── 生成校验报告 JSON ──
    report = {
        "book_id": book_id,
        "mode": mode,
        "validated_at": now,
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "core_deliverables": core_results,
        "writer_safety": {
            "forbids_raw_text": writer_safety.get("forbids_raw_text", False) if si_has_plan else False,
            "forbids_source_evidence": writer_safety.get("forbids_source_evidence", False) if si_has_plan else False,
            "forbids_candidate_assets": writer_safety.get("forbids_candidate_assets", False) if si_has_plan else False,
            "approved_only": writer_safety.get("approved_only", False) if si_has_plan else False,
        } if si_has_plan else {},
        "directory_check": {"exists": not missing_dirs, "missing_dirs": missing_dirs},
        "source_meta_check": {"exists": sm_path.exists()},
        "manifest_check": {"exists": man_path.exists(), "chapter_index_count": len(manifest.get("chapter_index", [])) if manifest else 0},
        "chapters_check": {"chapter_count": len(ch_files) if ch_dir.exists() else 0, "expected_count": expected_chapters},
        "chapter_cards_check": {"card_count": len(cc_files) if cc_dir.exists() else 0, "expected_count": expected_chapters},
        "craft_assets_check": {"candidate_count": len(candidate_files), "approved_count": len(approved_files), "rejected_count": len(rejected_files)},
    }

    report_path = valid_dir / "validation_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"  报告: {report_path}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
