# Generation Manifest - ch001_v1

## Commit
7d820d7

## 样本状态
可进入对照，但不是纯 Renderer Skill 样本。

## 样本等级
A-

## 主执行框架
production/renderer_skill_lab/

## 未启动的旧流程
- Run004
- Run003 / C Engine 正文生产流程
- B 车架正文生产流程
- A/B/C 多变体
- state_delta
- ledger
- reviewer
- completion_report

## 实际生成输入

### 输入 1
路径：production/renderer_skill_lab/inbox/seeds/ch001.md
用途：唯一情节素材来源。

### 输入 2
路径：production/renderer_skill_lab/skill/renderer_skill.md
用途：Renderer Skill 约束。
说明：这是生成 ch001_v1 时实际使用的 Renderer Skill 版本。

### 输入 3
路径：/home/agentuser/.hermes/skills/webnovel/webnovel_writer/SKILL.md
用途：Hermes 本地网文写作约束。
说明：该 skill 只作为通用写作约束参与，不是本次 Renderer Skill Lab 的正式 Skill 文件。
注意：因此 ch001_v1 不能表述为"纯 Renderer Skill v0 效果"。

### 输入 4
来源：用户本次会话任务指令。
用途：提供字数目标、禁止项、扩写边界。

### 输入 5
路径：production/phase8/reverse_assets/dachengqi/reverse_story_bible.md
用途：确认世界观连续性，包括九州大陆、飞升断绝、江离是当代人皇等。

## 原文隔离确认
- 未接触原文；
- 未提交原文；
- 未引用原文；
- 未使用 Phase7 / Phase8 正文生成产物。

## 正确审计口径
ch001_v1 是 Hermes 在 Renderer Skill 约束下，叠加既有 webnovel_writer skill 和 Phase8 世界观资产生成的第一版扩写样本。
它可以用于后续原文对照和 Skill Delta 提取，但不能被表述为"纯 Renderer Skill v0 效果"。
