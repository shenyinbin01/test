# Mainline Execution Plan

## 当前路线

当前主线从“继续叠 prompt patch”改为“发动机 + 车架 + 写回 + 治理”的闭环设计。

1. 保留 Human Texture v0 底座，不再扩成普通去 AI 味工具。
2. 完成 Character Agency / `scene_agency_packet` 的可审查设计。
3. 将 Consequence Ledger、Relationship Debt Ledger 和 State Delta 接成状态继承核心。
4. 创建 Longform hot path schema：`world_slice`、`single_book_story`、`volume_card`、`chapter_card`。
5. 定义 Story Orchestrator Lite 与 Narrative Renderer Contract。
6. 创建三章连续 MVP 设计包，不生成正文。
7. 定义 longform reviewer gate、drift detection 和 anti-feed quality gate。
8. 人工审查后，再决定是否做 synthetic dry run。
9. synthetic dry run 通过后，再考虑 Hermes / DeepSeek 三章小样本。
10. 三章小样本仍通过后，才讨论是否进入 skill-pack 实验分支。

## 工程节奏

第一步只做 contract、schema、gate 和设计包，不跑正文、不调用模型。

第二步做 synthetic dry run，只检查 schema 流转、artifact shape、state_delta 到 ledger reducer 的追溯关系，不生成小说正文。

第三步经项目负责人批准后，才让 Hermes / DeepSeek 跑三章连续小样本。

第四步如果三章小样本证明连续性提升，再设计实验分支 prompt patch；正式 skill-pack 不直接修改。

## 输出物验收

- 每个 YAML schema 都能被解析。
- 每个 schema 都说明 owner、readers、update_timing、failure_modes 和 not_for。
- `chapter_one_sentence` 只作为导航锚点，不作为完整章节合同。
- `state_delta` 是写后唯一增量事实。
- ledger 只能由 reducers 生成，不能由 Writer 或 Renderer 直接手改。
- Story Orchestrator Lite 不写正文、不替角色做选择。
- Narrative Renderer 不能改因果、资源、关系、知识状态和 accepted 章节合同。
- Reviewer gate 能明确退回 Orchestrator、Scene Engine、Renderer 或 Polisher。
