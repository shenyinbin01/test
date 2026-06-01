#!/usr/bin/env bash
# ============================================================================
# DeepCode tmux 状态监控 + 微信通知脚本
# 
# 设计思路：
# DeepCode ACP 模式的 notify 只在进程退出时触发，而非每次任务完成时。
# 因此 Hermes 无法依赖 DeepCode 内置 notify 来实现事件驱动。
# 
# 本脚本作为 Hermes 自身的一个检测工具，在 Hermes 收到用户询问"好了吗"
# 或超时后主动调用，检查 DeepCode tmux 会话中的最新任务输出。
#
# 用法：
#   tmux_monitor.sh [options]
#
# 参数：
#   --force-notify   强制发送微信通知（即使状态未变化）
#   --chat-id <id>   指定微信聊天 ID（默认：WEIXIN_HOME_CHANNEL）
#   --title <title>  通知标题前缀
# ============================================================================

set -euo pipefail

# === 参数 ===
FORCE_NOTIFY=false
CHAT_ID="${WEIXIN_HOME_CHANNEL:-o9cq803Qx92-E0CO3-LYxj7fZ80s@im.wechat}"
TITLE_PREFIX="DeepCode"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --force-notify) FORCE_NOTIFY=true; shift ;;
        --chat-id) CHAT_ID="$2"; shift 2 ;;
        --title) TITLE_PREFIX="$2"; shift 2 ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# === 1. 从 tmux 捕获 DeepCode 最新输出 ===
OUTPUT=$(tmux capture-pane -t deepcode -p -S -100 2>/dev/null) || {
    echo "[monitor] ERROR: Cannot capture tmux pane 'deepcode'. Session may be dead." >&2
    exit 1
}

# === 2. 提取状态行 ===
STATUS_LINE=$(echo "$OUTPUT" | grep -E "^status:\s+(completed|processing|failed|pending)" | tail -1)
TOKENS=$(echo "$STATUS_LINE" | grep -oP 'tokens:\s*\K\d+' || echo "0")
STATUS=$(echo "$STATUS_LINE" | grep -oP 'status:\s*\K\w+' || echo "unknown")

# === 3. 检查是否有 [FINAL_DONE] / [NEED_HUMAN] / [FAILED] 标记 ===
if echo "$OUTPUT" | grep -q "\[FINAL_DONE\]"; then
    MARKER="FINAL_DONE"
    TASK_DONE=true
elif echo "$OUTPUT" | grep -q "\[NEED_HUMAN\]"; then
    MARKER="NEED_HUMAN"
    TASK_DONE=true
elif echo "$OUTPUT" | grep -q "\[FAILED\]"; then
    MARKER="FAILED"
    TASK_DONE=true
else
    MARKER=""
    TASK_DONE=false
fi

# === 4. 提取标题（最后一个 ## 开头的行或 > 开头的任务描述） ===
TITLE=$(echo "$OUTPUT" | grep -E "^>\s+" | tail -1 | sed 's/^>\s*//' | head -c 80)
if [ -z "$TITLE" ]; then
    TITLE=$(echo "$OUTPUT" | grep -E "^##\s+" | tail -1 | sed 's/^##\s*//' | head -c 80)
fi
if [ -z "$TITLE" ]; then
    TITLE="${TITLE_PREFIX} 任务"
fi

# === 5. 提取摘要 ===
SUMMARY=""
if $TASK_DONE; then
    # 从标记之后提取关键行
    SUMMARY=$(echo "$OUTPUT" | grep -A 30 "\[FINAL_DONE\]\|\[NEED_HUMAN\]\|\[FAILED\]" | head -20)
elif [ "$STATUS" = "completed" ]; then
    # 从最后输出的非空行提取摘要
    SUMMARY=$(echo "$OUTPUT" | tail -40 | grep -v "^status:" | grep -v "^---" | grep -v "^enter send" | grep -v "^>" | head -10)
fi

echo "[monitor] status=$STATUS marker=${MARKER:-none} tokens=$TOKENS done=$TASK_DONE" >&2

# === 6. 计算耗时（从重复时间戳行估算） ===
# 取第一个和最后一个时间戳行的时间差
FIRST_TS=$(echo "$OUTPUT" | grep -oP '\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}' | head -1)
LAST_TS=$(echo "$OUTPUT" | grep -oP '\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}' | tail -1)
if [ -n "$FIRST_TS" ] && [ -n "$LAST_TS" ]; then
    FIRST_EPOCH=$(date -d "$FIRST_TS" +%s 2>/dev/null || echo 0)
    LAST_EPOCH=$(date -d "$LAST_TS" +%s 2>/dev/null || echo 0)
    DURATION=$((LAST_EPOCH - FIRST_EPOCH))
    [ "$DURATION" -lt 0 ] && DURATION=0
else
    DURATION="?"
fi

# === 7. 构建微信消息体 ===
if $TASK_DONE; then
    case "$MARKER" in
        FINAL_DONE) EMOJI="✅"; STATUS_TEXT="完成" ;;
        NEED_HUMAN) EMOJI="🤔"; STATUS_TEXT="需人工确认" ;;
        FAILED) EMOJI="❌"; STATUS_TEXT="失败" ;;
        *) EMOJI="ℹ️"; STATUS_TEXT="通知" ;;
    esac
else
    if [ "$STATUS" = "completed" ]; then
        EMOJI="✅"; STATUS_TEXT="空闲"
    elif [ "$STATUS" = "processing" ]; then
        EMOJI="⏳"; STATUS_TEXT="执行中"
    else
        EMOJI="ℹ️"; STATUS_TEXT="$STATUS"
    fi
fi

BODY="${EMOJI} DeepCode: ${TITLE}\n状态：${STATUS_TEXT}"
[ "$DURATION" != "?" ] && BODY="${BODY}\n耗时：${DURATION}s"
[ "$TOKENS" != "0" ] && BODY="${BODY}\nTokens：${TOKENS}"
if [ -n "$SUMMARY" ]; then
    BODY="${BODY}\n\n---\n${SUMMARY}"
fi

# === 7. 发送微信通知 ===
if $TASK_DONE || $FORCE_NOTIFY; then
    python3 /home/agentuser/.deepcode/notify_send_weixin.py \
        --status "$STATUS" \
        --title "$TITLE" \
        --duration "$DURATION" \
        --body "$BODY" \
        --chat-id "$CHAT_ID" \
        2>&1
    echo "[monitor] WeChat notification sent" >&2
else
    echo "[monitor] Task not done, skipping notification (use --force-notify to override)" >&2
fi

# === 8. 输出状态摘要到 stdout ===
cat << SUMMARY
{
  "status": "$STATUS",
  "marker": "${MARKER:-null}",
  "tokens": $TOKENS,
  "duration_seconds": "$DURATION",
  "task_done": $TASK_DONE,
  "title": "$TITLE"
}
SUMMARY
