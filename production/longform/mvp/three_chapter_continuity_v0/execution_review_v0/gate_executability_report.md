# Gate Executability Report

## Summary

The gates are executable enough for a three-chapter controlled sample. A few Standard gates are judgment-heavy, but they are acceptable for human review.

## Classification

| gate source | item | class | note |
|---|---|---|---|
| critical reviewer | chapter_contract_compliance | Clear and executable | Compare output to chapter card fields. |
| critical reviewer | state_delta_traceability | Clear and executable | Requires evidence refs. |
| critical reviewer | relationship_debt_continuity | Clear and executable | Check hot ledger and delta. |
| critical reviewer | knowledge_state_consistency | Clear and executable | Check event evidence and knowledge delta. |
| critical reviewer | renderer_overreach | Clear and executable | Compare Renderer output to forbidden changes. |
| critical reviewer | polisher_boundary | Clear and executable | Polisher must not repair structure. |
| critical reviewer | anti_feed_hard_fail | Clear and executable | Requires any meaningful state movement. |
| standard reviewer | volume_goal_progress | Clear and executable | Check progress, delay, reversal, or cost. |
| standard reviewer | reader_question_continuity | Clear and executable | Check before/after questions. |
| standard reviewer | agency_clarity | Needs clarification | Requires human judgment on bounded choice. |
| standard reviewer | foreshadow_payoff_tracking | Clear and executable | Check seed status and cost. |
| standard reviewer | narrator_overreach | Too subjective | Needs human judgment on evidence vs assertion. |
| standard reviewer | hook_payoff_balance | Needs clarification | Gate is useful but can be taste-sensitive. |
| drift lite | all critical drift items | Clear and executable | Each maps to a ledger or card field. |
| drift lite | standard drift items | Needs clarification | Useful after chapter output exists. |
| anti-feed lite | critical hard fail items | Clear and executable | Good fail-stop layer. |
| anti-feed lite | standard items | Needs clarification | Acceptable for manual review. |
| no-go conditions | all listed conditions | Clear and executable | These are pre-run or immediate stop checks. |

## Recommendation

Use all Critical gates as hard fail. Use Standard gates as score and reviewer notes, except `narrator_overreach`, which should remain human-reviewed rather than automated.
