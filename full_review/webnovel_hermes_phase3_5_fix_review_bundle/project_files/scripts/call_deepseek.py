#!/usr/bin/env python3
"""
call_deepseek.py — 统一 DeepSeek API 调用封装

支持模式：
  - mock：默认模式，生成示例输出，不真实调用 API
  - real：显式传入 --real 时启用真实 API 调用

用法示例：
  python scripts/call_deepseek.py --mock --system prompts/story_bible.md --input input.json --output out.md
  python scripts/call_deepseek.py --real --system prompts/story_bible.md --input input.json --output out.md \
    --task-name story_bible --log /data/logs/deepseek_calls.jsonl
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime


def load_env():
    """尝试加载 /etc/webnovel/.env（不输出密钥，失败时降级）"""
    env = {}
    # 1. 环境变量优先
    for k in ["DEEPSEEK_API_KEY", "DEEPSEEK_BASE_URL", "DEEPSEEK_MODEL"]:
        if os.environ.get(k):
            env[k] = os.environ[k]
    # 2. 尝试 /etc/webnovel/.env
    env_file = Path("/etc/webnovel/.env")
    if env_file.exists():
        try:
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() not in env and v.strip() and v.strip() != "***":
                        env[k.strip()] = v.strip()
        except PermissionError:
            pass  # 非 root 用户读不到，降级
    # 3. 尝试 Hermes config.yaml
    hermes_config = Path(os.path.expanduser("~/.hermes/config.yaml"))
    if hermes_config.exists():
        try:
            import yaml
            cfg = yaml.safe_load(hermes_config.read_text())
            ds = cfg.get("providers", {}).get("deepseek", {})
            if ds.get("api_key") and "DEEPSEEK_API_KEY" not in env:
                env["DEEPSEEK_API_KEY"] = ds["api_key"]
            if ds.get("base_url") and "DEEPSEEK_BASE_URL" not in env:
                env["DEEPSEEK_BASE_URL"] = ds["base_url"]
        except Exception:
            pass
    return env


def mock_call(system_prompt_path, user_input_path, output_path, task_name="default"):
    """Mock 模式：生成示例输出，不调用真实 API"""
    system_name = Path(system_prompt_path).stem if system_prompt_path else "default"
    input_name = Path(user_input_path).stem if user_input_path else "no_input"

    mock_content = f"""# Mock 输出 — 任务: {task_name}
# 模式: mock / 当前未调用 DeepSeek 真实 API
# 生成时间: {datetime.now().isoformat()}

## 章节规划摘要

本章目标：林砚在送外卖时第一次看见价格标签。

关键场景：
1. 林砚接单，前往送餐地点
2. 在客户单位电梯口看见老人头顶价格
3. 与光鲜客户形成反差
4. 第一次判断失误
5. 医院窗口 — 父亲价格归零

## 降 AI 腔改写说明

原始问题：
- 多处使用"他感到""他意识到"句式
- 解释性旁白偏多
- 对话口吻区分不够

改写方向：
- 替换"他感到震惊"为具体动作（手指停在按钮上）
- 删除解释性旁白，用对话推动
- 让老人和客户的对话口吻形成对比
"""

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(mock_content, encoding="utf-8")
        print(json.dumps({"success": True, "mode": "mock", "output": output_path}, ensure_ascii=False))
    else:
        print(mock_content)


def real_call(system_prompt_path, user_input_path, output_path,
              task_name="default", temperature=0.7, max_tokens=1200,
              timeout=60, retries=2, log_path=None, canon_text=None,
              hard_rules_text=None):
    """真实调用 DeepSeek API，支持重试和结构化日志

    Args:
        canon_text: 完整 canon_constraints.yaml 文本块，注入 system 末尾和 user 开头
        hard_rules_text: 章节级硬约束文本（如 chapter_beat 的禁止写法），注入 user message
    """
    env = load_env()
    api_key = env.get("DEEPSEEK_API_KEY")
    base_url = env.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = env.get("DEEPSEEK_MODEL", "deepseek-chat")

    if not api_key:
        print(json.dumps({
            "task_name": task_name, "mode": "real", "model": model,
            "success": False, "error_type": "config_error",
            "error_message": "未找到 DEEPSEEK_API_KEY"
        }, ensure_ascii=False))
        sys.exit(1)

    # 读取 system prompt
    system_content = ""
    if system_prompt_path:
        system_content = Path(system_prompt_path).read_text(encoding="utf-8")

    # 注入 canon 到 system message 末尾
    if canon_text:
        system_content += "\n\n" + canon_text

    # 读取 user input
    user_content = ""
    if user_input_path:
        user_content = Path(user_input_path).read_text(encoding="utf-8")

    if not user_content.strip():
        user_content = "请根据提示词生成内容。"

    # 注入 canon 和 hard rules 到 user message 开头
    prefix_parts = []
    if canon_text:
        prefix_parts.append(canon_text)
    if hard_rules_text:
        prefix_parts.append(hard_rules_text)
    if prefix_parts:
        user_content = "\n\n".join(prefix_parts) + "\n\n" + user_content

    import requests

    messages = []
    if system_content:
        messages.append({"role": "system", "content": system_content})
    if user_content:
        messages.append({"role": "user", "content": user_content})

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    start_time = datetime.now().isoformat()
    last_error = None
    status_code = None

    for attempt in range(1 + retries):
        try:
            resp = requests.post(
                f"{base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=timeout,
            )
            status_code = resp.status_code
            resp.raise_for_status()
            result = resp.json()

            if "choices" not in result or not result["choices"]:
                raise ValueError("DeepSeek 返回中没有 choices")

            content = result["choices"][0].get("message", {}).get("content", "")
            if not content.strip():
                raise ValueError("DeepSeek 返回内容为空")

            end_time = datetime.now().isoformat()

            # 写入输出文件
            if output_path:
                Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(content)

            # 结构化日志
            log_entry = {
                "task_name": task_name,
                "mode": "real",
                "model": model,
                "base_url": base_url.rstrip("/").replace("https://", "").replace("http://", ""),
                "start_time": start_time,
                "end_time": end_time,
                "success": True,
                "status_code": status_code,
                "error_type": None,
                "error_message": None,
                "output_path": str(Path(output_path).resolve()) if output_path else None,
                "prompt_files": {
                    "system": system_prompt_path,
                    "user_input": user_input_path,
                },
                "input_file": user_input_path,
            }

            _write_log(log_entry, log_path)

            print(json.dumps({
                "success": True, "mode": "real", "task_name": task_name,
                "output": output_path, "attempt": attempt + 1,
            }, ensure_ascii=False))
            return

        except requests.exceptions.Timeout as e:
            last_error = str(e)
            error_type = "timeout"
            status_code = status_code or 0
        except requests.exceptions.HTTPError as e:
            last_error = str(e)
            error_type = f"http_error"
            status_code = resp.status_code if 'resp' in dir() else 0
        except requests.exceptions.ConnectionError as e:
            last_error = str(e)
            error_type = "connection_error"
            status_code = 0
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            last_error = str(e)
            error_type = "response_parse_error"
            status_code = status_code or 0
        except Exception as e:
            last_error = str(e)
            error_type = "unknown_error"
            status_code = 0

        if attempt < retries:
            time.sleep(2 * (attempt + 1))

    # 全部重试失败
    end_time = datetime.now().isoformat()
    err_log_entry = {
        "task_name": task_name,
        "mode": "real",
        "model": model,
        "base_url": base_url.rstrip("/").replace("https://", "").replace("http://", ""),
        "start_time": start_time,
        "end_time": end_time,
        "success": False,
        "status_code": status_code,
        "error_type": error_type,
        "error_message": last_error,
        "output_path": str(Path(output_path).resolve()) if output_path else None,
        "prompt_files": {
            "system": system_prompt_path,
            "user_input": user_input_path,
        },
        "input_file": user_input_path,
    }
    _write_log(err_log_entry, log_path)

    print(json.dumps({
        "success": False, "mode": "real", "task_name": task_name,
        "error_type": error_type, "error_message": last_error,
    }, ensure_ascii=False))
    sys.exit(1)


def _write_log(entry, log_path):
    """写入结构化日志，禁止记录 API Key"""
    safe_entry = {k: v for k, v in entry.items()
                  if k not in ("api_key", "authorization", "token", "cookie", "password")}
    safe_entry.pop("api_key", None)
    if log_path:
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(safe_entry, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser(description="统一 DeepSeek 调用封装")
    parser.add_argument("--mock", action="store_true", help="mock 模式（默认）")
    parser.add_argument("--real", action="store_true", help="真实 API 调用")
    parser.add_argument("--system-prompt", dest="system", help="system prompt 文件路径")
    parser.add_argument("--user-prompt", dest="user_prompt", help="user prompt 文件路径")
    parser.add_argument("--input", help="输入文件路径（同 --user-prompt）")
    parser.add_argument("--output", help="输出文件路径")
    parser.add_argument("--log", help="结构化日志文件路径")
    parser.add_argument("--temperature", type=float, default=0.7, help="生成温度 (默认 0.7)")
    parser.add_argument("--max-tokens", type=int, default=1200, help="最大 token 数 (默认 1200)")
    parser.add_argument("--timeout", type=int, default=60, help="请求超时秒数 (默认 60)")
    parser.add_argument("--retries", type=int, default=2, help="失败重试次数 (默认 2)")
    parser.add_argument("--task-name", default="default", help="任务名称用于日志追踪")
    parser.add_argument("--canon-text", help="canon 约束文本文件的路径，内容会注入 system+user message")
    parser.add_argument("--hard-rules", help="章节级硬约束文本文件的路径，内容会注入 user message")
    args = parser.parse_args()

    # 兼容 --input 和 --user-prompt
    user_input = args.input or args.user_prompt

    # 读取 canon text
    canon_text = None
    if args.canon_text:
        canon_path = Path(args.canon_text)
        if canon_path.exists():
            canon_text = canon_path.read_text(encoding="utf-8")

    # 读取 hard rules
    hard_rules_text = None
    if args.hard_rules:
        hr_path = Path(args.hard_rules)
        if hr_path.exists():
            hard_rules_text = hr_path.read_text(encoding="utf-8")

    if args.real:
        real_call(
            system_prompt_path=args.system,
            user_input_path=user_input,
            output_path=args.output,
            task_name=args.task_name,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            timeout=args.timeout,
            retries=args.retries,
            log_path=args.log,
            canon_text=canon_text,
            hard_rules_text=hard_rules_text,
        )
    else:
        mock_call(args.system, user_input, args.output, task_name=args.task_name)


if __name__ == "__main__":
    main()
