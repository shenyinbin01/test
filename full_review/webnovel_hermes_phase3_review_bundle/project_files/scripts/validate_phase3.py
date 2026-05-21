#!/usr/bin/env python3
"""
validate_phase3.py — 阶段三产物验证脚本

支持：
  --mode mock  验证 phase3_mock_run/
  --mode real  验证 phase3_real_run/ + deepseek_calls.jsonl

用法：
  python scripts/validate_phase3.py --mode mock
  python scripts/validate_phase3.py --mode real
"""

import os
import sys
import json
from pathlib import Path


CODE_ROOT = Path(os.environ.get("WEBNOVEL_CODE_ROOT", "/opt/webnovel-hermes-wps"))
DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


def check_file_exists(path):
    exists = path.exists()
    size = path.stat().st_size if exists else 0
    return {"path": str(path), "exists": exists, "size_bytes": size}


def check_file_not_contains(path, patterns):
    """检查文件不包含指定敏感模式"""
    if not path.exists():
        return {"checked": str(path), "exists": False, "issues": []}
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {"checked": str(path), "exists": True, "issues": ["无法读取文件内容"]}
    issues = []
    for pat in patterns:
        if pat.lower() in text.lower():
            issues.append(f"发现敏感模式: {pat}")
    return {"checked": str(path), "exists": True, "issues": issues}


def validate_mock(output_root):
    """验证阶段三 mock 输出"""
    run_dir = output_root / "phase3_mock_run"
    required = [
        "story_bible_mock.md",
        "story_bible_mock.json",
        "chapter_beat_mock.md",
        "chapter_beat_mock.json",
        "humanize_mock.md",
        "humanize_mock.json",
        "phase3_mock_summary.md",
        "phase3_mock_summary.json",
    ]

    errors = []
    warnings = []
    checked_files = []

    for fname in required:
        f = run_dir / fname
        result = check_file_exists(f)
        checked_files.append(result)
        if not result["exists"]:
            errors.append(f"缺少文件: {fname}")

    # 检查 JSON 可解析
    for fname in required:
        if not fname.endswith(".json"):
            continue
        f = run_dir / fname
        if f.exists():
            try:
                data = json.loads(f.read_text())
                checked_files.append({"path": str(f), "json_parsable": True})
            except (json.JSONDecodeError, Exception):
                errors.append(f"JSON 解析失败: {fname}")
                checked_files.append({"path": str(f), "json_parsable": False})

    return {
        "mode": "mock",
        "output_root": str(run_dir),
        "checked_files": checked_files,
        "missing_files": [f for f in required if not (run_dir / f).exists()],
        "errors": errors,
        "warnings": warnings,
        "passed": len(errors) == 0,
    }


def validate_real(output_root):
    """验证阶段三 real 输出"""
    run_dir = output_root / "phase3_real_run"
    log_dir = output_root / "phase3_logs"

    required = [
        "story_bible_real.md",
        "story_bible_real.json",
        "chapter_beat_real.md",
        "chapter_beat_real.json",
        "humanize_real.md",
        "humanize_real.json",
        "phase3_real_summary.md",
        "phase3_real_summary.json",
    ]

    errors = []
    warnings = []
    checked_files = []

    # 检查输出文件
    for fname in required:
        f = run_dir / fname
        result = check_file_exists(f)
        checked_files.append(result)
        if not result["exists"]:
            errors.append(f"缺少文件: {fname}")

    # 检查 JSON 可解析
    for fname in required:
        if not fname.endswith(".json"):
            continue
        f = run_dir / fname
        if f.exists():
            try:
                data = json.loads(f.read_text())
                checked_files.append({"path": str(f), "json_parsable": True, "keys": list(data.keys())})
            except (json.JSONDecodeError, Exception):
                errors.append(f"JSON 解析失败: {fname}")
                checked_files.append({"path": str(f), "json_parsable": False})

    # 检查 deepseek_calls.jsonl
    calls_log = log_dir / "deepseek_calls.jsonl"
    calls_check = check_file_exists(calls_log)
    checked_files.append(calls_check)
    if not calls_check["exists"]:
        errors.append("缺少 deepseek_calls.jsonl")
    else:
        # 解析并验证
        try:
            lines = calls_log.read_text(encoding="utf-8").strip().splitlines()
            if len(lines) < 3:
                errors.append(f"deepseek_calls.jsonl 记录不足 3 条 (实际 {len(lines)} 条)")
            else:
                task_names = set()
                for line in lines:
                    if not line.strip():
                        continue
                    try:
                        entry = json.loads(line)
                        task_names.add(entry.get("task_name", ""))
                        # 安全检查
                        content = json.dumps(entry)
                        for pat in ["sk-", "Authorization:", "API Key"]:
                            if pat.lower() in content.lower() and "[REDACTED]" not in content:
                                if pat == "sk-" and "sk-" not in content:
                                    continue
                                errors.append(f"deepseek_calls.jsonl 中发现敏感模式: {pat}")
                    except json.JSONDecodeError:
                        errors.append("deepseek_calls.jsonl 中存在非法 JSON 行")

                for required_task in ["story_bible", "chapter_beat", "humanize"]:
                    if required_task not in task_names:
                        errors.append(f"deepseek_calls.jsonl 缺少 task: {required_task}")

                # 检查是否有 success 字段
                for line in lines:
                    if not line.strip():
                        continue
                    try:
                        entry = json.loads(line)
                        if "success" not in entry:
                            errors.append("deepseek_calls.jsonl 记录缺少 success 字段")
                    except json.JSONDecodeError:
                        pass

        except Exception as e:
            errors.append(f"读取 deepseek_calls.jsonl 失败: {e}")

    # 检查 phase3_real_summary.json 的 summary
    summary_file = run_dir / "phase3_real_summary.json"
    if summary_file.exists():
        try:
            summary = json.loads(summary_file.read_text())
            if not summary.get("has_failure", True):
                if not summary.get("has_failure", True):
                    pass  # 正常通过
            else:
                errors.append("phase3_real_summary.json 中 has_failure=true")
        except Exception:
            pass

    return {
        "mode": "real",
        "output_root": str(run_dir),
        "log_path": str(calls_log),
        "checked_files": checked_files,
        "missing_files": [f for f in required if not (run_dir / f).exists()],
        "errors": errors,
        "warnings": warnings,
        "passed": len(errors) == 0,
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description="阶段三产物验证")
    parser.add_argument("--mode", required=True, choices=["mock", "real"],
                        help="验证模式: mock 或 real")
    parser.add_argument("--output-root", default=str(DATA_ROOT / "demo_output"),
                        help="输出根目录 (默认 /data/webnovel-lab/demo_output)")
    args = parser.parse_args()

    output_root = Path(args.output_root)

    if args.mode == "mock":
        result = validate_mock(output_root)
    else:
        result = validate_real(output_root)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
