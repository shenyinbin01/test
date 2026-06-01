# DeepCode 通知链路问题报告

## 背景

Phase 8 故事工程流水线中，DeepCode 执行任务完成后需要自动通知用户（微信）。

## 当前架构

- Hermes 通过 tmux 管理 DeepCode 会话
- Hermes 使用 `tmux send-keys` 下发任务给 DeepCode
- DeepCode 执行任务并输出 `[FINAL_DONE]` 标记
- 用户需要在不主动询问的情况下收到 DeepCode 完成通知

## 问题一：DeepCode 内置 notify 不适用于每次任务完成

### DeepCode 配置

settings.json 中配置了 notify 字段指向 notify-feishu.sh：

```json
{
    "notify": "/home/agentuser/.deepcode/notify-feishu.sh"
}
```

### 实测结果

DeepCode ACP 模式的 notify 注入以下环境变量：
- DURATION, STATUS, FAIL_REASON, BODY, TITLE, WEBHOOK_URL

但 notify 脚本**只在 DeepCode 进程退出时被调用，每次任务完成后不触发**。

证据：任务完成后 status.json 被写入到 `/tmp/deepcode_jobs/<job_id>/`，但 notify-feishu.sh 中调用的 `notify_send_weixin.py` 没有执行痕迹（notify_error.log 不存在，微信未收到消息）。

### 影响

无法依赖 DeepCode 内置 notify 实现每次任务完成的事件驱动通知。

## 问题二：微信 iLink 接口间歇性 ret=-2

### 通知脚本架构

1. `notify-feishu.sh` — entrypoint，读取环境变量，写入 status.json，然后调用 notify_send_weixin.py
2. `notify_send_weixin.py` — Python 脚本，调用 Hermes gateway 的 `send_weixin_direct()` 函数
3. `send_weixin_direct()` — 位于 `gateway/platforms/weixin.py`，使用 iLink API（ilink/bot/sendmessage）

### 实测结果

部分调用成功（用户确认收到消息，message_id = `hermes-weixin-eb29325c...`），部分调用失败报 `ret=-2`：

```
[Weixin] send chunk failed to=o9cq803Q attempt=1/3, retrying in 1.00s: iLink sendmessage error: ret=-2 errcode=None errmsg=unknown error
[Weixin] send chunk failed to=o9cq803Q attempt=2/3, retrying in 2.00s: iLink sendmessage error: ret=-2 errcode=None errmsg=unknown error
[Weixin] send failed to=o9cq803Q: iLink sendmessage error: ret=-2 errcode=None errmsg=unknown error
```

成功时 message_id 格式为 `hermes-weixin-<uuid>`。

### 疑点

- `ret=-2` 在 iLink API 中代表什么？是否限流 / token 过期 / 网络抖动？
- 成功与失败的间隔很短（几分钟内），排除了长期 token 失效的可能
- 重试间隔 1s→2s 仍失败，说明不是瞬时抖动
- 是否需要增加退避策略或检查 token 有效性？

## 替代方案

已创建 `tmux_monitor.sh`：

功能：
1. 从 tmux 会话捕获 DeepCode 最新输出
2. 提取 `[FINAL_DONE]` / `[NEED_HUMAN]` / `[FAILED]` 标记
3. 提取任务标题、耗时、token 消耗
4. 提取关键摘要
5. 调用 `notify_send_weixin.py` 发送微信通知
6. 输出机器可解析的 JSON 状态摘要

用法：
```bash
bash /home/agentuser/.deepcode/tmux_monitor.sh [--force-notify] [--chat-id <id>] [--title <prefix>]
```

替代方案的核心变化：从"DeepCode 主动推"改为"Hermes 主动查"。

## 待审核

1. notify-feishu.sh 的逻辑是否合理？
2. notify_send_weixin.py 的异常处理是否足够？
3. tmux_monitor.sh 是否可以作为替代方案？
4. iLink ret=-2 的可能原因是什么？
5. 是否有更好的事件驱动通知方案？
