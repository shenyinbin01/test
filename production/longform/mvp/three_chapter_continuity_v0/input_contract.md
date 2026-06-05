# Input Contract

三章连续 MVP 的输入应尽量小，足以验证热路径，不足以滑成真实长篇大纲。

## 共用输入

- `world_slice`：最小世界切片。
- `single_book_story`：单书脊梁。
- `volume_card`：当前卷卡。
- `chapter_cards`：3 个连续章节卡。
- `initial_hot_ledger_slice`：初始热账本切片。

## A 组输入

- 3 个现有风格的 chapter beat。
- 粗粒度 `runtime_canon` 或状态摘要。
- 不提供 `chapter_card`。
- 不提供 `state_delta` schema。

## B 组输入

- `single_book_story`
- `volume_card`
- 3 个 `chapter_card`
- `state_delta.schema.yaml`
- ledger reducer rules
- 不提供 `scene_agency_packet`

## C 组输入

- B 组全部输入。
- 每章关键场景的 `scene_agency_packet`。
- Story Orchestrator Lite 约束。
- Renderer Contract 与 blocker 类型。

## 禁止输入

- raw corpus。
- 具体作者参照。
- 真实长篇正文。
- 完整 IP 宇宙资料。
- 可污染的原文片段。
