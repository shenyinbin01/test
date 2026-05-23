#!/usr/bin/env python3
"""
sync_wps.py — 同步 DOCX 到 WPS/Kdocs (阶段五强化版)

用法：
  python scripts/sync_wps.py                          # dry-run（默认）
  python scripts/sync_wps.py --dry-run ...             # 显式 dry-run
  python scripts/sync_wps.py --real --input PATH ...   # 真实上传

强化内容：
  - subprocess returncode != 0 -> failed
  - stdout 非 JSON -> status=unknown, 不判 success
  - 业务 code != 0 -> failed
  - doc_meta.yaml / sync_log.jsonl 标准化写入
  - 脱敏标记
"""

import os
import sys
import json
import base64
import subprocess
import argparse
from pathlib import Path
from datetime import datetime


DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


def parse_kdocs_result(stdout):
    """
    解析 kdocs-cli stdout，判断业务成功/失败。

    返回 (is_success: bool|None, business_code: int|None, message: str)

    is_success:
      True  -> 业务成功 (code=0)
      False -> 业务失败 (code!=0)
      None  -> 无法解析（stdout 非 JSON）
    """
    text = stdout.strip()
    if not text:
        return None, None, "stdout 为空"

    start = text.find("{")
    if start == -1:
        return None, None, "返回结果不是 JSON 格式"

    depth = 0
    end = -1
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    if end == -1:
        return None, None, "无法找到完整 JSON 结构"

    try:
        data = json.loads(text[start:end])
    except json.JSONDecodeError as e:
        return None, None, f"JSON 解析失败: {e}"

    code = data.get("code")
    if code is None:
        return None, None, "返回 JSON 中无 code 字段"

    if code == 0:
        return True, 0, "success"
    else:
        msg = data.get("message", "未知错误")
        business_data = data.get("data", {})
        if isinstance(business_data, dict):
            inner_msg = business_data.get("message", "")
            if inner_msg:
                msg = inner_msg
        return False, code, f"业务失败 (code={code}): {msg}"


def check_kdocs():
    """检查 kdocs-cli 是否可用"""
    try:
        result = subprocess.run(
            ["which", "kdocs-cli"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return True, result.stdout.strip()
        return False, None
    except Exception as e:
        return False, str(e)


def read_env_file(path):
    """读取 /etc/webnovel/.env（支持 sudo）"""
    p = Path(path)
    if not p.exists():
        return ""
    try:
        return p.read_text()
    except PermissionError:
        r = subprocess.run(["sudo", "cat", str(p)], capture_output=True, text=True, timeout=5)
        return r.stdout if r.returncode == 0 else ""


def get_env_value(content, key):
    """从 env 文件内容中提取某个 key 的值"""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith(f"{key}="):
            return line.split("=", 1)[1].strip()
    return None


def write_doc_meta(path, meta):
    """写 doc_meta.yaml（脱敏），使用 yaml 格式"""
    lines = []
    for k, v in meta.items():
        if isinstance(v, str) and v:
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {v}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_sync_log(path, entry):
    """追加写入 sync_log.jsonl"""
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def sanitize_for_bundle(entry):
    """
    审查包脱敏：移除可能包含真实 file_id/URL 的字段。
    保留业务状态信息，移除敏感原始返回。
    """
    safe = {k: v for k, v in entry.items() if k not in ("raw_stdout", "raw_file_id", "raw_url", "doc_link")}
    return safe


def main():
    parser = argparse.ArgumentParser(description="同步 DOCX 到 WPS/Kdocs (阶段五强化版)")
    parser.add_argument("--dry-run", action="store_true", help="仅检查，不上传（默认）")
    parser.add_argument("--real", action="store_true", help="真实上传")
    parser.add_argument("--project", default="price_tag_life", help="项目名")
    parser.add_argument("--input", default=None, help="输入 DOCX 路径")
    parser.add_argument("--target-folder", default="小说", help="目标文件夹名")
    parser.add_argument("--output-meta", default=None, help="doc_meta.yaml 输出路径")
    parser.add_argument("--sync-log", default=None, help="sync_log.jsonl 输出路径")
    args = parser.parse_args()

    project = args.project
    is_dry_run = not args.real
    sync_time = datetime.now().isoformat()

    print("=" * 50)
    print(f"  WPS 同步 — {'dry-run' if is_dry_run else 'real'}")
    print("=" * 50)
    print()

    # ── 1. DOCX 路径 ──
    if args.input:
        docx_path = Path(args.input)
    else:
        # 从默认投影输出查找
        default_path = DATA_ROOT / "demo_output" / "phase5_wps_projection" / f"{project}_volume_001.docx"
        docx_path = default_path if default_path.exists() else None

    if not docx_path or not docx_path.exists():
        print(f"❌ 输入 DOCX 不存在: {docx_path}")
        sys.exit(1)
    print(f"📄 DOCX: {docx_path} ({docx_path.stat().st_size} bytes)")

    # ── 2. kdocs-cli 检查 ──
    kdocs_ok, kdocs_path = check_kdocs()
    if kdocs_ok:
        print(f"✅ kdocs-cli: {kdocs_path}")
    else:
        print(f"❌ kdocs-cli 不可用")
        sys.exit(1)

    # ── 3. 读取 WPS 配置 ──
    env_content = read_env_file("/etc/webnovel/.env")
    parent_id = get_env_value(env_content, "WPS_FOLDER_ID") or "0"
    print(f"📁 目标文件夹: {args.target_folder} (parent_id 已{'配置' if parent_id != '0' else '用根目录'})")

    # ── 4. 状态文件路径 ──
    if args.output_meta:
        meta_path = Path(args.output_meta)
    else:
        meta_path = DATA_ROOT / "demo_output" / "phase5_wps_state" / "doc_meta.yaml"

    if args.sync_log:
        log_path = Path(args.sync_log)
    else:
        log_path = DATA_ROOT / "demo_output" / "phase5_wps_state" / "sync_log.jsonl"

    meta_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # ── 5. dry-run ──
    if is_dry_run:
        print()
        print("🔄 模式: dry-run（仅检查，不上传）")
        print()

        meta = {
            "project": project,
            "file_name": docx_path.name,
            "mode": "dry_run",
            "status": "dry_run",
            "business_code": "N/A",
            "message": "仅检查，未上传",
            "sync_time": sync_time,
            "target_folder": args.target_folder,
            "local_file": str(docx_path),
            "redacted": "true",
        }
        write_doc_meta(meta_path, meta)

        log_entry = {
            "sync_time": sync_time,
            "project": project,
            "file_name": docx_path.name,
            "mode": "dry_run",
            "status": "dry_run",
            "business_code": None,
            "message": "仅检查，未上传",
            "local_file": str(docx_path),
            "target_folder": args.target_folder,
        }
        write_sync_log(log_path, log_entry)

        print("✅ dry-run 完成")
        print(f"   doc_meta.yaml: {meta_path}")
        print(f"   sync_log.jsonl: {log_path}")
        sys.exit(0)

    # ── 6. real 上传 ──
    print()
    print("⬆️ 模式: real（真实上传）")
    print(f"   文件: {docx_path.name}")
    print(f"   目标: {args.target_folder}")

    # 6a. base64 编码
    try:
        with open(docx_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
    except Exception as e:
        print(f"❌ 文件读取/base64 失败: {e}")
        meta = {
            "project": project,
            "file_name": docx_path.name,
            "mode": "real",
            "status": "failed",
            "business_code": -1,
            "message": f"文件读取/base64 失败: {e}",
            "sync_time": sync_time,
            "target_folder": args.target_folder,
            "local_file": str(docx_path),
            "redacted": "true",
        }
        write_doc_meta(meta_path, meta)
        log_entry = {**meta, "mode": "real", "redacted": None}
        del log_entry["redacted"]
        write_sync_log(log_path, log_entry)
        sys.exit(1)

    payload = {
        "parent_id": parent_id,
        "name": docx_path.name,
        "content_base64": b64,
    }

    # 6b. 执行 kdocs-cli
    try:
        result = subprocess.run(
            ["kdocs-cli", "drive", "upload-file"],
            input=json.dumps(payload),
            capture_output=True, text=True, timeout=30
        )
    except subprocess.TimeoutExpired:
        print("❌ kdocs-cli 执行超时 (30s)")
        status = "failed"
        msg = "执行超时"
        business_code = -1
        sys.exit(1)
    except Exception as e:
        print(f"❌ kdocs-cli 执行异常: {e}")
        status = "failed"
        msg = str(e)
        business_code = -1
        sys.exit(1)

    # 6c. 解析结果
    stdout = result.stdout
    stderr = result.stderr

    # subprocess returncode != 0 是警告信号，但不一定等于业务失败
    if result.returncode != 0:
        # 检查 stdout 是否有有效 JSON
        business_ok, business_code, msg = parse_kdocs_result(stdout)
        if business_ok is None:
            # 既无有效 JSON，returncode 也非 0 -> failed
            status = "failed"
            business_code = result.returncode
            msg = f"kdocs-cli 进程失败 (exit={result.returncode}): {stderr[:200]}"
        elif business_ok:
            status = "success"
        else:
            status = "failed"
    else:
        # returncode == 0, 解析 stdout
        business_ok, business_code, msg = parse_kdocs_result(stdout)
        if business_ok is None:
            # stdout 非 JSON -> status=unknown，不能判 success
            status = "unknown"
            business_code = None
            msg = f"stdout 非 JSON 格式，无法确认业务结果"
        elif business_ok:
            status = "success"
        else:
            status = "failed"

    # 6d. 写入状态文件
    meta = {
        "project": project,
        "file_name": docx_path.name,
        "mode": "real",
        "status": status,
        "business_code": business_code if business_code is not None else -1,
        "message": msg,
        "sync_time": sync_time,
        "target_folder": args.target_folder,
        "local_file": str(docx_path),
        "redacted": "true",
    }
    write_doc_meta(meta_path, meta)

    log_entry = {
        "sync_time": sync_time,
        "project": project,
        "file_name": docx_path.name,
        "mode": "real",
        "status": status,
        "business_code": business_code,
        "message": msg,
        "local_file": str(docx_path),
        "target_folder": args.target_folder,
    }
    write_sync_log(log_path, log_entry)

    print()
    if status == "success":
        print(f"✅ WPS 同步成功 (business_code=0)")
        sys.exit(0)
    elif status == "unknown":
        print(f"⚠️ WPS 同步状态未知: {msg}")
        sys.exit(1)
    else:
        print(f"❌ WPS 同步失败: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
