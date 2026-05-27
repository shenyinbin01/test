#!/usr/bin/env python3
"""
export_review_package.py — 把老板需要看的 7 个核心交付物汇总成 review package。

用法:
  python tools/phase8/export_review_package.py --book-id toy_book --project-root .

输出:
  production/phase8/validation/{book_id}/phase8_review_package.md

内容顺序:
  1. 章节事实审计表摘要
  2. 逆向故事圣经摘要
  3. 人物卡列表
  4. 分卷结构摘要
  5. 读者债生命周期摘要
  6. 候选 / approved / rejected 技法摘要
  7. Skill 反哺方案摘要
  8. 缺失项和风险项
"""

import os, sys, yaml, json
from pathlib import Path
from datetime import datetime

from tools.phase8.common import resolve_project_root


def read_or(path, default=""):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return default


def main():
    import argparse
    parser = argparse.ArgumentParser(description="生成老板审计汇总包")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None, help="项目根目录，默认自动查找")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"

    book_id = args.book_id
    corpus = phase8 / "corpus" / book_id
    audit_dir = phase8 / "audit" / book_id
    reverse_dir = phase8 / "reverse_assets"
    reverse_book_dir = reverse_dir / book_id
    craft = phase8 / "craft_assets"
    skill_dir = phase8 / "skill_injection"
    valid_dir = phase8 / "validation" / book_id
    valid_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now().isoformat()
    output_lines = [
        f"# Phase 8 Review Package: {book_id}",
        f"> 生成时间: {now}",
        "",
        "---",
        "",
        "## 1. 章节事实审计表摘要",
        "",
    ]

    # 收集缺失项
    missing_items = []

    # 1. 审计报告摘要
    audit_report = audit_dir / "chapter_fact_audit_report.md"
    if audit_report.exists():
        text = read_or(audit_report)
        summary_lines = text.split("\n")[:30]
        output_lines.extend(summary_lines)
        output_lines.append("")
    else:
        output_lines.append("❌ **未就绪**: chapter_fact_audit_report.md 缺失")
        output_lines.append("")
        missing_items.append("chapter_fact_audit_report.md")

    # 2. 逆向故事圣经
    output_lines.extend(["---", "", "## 2. 逆向故事圣经", ""])
    bible_found = False
    for bp in [reverse_book_dir / "reverse_story_bible.md", reverse_dir / "reverse_story_bible.md"]:
        if bp.exists():
            text = read_or(bp)
            output_lines.extend(text.split("\n")[:15])
            output_lines.append("")
            bible_found = True
            break
    if not bible_found:
        output_lines.append("❌ **未就绪**: reverse_story_bible.md 缺失")
        output_lines.append("")
        missing_items.append("reverse_story_bible.md")

    # 3. 人物卡列表
    output_lines.extend(["---", "", "## 3. 人物卡列表", ""])
    char_found = False
    for ccp in [reverse_book_dir / "character_cards", reverse_dir / "character_cards"]:
        if ccp.exists():
            cards = sorted(ccp.glob("*.md"))
            if cards:
                output_lines.append(f"共 {len(cards)} 张人物卡：")
                for c in cards:
                    name = c.stem
                    content = read_or(c)[:100].replace("\n", " ")
                    output_lines.append(f"- **{name}**: {content}...")
                char_found = True
                break
    if not char_found:
        output_lines.append("❌ **未就绪**: character_cards 缺失")
        missing_items.append("character_cards/")
    output_lines.append("")

    # 4. 分卷结构
    output_lines.extend(["---", "", "## 4. 分卷结构摘要", ""])
    vol_found = False
    for vp in [reverse_book_dir / "volume_structure_report.md", reverse_dir / "volume_structure_report.md"]:
        if vp.exists():
            text = read_or(vp)
            output_lines.extend(text.split("\n")[:15])
            vol_found = True
            break
    if not vol_found:
        output_lines.append("❌ **未就绪**: volume_structure_report.md 缺失")
        missing_items.append("volume_structure_report.md")
    output_lines.append("")

    # 5. 读者债生命周期 / 钩子兑现地图
    output_lines.extend(["---", "", "## 5. 读者债生命周期 / 钩子兑现地图", ""])
    debt_found = False
    for dp in [reverse_book_dir / "reader_debt_lifecycle.md", reverse_dir / "reader_debt_lifecycle.md"]:
        if dp.exists():
            output_lines.append(f"✅ reader_debt_lifecycle.md 存在")
            debt_found = True
            break
    if not debt_found:
        output_lines.append("❌ **未就绪**: reader_debt_lifecycle.md 缺失")
        missing_items.append("reader_debt_lifecycle.md")
    hook_found = False
    for hp in [reverse_book_dir / "hook_payoff_map.md", reverse_dir / "hook_payoff_map.md"]:
        if hp.exists():
            output_lines.append(f"✅ hook_payoff_map.md 存在")
            hook_found = True
            break
    if not hook_found:
        output_lines.append("❌ **未就绪**: hook_payoff_map.md 缺失")
        missing_items.append("hook_payoff_map.md")
    output_lines.append("")

    # 6. 技法资产
    output_lines.extend(["---", "", "## 6. 技法资产摘要", ""])
    for status in ["candidate", "approved", "rejected"]:
        files_found = []
        for d in [craft / status, craft / book_id / status]:
            if d.exists():
                files_found.extend(sorted(d.glob("*")))
        files_found = [f for f in files_found if f.name != ".gitkeep"]
        if files_found:
            output_lines.append(f"- **{status}**: {len(files_found)} 个文件")
            for f in files_found:
                output_lines.append(f"  - {f.name}")
        else:
            output_lines.append(f"- **{status}**: 无")
    output_lines.append("")

    # 7. Skill 反哺方案
    output_lines.extend(["---", "", "## 7. Skill 反哺方案摘要", ""])
    plan_paths = list(skill_dir.glob("*.yaml")) + list(skill_dir.glob("*.md"))
    skill_found = False
    if plan_paths:
        for pp in plan_paths:
            head = read_or(pp).split("\n")[:10]
            output_lines.extend(head)
            skill_found = True
            break
    if not skill_found:
        output_lines.append("❌ **未就绪**: skill_injection_plan 缺失")
        missing_items.append("skill_injection_plan")
    output_lines.append("")

    # 8. 缺失项和风险项
    output_lines.extend(["---", "", "## 8. 缺失项和风险项", ""])
    if missing_items:
        output_lines.append("### 缺失项")
        for item in missing_items:
            output_lines.append(f"- ❌ {item}")
    else:
        output_lines.append("✅ 所有 7 个核心交付物均已就绪")
    output_lines.append("")

    output = "\n".join(output_lines)
    output_path = valid_dir / "phase8_review_package.md"
    output_path.write_text(output, encoding="utf-8")
    print(f"  ✅ Review package 已生成: {output_path}")
    print(f"     行数: {len(output_lines)}, 文件大小: {len(output)} bytes")
    if missing_items:
        print(f"     ⚠️ 缺失 {len(missing_items)} 项: {missing_items}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
