#!/usr/bin/env python3
"""
build_chapter_fact_audit.py — 读取 chapter_cards，生成 chapter_fact_audit_report.md。

用法:
  python tools/phase8/build_chapter_fact_audit.py --book-id toy_book

输出:
  production/phase8/audit/{book_id}/chapter_fact_audit_report.md

要求:
  - 如果 chapter_card 缺失，必须在报告里标记
  - 如果 confidence low，必须列入低置信度章节
  - 如果 evidence 缺失，必须列入待复核项
  - 不能为了报告好看而隐藏问题
"""

import os, sys, yaml
from pathlib import Path
from datetime import datetime

PROJECT = Path("/opt/webnovel-hermes-wps")
PHASE8 = PROJECT / "production" / "phase8"
TEMPLATES = PHASE8 / "templates"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="生成章节事实审计报告")
    parser.add_argument("--book-id", required=True)
    args = parser.parse_args()

    book_id = args.book_id
    corpus = PHASE8 / "corpus" / book_id
    audit = PHASE8 / "audit" / book_id
    audit.mkdir(parents=True, exist_ok=True)

    manifest_path = corpus / "manifest.yaml"
    if not manifest_path.exists():
        print(f"❌ manifest.yaml 不存在: {manifest_path}")
        sys.exit(1)

    manifest = yaml.safe_load(manifest_path.read_text()) or {}
    title = manifest.get("title", book_id)
    expected_count = manifest.get("chapter_count", 0)

    # 读取 chapter_cards
    cards_dir = corpus / "chapter_cards"
    if not cards_dir.exists():
        print(f"❌ chapter_cards 目录不存在: {cards_dir}")
        sys.exit(1)

    card_files = sorted(cards_dir.glob("*.yaml"))
    card_map = {}
    for cf in card_files:
        card = yaml.safe_load(cf.read_text()) or {}
        ch = card.get("chapter_number", 0)
        card_map[ch] = card

    # 收集信息
    missing = []
    low_conf = []
    anomalous = []
    rows = []
    all_hooks_opened = 0
    all_hooks_paid = 0
    all_debts_opened = 0
    all_debts_paid = 0
    unresolved_hooks = []
    open_debts = []
    review_items = []

    for ch in range(1, expected_count + 1):
        if ch not in card_map:
            missing.append(ch)
            rows.append(f"| {ch} | — | — | — | — | — | — | — | — | — | — | 0 | — |")
            review_items.append(f"- [缺失] 第 {ch} 章 chapter_card 缺失")
            continue

        card = card_map[ch]
        ch_title = card.get("title", "")
        one_sentence = card.get("one_sentence", "")
        ch_func = card.get("chapter_function", "")
        proto_change = card.get("protagonist_state_change", "")
        chars = ", ".join(card.get("characters_present", []))[:40]
        hooks_open = card.get("hook_opened", [])
        hooks_pay = card.get("hook_paid", [])
        debts_open = card.get("reader_debts_opened", [])
        debts_pay = card.get("reader_debts_paid", [])
        ending = card.get("ending_pull", "")[:30]
        evidence_count = len(card.get("evidence", []))
        confidence = card.get("confidence", "unknown")

        all_hooks_opened += len(hooks_open)
        all_hooks_paid += len(hooks_pay)
        all_debts_opened += len(debts_open)
        all_debts_paid += len(debts_pay)

        unresolved_hooks.extend(hooks_open)
        open_debts.extend(debts_open)

        if confidence == "low":
            low_conf.append(ch)
            review_items.append(f"- [低置信度] 第 {ch} 章置信度为 low")

        if evidence_count == 0:
            review_items.append(f"- [待复核] 第 {ch} 章无 evidence")
            anomalous.append(ch)

        rows.append(
            f"| {ch} | {ch_title} | {one_sentence} | {ch_func} | {proto_change} | {chars} "
            f"| {len(hooks_open)} | {len(hooks_pay)} | {len(debts_open)} | {len(debts_pay)} "
            f"| {ending} | {evidence_count} | {confidence} |"
        )

    # 渲染模板
    template_path = TEMPLATES / "chapter_fact_audit_report.template.md"
    template = template_path.read_text()

    report = template.format(
        title=title,
        book_id=book_id,
        chapter_count=expected_count,
        chapters_audited=len(card_map),
        missing_count=len(missing),
        missing_chapters=str(missing) if missing else "无",
        low_confidence_chapters=str(low_conf) if low_conf else "无",
        anomalous_chapters=str(anomalous) if anomalous else "无",
        chapter_rows="\n".join(rows),
        total_hooks_opened=all_hooks_opened,
        total_hooks_paid=all_hooks_paid,
        unresolved_hooks=str(unresolved_hooks) if unresolved_hooks else "无",
        total_debts_opened=all_debts_opened,
        total_debts_paid=all_debts_paid,
        open_debts=str(open_debts) if open_debts else "无",
        review_items="\n".join(review_items) if review_items else "无",
    )

    output_path = audit / "chapter_fact_audit_report.md"
    output_path.write_text(report, encoding="utf-8")
    print(f"  ✅ 审计报告已生成: {output_path}")
    print(f"     总章节: {expected_count}, 已审计: {len(card_map)}, 缺失: {len(missing)}, 低置信度: {len(low_conf)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
