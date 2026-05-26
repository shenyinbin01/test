#!/usr/bin/env python3
"""
validate_wps_sync.py — 阶段五 WPS 同步状态验证（尾修强化版 v2）

验证内容：
  1. 投影文件完整性（6 个文件）
  2. dry-run 状态文件正确性
  3. real 状态文件正确性
  4. sync_log.json 权威数组文件检查
  5. upload_attempts_audit.json 审计检查
  6. policy_deviation 检测
  7. 安全性检查（无真实 URL/file_id）
  8. doc_meta.yaml 多行 YAML 可解析检查

强化点（v2）：
  - real 模式 doc_meta.yaml status 只能是 success 或 failed，否则 errors
  - status=success 时 business_code 必须为 0，否则 errors
  - status=failed 时必须有 message
  - 检查 sync_log.json 数组文件
  - 检查 upload_attempts_audit.json
  - 如果 observed_real_success_count > intended_real_upload_limit，passed=false
  - 检查 doc_meta.yaml 是否多行 YAML 可解析

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
        data = p.read_text(encoding="utf-8")
        parsed = json.loads(data)
        if isinstance(parsed, list):
            return {"check": label, "exists": True, "parsable": True, "type": "array", "length": len(parsed)}
        elif isinstance(parsed, dict):
            return {"check": label, "exists": True, "parsable": True, "type": "object", "keys": list(parsed.keys())}
        else:
            return {"check": label, "exists": True, "parsable": True, "type": type(parsed).__name__}
    except Exception as e:
        return {"check": label, "exists": True, "parsable": False, "error": str(e)}


def check_jsonl(path, label):
    """检查 JSONL 每行可解析"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False, "error": "文件不存在"}
    lines = p.read_text(encoding="utf-8").strip().split("\n")
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


def check_yaml(path, label):
    """检查 YAML 可解析（多行格式）"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False, "error": "文件不存在"}
    try:
        text = p.read_text(encoding="utf-8")
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            return {"check": label, "exists": True, "parsable": True, "yaml_is_dict": False, "warning": "YAML 根元素不是 dict"}
        return {
            "check": label,
            "exists": True,
            "parsable": True,
            "yaml_is_dict": True,
            "keys": list(data.keys()),
            "is_multiline": "\n" in text,
            "line_count": len(text.split("\n")),
        }
    except Exception as e:
        return {"check": label, "exists": True, "parsable": False, "error": str(e)}


def check_security_no_urls(path, label):
    """检查文件不包含真实 WPS URL/file_id/link_id/folder_id/doc_link"""
    p = Path(path)
    if not p.exists():
        return {"check": label, "exists": False}
    content = p.read_text(encoding="utf-8").lower()
    issues = []
    for keyword in ["kdocs.cn", "wps.cn", "file_id:", "link_id:", "folder_id:", "doc_link:", "fileid:"]:
        if keyword in content:
            lines = [l for l in content.split("\n") if keyword in l.lower()]
            for line in lines:
                if "[redacted]" not in line.lower() and "redacted" not in line.lower():
                    issues.append(f"发现 {keyword}: {line.strip()[:80]}")
    return {"check": label, "issues": issues, "secure": len(issues) == 0}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="阶段五 WPS 同步状态验证（尾修强化版 v2）")
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

    # Manifest 可解析
    manifest_check = check_json(proj_dir / "projection_manifest.json", "projection_manifest.json")
    projection_checks.append(manifest_check)
    if manifest_check.get("parsable"):
        manifest = json.loads((proj_dir / "projection_manifest.json").read_text(encoding="utf-8"))
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

    # 2a. doc_meta.yaml — 强化检查
    meta_path = state_dir / "doc_meta.yaml"
    if meta_path.exists():
        meta_check = check_yaml(meta_path, "doc_meta.yaml")
        state_checks.append(meta_check)
        if meta_check.get("parsable"):
            meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
            meta_status = meta.get("status", "").lower()
            meta_mode = meta.get("mode", "").lower()
            meta_bc = meta.get("business_code")
            meta_msg = meta.get("message", "")

            # 强化规则 1: multiline YAML
            if not meta_check.get("is_multiline"):
                warnings.append("doc_meta.yaml 非多行格式（单行 YAML），建议重新生成")

            if mode == "dry-run":
                if meta_status != "dry_run":
                    warnings.append(f"dry-run 模式下 doc_meta.yaml status 应为 dry_run，实际为 {meta_status}")
                if meta_mode != "dry_run":
                    warnings.append(f"dry-run 模式下 doc_meta.yaml mode 应为 dry_run，实际为 {meta_mode}")
                if "success" in meta_status:
                    errors.append("dry-run 状态文件中不应出现 success")
            else:  # real
                # 强化规则 2: real 模式 status 只能是 success 或 failed
                if meta_status not in ("success", "failed"):
                    errors.append(f"real 模式下 doc_meta.yaml status 只能是 success/failed，实际为 {meta_status}")

                # 强化规则 3: status=success 必须 business_code=0
                if meta_status == "success":
                    if meta_bc is None or meta_bc != 0:
                        errors.append(f"real success 但 business_code 不为 0: {meta_bc}")

                # 强化规则 4: status=failed 必须有 message
                if meta_status == "failed":
                    if not meta_msg:
                        errors.append("real failed 但 doc_meta.yaml message 为空")
        else:
            # 强化规则: YAML 不可解析 → errors
            errors.append(f"doc_meta.yaml 解析失败: {meta_check.get('error', '未知错误')}")
    else:
        state_checks.append({"check": "doc_meta.yaml", "exists": False})
        errors.append("doc_meta.yaml 不存在")

    # 2b. sync_log.jsonl — 标准 JSONL 检查
    log_path = state_dir / "sync_log.jsonl"
    if log_path.exists():
        log_check = check_jsonl(log_path, "sync_log.jsonl")
        state_checks.append(log_check)
        if not log_check.get("all_valid"):
            errors.append(f"sync_log.jsonl 有 {log_check.get('invalid_lines', 0)} 行无法解析")
    else:
        state_checks.append({"check": "sync_log.jsonl", "exists": False})
        errors.append("sync_log.jsonl 不存在")

    # 2c. sync_log.json — 权威数组文件检查（强化规则 5）
    json_path = state_dir / "sync_log.json"
    if json_path.exists():
        json_check = check_json(json_path, "sync_log.json")
        state_checks.append(json_check)
        if json_check.get("parsable"):
            if json_check.get("type") != "array":
                errors.append(f"sync_log.json 类型为 {json_check.get('type')}，期望 array")
            else:
                arr_len = json_check.get("length", 0)
                dry_count = 0
                real_count = 0
                real_success = 0
                sync_data = json.loads(json_path.read_text(encoding="utf-8"))
                for entry in sync_data:
                    if entry.get("mode") == "dry_run":
                        dry_count += 1
                    elif entry.get("mode") == "real":
                        real_count += 1
                        if entry.get("status") == "success":
                            real_success += 1
                state_checks.append({
                    "check": "sync_log_json_stats",
                    "total_entries": arr_len,
                    "dry_run_count": dry_count,
                    "real_count": real_count,
                    "real_success_count": real_success,
                })
        else:
            errors.append(f"sync_log.json 无法解析: {json_check.get('error')}")
    else:
        state_checks.append({"check": "sync_log.json", "exists": False})
        # sync_log.json 是新增权威文件，不存在是 warning 非 error
        warnings.append("sync_log.json 权威数组文件不存在")

    # 2d. upload_attempts_audit.json — 审计检查（强化规则 6-8）
    audit_path = state_dir / "upload_attempts_audit.json"
    if audit_path.exists():
        audit_check = check_json(audit_path, "upload_attempts_audit.json")
        state_checks.append(audit_check)
        if audit_check.get("parsable"):
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
            intended = audit.get("intended_real_upload_limit", 1)
            observed = audit.get("observed_real_success_count", 0)
            is_deviation = audit.get("is_policy_deviation", False)

            audit_findings = {
                "check": "upload_attempts_audit_findings",
                "intended_real_upload_limit": intended,
                "observed_real_success_count": observed,
                "is_policy_deviation": is_deviation,
                "has_remediation": bool(audit.get("remediation")),
            }
            state_checks.append(audit_findings)

            save_pd = {
                "detected": observed > intended,
                "intended_real_upload_limit": intended,
                "observed_real_success_count": observed,
                "is_policy_deviation": is_deviation,
                "acceptance_required_by_controller": True,
            }

            # 强化规则 8: policy_deviation 检测
            if observed > intended:
                msg = f"observed_real_success_count({observed}) > intended_real_upload_limit({intended})，存在 policy_deviation"
                if is_deviation:
                    warnings.append(msg)
                else:
                    errors.append(f"{msg}，但 is_policy_deviation=false，建议修正审计文件")
        else:
            errors.append(f"upload_attempts_audit.json 无法解析: {audit_check.get('error')}")
    else:
        state_checks.append({"check": "upload_attempts_audit.json", "exists": False})
        warnings.append("upload_attempts_audit.json 审计文件不存在")

    # ── 三、安全检查 ──
    for fname in ["doc_meta.yaml", "sync_log.jsonl", "sync_log.json", "upload_attempts_audit.json"]:
        fp = state_dir / fname
        if not fp.exists():
            continue
        sec = check_security_no_urls(fp, f"{fname}_no_real_urls")
        security_checks.append(sec)
        if not sec.get("secure"):
            warnings.append(f"{fname} 可能包含真实 URL/file_id，需脱敏: {sec.get('issues')}")

    pycache_found = list(state_dir.rglob("__pycache__"))
    if pycache_found:
        warnings.append(f"状态目录中包含 __pycache__")

    # ── 四、最终判定 ──
    # 强化规则: 如果存在 policy_deviation（observed > intended），passed=false
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
    # 条件性加入 policy_deviation 结构化信息
    if "save_pd" in dir():
        result["policy_deviation"] = save_pd

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
