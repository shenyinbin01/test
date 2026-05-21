# chapter_beat Prompt Input Snapshot

## Time: 2026-05-21T22:17:19.854468

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
# Preflight Context — 第一章

## 当前状态概要

上一章结束时：林砚在医院缴费窗口，看见父亲头顶标签从5000逐步下降至归零消失，得知父亲已转ICU，银行卡掉在柜台，他转身跑向走廊尽头。

角色位置：医院缴费窗口→ICU方向走廊。状态：极度焦虑、震惊、困惑。

待解决线索：
- 父亲价格归零意味着什么（不是死亡，但迫在眉睫）
- 标签真实含义仍未知
- 老人身份未揭示
- 光鲜客户暴跌原因未完全揭示

## 本章写作注意事项

### 角色一致性
- **林砚**：克制、敏感、观察力强。此刻应呈现“压抑的慌乱”——行动迅速但沉默，内心有大量未说出口的推演。口吻保持现实感，不煽情。
- **父亲**：不出场对话，只作为病床上的存在。不写死亡。

### 设定一致性
- 价格归零 ≠ 死亡。不能写“心电图成直线”“生命倒计时”。
- 标签不是系统面板，不显示说明文字、任务提示、倒计时。
- 禁止出现：天秤会、组织、系统、等级、异能组织。

### 节奏控制
本章位于：**悬念释放+情感重压**阶段。
- 开篇直接从医院走廊开始，承接上章结尾。
- 中间穿插林砚回忆白天老人和客户的标签反差，形成对照。
- 结尾停在ICU门口，不进入病房，留白。

### 钩子衔接
本章开头需接：林砚跑向走廊尽头，ICU门在视线尽头。
- 建议：以动作和感官细节开场（脚步声、消毒水味、走廊灯光），不解释。

## 去AI腔提醒

1. **“他意识到”句式**：本章林砚处于困惑和直觉驱动状态，不要写“他意识到标签代表XXX”。他还不懂。
2. **心理描写过度**：避免大段内心独白。用动作、停顿、视线转移替代。
3. **标签数字出现场景**：只在林砚主动看的时候出现。不自动弹出、不闪烁、不伴随音效。
4. **“突然”“瞬间”滥用**：父亲价格归零是逐步下降（5000→归零），不是瞬间崩盘。用过程感替代突袭感。
5. **煽情收尾**：ICU门口不要写“他握紧拳头，眼里燃起火焰”。写他停下脚步，看见玻璃窗里的父亲，手里攥着那张掉在柜台的银行卡。

## Output
生成严格 JSON 格式的 beat 文件，4-6个场景，包含完整情绪弧和 canon_check。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md --input /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/prompt_input_chapter_beat.md --output /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/beat.md --task-name chapter_beat --max-tokens 1500 --canon-text /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4b_logs/deepseek_calls_phase4b.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
