# preflight_context Prompt Input Snapshot

## Time: 2026-05-21T22:36:42.434596

## Run ID: phase4b_20260521_223642

## System Prompt: /opt/webnovel-hermes-wps/templates/prompts/preflight_context.md

### System Prompt Content (truncated to show canon injection):
# role
你是一个小说章节写作上下文汇编者。你的任务是在写某一章之前，从现有素材中提取最重要的写作参考信息。

# input
- Story Bible
- runtime_canon（已发生事件）
- 待写章节的 chapter_outline
- deai_rules（去 AI 腔规则）

# output format
输出 Markdown，包含以下章节：

1. 当前状态概要（100字以内）
   - 上一章结束时发生了什么
   - 当前角色位置和状态
   - 当前有哪些待解决线索

2. 本章写作时需要注意的：
   - 角色一致性：哪些角色必须保持特定口吻
   - 设定一致性：不能和已发生事件矛盾
   - 节奏控制：本章位于哪个情绪阶段
   - 钩子衔接：本章开头需要接什么

3. 去 AI 腔提醒
   - 根据 deai_rules 列出本章最容易出现 AI 腔的环节

# quality
- 不要超过 800 字
- 辅助性内容，不是创作内容本身
- 每条提醒必须有具体场景对应，不能放空话

【Canon 约束】
- canon_constraint

...

### Canon Injection Evidence:
- canon_text file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt
- hard_rules file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt
- canonical tell (hardcoded in canon_text var): present

## User Prompt Input:

# Chapter 001 Preflight Context Generation — 第一章开局

## 重要提示
这是全书第一章，故事尚未开始。不要写'上一章结束时'或'承接上章'。
所有角色处于初始状态，没有已发生事件。

## Chapter Goal
林砚在送外卖时第一次看见价格标签，误以为代表财富，老人高价与客户快速下跌形成反差，第一次判断失误，结尾到医院缴费窗口看见父亲价格归零

## Must Include
- 外卖场景
- 老人高价标签
- 光鲜客户标签下跌
- 林砚误判
- 医院缴费窗口
- 父亲病重
- 价格归零

## 角色初始状态（第一章开始前）
- 林砚：24岁外卖员，父亲病重，经济压力大，尚未觉醒任何能力
- 林父：病重住院，缴费期限紧迫

## Output
生成本章 preflight_context.md（不超过800字），包含：
- 当前状态概要（从初始状态出发）
- 角色初始状态
- 本章目标
- 本章约束（禁止父亲死亡、禁止生命倒计时等）
注意：这是故事的开端，不要引用任何已发生事件。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/preflight_context.md --input /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/prompt_input_preflight_context.md --output /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/preflight_context.md --task-name preflight_context --max-tokens 1200 --canon-text /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4b_logs/deepseek_calls_phase4b_20260521_223642.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
