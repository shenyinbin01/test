# Mainline Execution Plan

## 接下来先做什么

1. 不再优先扩展 Work Voice 字段。
2. 创建 Character Agency MVP 设计包。
3. 创建 `scene_agency_packet.schema.yaml`。
4. 创建 `consequence_ledger.schema.yaml`。
5. 创建 `relationship_debt_ledger.schema.yaml`。
6. 创建 reviewer gate 草案。
7. 创建 1-scene MVP 设计。
8. 等项目负责人审后，再决定是否 patch skill-pack。

## 建议工程节奏

第一步只做 contract 和 schema，不跑正文。

第二步用一个场景 brief 做 A/B/C 设计，不直接生成正文。

第三步在项目负责人确认后，才决定是否进入实验分支 prompt patch。

第四步如果 prompt patch 通过，再考虑与 Human Texture / Work Voice 的接口合并。

## 输出物验收

- 每个 schema 都能被 YAML 解析。
- 每个 packet 字段都有定义、例子和禁用方式。
- Reviewer gate 能明确标记 `not_polisher_job: true`。
- 后果必须能进入下一场景或下一章状态。
