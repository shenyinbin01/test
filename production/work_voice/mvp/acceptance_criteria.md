# Acceptance Criteria

本文件定义 Work Voice MVP 设计包通过标准。

## 目录完整

- `production/work_voice/mvp/README.md`
- `production/work_voice/mvp/sample_plan.md`
- `production/work_voice/mvp/acceptance_criteria.md`
- `production/work_voice/mvp/risk_register.md`
- `production/work_voice/mvp/status.yaml`
- `production/work_voice/mvp/voice_observation_cards/`
- `production/work_voice/mvp/aggregation/`
- `production/work_voice/mvp/voice_contract/`
- `production/work_voice/mvp/validation/`

## Schema 完整

- `voice_observation_card_schema.yaml` 包含所有必需字段，并为每个字段定义 `type`、`required`、`description`、`allowed_values` 或 `examples`、`forbidden_content`。
- `voice_contract_schema.yaml` 包含所有必需字段，并为每个字段定义 `type`、`required`、`description`、`examples`、`forbidden_content`。

## 模板可填写

- Markdown 和 YAML 模板均为空模板，不填真实作品内容。
- 每个关键字段都有填写提示。
- 模板能由人工 Reviewer 或 Hermes 后续填充，不需要解释隐藏规则。

## 边界清晰

- 明确区分 `transferable_voice_rule` 与 `non_transferable_original_element`。
- 明确禁止作者复刻和具体作者模仿。
- 明确禁止 raw corpus、原文句子、可识别桥段入库。
- 明确本轮不改 `skill-pack`、不改 `production/phase8`、不新增 `approved_patterns`。

## 验证可执行

- A/B/C 验证计划定义 A、B、C 的输入条件、禁用输入、评分维度、pass/fail 阈值、污染检查和重跑条件。
- Reviewer gate 能判断失败应退回 Planner、Writer、Polisher 或 Work Voice Contract 哪一层。
- 明确“缺少作者站位不能交给 Polisher 救”。

## 可作为下一阶段输入

通过标准：

- 项目负责人能直接使用 `sample_plan.md` 规划观察样本。
- 人工 Reviewer 能直接填写 observation card。
- Hermes 能把 `work_voice_map` 汇总为 `voice_contract`。
- 后续 skill-pack injection design 能基于本包定义 Planner / Writer / Reviewer 接口。
