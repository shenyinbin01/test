# v0 to v1 Diff Summary

1. `chapter_card` 分层为 Lite / Standard / Research。
2. Lite 成为后续真实三章实验默认输入。
3. Reviewer gate 分层为 Critical / Standard / Research。
4. 真实三章小样本只跑 Critical + Standard，不跑 Research。
5. `state_delta` 增加 `status`、`conflict_report`、`provenance`。
6. 只有 accepted `state_delta` 可进入 reducers。
7. `event_log` 字段统一为 `source_chapter_id`、`source_scene_id`、`source_agency_packet_id`。
8. `spotlight_budget` 新增，并归 Story Orchestrator Lite 管理。
9. hot ledger slice 新增，Writer / Renderer 不读取全量 ledger。
10. reducer conflict handling 补齐，冲突阻塞自动归并。
11. Anti-feed gate 压缩为 Critical hard fail + Standard + Research。
12. Drift Detection 压缩为 Critical + Standard + Research，并给重复骨架提供量化签名。

## Interpretation

v1 不再追求把所有风险都放进默认链路，而是把默认链路压到能真实试跑的程度。
