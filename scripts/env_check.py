#!/usr/bin/env python3
"""
env_check.py — 环境检查脚本
用途：检查项目运行环境是否就绪。
不输出任何真实密钥。
"""

import sys
import os
import platform
import subprocess
from pathlib import Path


def check(label, condition, detail=""):
    status = "✅" if condition else "❌"
    detail_str = f" — {detail}" if detail else ""
    print(f"  {status} {label}{detail_str}")
    return condition


def run():
    print("=" * 50)
    print("  webnovel-hermes-wps 环境检查报告")
    print("=" * 50)
    print()

    all_ok = True

    # 1. Python 版本
    py_version = sys.version.split()[0]
    py_ok = check("Python 版本", py_version.startswith("3."), py_version)

    # 2. 项目根目录
    code_root = Path(os.environ.get("WEBNOVEL_CODE_ROOT", "/opt/webnovel-hermes-wps"))
    cr_ok = check("代码根目录存在", code_root.exists(), str(code_root))

    # 3. 数据目录
    data_root = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab"))
    dr_ok = check("数据根目录存在", data_root.exists(), str(data_root))

    # 4. 数据目录可读写
    rw_ok = True
    if data_root.exists():
        try:
            test_file = data_root / ".write_test"
            test_file.write_text("ok")
            test_file.unlink()
            rw_ok = check("数据目录可写", True)
        except PermissionError:
            rw_ok = check("数据目录可写", False, "权限不足")
            all_ok = False
    else:
        rw_ok = check("数据目录可写", False, "目录不存在")
        all_ok = False

    # 5. /etc/webnovel/
    env_dir = Path("/etc/webnovel")
    ed_ok = check("/etc/webnovel/ 目录存在", env_dir.exists())
    env_file = env_dir / ".env"
    ef_ok = check("/etc/webnovel/.env 存在", env_file.exists())

    # 6. .env.example
    env_example = code_root / ".env.example"
    ee_ok = check(".env.example 存在", env_example.exists())

    # 7. 检查必需目录
    required_dirs = [
        code_root / "skills",
        code_root / "schemas",
        code_root / "scripts",
        code_root / "templates" / "prompts",
        code_root / "templates" / "deai_rules",
        code_root / "templates" / "wps",
        code_root / "docs",
    ]
    dirs_ok = True
    for d in required_dirs:
        if not d.exists():
            dirs_ok = False
            check(f"目录 {d.name} 存在", False)
    if dirs_ok:
        check("必需目录完整", True, f"{len(required_dirs)} 个")
    else:
        all_ok = False

    # 8. Python 依赖
    deps_ok = True
    try:
        import yaml
        check("PyYAML", True, yaml.__version__)
    except ImportError:
        check("PyYAML", False)
        deps_ok = False
        all_ok = False

    try:
        import docx
        check("python-docx", True, docx.__version__)
    except ImportError:
        check("python-docx", False, "降级为 Markdown 输出")
        # not fatal

    try:
        import requests
        check("requests", True, requests.__version__)
    except ImportError:
        check("requests", False)
        deps_ok = False

    # 9. kdocs-cli
    kdocs_ok = False
    kdocs_path = os.path.expanduser("~/.local/bin/kdocs-cli")
    if os.path.isfile(kdocs_path):
        kdocs_ok = True
        check("kdocs-cli 已安装", True)
    else:
        check("kdocs-cli 已安装", False, "WPS 同步不可用")

    print()
    print("-" * 50)
    if all_ok:
        print("  结论：✅ 环境就绪，可以继续执行。")
    else:
        print("  结论：❌ 存在需要解决的问题，请参考上面的 ❌ 项。")
    print("-" * 50)


if __name__ == "__main__":
    run()
