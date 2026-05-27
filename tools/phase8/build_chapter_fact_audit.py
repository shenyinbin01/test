#!/usr/bin/env python3
"""
build_chapter_fact_audit.py — 读取 chapter_cards，生成 chapter_fact_audit_report.md。

用法:
  python tools/phase8/build_chapter_fact_audit.py --book-id toy_book --project-root .

输出:
  production/phase8/audit/{book_id}/chapter_fact_audit_report.md

要求:
  - 如果 chapter_card 缺失，必须在报告里标记
  - 如果 confidence low，必须列入低置信度章节
  - 如果 evidence 缺失，必须列入待复核项
  - 不能为了报告好看而隐藏问题
  - hook / reader_debt 按 ID 统计 opened、paid、unresolved
  - 旧字符串格式标记 legacy_unmatched
"""

import os, sys, yaml
from pathlib import Path
from datetime import datetime

# 确保项目根目录在 sys.path 中，支持直接运行
_THIS_FILE = Path(__file__).resolve()
for _p in [_THIS_FILE.parent.parent.parent, *_THIS_FILE.parents]:
    if (_p / "tools" / "phase8").exists():
        if str(_p) not in sys.path:
            sys.path.insert(0, str(_p))
        break

from tools.phase8.common import resolve_project_root


def _normalize_hook_debt(items):
    """
    统一处理 hook_opened / hook_paid / reader_debts_opened / reader_debts_paid。
    支持两种格式：
      - 新格式 dict: [{"id": "H001", "text": "..."}]
      - 旧格式 str:  ["三百万缺口"]
    返回 (ids_dict, legacy_list)
      ids_dict: {id: text/payoff}
      legacy_list: [text_string, ...]
    """
    ids = {}
    legacy = []
    for item in items:
        if isinstance(item, dict):
            iid = item.get("id", "")
            text = item.get("text") or item.get("payoff") or ""
            if iid:
                ids[iid] = text
            else:
                legacy.append(text or str(item))
        elif isinstance(item, str):
            legacy.append(item)
        else:
            legacy.append(str(item))
    return ids, legacy


def main():
    import argparse
    parser = argparse.ArgumentParser(description="生成章节事实审计报告")
    parser.add_argument("--book-id", required=True)
    parser.add_argument("--project-root", default=None, help="项目根目录，默认自动查找")
    args = parser.parse_args()

    project_root = resolve_project_root(args.project_root)
    phase8 = project_root / "production" / "phase8"
    templates_dir = phase8 / "templates"

    book_id = args.book_id
    corpus = phase8 / "corpus" / book_id
    audit = phase8 / "audit" / book_id
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

    # ── 收集信息 ──
    missing = []
    low_conf = []
    anomalous = []
    rows = []
    review_items = []

    # hook/debt ID 级统计
    all_hooks_opened_ids = {}
    all_hooks_paid_ids = {}
    all_debts_opened_ids = {}
    all_debts_paid_ids = {}
    legacy_unmatched_hooks = []
    legacy_unmatched_debts = []
    anomalous_paid_without_open_hooks = []
    anomalous_paid_without_open_debts = []

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
        hooks_open_raw = card.get("hook_opened", [])
        hooks_pay_raw = card.get("hook_paid", [])
        debts_open_raw = card.get("reader_debts_opened", [])
        debts_pay_raw = card.get("reader_debts_paid", [])
        ending = card.get("ending_pull", "")[:30]
        evidence_count = len(card.get("evidence", []))
        confidence = card.get("confidence", "unknown")

        # 规范化 hook/debt
        ho_ids, ho_legacy = _normalize_hook_debt(hooks_open_raw)
        hp_ids, hp_legacy = _normalize_hook_debt(hooks_pay_raw)
        do_ids, do_legacy = _normalize_hook_debt(debts_open_raw)
        dp_ids, dp_legacy = _normalize_hook_debt(debts_pay_raw)

        all_hooks_opened_ids.update(ho_ids)
        all_hooks_paid_ids.update(hp_ids)
        all_debts_opened_ids.update(do_ids)
        all_debts_paid_ids.update(dp_ids)
        legacy_unmatched_hooks.extend(ho_legacy + hp_legacy)
        legacy_unmatched_debts.extend(do_legacy + dp_legacy)

        # 检查 paid without open
        for hid in hp_ids:
            if hid not in ho_ids and hid not in all_hooks_opened_ids:
                anomalous_paid_without_open_hooks.append({"chapter": ch, "id": hid})
        for did in dp_ids:
            if did not in do_ids and did not in all_debts_opened_ids:
                anomalous_paid_without_open_debts.append({"chapter": ch, "id": did})

        if confidence == "low":
            low_conf.append(ch)
            review_items.append(f"- [低置信度] 第 {ch} 章置信度为 low")

        if evidence_count == 0:
            review_items.append(f"- [待复核] 第 {ch} 章无 evidence")
            anomalous.append(ch)

        rows.append(
            f"| {ch} | {ch_title} | {one_sentence} | {ch_func} | {proto_change} | {chars} "
            f"| {len(ho_ids) + len(ho_legacy)} | {len(hp_ids) + len(hp_legacy)} | {len(do_ids) + len(do_legacy)} | {len(dp_ids) + len(dp_legacy)} "
            f"| {ending} | {evidence_count} | {confidence} |"
        )

    # ── 计算 resolved / unresolved ──
    opened_ids = set(all_hooks_opened_ids.keys())
    paid_ids = set(all_hooks_paid_ids.keys())
    unresolved_ids = opened_ids - paid_ids
    resolved_ids = opened_ids & paid_ids
    unresolved_hooks_list = [{"id": hid, "text": all_hooks_opened_ids[hid]} for hid in sorted(unresolved_ids)]
    resolved_hooks_list = [{"id": hid} for hid in sorted(resolved_ids)]

    opened_debt_ids = set(all_debts_opened_ids.keys())
    paid_debt_ids = set(all_debts_paid_ids.keys())
    unresolved_debt_ids = opened_debt_ids - paid_debt_ids
    resolved_debt_ids = opened_debt_ids & paid_debt_ids
    unresolved_debts_list = [{"id": did, "text": all_debts_opened_ids[did]} for did in sorted(unresolved_debt_ids)]
    resolved_debts_list = [{"id": did} for did in sorted(resolved_debt_ids)]

    # ── 输出报告 ──
    lines = [
        "# 章节事实审计报告",
        "",
        f"> 书名：{title}",
        f"> 书籍 ID：{book_id}",
        f"> 总章节：{expected_count} | 已审计：{len(card_map)} | 缺失：{len(missing)}",
        "",
        "## 章节覆盖率",
        "",
        f"- 已审计章节：{len(card_map)}/{expected_count}",
        f"- 缺失章节：{str(missing) if missing else '无'}",
        f"- 低置信度章节：{str(low_conf) if low_conf else '无'}",
        f"- 异常章节：{str(anomalous) if anomalous else '无'}",
        "",
        "## 逐章事实表",
        "",
        "| 章 | 标题 | 一句话摘要 | 功能 | 主角状态变化 | 主要人物 | 钩子开启 | 钩子兑现 | 债开启 | 债兑现 | 章尾拉力 | 证据 | 置信度 |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    lines.extend(rows)

    lines += [
        "",
        "## 钩子 / 回收总览",
        "",
        f"- 总钩子开启（ID追踪）：{len(opened_ids)}",
        f"- 已兑现：{len(resolved_ids)}",
        f"- 未兑现：{len(unresolved_ids)}",
        f"- 未兑现详情：{unresolved_hooks_list if unresolved_hooks_list else '无'}",
        f"- legacy格式（未参与ID匹配）：{len(legacy_unmatched_hooks)}",
    ]
    if anomalous_paid_without_open_hooks:
        lines.append(f"- ⚠️ 兑现但无开启记录：{anomalous_paid_without_open_hooks}")

    lines += [
        "",
        "## 读者债总览",
        "",
        f"- 总债务开启（ID追踪）：{len(opened_debt_ids)}",
        f"- 已兑现：{len(resolved_debt_ids)}",
        f"- 未兑现：{len(unresolved_debt_ids)}",
        f"- 未兑现详情：{unresolved_debts_list if unresolved_debts_list else '无'}",
        f"- legacy格式（未参与ID匹配）：{len(legacy_unmatched_debts)}",
    ]
    if anomalous_paid_without_open_debts:
        lines.append(f"- ⚠️ 兑现但无开启记录：{anomalous_paid_without_open_debts}")

    lines += [
        "",
        "## 待人工复核事项",
        "",
    ]
    if review_items:
        lines.extend(review_items)
    else:
        lines.append("无")

    # 如果有 anomalous 或 legacy 也列出来
    if anomalous_paid_without_open_hooks:
        for a in anomalous_paid_without_open_hooks:
            lines.append(f"- [异常] 第 {a['chapter']} 章钩子 {a['id']} 已兑现但无开启记录")
    if anomalous_paid_without_open_debts:
        for a in anomalous_paid_without_open_debts:
            lines.append(f"- [异常] 第 {a['chapter']} 章债务 {a['id']} 已兑现但无开启记录")
    if legacy_unmatched_hooks:
        lines.append(f"- [legacy] {len(legacy_unmatched_hooks)} 个钩子使用旧字符串格式，未参与ID匹配")

    output_path = audit / "chapter_fact_audit_report.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  ✅ 审计报告已生成: {output_path}")
    print(f"     总章节: {expected_count}, 已审计: {len(card_map)}, 缺失: {len(missing)}, 低置信度: {len(low_conf)}")
    print(f"     钩子: opened={len(opened_ids)}, paid={len(resolved_ids)}, unresolved={len(unresolved_ids)}")
    print(f"     读者债: opened={len(opened_debt_ids)}, paid={len(resolved_debt_ids)}, unresolved={len(unresolved_debt_ids)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
