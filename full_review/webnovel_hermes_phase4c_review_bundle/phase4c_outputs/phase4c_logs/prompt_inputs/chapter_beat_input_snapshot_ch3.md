# chapter_beat Prompt Input Snapshot (Chapter 3)

## Time: 2026-05-23T09:28:41.176555

## Run ID: phase4c_20260523_092706

## System Prompt: /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md

### System Prompt Content (truncated):
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
- canon_text file used: /data/webnovel-lab/demo_output/phase4c_logs/phase4c_canon.txt
- hard_rules file used: /data/webnovel-lab/demo_output/phase4c_logs/chapter_003_hard_rules.txt
## User Prompt Input:

# Chapter 003 Beat Generation

## Outline
chapter: 3
goal: 林砚第一次主动干预选择，标签变化，付出代价，父亲病情持续，自己标签异常
must_include:
- 承接第二章标签暴跌/现实危险线索
- 林砚主动选择
- 价格标签变化
- 选择代价
- 能力副作用
- 父亲病情压力
- 自己标签异常钩子
scenes:
- location: 医院/街道
  order: 1
  purpose: 展示第二章的后果与林砚的状态
  title: 承接第二章
- location: 医院内
  order: 2
  purpose: 发现病人家属标签随选择变化
  title: 观察标签变化
- location: 医院/街道
  order: 3
  purpose: 林砚第一次主动干预选择
  title: 第一次主动选择
- location: 路上
  order: 4
  purpose: 付出代价，能力副作用显现
  title: 选择代价
- location: 场景结尾
  order: 5
  purpose: 发现自己的标签也在异常变化
  title: 自己标签异常
title: 第一次主动选择


## Preflight Context
# Chapter 003 Preflight Context

## 当前状态概要

林砚父亲正在抢救中，心率持续下降。电话中女声告知“时间不多”后挂断。林砚已确认标签能预警危险（光鲜客户诈骗案），但父亲头顶价格归零后变为空白，与常人不同。他获得风险评估师“方迟”名片，老人暗示他理解有误。能力副作用（头痛、短暂失明、耳鸣）持续存在。

**位置**：医院病房门口（父亲抢救中）
**待解决线索**：
- 父亲头顶空白含义
- 方迟身份与能力真相
- 老人未说完的话
- 未知号码短信来源
- 地下停车场中年男人（七位数闪烁红光）

---

## 本章写作注意

### 角色一致性
- **林砚**：克制、敏感、观察力强。面对父亲抢救应表现出克制下的焦虑，不是崩溃大哭。对能力的使用从被动观察转为主动试探，但仍有犹豫和恐惧。
- **父亲**：病重昏迷中，不能苏醒、不能说话、不能互动。只能通过监护仪声音、护士对话、林砚视角观察来呈现状态。
- **电话女声**：保持神秘，不揭示身份，不多说一句话，只提供线索或压力。

### 设定一致性
- 标签不是寿命：父亲抢救不能与标签数值变化同步（如数字随心跳下降）
- 标签不是系统：林砚不能看到自己标签的详细解释或操作说明
- 能力副作用必须出现：本章至少出现一次头痛/短暂失明/耳鸣
- 父亲必须存活：抢救后病情稳定或暂时稳定，不能死亡

### 节奏控制
- **情绪阶段**：高潮后回落期（第二章结尾抢救→本章前半段紧张等待→后半段新发现）
- **节奏建议**：
  - 开篇：抢救进行中，林砚在走廊等待，紧张氛围
  - 中段：抢救结束/暂时稳定，林砚观察病人家属标签变化，第一次主动干预
  - 后段：林砚查看自己标签，发现异常，引入新悬念
- **节奏陷阱**：不能连续高潮，抢救后需要缓冲段落

### 钩子衔接
- **本章开头**：直接承接第二章结尾——抢救正在进行，林砚站在走廊，电话已挂断
- **本章结尾**：林砚发现自己头顶标签异常（与常人不同），但具体含义不明

---

## 去 AI 腔提醒

1. **“标签变化”场景**：病人家属因选择上升标签时，不要写“标签数字跳动了一下，从X变成了Y”，避免系统面板感。写“数字边缘亮了一下，像被什么力量推了一把”。

2. **“林砚第一次主动干预”场景**：不要写“他决定使用能力，集中精神”，避免游戏技能释放感。写“他盯着那个数字，脑子里只有一个念头——让它动一下试试”。

3. **“自己标签异常”场景**：不要写“系统提示：您的标签显示为异常状态”，避免系统面板。写“林砚低头看自己，那个数字……和别人的不一样”。

4. **“选择代价”场景**：不要写“他付出了XX代价，获得了XX回报”，避免游戏化。写“林砚蹲在地上，耳鸣嗡嗡响，手里攥着那张纸条——他不知道值不值”。

5. **父亲病情描述**：不要写“生命体征平稳”“病情稳定”，避免医疗报告感。写“监护仪的线条恢复了平稳，护士说暂时没事了”。

6. **避免这些词**：“然而”“但是”“突然”“就在这时”“只见”“不禁”“心中一惊”“下意识地”“瞬间”“仿佛”。

7. **心理描写**：不要写“林砚心想”，直接写他的观察和感受。例如：“走廊里消毒水的味道让他想起母亲住院那一年。他甩甩头，不让自己想下去。”

---

## 本章禁止内容
- ❌ 父亲死亡或濒死
- ❌ 标签等于寿命/生命倒计时
- ❌ 林砚完全掌握能力规则
- ❌ 林砚能力大幅变强或完全控制
- ❌ 系统面板、任务提示、充值商城
- ❌ 天秤会、组织、全球异能体系
- ❌ 老人或女声完全揭示标签真相
- ❌ 林砚与父亲生命数值同步

## Output
生成严格 JSON 格式的 beat 文件，4-6个场景，包含完整情绪弧和 canon_check。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md --input /data/webnovel-lab/demo_output/phase4c_real_run/chapter_003/prompt_input_chapter_beat.md --output /data/webnovel-lab/demo_output/phase4c_real_run/chapter_003/beat.md --task-name chapter_beat --max-tokens 1500 --canon-text /data/webnovel-lab/demo_output/phase4c_logs/phase4c_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4c_logs/chapter_003_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4c_logs/deepseek_calls_phase4c_20260523_092706.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
