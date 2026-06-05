# Manual Review Guide

人工审查优先看“是否值得进入 synthetic dry run”，不是评判某个正文版本。

## 审查顺序

1. 先看 `single_book_story` 是否足以约束卷和章。
2. 再看 `volume_card` 是否有阶段目标、压力、回收窗口和结尾状态。
3. 再看三个 `chapter_card` 是否是状态变化合同，而不是一章一句话扩写。
4. 再看 `state_delta` 与 ledger reducers 是否可追溯。
5. 再看 Story Orchestrator Lite 是否只管边界。
6. 再看 Renderer Contract 是否足以阻止结构修补。
7. 最后看 Reviewer Gate 是否能判断退回层级。

## 必问问题

- 这套设计是否比当前逐章生成更可能保留连续性？
- 哪些字段是必要的，哪些可能过重？
- `chapter_card` 是否压死人物主动感？
- `state_delta` 是否能作为唯一写后增量事实？
- Renderer blocker 是否足够明确？
- 是否有任何地方把 Polisher 重新变成救稿角色？

## 通过人工审查后

进入 Codex synthetic dry run，只检查 schema flow 和 artifact shape，不生成正文。
