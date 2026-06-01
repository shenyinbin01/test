# DeepCode 通知链路问题报告（修正版）

## 背景

Phase 8 故事工程流水线中，DeepCode 执行任务完成后需要自动通知用户（微信）。

## 隔离实验

### Step 1: status.json 是谁写的

**结论：notify-feishu.sh 写的。**

notify-feishu.sh 第46-56行通过 bash heredoc 写入 status.json。DeepCode CLI 源代码中**没有**任何写 status.json 的逻辑（grep "status.json" 在 DeepCode cli.js 中返回空）。所以 status.json 的存在本身就是 notify-feishu.sh 被调用的有力证据。

### 实验A: 手工执行 notify-feishu.sh

操作：
```bash
STATUS=completed TITLE=test DURATION=1 \
BODY='[FINAL_DONE]\nmanual notify test' \
JOB_ID=manual_test_$(date +%s) \
bash /home/agentuser/.deepcode/notify-feishu.sh
```

结果：
- ✅ status.json 写入成功（含正确的 title/body/duration）
- ❌ notify_send_weixin.py 执行但发微信失败（ret=-2），但 notify_error.log **未生成**（因为 notify_send_weixin.py 没有 sys.exit(1)）
- 脚本 exit code = 0（错误被忽略）

### 实验B: 手工执行 notify_send_weixin.py

```bash
python3 notify_send_weixin.py \
  --status completed --title "manual direct test" --duration 1 \
  --body "[FINAL_DONE] test" \
  --chat-id "o9cq803Qx92-E0CO3-LYxj7fZ80s@im.wechat"
```

结果：
- ❌ ret=-2 **100% 稳定复现**（连续测试 5 次全部失败，短/字符串/极短消息均失败）
- ✅ 错误信息正确输出到 stderr
- ❌ Python exit code = 0（即使失败）
- ✅ 修复后 exit code = 1

### 实验C: DeepCode 真实任务完成实验

操作：
1. 在 notify-feishu.sh 第3行插入日志：`echo "$(date -Is) notify invoked ..." >> /tmp/deepcode_notify_invoked.log`
2. 通过 tmux send-keys 向 DeepCode 发送最小任务

结果：
- ✅ `/tmp/deepcode_notify_invoked.log` 写入：
  ```
  2026-06-01T21:35:32+08:00 notify invoked JOB_ID= STATUS=completed TITLE=创建并写入...
  ```
- ✅ status.json 写入 `/tmp/deepcode_jobs/deepcode_20260601_213532_3461972/status.json`
- ❌ notify_error.log 写到了 `/tmp/deepcode_jobs/notify_error.log`（因为 JOB_ID 环境变量为空，Python 脚本回退到 `/tmp/deepcode_jobs` 根目录）
- ❌ 微信发送失败（ret=-2）

### 关键纠正：DeepCode notify 触发时机

**原始问题报告的错误判断：** "DeepCode ACP notify 只在进程退出时触发，不是每次任务完成后触发"

**修正后结论：** ❌ 错误。DeepCode 的 `maybeNotifyTaskCompletion()` 在 `activateSession()` 的 `finally` 块中调用，**每次用户输入后、模型完成推理后都会触发**。实验C 的日志证明任务完成后 notify-feishu.sh 立即被调用（而非进程退出时）。

## 真正的问题

### 问题一：微信 iLink 接口 ret=-2（100% 持续）

- ret=-2 是 iLink API 服务器返回的通用错误码
- 非 HTTP 层问题（HTTP 200 + JSON body 中的 ret=-2）
- 非 session expired（-14 才是）
- 与消息长度无关（极短消息也失败）
- **100% 稳定复现**，近期所有调用均失败
- 之前一次成功（`hermes-weixin-eb29325c...`）可能是极偶然情况或 token 状态刚刷新
- 可能原因：token 过期、账号被限流、iLink 服务端问题

### 问题二：notify_send_weixin.py 失败时不报错

- 微信发送失败后没有 `sys.exit(1)`，只 print 了错误
- notify-feishu.sh 的 `|| echo "fail"` 保护使整体脚本 exit 0
- notify_error.log 只在 except 块中写入，send_weixin_direct 返回 success=false 时走 if-else 不写入

### 问题三：notify-feishu.sh 使用 bash heredoc 拼 JSON

- TITLE/BODY/FAIL_REASON 可能包含引号、换行符
- bash heredoc 不做 JSON 转义，会导致 JSON 损坏

### 问题四：chat_id 硬编码

- notify-feishu.sh 硬编码了 `o9cq803Qx92-E0CO3-LYxj7fZ80s@im.wechat`
- 应该优先读 WEIXIN_HOME_CHANNEL 环境变量

## 修复内容

### notify_send_weixin.py 修复

1. 发送失败时 `sys.exit(1)`（之前是 0）
2. 成功/失败都写结构化日志到 notify_error.log（包含 chat_id、account_id、base_url 是否为空、ret、errmsg、message_id）
3. 结构化日志不包含 token

### notify-feishu.sh 修复

1. status.json 改为通过 notify_send_weixin.py 统一写入（Pyhon 做 JSON 序列化，避免 bash heredoc 问题）
2. chat_id 优先读 WEIXIN_HOME_CHANNEL 环境变量，不再硬编码
3. 原有的飞书 Node payload 保留，但需要 `export SUMMARY TITLE STATUS DURATION FAIL_REASON JOB_ID` 到环境（已在 Python 脚本中 export）

## 当前状态

| 问题 | 状态 |
|------|------|
| DeepCode notify 是否在每任务完成时触发 | ✅ 是（每次 finally 块调用） |
| notify-feishu.sh 是否被调用 | ✅ 是（每次任务完成时） |
| --- status.json 是否写入 | ✅ 是（notify-feishu.sh 写入） |
| 微信发送是否独立可用 | ❌ 否（ret=-2 100% 持续失败） |
| ret=-2 的复现条件 | 100% 复现，与消息长度/内容无关，可能与 token/账号状态有关 |

## ret=-2 排查下一步

- 检查 WEIXIN_TOKEN 是否过期（已在 notify_error.log 中记录 account_id 和 base_url）
- 检查 iLink 服务端状态
- 检查账号 `f6e5d0a06d50@im.bot` 是否被限流
- 建议：在 Hermes gateway 的 get_updates 正常拉取消息时，同步检查 token 有效性

## 推荐最终方案

1. **DeepCode 原生 notify 可用** → 使用原生 notify（已验证：每次任务完成时触发）
2. **微信 iLink 不稳定** → 已修复：失败时 exit 1 + 结构化日志，方便追踪
3. **兜底方案** → tmux_monitor.sh（Hermes 主动检测，用户询问或定时检查时使用）

## tmux_monitor.sh 定位说明

tmux_monitor.sh 是**兜底方案**，不是真正的事件驱动方案。

- 用途：在用户询问"好了吗"时，或定时任务轮询时，主动检查 DeepCode tmux 会话是否有 `[FINAL_DONE]` 标记
- 定位：解决了 Hermes 侧"可检测与可补发"的问题，但不能替代 DeepCode 原生的任务完成事件推送
- 不应用来描述为"解决了 DeepCode 完成后主动通知"
