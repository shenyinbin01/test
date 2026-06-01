#!/usr/bin/env python3
"""
validate_craft_assets.py — Phase 8 Craft Assets 校验脚本

用法:
    python tools/phase8/validate_craft_assets.py --book-id dachengqi --project-root .

检查项:
    1. manifest.yaml 可解析
    2. draft pattern 数量匹配
    3. rejected pattern 数量匹配
    4. 所有 pattern status 为 draft
    5. approved_patterns_generated=0
    6. 无原作人名
    7. 无原作专属设定词
    8. 每个 pattern 包含 How To Use
    9. 每个 pattern 包含 Original Contamination Guard
    10. 每个 pattern 包含 suggested_target_skill
    11. 每个 pattern 包含 Boundary
    12. 每个 pattern 包含 solves_writing_problem
"""

import argparse
import json
import sys
import re
from pathlib import Path

import yaml

try:
    from common import resolve_project_root
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from common import resolve_project_root


# ── 原作专属设定词黑名单 ──
FORBIDDEN_WORDS = [
    "人皇", "九州", "域外天魔", "天道", "大乘期", "逆袭系统",
    "人皇殿", "道宗", "天元皇朝", "须弥老佛", "长存仙翁",
    "江离", "白宏图", "玉隐", "净心圣女", "红尘仙子",
    "初帝", "闲人江离", "神藏教", "神藏尊者", "黑色潮汐",
    "时间长河", "成仙天梯", "姬止", "后土皇祇",
    "辟谷丹", "灵厨", "秦乱", "于丰", "袁五行",
    "张离", "钱离", "孔离",
]

# ── 原作人物名黑名单 ──
FORBIDDEN_NAMES = [
    "江离", "白宏图", "玉隐", "净心圣女", "红尘仙子",
    "长存仙翁", "须弥老佛", "初帝", "闲人江离", "姬止",
    "姬空空", "秦乱", "于丰", "袁五行", "张孔虎",
    "洛影", "布静", "李二", "如意葫芦",
]


def check_manifest(assets_dir: Path) -> dict:
    """检查 manifest.yaml"""
    manifest_path = assets_dir / "manifest.yaml"
    if not manifest_path.exists():
        return {"ok": False, "error": "manifest.yaml not found"}

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    errors = []

    # 1. manifest 可解析
    if manifest is None:
        return {"ok": False, "error": "manifest.yaml is empty or unparseable"}

    # 3. rejected pattern 数量
    reject_count = manifest.get("reject", None)
    if reject_count is None:
        errors.append("manifest 缺少 reject 字段")

    # 4. status
    if manifest.get("status") != "draft":
        errors.append(f"manifest status={manifest.get('status')}, expected 'draft'")

    # 5. approved_patterns_generated=0
    if manifest.get("approved_patterns_generated") != 0:
        errors.append(
            f"approved_patterns_generated={manifest.get('approved_patterns_generated')}, expected 0"
        )

    # 检查 forbidden_sources_checked
    if not manifest.get("forbidden_sources_checked"):
        errors.append("forbidden_sources_checked is not true")

    # 检查 original_contamination_check
    if not manifest.get("original_contamination_check"):
        errors.append("original_contamination_check is not true")

    return {
        "ok": len(errors) == 0,
        "error": "; ".join(errors) if errors else None,
        "manifest": manifest,
    }


def scan_pattern_files(assets_dir: Path) -> tuple[list[Path], list[Path]]:
    """扫描 draft 和 rejected 文件"""
    draft_files = []
    rejected_files = []

    # 排除非 pattern 目录
    skip_dirs = {""}  # root files like README.md, manifest.yaml

    for md_file in assets_dir.rglob("*.md"):
        rel = md_file.relative_to(assets_dir)
        if rel.parts[0] == "rejected_patterns":
            rejected_files.append(md_file)
        elif len(rel.parts) > 1:  # 在子目录中
            draft_files.append(md_file)

    return draft_files, rejected_files


def _extract_teachable_content(content: str) -> str:
    """提取卡片的教学部分：排除 Contamination Guard (8) 和 Evidence Source (9)"""
    lines = content.split("\n")
    result = []
    skip = False
    for line in lines:
        stripped = line.strip()
        # 进入跳过区：Contamination Guard 或 Evidence Source
        if stripped.startswith("## 8.") and "Contamination" in stripped:
            skip = True
            continue
        if stripped.startswith("## 9.") and "Evidence" in stripped:
            skip = True
            continue
        # 如果当前是跳过状态，遇到下一个 ## 或 ### 大标题就退出
        if skip and (stripped.startswith("## ") or stripped.startswith("### ")):
            skip = False
        if not skip:
            result.append(line)
    return "\n".join(result)


def check_pattern_card(filepath: Path) -> dict:
    """检查单张技法卡"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []
    warnings = []

    # 仅在"教学部分"检查原作污染（排除 Contamination Guard 和 Evidence Source）
    teachable = _extract_teachable_content(content)

    # 6. 无原作人名
    for name in FORBIDDEN_NAMES:
        if name in teachable:
            errors.append(f"发现原作人物名: '{name}'")

    # 7. 无原作专属设定词
    for word in FORBIDDEN_WORDS:
        if word in teachable:
            errors.append(f"发现原作设定词: '{word}'")

    # 8. 包含 How To Use
    if "How To Use" not in content:
        errors.append("缺少 How To Use 节")

    # 9. 包含 Original Contamination Guard
    if "Original Contamination Guard" not in content:
        errors.append("缺少 Original Contamination Guard 节")

    # 10. 包含 suggested_target_skill
    if "suggested_target_skill" not in content:
        errors.append("缺少 suggested_target_skill 字段")

    # 11. 包含 Boundary
    if "## 7. Boundary" not in content:
        errors.append("缺少 Boundary 节")

    # 12. 包含 solves_writing_problem
    if "Solves Writing Problem" not in content:
        errors.append("缺少 Solves Writing Problem 节")

    # 额外检查：status 字段
    if "status" in content:
        if not re.search(r'status["\s:|]+\s*draft', content):
            warnings.append("status 字段不是 draft")

    return {"ok": len(errors) == 0, "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description="Validate Phase 8 Craft Assets")
    parser.add_argument("--book-id", required=True, help="book identifier (e.g., dachengqi)")
    parser.add_argument("--project-root", default=".", help="project root directory")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    assets_dir = project_root / "production" / "phase8" / "craft_assets" / f"{args.book_id}_draft"

    if not assets_dir.exists():
        print(f"❌ Assets directory not found: {assets_dir}")
        sys.exit(1)

    all_ok = True
    results = {}

    # ── 1. 检查 manifest ──
    print("=" * 60)
    print("1. 检查 manifest.yaml")
    manifest_result = check_manifest(assets_dir)
    results["manifest"] = manifest_result
    if manifest_result["ok"]:
        print("   ✅ manifest.yaml 可解析，status=draft, approved=0")
    else:
        print(f"   ❌ {manifest_result['error']}")
        all_ok = False

    # ── 扫描文件 ──
    draft_files, rejected_files = scan_pattern_files(assets_dir)
    manifest = manifest_result.get("manifest", {})

    # ── 2. draft pattern 数量 ──
    print("=" * 60)
    print("2. 检查 draft pattern 数量")
    expected_draft = manifest.get("draft_patterns_generated", 20)
    actual_draft = len(draft_files)
    results["draft_count"] = {"expected": expected_draft, "actual": actual_draft}
    if actual_draft == expected_draft:
        print(f"   ✅ draft 数量匹配: {actual_draft} = {expected_draft}")
    else:
        print(f"   ❌ draft 数量不匹配: {actual_draft} != {expected_draft}")
        all_ok = False

    # ── 3. rejected pattern 数量 ──
    print("=" * 60)
    print("3. 检查 rejected pattern 数量")
    expected_reject = manifest.get("reject", 2)
    actual_reject = len(rejected_files)
    results["reject_count"] = {"expected": expected_reject, "actual": actual_reject}
    if actual_reject == expected_reject:
        print(f"   ✅ rejected 数量匹配: {actual_reject} = {expected_reject}")
    else:
        print(f"   ❌ rejected 数量不匹配: {actual_reject} != {expected_reject}")
        all_ok = False

    # ── 4-12. 逐卡检查 ──
    print("=" * 60)
    print("4-12. 逐卡检查")

    total_errors = 0
    total_warnings = 0

    for df in sorted(draft_files):
        rel = df.relative_to(assets_dir)
        card_result = check_pattern_card(df)
        results[str(rel)] = card_result

        if card_result["ok"]:
            if card_result["warnings"]:
                print(f"   ⚠️  {rel.name}: {len(card_result['warnings'])} warnings")
                total_warnings += len(card_result["warnings"])
            else:
                print(f"   ✅ {rel.name}")
        else:
            print(f"   ❌ {rel.name}: {'; '.join(card_result['errors'])}")
            total_errors += len(card_result["errors"])
            all_ok = False

    # ── 汇总 ──
    print("=" * 60)
    print("汇总")

    check_names = [
        "1. manifest.yaml 可解析",
        "2. draft pattern 数量",
        "3. rejected pattern 数量",
        "4. status 全部为 draft",
        "5. approved_patterns_generated=0",
        "6. 无原作人名",
        "7. 无原作专属设定词",
        "8. 包含 How To Use",
        "9. 包含 Original Contamination Guard",
        "10. 包含 suggested_target_skill",
        "11. 包含 Boundary",
        "12. 包含 solves_writing_problem",
    ]

    # 重新计算每项
    all_status_draft = True
    any_orig_name = False
    any_orig_word = False
    any_missing_howto = False
    any_missing_guard = False
    any_missing_skill = False
    any_missing_boundary = False
    any_missing_solves = False

    for key, cr in results.items():
        if key in ("manifest", "draft_count", "reject_count"):
            continue
        if isinstance(cr, dict) and "errors" in cr:
            for e in cr["errors"]:
                if "原作人物名" in e:
                    any_orig_name = True
                if "原作设定词" in e:
                    any_orig_word = True
                if "How To Use" in e:
                    any_missing_howto = True
                if "Original Contamination Guard" in e:
                    any_missing_guard = True
                if "suggested_target_skill" in e:
                    any_missing_skill = True
                if "Boundary" in e:
                    any_missing_boundary = True
                if "Solves Writing Problem" in e:
                    any_missing_solves = True

    checks = {
        "1. manifest.yaml 可解析": manifest_result["ok"],
        "2. draft pattern 数量": actual_draft == expected_draft,
        "3. rejected pattern 数量": actual_reject == expected_reject,
        "4. status 全部为 draft": manifest_result["ok"] and manifest.get("status") == "draft",
        "5. approved_patterns_generated=0": manifest_result["ok"] and manifest.get("approved_patterns_generated") == 0,
        "6. 无原作人名": not any_orig_name,
        "7. 无原作专属设定词": not any_orig_word,
        "8. 包含 How To Use": not any_missing_howto,
        "9. 包含 Original Contamination Guard": not any_missing_guard,
        "10. 包含 suggested_target_skill": not any_missing_skill,
        "11. 包含 Boundary": not any_missing_boundary,
        "12. 包含 solves_writing_problem": not any_missing_solves,
    }

    for name, passed in checks.items():
        if passed:
            print(f"   ✅ {name}")
        else:
            print(f"   ❌ {name}")
            all_ok = False

    print(f"\n   Total errors: {total_errors}, Total warnings: {total_warnings}")
    print(f"   Draft files: {actual_draft}, Rejected files: {actual_reject}")

    if all_ok:
        print("\n🎉 All checks passed!")
        sys.exit(0)
    else:
        print(f"\n❌ Validation failed with {total_errors} error(s)")
        sys.exit(1)


if __name__ == "__main__":
    main()
