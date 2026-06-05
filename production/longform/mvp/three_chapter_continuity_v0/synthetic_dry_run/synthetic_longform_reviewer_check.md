# Synthetic Longform Reviewer Check

本文件模拟 Longform Reviewer Gate。结果只验证结构，不评价文学质量。

| dimension | result | reason | return_to |
|---|---|---|---|
| `chapter_contract_compliance` | pass | all three chapter cards have before / after state changes | none |
| `volume_goal_progress` | pass | each chapter blocks, restores, or partially advances `volume_goal_01` | none |
| `state_delta_traceability` | pass | each delta links to `event_log` and `scene_agency_packet` evidence refs | none |
| `relationship_debt_continuity` | pass | `relationship_debt_01` is created, refreshed, and carried into after-ch3 view | none |
| `knowledge_state_consistency` | pass | `hidden_fact_A` moves from suspected to supported_partial without full verification | none |
| `reader_question_continuity` | pass | questions are refreshed, partially paid, or carried forward | none |
| `foreshadow_payoff_tracking` | pass | `payoff_01` moves from setup to partial payoff | none |
| `agency_clarity` | pass | each scene packet has goal, belief, options, tactic, cost, and blindspot | none |
| `narrator_overreach` | synthetic_not_tested | no prose was generated | Renderer / Work Voice if later detected |
| `renderer_overreach` | pass_shape_only | renderer blockers define forbidden changes; no draft was generated | Renderer Contract |
| `anti_feed_quality` | pass_shape_only | gates can be applied to artifacts, but prose effect is not tested | Reviewer |
| `polisher_boundary` | pass | no polisher action is requested | none |

## Gate Result

`pass_for_synthetic_shape_validation`

## Required Human Attention

- `narrator_overreach` cannot be fully tested without generated prose.
- Reviewer gate may become heavy if all 12 dimensions require full manual scoring for every chapter.
