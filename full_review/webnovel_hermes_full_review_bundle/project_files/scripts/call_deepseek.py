#!/usr/bin/env python3
"""
call_deepseek.py — 统一 DeepSeek API 调用封装
本阶段默认使用 mock 模式，不真实调用 API。
通过 --real 参数启用真实 API 调用。
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime


def load_env():
    """尝试加载 /etc/webnovel/.env"""
    env_file = Path("/etc/webnovel/.env")
    env = {}
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def mock_call(system_prompt_path, user_input_path, output_path):
    """Mock 模式：生成示例输出，不调用真实 API"""
    system_name = Path(system_prompt_path).stem if system_prompt_path else "default"
    input_name = Path(user_input_path).stem if user_input_path else "no_input"

    mock_content = f"""# Mock 输出 — 模式: {system_name} / 输入: {input_name}
# 当前为 mock/demo 模式，不调用 DeepSeek 真实 API
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

## 正文片段（Mock）

外卖箱在电动车后座颠了一下，林砚伸手按住。

手机上跳出新订单——望江路 18 号，302 室。他扫了一眼地址，拧转油门。

六分钟后他站在一栋老式写字楼的电梯里，数字一格一格往上跳。电梯门开的时候，走廊里站着一个穿灰色中山装的老头，正低头看手机。

林砚本来没在意。但他走过去的时候余光扫到老人头顶——那里浮着一排数字，像是透明的投影，又像视网膜上的残影。

他停了一下。

那个数字大得离谱。

"""

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        Path(output_path).write_text(mock_content)
        print(f"✅ Mock 输出已写入: {output_path}")
    else:
        print(mock_content)


def real_call(system_prompt_path, user_input_path, output_path):
    """真实调用 DeepSeek API"""
    env = load_env()
    api_key = env.get("DEEPSEEK_API_KEY") or os.environ.get("DEEPSEEK_API_KEY")
    base_url = env.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
    model = env.get("DEEPSEEK_MODEL", "deepseek-chat")

    if not api_key:
        print("❌ 错误: 未找到 DEEPSEEK_API_KEY。请配置 /etc/webnovel/.env")
        sys.exit(1)

    # 读取 system prompt
    system_content = ""
    if system_prompt_path:
        system_content = Path(system_prompt_path).read_text(encoding="utf-8")

    # 读取 user input
    user_content = ""
    if user_input_path:
        user_content = Path(user_input_path).read_text(encoding="utf-8")

    import requests

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    messages = []
    if system_content:
        messages.append({"role": "system", "content": system_content})
    if user_content:
        messages.append({"role": "user", "content": user_content})
    else:
        messages.append({"role": "user", "content": "请根据提示词生成内容。"})

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
    }

    try:
        resp = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=payload,
            timeout=120,
        )
        resp.raise_for_status()
        result = resp.json()
        content = result["choices"][0]["message"]["content"]

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            Path(output_path).write_text(content, encoding="utf-8")
            print(f"✅ DeepSeek 输出已写入: {output_path}")
        else:
            print(content)

        # 记录调用日志
        log_dir = Path(os.environ.get("WEBNOVEL_DATA_ROOT", "/data/webnovel-lab")) / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "system_prompt": system_prompt_path,
            "user_input": user_input_path,
            "output": output_path,
            "success": True,
        }
        log_file = log_dir / "model_calls.jsonl"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

    except Exception as e:
        print(f"❌ DeepSeek API 调用失败: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="统一 DeepSeek 调用")
    parser.add_argument("--system", help="system prompt 文件路径")
    parser.add_argument("--input", help="user input 文件路径")
    parser.add_argument("--output", help="输出文件路径")
    parser.add_argument("--real", action="store_true", help="启用真实 API 调用（默认 mock）")
    args = parser.parse_args()

    if args.real:
        real_call(args.system, args.input, args.output)
    else:
        mock_call(args.system, args.input, args.output)


if __name__ == "__main__":
    main()
