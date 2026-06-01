#!/usr/bin/env bash
# DeepCode 任务完成通知脚本
# 调用方式：由 DeepCode settings.json 的 notify 字段触发
# 注入环境变量：DURATION, STATUS, FAIL_REASON, BODY, TITLE, WEBHOOK_URL
#
# 功能：
# 1. 写入状态文件 /tmp/deepcode_jobs/<job_id>/
# 2. 发送微信通知
# 3. 如果配置了 WEBHOOK_URL，发送飞书卡片消息

set -euo pipefail

# ============================================================
# 读取环境变量（带默认值）
# ============================================================
STATUS="${STATUS:-unknown}"
TITLE="${TITLE:-Untitled}"
DURATION="${DURATION:-0}"
FAIL_REASON="${FAIL_REASON:-}"
BODY="${BODY:-}"
WEBHOOK_URL="${WEBHOOK_URL:-}"

# ============================================================
# 生成 job_id
# ============================================================
if [ -n "${JOB_ID:-}" ]; then
    JOB_ID="$JOB_ID"
else
    JOB_ID="deepcode_$(date +%Y%m%d_%H%M%S)_$$"
fi

# ============================================================
# 聊天目标：优先 WEIXIN_HOME_CHANNEL 环境变量
# ============================================================
CHAT_ID="${WEIXIN_HOME_CHANNEL:-o9cq803Qx92-E0CO3-LYxj7fZ80s@im.wechat}"

# ============================================================
# 写入状态文件和发送微信通知（统一用 Python 处理）
# ============================================================
JOBS_DIR="/tmp/deepcode_jobs"
JOB_DIR="$JOBS_DIR/$JOB_ID"
mkdir -p "$JOB_DIR"

WEIXIN_SEND_SCRIPT="/home/agentuser/.deepcode/notify_send_weixin.py"
if [ -x "$WEIXIN_SEND_SCRIPT" ]; then
    python3 "$WEIXIN_SEND_SCRIPT" \
        --status "$STATUS" \
        --title "$TITLE" \
        --duration "$DURATION" \
        --body "$BODY" \
        --fail-reason "$FAIL_REASON" \
        --job-id "$JOB_ID" \
        --result-path "$JOB_DIR/status.json" \
        --chat-id "$CHAT_ID" \
        2>&1
    NOTIFY_EXIT=$?
    if [ "$NOTIFY_EXIT" -ne 0 ]; then
        echo "[notify] WeChat send failed (exit=$NOTIFY_EXIT)" >&2
    fi
fi

# ============================================================
# 飞书 Webhook 通知（仅在配置了 WEBHOOK_URL 时发送）
# ============================================================
if [ -n "$WEBHOOK_URL" ]; then
    # 构建飞书卡片消息（摘要版）
    SUMMARY=""
    if echo "$BODY" | grep -q "\[FINAL_DONE\]" 2>/dev/null; then
        SUMMARY=$(echo "$BODY" | grep -A 10 "\[FINAL_DONE\]" | head -12)
    elif echo "$BODY" | grep -q "\[NEED_HUMAN\]" 2>/dev/null; then
        SUMMARY=$(echo "$BODY" | grep -A 10 "\[NEED_HUMAN\]" | head -12)
    elif echo "$BODY" | grep -q "\[FAILED\]" 2>/dev/null; then
        SUMMARY=$(echo "$BODY" | grep -A 10 "\[FAILED\]" | head -12)
    else
        SUMMARY="${BODY:0:500}"
    fi

    # 用 node 构建安全的 JSON payload（避免 bash 转义问题）
    PAYLOAD=$(node -e "
const summary = process.env.SUMMARY || '(no output)';
const title = process.env.TITLE || 'Untitled';
const status = process.env.STATUS || 'unknown';
const duration = process.env.DURATION || '0';
const failReason = process.env.FAIL_REASON || '';

let emoji = '✅';
let statusText = '已完成';
if (status === 'failed') { emoji = '❌'; statusText = '失败'; }

const content = '**' + emoji + ' DeepCode 任务 ' + statusText + '**\\\\n'
    + '> **任务：** ' + title + '\\\\n'
    + '> **耗时：** ' + duration + 's\\\\n'
    + (failReason ? '> **失败原因：** ' + failReason + '\\\\n' : '')
    + '> **Job ID：** ' + (process.env.JOB_ID || 'N/A') + '\\\\n\\\\n'
    + summary.slice(0, 1500);

process.stdout.write(JSON.stringify({
    msg_type: 'interactive',
    card: {
        header: {
            title: { tag: 'plain_text', content: 'DeepCode: ' + title + ' ' + statusText },
            template: status === 'failed' ? 'red' : 'green'
        },
        elements: [
            { tag: 'markdown', content: content }
        ]
    }
}));
" 2>/dev/null) || PAYLOAD='{"msg_type":"text","content":{"text":"[notify error] failed to build feishu payload"}}'

    # 发送飞书 webhook（失败不退出主流程）
    curl -s -X POST "$WEBHOOK_URL" \
        -H "Content-Type: application/json" \
        -d "$PAYLOAD" \
        --connect-timeout 5 \
        --max-time 10 \
        > /dev/null 2>&1 || echo "[notify] feishu webhook failed (non-fatal)" >&2
fi

exit 0
