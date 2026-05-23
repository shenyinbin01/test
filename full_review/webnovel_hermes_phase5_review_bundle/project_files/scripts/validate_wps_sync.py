#!/usr/bin/env python3
"""
validate_wps_sync.py — 阶段五 WPS 同步状态验证

验证内容：
  1. 投影文件完整性（6 个文件）
  2. dry-run 状态文件正确性
  3. real 状态文件正确性
  4. 安全性检查

支持参数：
  --projection-root  投影目录
  --state-root       状态目录
  --mode             dry-run / real
"""

import os
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime


DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


def check_file(path, label):
    """检查文件是否存在且非空"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False, "error": "文件不存在"}
    if p.stat().st_size == 0:
        return {"check": label, "exists": True, "error": "文件为空"}
    return {"check": label, "exists": True, "ok": True, "size_bytes": p.stat().st_size}


def check_json(path, label):
    """检查 JSON 可解析"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False, "error": "文件不存在"}
    try:
        data = json.loads(p.read_text())
        return {"check": label, "exists": True, "parsable": True, "keys": list(data.keys())}
    except Exception as e:
        return {"check": label, "exists": True, "parsable": False, "error": str(e)}


def check_jsonl(path, label):
    """检查 JSONL 每行可解析"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False, "error": "文件不存在"}
    lines = p.read_text().strip().split("\n")
    valid = 0
    invalid = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            json.loads(line)
            valid += 1
        except Exception:
            invalid += 1
    return {
        "check": label,
        "exists": True,
        "line_count": len(lines),
        "valid_lines": valid,
        "invalid_lines": invalid,
        "all_valid": invalid == 0,
    }


def check_security_no_urls(path, label):
    """检查文件不包含真实 WPS URL/file_id/link_id/folder_id"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False}
    content = p.read_text().lower()
    issues = []
    for keyword in ["kdocs.cn", "wps.cn", "file_id:", "link_id:", "folder_id:", "doc_link:"]:
        if keyword in content:
            # 检查是否是 [REDACTED] 后的残留
            lines = [l for l in content.split("\n") if keyword in l.lower()]
            for line in lines:
                if "[redacted]" not in line.lower():
                    issues.append(f"发现 {keyword}: {line.strip()[:80]}")
    return {"check": label, "issues": issues, "secure": len(issues) == 0}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="阶段五 WPS 同步状态验证")
    parser.add_argument("--projection-root", default=str(DATA_ROOT / "demo_output" / "phase5_wps_projection"))
    parser.add_argument("--state-root", default=str(DATA_ROOT / "demo_output" / "phase5_wps_state"))
    parser.add_argument("--mode", choices=["dry-run", "real"], default="dry-run", help="验证模式")
    args = parser.parse_args()

    proj_dir = Path(args.projection_root)
    state_dir = Path(args.state_root)
    mode = args.mode

    errors = []
    warnings = []
    projection_checks = []
    state_checks = []
    security_checks = []

    # ── 一、投影文件检查 ──
    required_files = [
        "price_tag_life_ch001.md",
        "price_tag_life_ch002.md",
        "price_tag_life_ch003.md",
        "price_tag_life_volume_001.md",
        "price_tag_life_volume_001.docx",
        "projection_manifest.json",
    ]
    for fname in required_files:
        result = check_file(proj_dir / fname, fname)
        projection_checks.append(result)
        if not result.get("ok"):
            errors.append(f"投影文件缺失或为空: {fname}")

    # Manifest 可解析检查
    manifest_check = check_json(proj_dir / "projection_manifest.json", "projection_manifest.json")
    projection_checks.append(manifest_check)
    if manifest_check.get("parsable"):
        manifest = json.loads((proj_dir / "projection_manifest.json").read_text())
        chapters = manifest.get("chapters", [])
        projection_checks.append({
            "check": "manifest_chapters_count",
            "count": len(chapters),
            "expected": 3,
        })
        if len(chapters) != 3:
            errors.append(f"projection_manifest.json chapters 数量为 {len(chapters)}，期望 3")
    else:
        errors.append("projection_manifest.json 无法解析")

    # ── 二、状态文件检查 ──
    meta_path = state_dir / "doc_meta.yaml"
    if meta_path.exists():
        meta_text = meta_path.read_text()
        try:
            meta = yaml.safe_load(meta_text)
            state_checks.append({
                "check": "doc_meta.yaml",
                "exists": True,
                "parsable": True,
                "status": meta.get("status"),
                "mode": meta.get("mode"),
            })
            if mode == "dry-run":
                if meta.get("status") != "dry_run":
                    warnings.append(f"dry-run 模式下 doc_meta.yaml status 应为 dry_run，实际为 {meta.get('status')}")
                if meta.get("mode") != "dry_run":
                    warnings.append(f"dry-run 模式下 doc_meta.yaml mode 应为 dry_run，实际为 {meta.get('mode')}")
                if "success" in str(meta.get("status")):
                    errors.append("dry-run 状态文件中不应出现 success")
            else:  # real
                if meta.get("status") not in ("success", "failed"):
                    warnings.append(f"real 模式下 doc_meta.yaml status 应为 success/failed，实际为 {meta.get('status')}")
                if meta.get("status") == "success":
                    bc = meta.get("business_code")
                    if bc != 0:
                        errors.append(f"real success 但 business_code 不为 0: {bc}")
        except Exception as e:
            state_checks.append({"check": "doc_meta.yaml", "exists": True, "parsable": False, "error": str(e)})
            errors.append(f"doc_meta.yaml 解析失败: {e}")
    else:
        state_checks.append({"check": "doc_meta.yaml", "exists": False})
        errors.append("doc_meta.yaml 不存在")

    # sync_log.jsonl
    log_path = state_dir / "sync_log.jsonl"
    if log_path.exists():
        log_check = check_jsonl(log_path, "sync_log.jsonl")
        state_checks.append(log_check)
        if not log_check.get("all_valid"):
            errors.append(f"sync_log.jsonl 有 {log_check.get('invalid_lines', 0)} 行无法解析")
    else:
        state_checks.append({"check": "sync_log.jsonl", "exists": False})
        errors.append("sync_log.jsonl 不存在")

    # ── 三、安全检查 ──
    for fname in ["doc_meta.yaml", "sync_log.jsonl"]:
        fp = state_dir / fname
        sec = check_security_no_urls(fp, f"{fname}_no_real_urls")
        security_checks.append(sec)
        if not sec.get("secure"):
            warnings.append(f"{fname} 可能包含真实 URL/file_id，需脱敏: {sec.get('issues')}")

    # 检查 __pycache__
    pycache_found = list(state_dir.rglob("__pycache__"))
    if pycache_found:
        warnings.append(f"状态目录中包含 __pycache__")

    # ── 最终判定 ──
    passed = len(errors) == 0

    result = {
        "mode": mode,
        "projection_root": str(proj_dir),
        "state_root": str(state_dir),
        "passed": passed,
        "errors": errors,
        "warnings": warnings,
        "projection_checks": projection_checks,
        "state_checks": state_checks,
        "security_checks": security_checks,
    }

    # 输出到文件
    result_path = state_dir / "validate_wps_sync_result.json"
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    # 终端输出
    print(f"[validate_wps_sync] mode={mode}")
    print(f"  errors: {len(errors)}")
    for e in errors:
        print(f"  ❌ {e}")
    for w in warnings:
        print(f"  ⚠️ {w}")
    print(f"  passed: {passed}")

    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
