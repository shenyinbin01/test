#!/usr/bin/env python3
"""
sync_wps.py — 同步 DOCX 到 WPS/Kdocs
用法：
  python scripts/sync_wps.py            # dry-run（默认）
  python scripts/sync_wps.py --dry-run  # 显式 dry-run
  python scripts/sync_wps.py --real     # 真实上传
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime


DATA_ROOT = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))


def parse_result(stdout):
    """解析 kdocs-cli stdout，判断真实业务成功/失败"""
    # 去掉升级提示等非 JSON 后缀
    text = stdout.strip()
    # 找到 JSON 起始位置
    start = text.find("{")
    if start == -1:
        return None, "返回结果不是 JSON 格式"
    
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
        return None, "无法找到完整的 JSON 结构"
    
    try:
        data = json.loads(text[start:end])
    except json.JSONDecodeError as e:
        return None, f"JSON 解析失败: {e}"
    
    # 检查业务状态码
    code = data.get("code")
    if code == 0:
        # 进一步检查 data.data 中是否有 id/file_id 等成功字段
        inner = data.get("data", {})
        if isinstance(inner, dict):
            inner_data = inner.get("data", {})
            if inner_data.get("id") or inner_data.get("file_id"):
                return True, "success"
            elif code == 0:
                return True, "success"
        return True, "success"
    else:
        msg = data.get("message", "未知错误")
        return False, f"业务失败 (code={code}): {msg}"


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


def check_env():
    """检查 /etc/webnovel/.env 是否有 WPS 配置"""
    env_file = Path("/etc/webnovel/.env")
    if not env_file.exists():
        return False, "/etc/webnovel/.env 不存在"

    try:
        env_content = env_file.read_text()
    except PermissionError:
        result = subprocess.run(
            ["sudo", "cat", str(env_file)], capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            env_content = result.stdout
        else:
            return False, "无法读取 /etc/webnovel/.env: 权限不足"

    required_keys = ["WPS_FOLDER_ID"]
    missing = [k for k in required_keys if f"{k}=" not in env_content]
    if missing:
        return False, f"缺少配置: {', '.join(missing)}"

    return True, "WPS 环境就绪"


def upload_to_kdocs(docx_path, parent_id):
    """使用 kdocs-cli 上传 DOCX，返回 (ok, message)"""
    name = docx_path.name
    
    # 先对文件做 base64
    try:
        with open(docx_path, "rb") as f:
            import base64
            b64 = base64.b64encode(f.read()).decode("ascii")
    except Exception as e:
        return False, f"文件读取或 base64 编码失败: {e}"

    payload = {
        "parent_id": parent_id,
        "name": name,
        "content_base64": b64,
    }
    
    try:
        result = subprocess.run(
            ["kdocs-cli", "drive", "upload-file"],
            input=json.dumps(payload),
            capture_output=True, text=True, timeout=30
        )
    except subprocess.TimeoutExpired:
        return False, "kdocs-cli 执行超时 (30s)"
    except Exception as e:
        return False, f"kdocs-cli 执行异常: {e}"

    if result.returncode != 0:
        return False, f"kdocs-cli 进程失败 (exit={result.returncode}): {result.stderr[:200]}"

    # 解析 stdout 判断业务成功
    ok, msg = parse_result(result.stdout)
    if ok is None:
        return False, msg
    return ok, msg


def write_sync_log(wps_dir, entry):
    """写入同步日志"""
    log_file = wps_dir / "sync_log.jsonl"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def write_doc_meta(wps_dir, meta):
    """写入文档元信息（不写入完整 stdout）"""
    safe_fields = ["file", "sync_time", "status", "message"]
    filtered = {k: v for k, v in meta.items() if k in safe_fields}
    yaml_lines = [f"{k}: {v}" for k, v in filtered.items()]
    (wps_dir / "doc_meta.yaml").write_text("\n".join(yaml_lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="同步 DOCX 到 WPS/Kdocs")
    parser.add_argument("--dry-run", action="store_true", help="仅检查，不上传（默认）")
    parser.add_argument("--real", action="store_true", help="真实上传")
    args = parser.parse_args()

    # 默认 dry-run
    is_dry_run = not args.real

    print("=" * 50)
    print("  WPS 同步检查")
    print("=" * 50)
    print()

    # 1. 查找 Demo 项目的 DOCX
    novels_dir = DATA_ROOT / "workspace" / "novels"
    docx_path = None
    project_dir = None

    for name in ["price_tag_life"]:
        exports_dir = novels_dir / name / "exports"
        if exports_dir.exists():
            docxs = list(exports_dir.glob("*.docx"))
            if docxs:
                docx_path = docxs[0]
                project_dir = novels_dir / name
                break

    if not docx_path:
        print("⚠️ 未找到 DOCX 文件。")
        entry = {
            "timestamp": datetime.now().isoformat(),
            "status": "skipped",
            "reason": "DOCX 未生成",
        }
        (DATA_ROOT / "logs").mkdir(parents=True, exist_ok=True)
        with open(DATA_ROOT / "logs" / "sync_skipped.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"  DOCX 路径: {novels_dir / name / 'exports/*.docx'}")
        sys.exit(1)

    print(f"📄 找到 DOCX: {docx_path}")
    print()

    # 2. 检查 kdocs-cli
    kdocs_avail, kdocs_info = check_kdocs()
    if kdocs_avail:
        print(f"✅ kdocs-cli: {kdocs_info}")
    else:
        print(f"⚠️ kdocs-cli 不可用: {kdocs_info}")

    # 3. 检查 WPS 环境
    env_ok, env_msg = check_env()
    if env_ok:
        print(f"✅ {env_msg}")
    else:
        print(f"⚠️ {env_msg}")

    print()

    # 4. 准备记录目录
    if project_dir:
        wps_dir = project_dir / "wps"
        wps_dir.mkdir(parents=True, exist_ok=True)
    else:
        wps_dir = None

    # 5. 获取 parent_id
    env_file = Path("/etc/webnovel/.env")
    parent_id = "0"
    if env_file.exists():
        try:
            content = env_file.read_text()
        except PermissionError:
            r = subprocess.run(["sudo", "cat", str(env_file)], capture_output=True, text=True, timeout=5)
            content = r.stdout if r.returncode == 0 else ""
        for line in content.splitlines():
            if line.startswith("WPS_FOLDER_ID="):
                val = line.split("=", 1)[1].strip()
                if val:
                    parent_id = val

    # 6. 执行
    if is_dry_run:
        print("🔄 模式: dry-run（仅检查，不上传）")
        print()
        print(f"  DOCX 本地路径: {docx_path}")
        if not kdocs_avail:
            print(f"  阻塞: kdocs-cli 不可用")
        if not env_ok:
            print(f"  阻塞: {env_msg}")
        print()

        if wps_dir:
            write_doc_meta(wps_dir, {
                "file": docx_path.name,
                "sync_time": datetime.now().isoformat(),
                "status": "dry_run",
                "message": "仅检查，未上传",
            })
            write_sync_log(wps_dir, {
                "timestamp": datetime.now().isoformat(),
                "file": str(docx_path),
                "status": "dry_run",
            })

        print("✅ 同步检查完成（dry-run）")
        print(f"  DOCX 保留在: {docx_path}")

    else:
        if not kdocs_avail:
            print("❌ kdocs-cli 不可用，无法上传")
            if wps_dir:
                write_doc_meta(wps_dir, {
                    "file": docx_path.name,
                    "sync_time": datetime.now().isoformat(),
                    "status": "failed",
                    "message": "kdocs-cli 不可用",
                })
            sys.exit(1)

        if not env_ok:
            print("❌ WPS 环境未就绪，无法上传")
            if wps_dir:
                write_doc_meta(wps_dir, {
                    "file": docx_path.name,
                    "sync_time": datetime.now().isoformat(),
                    "status": "failed",
                    "message": env_msg,
                })
            sys.exit(1)

        print("⬆️ 模式: real（真实上传）")
        success, msg = upload_to_kdocs(docx_path, parent_id)

        if success:
            print(f"✅ WPS 同步成功")
            if wps_dir:
                write_doc_meta(wps_dir, {
                    "file": docx_path.name,
                    "sync_time": datetime.now().isoformat(),
                    "status": "success",
                    "message": "上传成功",
                })
                write_sync_log(wps_dir, {
                    "timestamp": datetime.now().isoformat(),
                    "file": str(docx_path),
                    "status": "success",
                })
        else:
            print(f"❌ WPS 同步失败: {msg}")
            if wps_dir:
                write_doc_meta(wps_dir, {
                    "file": docx_path.name,
                    "sync_time": datetime.now().isoformat(),
                    "status": "failed",
                    "message": msg,
                })
                write_sync_log(wps_dir, {
                    "timestamp": datetime.now().isoformat(),
                    "file": str(docx_path),
                    "status": "failed",
                    "error": msg,
                })
            sys.exit(1)


if __name__ == "__main__":
    main()
