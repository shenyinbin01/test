# Output Contract

本轮设计阶段不生成正文。后续获批实验时，输出应区分中间产物和正文草稿，避免只比较成文。

## A 组预期输出

- `draft_chapter_1.md`
- `draft_chapter_2.md`
- `draft_chapter_3.md`
- 粗粒度 writeback report

## B 组预期输出

- 3 个 `chapter_card`
- 3 份 `state_delta`
- reducer 输出的账本视图：
  - plot ledger
  - character state ledger
  - relationship debt ledger
  - knowledge ledger
  - resource ledger
  - reader question ledger
  - foreshadow payoff ledger
  - volume progress ledger
- 三章连续 review report

## C 组预期输出

- B 组全部输出。
- 关键场景 `scene_agency_packet`。
- `event_log`。
- Story Orchestrator Lite report。
- Renderer `render_report`。
- Renderer blocker，如有。

## 共同验收

- 所有 state_delta 必须可追溯。
- 所有 ledger 更新必须来自 reducer。
- Reviewer gate 必须明确退回层级。
- Polisher 不得补结构洞。
