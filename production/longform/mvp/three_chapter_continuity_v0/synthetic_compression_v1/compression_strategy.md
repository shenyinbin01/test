# Compression Strategy

## Core Rule

真实小样本优先使用 Lite。Standard 用于正常三章实验。Research 仅用于架构研究，不进入默认链路。

## Compression Moves

1. `chapter_one_sentence` 保留为导航锚点，但不是完整合同。
2. `chapter_card` Lite 只保留最小状态变化合同。
3. Writer / Renderer 不读取全量 ledger，只读取 hot ledger slice。
4. Reviewer gate 分为 Critical / Standard / Research。
5. Anti-feed gate Lite 只保留一票否决项。
6. `state_delta` 增加 `status`，只有 accepted 可进入 reducers。
7. Reducer 输出必须带 provenance，冲突时生成 conflict report。
8. Spotlight budget 进入 Orchestrator 管理，不让 Renderer临时决定聚光。

## Default For Real Three-chapter Sample

默认输入：

- `world_slice`
- `single_book_story`
- `volume_card`
- `chapter_card_lite`
- one scene agency packet per chapter
- standardized event_log
- `state_delta_v1`
- hot ledger slice
- Critical + Standard reviewer gate

不默认输入：

- full ledger views
- Research gate
- multi-agent logs
- long drift analytics
- full IP universe
