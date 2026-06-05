# Synthetic v1 Reviewer Check

## v0 -> v1 Gate Movement

| gate | v0 status | v1 status | reason |
|---|---|---|---|
| `chapter_contract_compliance` | full reviewer dimension | Critical | must remain default hard check |
| `state_delta_traceability` | full reviewer dimension | Critical | required before reducers |
| `relationship_debt_continuity` | full reviewer dimension | Critical | prevents relationship evaporation |
| `knowledge_state_consistency` | full reviewer dimension | Critical | prevents focalization / reveal errors |
| `renderer_overreach` | full reviewer dimension | Critical | protects causality |
| `polisher_boundary` | full reviewer dimension | Critical | prevents late structural repair |
| `anti_feed_quality` | broad gate | Critical hard fail subset | keep only one-vote fail items by default |
| `volume_goal_progress` | full reviewer dimension | Standard | important but can be human-reviewed in sample |
| `reader_question_continuity` | full reviewer dimension | Standard | needed for three-chapter sample |
| `agency_clarity` | full reviewer dimension | Standard | necessary but not every artifact must be research-scored |
| `foreshadow_payoff_tracking` | full reviewer dimension | Standard | useful for three chapters |
| `narrator_overreach` | prose-dependent | Standard | only meaningful when prose exists |
| `template_pattern_drift` | not quantified | Research | moved out of default; quantified signature proposed |

## v1 Enough For Real Three-chapter Sample?

Yes, with constraints:

- Use Lite chapter cards as default.
- Run Critical + Standard gate only.
- Use hot ledger slice, not full ledger views.
- Keep Research gate out of prompt input.
- Require `state_delta.status == accepted` before reducer merge.

## Watch Items

- Lite may omit `required_reveal`; Orchestrator must ensure reveal constraints separately.
- Narrator overreach cannot be tested until generated prose exists.
- Critical gate must stay short enough for actual reviewer use.
