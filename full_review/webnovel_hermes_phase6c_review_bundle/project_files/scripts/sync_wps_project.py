#!/usr/bin/env python3
"""
sync_wps_project.py — Phase 6C: WPS 项目化同步工具

支持 dry-run 和 real 模式。
只同步允许的 4 个 docx 文档。
不修改 .story-system，不修改正文。
"""

import os, sys, json, uuid, base64, subprocess
from pathlib import Path
from datetime import datetime

ALLOWED_DOC_KEYS = {"volume_current", "story_bible", "wiki", "archive"}

def generate_run_id():
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")
    return f"phase6c-{ts}-{str(uuid.uuid4())[:8]}"

def parse_kdocs_result(stdout):
    text = stdout.strip()
    if not text:
        return None, None, "stdout 为空"
    start = text.find("{")
    if start == -1:
        return None, None, "不是 JSON 格式"
    depth, end = 0, -1
    for i in range(start, len(text)):
        if text[i] == "{": depth += 1
        elif text[i] == "}": depth -= 1
        if depth == 0: end = i + 1; break
    if end == -1:
        return None, None, "无法找到完整 JSON"
    try:
        data = json.loads(text[start:end])
    except json.JSONDecodeError as e:
        return None, None, f"JSON 解析失败: {e}"
    code = data.get("code")
    if code is None:
        return None, None, "无 code 字段"
    if code == 0:
        return True, 0, "success"
    msg = data.get("message", "未知错误")
    return False, code, f"业务失败 (code={code}): {msg}"

def redact_env_val(key, val):
    return "[REDACTED]" if val and val != "0" else val

def read_env_file(path):
    p = Path(path)
    if not p.exists(): return ""
    try:
        return p.read_text()
    except PermissionError:
        return ""

def get_env_value(content, key):
    for line in content.splitlines():
        line = line.strip()
        if line.startswith(f"{key}="):
            return line.split("=", 1)[1].strip()
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Phase 6C: WPS 项目化同步")
    parser.add_argument("--project", default="price_tag_life")
    parser.add_argument("--projection-root", default="/data/webnovel-lab/demo_output/phase6c_wps_project_projection")
    parser.add_argument("--state-root", default="/data/webnovel-lab/demo_output/phase6c_wps_project_state")
    parser.add_argument("--dry-run", action="store_true", default=True)
    parser.add_argument("--real", action="store_true")
    args = parser.parse_args()

    proj_root = Path(args.projection_root)
    state_root = Path(args.state_root)
    state_root.mkdir(parents=True, exist_ok=True)

    is_dry_run = not args.real
    run_id = generate_run_id()
    sync_time = datetime.now().isoformat()

    print(f"{'='*50}")
    print(f"  Phase 6C WPS 项目同步 — {'dry-run' if is_dry_run else 'real'}")
    print(f"  run_id: {run_id}")
    print(f"{'='*50}\n")

    # 1. 读取 manifest
    manifest_path = proj_root / "wps_project_manifest.json"
    if not manifest_path.exists():
        print(f"❌ manifest 不存在: {manifest_path}")
        sys.exit(1)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    print(f"✅ manifest 已读取: {manifest['project_id']} / {manifest['title']}")
    print(f"   文档数: {len(manifest['documents'])}")

    # 2. 生成 sync plan
    plan_entries = []
    for doc in manifest["documents"]:
        if doc["doc_key"] not in ALLOWED_DOC_KEYS:
            print(f"  ⏭ 跳过未允许文档: {doc['doc_key']}")
            continue
        local_path = Path(doc["local_path"])
        if not local_path.exists():
            print(f"  ❌ 本地文件不存在: {doc['title']} ({local_path})")
            continue
        plan_entries.append({
            "doc_key": doc["doc_key"],
            "title": doc["title"],
            "local_path": str(local_path),
            "target_folder": doc["target_folder"],
            "size_bytes": local_path.stat().st_size,
        })

    # 写 sync plan
    sync_plan = {
        "run_id": run_id,
        "mode": "dry_run" if is_dry_run else "real",
        "project_id": args.project,
        "project_folder": manifest["project_folder"],
        "created_at": sync_time,
        "entries": plan_entries,
        "redacted": True,
    }
    (state_root / "wps_project_sync_plan.json").write_text(
        json.dumps(sync_plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n📋 sync_plan: {len(plan_entries)} 个文档待同步\n")

    if is_dry_run:
        print(f"🔄 dry-run 完成，未调用 kdocs-cli")
        print(f"   sync_plan: {state_root}/wps_project_sync_plan.json")
        # write doc_meta dry-run
        meta = {
            "project_id": args.project,
            "mode": "dry_run",
            "status": "dry_run",
            "project_folder": manifest["project_folder"],
            "documents": [{"doc_key": e["doc_key"], "title": e["title"],
                           "local_path": e["local_path"], "target_folder": e["target_folder"],
                           "status": "dry_run", "redacted": True} for e in plan_entries],
            "folders": manifest["folders"],
            "sync_time": sync_time,
            "run_id": run_id,
            "redacted": True,
        }
        (state_root / "wps_project_doc_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        log_entry = {"sync_time": sync_time, "project_id": args.project,
                     "mode": "dry_run", "status": "dry_run", "run_id": run_id, "redacted": True}
        (state_root / "wps_project_sync_log.json").write_text(
            json.dumps([log_entry], ensure_ascii=False, indent=2), encoding="utf-8")
        (state_root / "wps_project_sync_log.jsonl").write_text(
            json.dumps(log_entry, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"   状态文件已生成")
        sys.exit(0)

    # ── Real ──
    print("⬆️  real 模式")
    
    # 读取 WPS 配置
    env_content = read_env_file("/etc/webnovel/.env")
    parent_id = get_env_value(env_content, "WPS_FOLDER_ID") or None
    if not parent_id:
        print("❌ WPS 配置不完整（WPS_FOLDER_ID 缺失）")
        meta = {"project_id": args.project, "mode": "real", "status": "skipped",
                "message": "WPS_FOLDER_ID 缺失", "sync_time": sync_time, "run_id": run_id, "redacted": True}
        (state_root / "wps_project_doc_meta.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        (state_root / "sync_wps_project_real.skipped.txt").write_text(
            f"Skipped: WPS_FOLDER_ID missing\nrun_id: {run_id}\n", encoding="utf-8")
        sys.exit(0)

    # 检查 kdocs-cli
    try:
        subprocess.run(["which", "kdocs-cli"], capture_output=True, text=True, timeout=5, check=True)
    except:
        print("❌ kdocs-cli 不可用")
        sys.exit(1)

    # 检查依赖
    try:
        import yaml
    except ImportError:
        print("❌ PyYAML 不可用")
        sys.exit(1)

    # 读取文件夹映射
    folder_map = {}
    structure_path = proj_root / "wps_project_structure.yaml"
    if structure_path.exists():
        struct = yaml.safe_load(structure_path.read_text(encoding="utf-8"))
        for f in struct.get("folders", []):
            folder_map[f["key"]] = f["name"]

    doc_results = []
    all_success = True
    any_success = False
    any_failed = False

    for entry in plan_entries:
        doc_key = entry["doc_key"]
        local_path = Path(entry["local_path"])
        target_name = folder_map.get(doc_key, entry["target_folder"])
        
        print(f"\n📄 [{doc_key}] {entry['title']} -> {target_name}")

        # Base64 编码
        try:
            b64 = base64.b64encode(local_path.read_bytes()).decode("ascii")
        except Exception as e:
            print(f"  ❌ base64 失败: {e}")
            doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                "status": "failed", "business_code": -1, "message": str(e), "redacted": True})
            all_success = False; any_failed = True
            continue

        payload = {
            "parent_id": parent_id,
            "name": local_path.name,
            "content_base64": b64,
        }

        try:
            result = subprocess.run(["kdocs-cli", "drive", "upload-file"],
                                    input=json.dumps(payload), capture_output=True,
                                    text=True, timeout=30)
        except subprocess.TimeoutExpired:
            print(f"  ❌ 超时")
            doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                "status": "failed", "business_code": -1, "message": "timeout", "redacted": True})
            all_success = False; any_failed = True
            continue
        except Exception as e:
            print(f"  ❌ 异常: {e}")
            doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                "status": "failed", "business_code": -1, "message": str(e), "redacted": True})
            all_success = False; any_failed = True
            continue

        stdout = result.stdout
        stderr = result.stderr

        if result.returncode != 0:
            business_ok, business_code, msg = parse_kdocs_result(stdout)
            if business_ok is None:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "failed", "business_code": result.returncode,
                                    "message": f"进程失败: {stderr[:200]}", "redacted": True})
            elif business_ok:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "success", "business_code": 0,
                                    "message": "success", "redacted": True})
                any_success = True
            else:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "failed", "business_code": business_code,
                                    "message": msg, "redacted": True})
                all_success = False; any_failed = True
        else:
            business_ok, business_code, msg = parse_kdocs_result(stdout)
            if business_ok is None:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "unknown", "business_code": None,
                                    "message": "stdout 非 JSON", "redacted": True})
                all_success = False; any_failed = True
            elif business_ok:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "success", "business_code": 0,
                                    "message": "success", "redacted": True})
                any_success = True
            else:
                doc_results.append({"doc_key": doc_key, "title": entry["title"],
                                    "status": "failed", "business_code": business_code,
                                    "message": msg, "redacted": True})
                all_success = False; any_failed = True

        status_str = doc_results[-1]["status"]
        print(f"  {'✅' if status_str == 'success' else '❌'} {status_str}")

    # 判定整体状态
    if all_success:
        overall_status = "success"
    elif any_success and any_failed:
        overall_status = "partial"
    else:
        overall_status = "failed"

    # 写状态文件
    meta = {
        "project_id": args.project,
        "mode": "real",
        "status": overall_status,
        "project_folder": manifest["project_folder"],
        "documents": doc_results,
        "folders": manifest["folders"],
        "sync_time": sync_time,
        "run_id": run_id,
        "redacted": True,
    }
    (state_root / "wps_project_doc_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    log_entry = {"sync_time": sync_time, "project_id": args.project, "mode": "real",
                 "status": overall_status, "doc_count": len(doc_results),
                 "success_count": sum(1 for d in doc_results if d["status"] == "success"),
                 "failed_count": sum(1 for d in doc_results if d["status"] == "failed"),
                 "run_id": run_id, "redacted": True}
    (state_root / "wps_project_sync_log.json").write_text(
        json.dumps([log_entry], ensure_ascii=False, indent=2), encoding="utf-8")
    (state_root / "wps_project_sync_log.jsonl").write_text(
        json.dumps(log_entry, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"\n📊 状态: {overall_status}")
    print(f"   成功: {sum(1 for d in doc_results if d['status']=='success')}")
    print(f"   失败: {sum(1 for d in doc_results if d['status']=='failed')}")
    print(f"   未知: {sum(1 for d in doc_results if d['status']=='unknown')}")

    if overall_status == "success":
        sys.exit(0)
    elif overall_status == "partial":
        sys.exit(2)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
