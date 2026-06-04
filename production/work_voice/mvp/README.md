# Work Voice MVP Design Package

本目录是 Work Voice / Narrative Stance MVP 的设计包，用于后续 Hermes / DeepSeek / 项目负责人进行受控 A/B/C 验证准备。本轮只做结构化设计，不生成正文，不读取 raw corpus，不修改正式 `skill-pack`。

## 定位

Work Voice 是 Human Texture 之后的上层叙述合同。

- Human Texture 解决“人物 / 信息 / 关系不像人”：人物是否有私欲、关系是否有后果、信息是否通过人和场景发生。
- Work Voice 解决“讲故事的人是否稳定存在”：叙述者站在哪里，离主角多近，把读者当什么，怎么看世界，什么时候插嘴或隐身。

Work Voice 不等于作者指纹，不等于复刻作者，不等于普通文风润色，也不负责直接写正文。它的产物服务 Planner / Writer / Reviewer，但本轮不改 `skill-pack`。

## MVP 产物流

1. `sample_plan.md`：规划受控观察样本，不保存原文。
2. `voice_observation_cards/`：定义单个样本的观察卡 schema 和人工填写模板。
3. `aggregation/`：把观察卡汇总为 `work_voice_map`、可迁移资产和不可迁移元素。
4. `voice_contract/`：把可迁移声音规则转成 Writer 可执行合同。
5. `validation/`：定义 A/B/C 验证、Reviewer gate、污染检查和评分模板。

## 使用边界

- evidence 只能是抽象引用，例如“作品名 + 章节 / 场景位置 / 人工备注编号”。
- 禁止复制原文句子。
- 禁止保存 raw corpus。
- 禁止把 `source_work_id` 当作风格标签。
- 禁止生成“某作者风格”的写作目标。
- 如果缺少作者站位，不能交给 Polisher 救；应退回 Work Voice Contract / Planner / Writer。

## 下一步

本设计包通过人工验收后，可进入 Work Voice skill-pack injection design：设计如何把 `voice_contract` 注入 Planner / Writer / Reviewer，但仍需在正式修改 `skill-pack` 前完成 A/B/C 证明。
