#!/usr/bin/env bash
# DeepCode 任务完成通知脚本
# 调用方式：由 DeepCode settings.json 的 notify 字段触发
# 注入环境变量：DURATION, STATUS, FAIL_REASON, BODY, TITLE, WEBHOOK_URL
#
# 功能：
# 1. 写入状态文件 /tmp/deepcode_jobs/<job_id>/
# 2. 如果配置了 WEBHOOK_URL，发送飞书卡片消息
# 3. BODY 最长截取 2000 字

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
# 写入状态文件
# ============================================================
JOBS_DIR="/tmp/deepcode_jobs"
JOB_DIR="$JOBS_DIR/$JOB_ID"
mkdir -p "$JOB_DIR"

# 摘要 BODY（截取 2000 字 + 保留最后 500 字用于上下文）
BODY_SUMMARY="${BODY:0:2000}"
if [ "${#BODY}" -gt 2000 ]; then
    BODY_SUMMARY="${BODY_SUMMARY}\n\n...(truncated, full length: ${#BODY} chars)..."
fi

# 写入 status.json
cat > "$JOB_DIR/status.json" << JSONEOF
{
  "job_id": "$JOB_ID",
  "status": "$STATUS",
  "title": "$TITLE",
  "duration_seconds": $DURATION,
  "fail_reason": "$FAIL_REASON",
  "body_length": ${#BODY},
  "generated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
JSONEOF

# 写入 last_output.md（摘要版）
cat > "$JOB_DIR/last_output.md" << MDEOF
# DeepCode 任务完成报告

**状态：** $STATUS
**任务：** $TITLE
**耗时：** ${DURATION}s
**Job ID：** $JOB_ID

---

$BODY_SUMMARY
MDEOF

echo "[notify] status written to $JOB_DIR/status.json" >&2

# ============================================================
# 微信主动通知（核心事件驱动）
# ============================================================
WEIXIN_SEND_SCRIPT="/home/agentuser/.deepcode/notify_send_weixin.py"
if [ -x "$WEIXIN_SEND_SCRIPT" ]; then
    # 提取 marker 和 summary 用于微信消息
    python3 "$WEIXIN_SEND_SCRIPT" \
        --status "$STATUS" \
        --title "$TITLE" \
        --duration "$DURATION" \
        --body "$BODY" \
        --fail-reason "$FAIL_REASON" \
        --job-id "$JOB_ID" \
        --result-path "$JOB_DIR/status.json" \
        --chat-id "o9cq803Qx92-E0CO3-LYxj7fZ80s@im.wechat" \
        2>&1 || echo "[notify] WeChat send failed (non-fatal)" >&2
fi

# ============================================================
# 飞书 Webhook 通知（仅在配置了 WEBHOOK_URL 时发送）
# ============================================================
if [ -n "$WEBHOOK_URL" ]; then
    # 构建飞书卡片消息（摘要版，不塞完整 BODY）
    # 从 BODY 中提取关键信息
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

const content = '**' + emoji + ' DeepCode 任务 ' + statusText + '**\\n'
    + '> **任务：** ' + title + '\\n'
    + '> **耗时：** ' + duration + 's\\n'
    + (failReason ? '> **失败原因：** ' + failReason + '\\n' : '')
    + '> **Job ID：** ' + (process.env.JOB_ID || 'N/A') + '\\n\\n'
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
