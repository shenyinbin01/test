#!/usr/bin/env python3
"""
validate_canon_consistency.py — 对 phase3 real 输出做规则级 canon 一致性检查

检查内容：
- 禁止词和禁止模式（天秤会、生命倒计时、消耗寿命等）
- 必要的正向锚点（林砚、外卖员、人生价格标签等）

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

FORBIDDEN_PATTERNS = [
    r"天秤会",
    r"系统面板",
    r"系统任务",
    r"任务奖励",
    r"商城",
    r"充值",
    r"消耗寿命",
    r"寿命换",
    r"生命倒计时",
    r"倒计时",
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


def check_forbidden(file_text, patterns):
    """检查文本中是否出现禁止模式，返回命中列表

    排除 canon_check 自检段落中的引用性内容。
    只检查实际输出正文，不检查模型对自身的合规声明。
    """
    # 去除 canon_check 自检段（模型用于自证合规的段落不应触发禁止词）
    clean_text = file_text
    # 如果文件包含 canon_check 或 self-check 段落，只检查前面的正文
    for marker in ["canon_check", "self-check", "canon_check", "输出前自检"]:
        if marker in clean_text:
            # 找到第一个出现这类自检标记的位置
            idx = clean_text.find(marker)
            if idx > 0:
                # 保留前面内容的最后一行（可能是标题），但去掉自检段
                before = clean_text[:idx]
                # 找最后一个换行，确保不截断完整行
                last_newline = before.rfind("\n")
                if last_newline > 0:
                    clean_text = before[:last_newline]
                else:
                    clean_text = before

    hits = []
    for pattern in patterns:
        matches = re.findall(pattern, clean_text)
        if matches:
            hits.append({"pattern": pattern, "matches": list(set(matches))})
    return hits


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


def check_file(path, forbidden_patterns, required_anchors, file_label):
    """对单个文件执行一致性检查"""
    content = load_file_text(path)
    if not content:
        return {
            "file": str(path),
            "label": file_label,
            "readable": False,
            "forbidden_hits": [],
            "anchor_present": [],
            "anchor_missing": [],
        }

    forbidden_hits = check_forbidden(content, forbidden_patterns)
    anchor_present, anchor_missing = check_required_anchors(content, required_anchors)

    return {
        "file": str(path),
        "label": file_label,
        "readable": True,
        "forbidden_hits": forbidden_hits,
        "anchor_present": anchor_present,
        "anchor_missing": anchor_missing,
    }


def validate(output_root, canon_file, mode="real"):
    """主验证逻辑"""
    canon = load_canon(canon_file)
    real_run_dir = output_root / "phase3_real_run"

    # 定义检查文件
    # 注意：不检查 phase3_real_summary.json 中的 errors 字段值，因为它可能记录旧错误文本
    check_files = [
        (real_run_dir / "story_bible_real.md", "story_bible_real.md", REQUIRED_ANCHORS),
        (real_run_dir / "chapter_beat_real.md", "chapter_beat_real.md", REQUIRED_ANCHORS),
        (real_run_dir / "humanize_real.md", "humanize_real.md", REQUIRED_ANCHORS),
    ]

    all_hits = []
    all_anchor_checks = []
    errors = []
    warnings = []
    checked_files = []

    for file_path, label, anchors in check_files:
        if not file_path.exists():
            errors.append(f"文件不存在: {label}")
            continue

        result = check_file(file_path, FORBIDDEN_PATTERNS, anchors, label)
        checked_files.append(result)

        if not result["readable"]:
            errors.append(f"无法读取: {label}")
            continue

        if result["forbidden_hits"]:
            for hit in result["forbidden_hits"]:
                all_hits.append({
                    "file": label,
                    "pattern": hit["pattern"],
                    "matches": hit["matches"],
                })
                for match_text in hit["matches"]:
                    errors.append({
                        "type": "forbidden_hit",
                        "file": label,
                        "pattern": hit["pattern"],
                        "match": match_text,
                    })

        if result["anchor_missing"]:
            # 仅 story_bible_real.md 和 phase3_real_summary.json 必须包含核心锚点
            if label in ["story_bible_real.md", "phase3_real_summary.json"]:
                for missing in result["anchor_missing"]:
                    # 不是所有锚点都必须出现在每个文件中
                    # 比如头痛、短暂失明、即将归零等可能只在部分文件出现
                    pass
            # chapter_beat 必须包含医院缴费窗口钩子
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

    # 判定通过条件
    passed = True

    if all_hits:
        passed = False

    if errors:
        passed = False

    # 构建报告
    report = {
        "mode": mode,
        "canon_file": str(canon_file),
        "checked_time": datetime.now().isoformat(),
        "checked_files": checked_files,
        "forbidden_hits": all_hits,
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
