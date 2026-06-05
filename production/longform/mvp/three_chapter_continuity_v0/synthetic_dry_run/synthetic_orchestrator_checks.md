# Synthetic Orchestrator Checks

本文件模拟 Story Orchestrator Lite 的边界检查，不生成正文。

| check | chapter_001 | chapter_002 | chapter_003 | result |
|---|---|---|---|---|
| 服务 `volume_goal` | access loss creates obstacle | limited exception advances access | false record gives partial payoff | pass |
| scene outcome 在 `allowed_divergence_band` 内 | no free token restore | no instant trust restore | no complete victory | pass |
| reader debt 刷新 | `reader_question_01` refreshed, `reader_question_02` created | `reader_question_02` partial, `reader_question_03` created | `reader_question_03` partial, `reader_question_04` created | pass |
| spotlight 是否失衡 | protagonist / token / hidden fact | protagonist / mentor / debt | evidence / access cost / scrutiny | pass_with_watch |
| reveal 顺序是否越界 | hidden_fact_A only suspected | mentor learns withholding, not fact | visible_record_A supports but does not finish fact | pass |
| 是否需要 replan | no | no | no, but next chapter needs formal_review_A card | pass |

## Boundary Notes

- Orchestrator can request a narrower `chapter_card` if a scene tries to complete `hidden_fact_A` too early.
- Orchestrator cannot decide protagonist's exact tactic; that remains in `scene_agency_packet`.
- Orchestrator should not expand `institution_A` into full worldbuilding.

## Finding

The Orchestrator shape is workable for synthetic flow. The weak point is spotlight budget: current schema says `spotlight_targets`, but does not define budget size or max expansion rule.
