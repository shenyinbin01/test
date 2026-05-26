#!/usr/bin/env python3
"""
validate_wps_project.py — Phase 6C: WPS 项目化验证工具

检查 projection 完整性、状态文件可解析性、安全脱敏。
支持 dry-run 和 real 模式验证。
"""

import os, sys, json, yaml
from pathlib import Path


def check(label, condition, detail=""):
    status = "✅" if condition else "❌"
    d = f" — {detail}" if detail else ""
    print(f"  {status} {label}{d}")
    return condition


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Phase 6C: WPS 项目化验证")
    parser.add_argument("--project", default="price_tag_life")
    parser.add_argument("--projection-root",
                        default="/data/webnovel-lab/demo_output/phase6c_wps_project_projection")
    parser.add_argument("--state-root",
                        default="/data/webnovel-lab/demo_output/phase6c_wps_project_state")
    parser.add_argument("--mode", choices=["dry-run", "real"], default="dry-run")
    args = parser.parse_args()

    proj_root = Path(args.projection_root)
    state_root = Path(args.state_root)
    mode = args.mode

    print(f"{'='*50}")
    print(f"  Phase 6C WPS 项目验证 — mode={mode}")
    print(f"  project: {args.project}")
    print(f"{'='*50}\n")

    errors = []
    warnings = []
    projection_checks = []
    sync_state_checks = []
    security_checks = []

    # ── Projection 检查 ──
    print("📂 Projection 检查")
    print("-" * 40)

    c = check("projection_root 存在", proj_root.exists(), str(proj_root))
    projection_checks.append({"check": "projection_root", "passed": c})

    manifest_path = proj_root / "wps_project_manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            c = check("manifest 可解析", True)
            projection_checks.append({"check": "manifest_parsable", "passed": c})
            c = check(f"  项目: {manifest.get('project_id','')}", True)
            c = check(f"  文档数: {len(manifest.get('documents',[]))}", True)
            c = check(f"  文件夹数: {len(manifest.get('folders',[]))}", True)
        except json.JSONDecodeError:
            errors.append("manifest.json 不可解析")
            c = check("manifest 可解析", False)
            projection_checks.append({"check": "manifest_parsable", "passed": False})
    else:
        errors.append("wps_project_manifest.json 不存在")
        projection_checks.append({"check": "manifest_exists", "passed": False})

    structure_path = proj_root / "wps_project_structure.yaml"
    if structure_path.exists():
        try:
            struct = yaml.safe_load(structure_path.read_text(encoding="utf-8"))
            c = check("structure 可解析", True)
            projection_checks.append({"check": "structure_parsable", "passed": c})
        except Exception:
            errors.append("wps_project_structure.yaml 不可解析")
            c = check("structure 可解析", False)
            projection_checks.append({"check": "structure_parsable", "passed": False})
    else:
        errors.append("wps_project_structure.yaml 不存在")
        projection_checks.append({"check": "structure_exists", "passed": False})

    # 必需 docx
    required_docs = {
        "volume_current": "publish/人生价格标签_第一卷_当前版.docx",
        "story_bible": "story_bible/人生价格标签_Story_Bible_当前版.docx",
        "wiki": "wiki/人生价格标签_小说Wiki_当前版.docx",
        "archive": None,  # 动态名
    }
    for dk, rel_path in required_docs.items():
        if rel_path:
            dp = proj_root / rel_path
            c = check(f"  docx {dk} 存在", dp.exists() and dp.stat().st_size > 0)
            projection_checks.append({"check": f"docx_{dk}", "passed": c})
            if not c:
                errors.append(f"缺少 docx: {dk}")
            # sha256
            sha_path = dp.with_suffix(".docx.sha256") if dp.suffix == ".docx" else None
            if sha_path and sha_path.exists():
                check(f"  sha256 {dk}", True)
            elif sha_path:
                warnings.append(f"缺少 sha256: {dk}")
        else:
            # archive 动态名查找
            arch_dir = proj_root / "archive"
            found = list(arch_dir.glob("*_第一卷前三章.docx"))
            if found:
                c = check(f"  docx archive 存在 ({found[0].name})", found[0].stat().st_size > 0)
            else:
                errors.append("缺少 archive docx")
                c = check("  docx archive 存在", False)
            projection_checks.append({"check": "docx_archive", "passed": c})

    # ════════ State 检查 ════════
    print()
    print("📂 State 检查")
    print("-" * 40)

    state_files = {
        "wps_project_doc_meta.json": "doc_meta",
        "wps_project_sync_log.json": "sync_log_json",
        "wps_project_sync_log.jsonl": "sync_log_jsonl",
        "wps_project_sync_plan.json": "sync_plan",
    }
    for sfname, key in state_files.items():
        sfp = state_root / sfname
        if sfp.exists():
            try:
                d = json.loads(sfp.read_text(encoding="utf-8"))
                c = check(f"  {sfname} 可解析", True)
                sync_state_checks.append({"check": f"{key}_parsable", "passed": True})
            except json.JSONDecodeError:
                errors.append(f"{sfname} 不可解析")
                c = check(f"  {sfname} 可解析", False)
                sync_state_checks.append({"check": f"{key}_parsable", "passed": False})
        else:
            warnings.append(f"{sfname} 不存在（state 可能为空）")
            sync_state_checks.append({"check": f"{key}_exists", "passed": False})

    # sync_log.jsonl 逐行检查
    jsonl_path = state_root / "wps_project_sync_log.jsonl"
    if jsonl_path.exists():
        line_ok = True
        for i, line in enumerate(jsonl_path.read_text(encoding="utf-8").strip().split("\n"), 1):
            if line.strip():
                try:
                    json.loads(line)
                except json.JSONDecodeError:
                    errors.append(f"syc_log.jsonl 第 {i} 行不是合法 JSON")
                    line_ok = False
        if line_ok:
            check("  sync_log.jsonl 所有行合法", True)

    # ── 模式特定检查 ──
    print()
    print("🔒 安全检查")
    print("-" * 40)
    sec_ok = True

    for root_dir in [proj_root, state_root]:
        if not root_dir.exists():
            continue
        for f in root_dir.rglob("*"):
            if f.is_file():
                try:
                    content = f.read_text(encoding="utf-8", errors="ignore")
                    for pattern, name in [("sk-", "API Key (sk-)"),
                                          ("Authorization", "Authorization"),
                                          ("token", "token"),
                                          ("cookie", "cookie"),
                                          ("password", "password"),
                                          ("file_id", "file_id"),
                                          ("folder_id", "folder_id"),
                                          ("link_id", "link_id"),
                                          ("doc_link", "doc_link")]:
                        # 仅检查对应目录下的非占位符出现
                        if pattern in content:
                            rel = f.relative_to(root_dir)
                            # 字段名允许出现
                            if f.suffix in (".json", ".yaml") and content.count(pattern) <= content.count("[REDACTED"):
                                continue
                            if pattern in ["token", "file_id", "folder_id", "link_id", "doc_link"] and content.count("[REDACTED") >= content.count(pattern):
                                continue
                            errors.append(f"安全检查: {rel} 包含 {name}")
                            sec_ok = False
                except:
                    pass

    c = check("无真实敏感信息", sec_ok)
    security_checks.append({"check": "no_sensitive_data", "passed": sec_ok})
    if not sec_ok:
        for e in errors:
            if "安全检查" in e:
                print(f"    ❌ {e}")

    # ════════ 模式验证 ════════
    if mode == "dry-run":
        meta_path = state_root / "wps_project_doc_meta.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                if meta.get("mode") == "real":
                    warnings.append("dry-run 模式下不应有 real 记录")
                elif meta.get("status") == "success":
                    warnings.append("dry-run 模式下 status 不应为 success")
            except:
                pass

    if mode == "real":
        meta_path = state_root / "wps_project_doc_meta.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                status = meta.get("status")
                if status == "skipped":
                    warnings.append("real 被跳过（WPS 配置不完整）")
            except:
                pass

    # ════════ 报告 ════════
    result = {
        "project_id": args.project,
        "mode": mode,
        "projection_checks": projection_checks,
        "sync_state_checks": sync_state_checks,
        "security_checks": security_checks,
        "errors": errors,
        "warnings": warnings,
        "passed": len(errors) == 0,
    }

    # 写结果
    state_root.mkdir(parents=True, exist_ok=True)
    (state_root / "validate_wps_project_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'='*50}")
    print(f"  验证结果: {'✅ 通过' if result['passed'] else '❌ 失败'}")
    print(f"  errors: {len(errors)}, warnings: {len(warnings)}")
    print(f"{'='*50}")

    if errors:
        for e in errors:
            print(f"  ❌ {e}")
    if warnings:
        for w in warnings:
            print(f"  ⚠️  {w}")

    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
