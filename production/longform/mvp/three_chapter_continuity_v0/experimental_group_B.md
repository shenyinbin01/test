# Experimental Group B: Longform Structure

B 组测试长篇车架和 Delta First 状态写回，不测试场景行动包。

## 使用能力

- `single_book_story`
- `volume_card`
- 3 个连续 `chapter_card`
- `state_delta`
- ledger reducers
- longform reviewer gate

## 不使用能力

- `scene_agency_packet`
- Story Orchestrator Lite
- Renderer blocker
- 完整 multi-agent

## 要证明什么

- 章节卡是否比一章一句话更能管理连续性。
- `state_delta` 是否能让状态继承更可追溯。
- 多账本视图是否能减少关系债、信息状态和读者问题丢失。

## 预期风险

- 账本正确但正文无生气。
- 章节卡过细导致人物变木偶。
- 状态写回成本过高。
- reviewer 负担变重。

## 通过倾向

B 不需要比 C 更有活性，但应至少明显优于 A 的连续性和状态继承。
