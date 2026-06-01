#!/usr/bin/env python3
"""
DeepCode notify → WeChat 主动通知脚本
由 notify-feishu.sh 调用的 Python 后端。
直接从 shell 调用 send_weixin_direct() 发送微信消息。

用法：
  python3 notify_send_weixin.py --status completed --title "Task" --duration 120 \\
      --body "summary text" --fail-reason "" [--chat-id "xxx@im.wechat"]

依赖：
  - Hermes gateway 的 Python 环境（已安装 aiohttp、python-dotenv）
  - .env 文件中有 WEIXIN_TOKEN / WEIXIN_ACCOUNT_ID 等
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

# 确保能找到 Hermes 的模块
HERMES_AGENT = Path("/home/agentuser/.hermes/hermes-agent")
sys.path.insert(0, str(HERMES_AGENT))

# 加载 .env
from dotenv import load_dotenv
load_dotenv("/home/agentuser/.hermes/.env")

# 默认微信目标
DEFAULT_CHAT_ID = os.getenv("WEIXIN_HOME_CHANNEL", "")


def detect_marker(body: str) -> str:
    """从 BODY 中识别任务状态标记。"""
    if "[FINAL_DONE]" in body:
        return "FINAL_DONE"
    if "[NEED_HUMAN]" in body:
        return "NEED_HUMAN"
    if "[FAILED]" in body:
        return "FAILED"
    return "UNKNOWN"


def extract_summary(body: str, marker: str, max_len: int = 1000) -> str:
    """从 BODY 中提取摘要。"""
    if marker == "FINAL_DONE":
        lines = []
        capture = False
        for line in body.split("\n"):
            if "[FINAL_DONE]" in line:
                capture = True
                continue
            if capture:
                if line.startswith("[") and line.strip().endswith("]"):
                    break
                lines.append(line)
        summary = "\n".join(lines).strip()
        if summary:
            return summary[:max_len]
    elif marker == "NEED_HUMAN":
        lines = []
        capture = False
        for line in body.split("\n"):
            if "[NEED_HUMAN]" in line:
                capture = True
                continue
            if capture:
                if line.startswith("[") and line.strip().endswith("]"):
                    break
                lines.append(line)
        summary = "\n".join(lines).strip()
        if summary:
            return summary[:max_len]
    elif marker == "FAILED":
        lines = []
        capture = False
        for line in body.split("\n"):
            if "[FAILED]" in line:
                capture = True
                continue
            if capture:
                if line.startswith("[") and line.strip().endswith("]"):
                    break
                lines.append(line)
        summary = "\n".join(lines).strip()
        if summary:
            return summary[:max_len]
    # fallback: 取前 500 字
    return body[:max_len].strip()


async def main():
    parser = argparse.ArgumentParser(description="Send DeepCode notify to WeChat")
    parser.add_argument("--status", default="completed")
    parser.add_argument("--title", default="Untitled")
    parser.add_argument("--duration", default="0")
    parser.add_argument("--body", default="")
    parser.add_argument("--fail-reason", default="")
    parser.add_argument("--chat-id", default=DEFAULT_CHAT_ID)
    parser.add_argument("--job-id", default="")
    parser.add_argument("--result-path", default="")
    args = parser.parse_args()

    if not args.chat_id:
        print("[notify-send] ERROR: No chat_id (WEIXIN_HOME_CHANNEL not set)", file=sys.stderr)
        sys.exit(1)

    marker = detect_marker(args.body)
    summary = extract_summary(args.body, marker)

    # 构建微信消息
    if marker == "FINAL_DONE":
        header = f"✅ DeepCode 任务完成：{args.title}"
    elif marker == "NEED_HUMAN":
        header = f"🤔 DeepCode 需要你确认：{args.title}"
    elif marker == "FAILED":
        header = f"❌ DeepCode 任务失败：{args.title}"
    else:
        header = f"ℹ️ DeepCode 任务通知：{args.title}"

    lines = [header, f"状态：{marker} | 耗时：{args.duration}s"]

    # 提取 completed_items / changed_files / tests 等关键字段
    if summary:
        # 保留关键字段
        key_lines = []
        for line in summary.split("\n"):
            line = line.strip()
            if not line:
                continue
            if line.startswith("- ") or line.startswith("* "):
                key_lines.append(line)
            elif any(
                kw in line.lower()
                for kw in ["completed", "changed", "failed", "blocking", "option", "progress", "risk", "suggest"]
            ):
                key_lines.append(line)
        if key_lines:
            lines.append("")
            lines.extend(key_lines[:12])  # 最多 12 行
        else:
            lines.append("")
            lines.append(summary[:500])

    if args.fail_reason:
        lines.append("")
        lines.append(f"失败原因：{args.fail_reason}")

    if args.result_path:
        lines.append("")
        lines.append(f"结果文件：{args.result_path}")

    if args.job_id:
        lines.append(f"Job ID：{args.job_id}")

    message = "\n".join(lines)

    # 调用 send_weixin_direct
    try:
        from gateway.platforms.weixin import send_weixin_direct

        result = await send_weixin_direct(
            extra={
                "account_id": os.getenv("WEIXIN_ACCOUNT_ID", ""),
                "base_url": os.getenv("WEIXIN_BASE_URL", ""),
                "cdn_base_url": os.getenv("WEIXIN_CDN_BASE_URL", ""),
                "token": os.getenv("WEIXIN_TOKEN", ""),
            },
            token=os.getenv("WEIXIN_TOKEN", ""),
            chat_id=args.chat_id,
            message=message,
        )
        if result.get("success"):
            print(f"[notify-send] WeChat sent: {result.get('message_id', '?')}", file=sys.stderr)
        else:
            print(f"[notify-send] WeChat send failed: {result.get('error', '?')}", file=sys.stderr)
            # 写错误日志
            err_dir = f"/tmp/deepcode_jobs/{args.job_id}" if args.job_id else "/tmp/deepcode_jobs"
            Path(err_dir).mkdir(parents=True, exist_ok=True)
            Path(f"{err_dir}/notify_error.log").write_text(
                json.dumps({"error": result.get("error", "unknown"), "result": str(result)}, ensure_ascii=False)
            )
    except Exception as e:
        print(f"[notify-send] Exception: {e}", file=sys.stderr)
        err_dir = f"/tmp/deepcode_jobs/{args.job_id}" if args.job_id else "/tmp/deepcode_jobs"
        Path(err_dir).mkdir(parents=True, exist_ok=True)
        Path(f"{err_dir}/notify_error.log").write_text(
            json.dumps({"error": str(e)}, ensure_ascii=False)
        )


if __name__ == "__main__":
    asyncio.run(main())
