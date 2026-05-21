#!/usr/bin/env python3
"""
validate_canon_consistency.py — 对 phase3 real 输出做规则级 canon 一致性检查

检查内容：
- 禁止词和禁止模式（天秤会、生命倒计时、消耗寿命等）
- 必要的正向锚点（林砚、外卖员、人生价格标签等）
- 支持否定句豁免和语境豁免

输出 canon_consistency_report.json，passed=true 时退出 0，否则退出 1。
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime


# ── 配置 ─────────────────────────────────────────────────────

DEFAULT_OUTPUT_ROOT = Path("/data/webnovel-lab/demo_output")
DEFAULT_CANON = Path("/data/webnovel-lab/workspace/novels/price_tag_life/canon_constraints.yaml")

# 禁止模式（具体化，减少伪阳性）
FORBIDDEN_PATTERNS = [
    r"天秤会",
    r"系统面板",
    r"系统任务",
    r"任务奖励",
    r"系统充值",
    r"充值入口",
    r"充值商城",
    r"充值获得",
    r"氪金",
    r"商城充值",
    r"充值点数",
    r"充值兑换",
    r"消耗寿命",
    r"寿命换",
    r"生命倒计时",
    r"触碰改变命运",
    r"触碰改写命运",
    r"父母早逝",
    r"母亲去世",
    r"父亲已死",
    r"父亲死亡",
    r"全球异能",
    r"等级体系",
    r"心电图同步",
    r"生命数值同步",
]

# 旧有的大范围模式，用于发现但需要上下文豁免
WIDE_PATTERNS = {
    "倒计时": {"type": "negation_check", "negation_prefixes": ["不是", "并非", "不等于", "不是死亡", "不是生命", "并非死亡", "并非生命", "不等于死亡", "不等于生命"]},
    "充值": {"type": "context_check", "allowed_context": ["医院", "缴费", "住院费", "余额不足", "窗口", "电子提示音"]},
    "商城": {"type": "negation_check", "negation_prefixes": ["不是", "并非"]},
}

REQUIRED_ANCHORS = [
    "林砚",
    "外卖员",
    "父亲病重",
    "人生价格标签",
    "不是单纯财富",
    "选择代价",
    "头痛",
    "短暂失明",
    "医院缴费窗口",
    "即将归零",
]


def load_canon(file_path):
    """加载 canon_constraints.yaml"""
    import yaml
    if file_path.exists():
        return yaml.safe_load(file_path.read_text())
    return {}


def load_file_text(file_path):
    """读取文件内容，失败返回空字符串"""
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception:
        return ""


def strip_self_check_section(file_text):
    """去除 canon_check / self-check 自检段落，只返回正文"""
    for marker in ["canon_check", "self-check", "输出前自检", "# self-check strict"]:
        if marker in file_text:
            idx = file_text.find(marker)
            if idx > 0:
                before = file_text[:idx]
                last_newline = before.rfind("\n")
                if last_newline > 0:
                    file_text = before[:last_newline]
                else:
                    file_text = before
    return file_text


def get_context(text, match_pos, context_chars=20):
    """获取匹配位置前后的上下文文本"""
    start = max(0, match_pos - context_chars)
    end = min(len(text), match_pos + context_chars)
    return text[start:end]


def is_negated(text, match_pos, pattern, negation_prefixes):
    """
    判断匹配位置是否处于否定语境中。
    检查 match_pos 前 15 个字符内是否出现否定前缀。
    """
    lookback_start = max(0, match_pos - 15)
    context_before = text[lookback_start:match_pos]
    for prefix in negation_prefixes:
        if prefix in context_before:
            return True
    return False


def is_allowed_payment_context(text, match_pos):
    """
    判断"充值"的上下文是否为医院缴费场景。
    """
    start = max(0, match_pos - 40)
    end = min(len(text), match_pos + 40)
    context = text[start:end]
    allowed_words = ["医院", "缴费", "住院费", "余额不足", "窗口", "电子提示音"]
    for w in allowed_words:
        if w in context:
            return True
    return False


def check_forbidden_with_exemptions(file_text, patterns, wide_patterns):
    """
    检查文本中是否出现禁止模式，支持否定句豁免和语境豁免。
    
    返回:
        hits: 真实 forbidden hits
        ignored: 被豁免的命中
    """
    # 先去自检段
    clean_text = strip_self_check_section(file_text)
    
    # 先检查精确模式
    hits = []
    ignored = []
    
    for pattern in patterns:
        for m in re.finditer(pattern, clean_text):
            match_text = m.group()
            match_pos = m.start()
            ctx = get_context(clean_text, match_pos, 20)
            hits.append({
                "pattern": pattern,
                "match": match_text,
                "position": match_pos,
                "context": ctx,
            })
    
    # 检查大范围模式（需要上下文判断）
    for pattern, rules in wide_patterns.items():
        for m in re.finditer(pattern, clean_text):
            match_text = m.group()
            match_pos = m.start()
            ctx = get_context(clean_text, match_pos, 20)
            
            exempted = False
            reason = None
            
            if rules.get("type") == "negation_check":
                prefixes = rules.get("negation_prefixes", [])
                if is_negated(clean_text, match_pos, pattern, prefixes):
                    exempted = True
                    reason = "negated_context"
            
            if rules.get("type") == "context_check":
                allowed = rules.get("allowed_context", [])
                if is_allowed_payment_context(clean_text, match_pos):
                    exempted = True
                    reason = "allowed_payment_context"
            
            if exempted:
                ignored.append({
                    "pattern": pattern,
                    "match": match_text,
                    "reason": reason,
                    "context": ctx,
                })
            else:
                hits.append({
                    "pattern": pattern,
                    "match": match_text,
                    "position": match_pos,
                    "context": ctx,
                })
    
    return hits, ignored


def check_required_anchors(file_text, anchors):
    """检查必要的锚点是否保留，返回缺失列表和保留列表"""
    present = []
    missing = []
    for anchor in anchors:
        if anchor in file_text:
            present.append(anchor)
        else:
            missing.append(anchor)
    return present, missing


def check_file(path, forbidden_patterns, wide_patterns, required_anchors, file_label):
    """对单个文件执行一致性检查"""
    content = load_file_text(path)
    if not content:
        return {
            "file": str(path),
            "label": file_label,
            "readable": False,
            "forbidden_hits": [],
            "ignored_hits": [],
            "anchor_present": [],
            "anchor_missing": [],
        }

    forbidden_hits, ignored_hits = check_forbidden_with_exemptions(content, forbidden_patterns, wide_patterns)
    anchor_present, anchor_missing = check_required_anchors(content, required_anchors)

    return {
        "file": str(path),
        "label": file_label,
        "readable": True,
        "forbidden_hits": forbidden_hits,
        "ignored_hits": ignored_hits,
        "anchor_present": anchor_present,
        "anchor_missing": anchor_missing,
    }


def validate(output_root, canon_file, mode="real"):
    """主验证逻辑"""
    canon = load_canon(canon_file)
    real_run_dir = output_root / "phase3_real_run"

    check_files = [
        (real_run_dir / "story_bible_real.md", "story_bible_real.md", REQUIRED_ANCHORS),
        (real_run_dir / "chapter_beat_real.md", "chapter_beat_real.md", REQUIRED_ANCHORS),
        (real_run_dir / "humanize_real.md", "humanize_real.md", REQUIRED_ANCHORS),
    ]

    all_hits = []
    all_ignored = []
    all_anchor_checks = []
    errors = []
    warnings = []
    checked_files = []

    for file_path, label, anchors in check_files:
        if not file_path.exists():
            errors.append(f"文件不存在: {label}")
            continue

        result = check_file(file_path, FORBIDDEN_PATTERNS, WIDE_PATTERNS, anchors, label)
        checked_files.append(result)

        if not result["readable"]:
            errors.append(f"无法读取: {label}")
            continue

        if result["forbidden_hits"]:
            for hit in result["forbidden_hits"]:
                all_hits.append(hit)
                errors.append({
                    "type": "forbidden_hit",
                    "file": label,
                    "pattern": hit["pattern"],
                    "match": hit["match"],
                    "context": hit.get("context", ""),
                })

        if result["ignored_hits"]:
            for hit in result["ignored_hits"]:
                all_ignored.append({
                    "file": label,
                    "pattern": hit["pattern"],
                    "match": hit["match"],
                    "reason": hit.get("reason", "unknown"),
                    "context": hit.get("context", ""),
                })

        if result["anchor_missing"]:
            if label == "chapter_beat_real.md":
                if "医院缴费窗口" in result["anchor_missing"]:
                    warnings.append(f"{label}: 缺少关键锚点 '医院缴费窗口'")
                if "即将归零" in result["anchor_missing"]:
                    warnings.append(f"{label}: 缺少关键锚点 '即将归零'")

        all_anchor_checks.append({
            "file": label,
            "present": result["anchor_present"],
            "missing": result["anchor_missing"],
        })

    if all_ignored:
        warnings.append(f"免除 {len(all_ignored)} 次伪阳性（缺省语境）")

    # 判定通过条件
    passed = (len(all_hits) == 0 and len(errors) == 0)

    # 构建报告
    report = {
        "mode": mode,
        "canon_file": str(canon_file),
        "checked_time": datetime.now().isoformat(),
        "checked_files": checked_files,
        "forbidden_hits": all_hits,
        "ignored_hits": all_ignored,
        "required_anchor_checks": all_anchor_checks,
        "errors": errors,
        "warnings": warnings,
        "passed": passed,
    }

    # 输出报告
    report_dir = output_root / "phase3_logs"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / "canon_consistency_report.json"
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"  Canon consistency: {'✅ PASS' if passed else '❌ FAIL'}")
    if all_hits:
        print(f"    Forbidden hits: {len(all_hits)}")
    if all_ignored:
        print(f"    Ignored (exempted): {len(all_ignored)}")
    if errors:
        print(f"    Errors: {len(errors)}")
    if warnings:
        for w in warnings:
            print(f"    ⚠️  {w}")

    print(f"    Report: {report_path}")
    return report


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Canon 一致性检查")
    parser.add_argument("--mode", choices=["real", "mock"], default="real",
                        help="模式（默认 real）")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT),
                        help="输出根目录 (默认 /data/webnovel-lab/demo_output)")
    parser.add_argument("--canon", default=str(DEFAULT_CANON),
                        help="canon 约束文件路径")
    args = parser.parse_args()

    output_root = Path(args.output_root)
    canon_file = Path(args.canon)

    print(f"  [validate_canon_consistency] mode={args.mode}")
    print(f"  Canon 文件: {canon_file}")
    print()

    report = validate(output_root, canon_file, mode=args.mode)

    if report["passed"]:
        print("\n  ✅ Canon consistency 通过")
        sys.exit(0)
    else:
        print("\n  ❌ Canon consistency 未通过")
        sys.exit(1)


if __name__ == "__main__":
    main()
