# preflight_context Prompt Input Snapshot

## Time: 2026-05-21T22:17:10.567784

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

# Chapter 001 Preflight Context Generation

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

## Runtime Canon Events
- 林砚在送外卖时第一次看见人生价格标签
- 发现老人头顶价格异常高
- 发现光鲜客户价格快速下跌
- 林砚误以为标签代表财富
- 医院缴费窗口看见父亲头顶价格归零
- 林砚回访光鲜客户的地址调查线索
- 发现客户标签暴跌与治安事件有关
- 林砚对标签的理解从财富推进一步
- 使用能力后出现头痛后遗症
- 父亲病情仍然持续
- 林砚在医院观察收费员和病人家属的标签变化
- 发现标签随选择变化
- 第一次主动试图理解和使用能力
- 观察自己的标签发现异常变化
- 父亲病情压力仍然存在
- 林砚在送外卖爬楼梯时首次看见老人头顶浮现87,000,000的数字标签
- 林砚在路边观察快递员头顶80万、宝马车主头顶12万，发现数字与财富无关
- 林砚给高档小区客户送餐时，看见其头顶标签从32万快速下跌，并听见门内争吵声
- 林砚在老人递外卖时无意触碰，发现标签从87,000,000涨到87,200,000
- 林砚赶到医院，在缴费窗口方向看见父亲头顶标签从5000逐步下降至归零消失
- 林砚得知父亲已转ICU，银行卡掉在柜台，转身跑向走廊尽头

## Output
生成本章 preflight_context.md（不超过800字），包含当前状态概要、角色状态、已发生事件引用、开放线索、本章约束。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/preflight_context.md --input /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/prompt_input_preflight_context.md --output /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/preflight_context.md --task-name preflight_context --max-tokens 1200 --canon-text /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4b_logs/deepseek_calls_phase4b.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
