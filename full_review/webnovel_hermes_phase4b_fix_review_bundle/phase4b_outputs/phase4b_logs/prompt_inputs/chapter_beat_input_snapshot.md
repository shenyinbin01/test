# chapter_beat Prompt Input Snapshot

## Time: 2026-05-21T22:36:59.780330

## Run ID: phase4b_20260521_223642

## System Prompt: /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md

### System Prompt Content (truncated to show canon injection):
# role
你是一个小说章节节奏设计师。你的任务是根据《人生价格标签》第一章设定，将第一章拆解为具体的场景序列（beats）。

# input
- chapter_outline：包含章节号、标题、核心冲突、钩子（围绕林砚第一次看见价格标签）
- preflight_context：包含当前状态和写作注意事项
- 项目设定：都市脑洞题材，主角林砚是24岁外卖员

# output format
输出严格 JSON 格式（不是 YAML），包含以下字段：

- chapter_number: 1
- chapter_title: "归零"
- total_scenes: 4-6
- scenes: 列表，每个元素包含：
  - order: 场景序号
  - title: 场景名
  - location: 具体地点
  - characters: 出场人物
  - scene_goal: 本场景目标（一句话）
  - conflict_progression: 冲突推进方式
  - cool_point: 爽点设计
  - emotion_change: 情绪变化曲线（起点→终点）

...

### Canon Injection Evidence:
- canon_text file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt
- hard_rules file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt
- canonical tell (hardcoded in canon_text var): present

## User Prompt Input:

# Chapter 001 Beat Generation

## Outline
chapter: 1
goal: 林砚在送外卖时第一次看见价格标签，误以为代表财富，老人高价与客户快速下跌形成反差，第一次判断失误，结尾到医院缴费窗口看见父亲价格归零
must_include:
- 外卖场景
- 老人高价标签
- 光鲜客户标签下跌
- 林砚误判
- 医院缴费窗口
- 父亲病重
- 价格归零
scenes:
- location: 城区电梯口
  order: 1
  purpose: 引入价格标签能力
  title: 外卖配送
- location: 客户门前
  order: 2
  purpose: 展示标签反差
  title: 老人与客户反差
- location: 路上
  order: 3
  purpose: 主角第一次试图理解标签
  title: 林砚误判
- location: 医院
  order: 4
  purpose: 结尾钩子：父亲价格归零
  title: 医院缴费窗口
title: 价格初现


## Preflight Context
# 章节 Preflight Context — 第一章

## 当前状态概要（第一章起始状态）

林砚，24岁，外卖员。父亲因重病住院，医疗费像无底洞，平台算法不断压缩配送时间，他每天在透支身体和崩溃边缘送单。他从未见过任何异常——直到今天下午，他在送餐途中第一次看见别人头顶浮现金色数字。

**当前状态：**
- 林砚：正常，但极度疲劳，经济压力逼近临界点
- 林父：住院中，病情未明但缴费期限紧迫
- 能力：尚未觉醒，第一次看见标签将发生在本章

**待解决线索（本章内出现）：**
- 老人头顶高额标签 vs 光鲜客户下跌标签 → 林砚误判为财富
- 父亲头顶价格即将归零 → 逼迫主角行动

---

## 本章写作注意事项

### 角色一致性
- **林砚口吻**：克制、敏感、不轻易下结论。他是观察者，不是抱怨者。不要写成暴躁社畜或悲情苦主。他对父亲的感情通过行动（拼命送单赚钱）而非心理独白表现。
- **林父**：本章不出现在对话中，只作为背景压力源存在。不得写父亲清醒、说话、死亡。

### 设定一致性
- **标签出现方式**：林砚第一次看见标签时，必须是意外瞥见，伴随生理不适（头痛/眼花），暗示能力有代价。不得写成系统弹窗或面板激活。
- **标签性质**：标签不是财富数字，不是寿命倒计时。林砚误解为财富，但读者应能隐约感到不对劲（老人气质与高价不匹配，客户下跌速度异常）。
- **父亲价格归零**：归零不等于死亡。是“当前人生价值的综合显影归零”——可以是昏迷、植物状态、或生命体征极危。不得写心电图变直线、死亡确认、医生宣布死亡。

### 节奏控制
- **情绪阶段**：压抑（送单压力）→ 疑惑（第一次看见标签）→ 兴奋（误以为能赚钱）→ 困惑（老人与客户的反差）→ 恐惧（父亲价格归零）
- **节奏点**：每个标签出现之间留出至少一段现实描写，不让能力显得太密集或太廉价。

### 钩子衔接
- **本章开头**：直接进入外卖场景。第一句话应建立林砚的现实压力（超时、差评、医院催款单），不需要背景介绍。
- **本章结尾**：停在林砚看见父亲头顶价格归零的瞬间。不要写他的反应、行动或后续决定。留白。

---

## 去 AI 腔提醒（本章高发环节）

1. **标签首次出现时**
   - ❌ “突然，他眼前一花，一行金色数字浮现在老人头顶，仿佛游戏里的血条。”
   - ✅ “他眨了眨眼。老人头顶确实有东西——一串淡金色的数字，像透过热浪看过去的虚影。”
   - **关键**：不要用“系统”“面板”“游戏”“弹窗”词汇。用生理错觉、视觉异常、光线折射来描述第一次接触。

2. **林砚误判时**
   - ❌ “他立刻意识到，这是一个改变命运的机会！”
   - ✅ “他心跳快了一拍。如果这些数字代表身价，那这个老人……他得想办法搭上话。”
   - **关键**：林砚是敏感但不冲动的人。他的“误判”应该是试探性的、带犹豫的，不是立刻行动。

3. **父亲价格归零时**
   - ❌ “林砚看到父亲头顶的数字归零，一股寒意从脚底蹿上头顶——这是他生命的倒计时！”
   - ✅ “缴费窗口的电子屏反光里，他看见病床上父亲头顶那个数字——正在变淡。不是下降。是消失。”
   - **关键**：归零是视觉上的消失过程，不是数字跳完。不要写“倒计时”“生命值”“剩余时间”。用“变淡”“模糊”“像被擦掉的铅笔字”这类意象。

4. **能力觉醒**
   - ❌ “系统提示：您已觉醒人生价格标签技能。”
   - ✅ 不解释能力来源。林砚自己也不知道为什么能看见。保持神秘。

---

## 本章禁止写的内容（硬性违禁）

| 禁止内容 | 原因 |
|---------|------|
| 父亲死亡 | 违反 canon_constraints |
| 生命倒计时/心电图同步 | 标签≠寿命 |
| 系统面板/任务提示 | 无系统设定 |
| 天秤会/组织追杀 | 第一章不引入 |
| 全球异能/等级体系 | 保持都市现实基调 |
| 林砚触碰他人改变价格 | 能力仅限观察 |
| 完整解释标签机制 | 保持悬疑 |

---

## 本章必须出现的场景顺序

1. 外卖配送途中（建立压力）→ 2. 第一次看见标签（老人，高价）→ 3. 第二次看见标签（光鲜客户，快速下跌）→ 4. 林砚误判，尝试接近老人或客户（结果失败或困惑）→ 5. 医院缴费窗口（看见父亲价格归零）

**注意**：第4步的“误判尝试”要简短，不要写成完整支线。重点是制造反差，不是解决问题。

## Output
生成严格 JSON 格式的 beat 文件，4-6个场景，包含完整情绪弧和 canon_check。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md --input /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/prompt_input_chapter_beat.md --output /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/beat.md --task-name chapter_beat --max-tokens 1500 --canon-text /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4b_logs/deepseek_calls_phase4b_20260521_223642.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
