#!/usr/bin/env python3
"""
export_review_package.py — 把老板需要看的 7 个核心交付物汇总成 review package。

用法:
  python tools/phase8/export_review_package.py --book-id toy_book

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

PROJECT = Path("/opt/webnovel-hermes-wps")
PHASE8 = PROJECT / "production" / "phase8"


def read_or(path, default=""):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return default


def main():
    import argparse
    parser = argparse.ArgumentParser(description="生成老板审计汇总包")
    parser.add_argument("--book-id", required=True)
    args = parser.parse_args()

    book_id = args.book_id
    corpus = PHASE8 / "corpus" / book_id
    audit_dir = PHASE8 / "audit" / book_id
    reverse_dir = PHASE8 / "reverse_assets"
    craft_dir = PHASE8 / "craft_assets"
    skill_dir = PHASE8 / "skill_injection"
    valid_dir = PHASE8 / "validation"
    valid_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now().isoformat()
    lines = [
        f"# Phase 8 Review Package: {book_id}",
        f"> 生成时间: {now}",
        "",
        "---",
        "",
        "## 1. 章节事实审计表摘要",
        "",
    ]

    # 1. 审计报告摘要
    audit_report = audit_dir / "chapter_fact_audit_report.md"
    if audit_report.exists():
        text = read_or(audit_report)
        # 取前 30 行
        summary_lines = text.split("\n")[:30]
        lines.extend(summary_lines)
        lines.append("")
    else:
        lines.append("❌ **未就绪**: chapter_fact_audit_report.md 缺失")
        lines.append("")

    # 2. 逆向故事圣经
    lines.extend(["---", "", "## 2. 逆向故事圣经", ""])
    bible_paths = [
        reverse_dir / "reverse_story_bible.md",
        reverse_dir / book_id / "reverse_story_bible.md",
    ]
    bible_found = False
    for bp in bible_paths:
        if bp.exists():
            text = read_or(bp)
            head_lines = text.split("\n")[:15]
            lines.extend(head_lines)
            lines.append("")
            bible_found = True
            break
    if not bible_found:
        lines.append("❌ **未就绪**: reverse_story_bible.md 缺失")
        lines.append("")

    # 3. 人物卡列表
    lines.extend(["---", "", "## 3. 人物卡列表", ""])
    char_card_paths = [
        reverse_dir / "character_cards",
        reverse_dir / book_id / "character_cards",
    ]
    char_found = False
    for ccp in char_card_paths:
        if ccp.exists():
            cards = sorted(ccp.glob("*.md"))
            if cards:
                lines.append(f"共 {len(cards)} 张人物卡：")
                for c in cards:
                    name = c.stem
                    content = read_or(c)[:100].replace("\n", " ")
                    lines.append(f"- **{name}**: {content}...")
                char_found = True
                break
    if not char_found:
        lines.append("❌ **未就绪**: character_cards 缺失")
    lines.append("")

    # 4. 分卷结构
    lines.extend(["---", "", "## 4. 分卷结构摘要", ""])
    vol_paths = [
        reverse_dir / "volume_structure_report.md",
        reverse_dir / book_id / "volume_structure_report.md",
    ]
    vol_found = False
    for vp in vol_paths:
        if vp.exists():
            text = read_or(vp)
            head = text.split("\n")[:15]
            lines.extend(head)
            vol_found = True
            break
    if not vol_found:
        lines.append("❌ **未就绪**: volume_structure_report.md 缺失")
    lines.append("")

    # 5. 读者债生命周期
    lines.extend(["---", "", "## 5. 读者债生命周期 / 钩子兑现地图", ""])
    debt_paths = [
        reverse_dir / "reader_debt_lifecycle.md",
        reverse_dir / book_id / "reader_debt_lifecycle.md",
    ]
    hook_paths = [
        reverse_dir / "hook_payoff_map.md",
        reverse_dir / book_id / "hook_payoff_map.md",
    ]
    debt_found = False
    for dp in debt_paths:
        if dp.exists():
            lines.append(f"✅ reader_debt_lifecycle.md 存在 ({read_or(dp).split(chr(10))[0]})")
            debt_found = True
            break
    if not debt_found:
        lines.append("❌ **未就绪**: reader_debt_lifecycle.md 缺失")
    hook_found = False
    for hp in hook_paths:
        if hp.exists():
            lines.append(f"✅ hook_payoff_map.md 存在 ({read_or(hp).split(chr(10))[0]})")
            hook_found = True
            break
    if not hook_found:
        lines.append("❌ **未就绪**: hook_payoff_map.md 缺失")
    lines.append("")

    # 6. 技法资产
    lines.extend(["---", "", "## 6. 技法资产摘要", ""])
    for status in ["candidate", "approved", "rejected"]:
        d = craft_dir / status
        if d.exists():
            files = sorted(d.glob("*"))
            lines.append(f"- **{status}**: {len(files)} 个文件")
            for f in files:
                lines.append(f"  - {f.name}")
        else:
            lines.append(f"- **{status}**: 目录缺失")
    lines.append("")

    # 7. Skill 反哺方案
    lines.extend(["---", "", "## 7. Skill 反哺方案摘要", ""])
    plan_paths = list(skill_dir.glob("*.yaml")) + list(skill_dir.glob("*.md"))
    if plan_paths:
        for pp in plan_paths:
            head = read_or(pp).split("\n")[:10]
            lines.extend(head)
    else:
        lines.append("❌ **未就绪**: skill_injection_plan 缺失")
    lines.append("")

    # 8. 缺失项和风险项
    lines.extend(["---", "", "## 8. 缺失项和风险项", ""])
    missing_items = []
    if not audit_report.exists():
        missing_items.append("chapter_fact_audit_report.md")
    if not bible_found:
        missing_items.append("reverse_story_bible.md")
    if not char_found:
        missing_items.append("character_cards/")
    if not vol_found:
        missing_items.append("volume_structure_report.md")
    if not debt_found:
        missing_items.append("reader_debt_lifecycle.md")
    if not hook_found:
        missing_items.append("hook_payoff_map.md")
    if not plan_paths:
        missing_items.append("skill_injection_plan")
    if missing_items:
        lines.append("### 缺失项")
        for item in missing_items:
            lines.append(f"- ❌ {item}")
    else:
        lines.append("✅ 所有 7 个核心交付物均已就绪")
    lines.append("")

    output = "\n".join(lines)
    output_path = valid_dir / f"{book_id}_phase8_review_package.md"
    output_path.write_text(output, encoding="utf-8")
    print(f"  ✅ Review package 已生成: {output_path}")
    print(f"     行数: {len(lines)}, 文件大小: {len(output)} bytes")

    return 0


if __name__ == "__main__":
    sys.exit(main())
