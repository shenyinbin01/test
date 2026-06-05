# Drift Detection Lite

Drift detection runs after Reviewer and state delta review. It checks whether the three-chapter chain is still following the intended spine.

## Critical Drift

| drift | detection_method | common_cause | response | return_to |
|---|---|---|---|---|
| mainline_drift | `plot_change` no longer links to book or volume goal. | Chapter follows local incident without spine pressure. | Re-anchor chapter card to volume goal. | Orchestrator |
| volume_goal_drift | Chapter has no progress, delay, reversal, or cost on volume goal. | Hook replaces advancement. | Require explicit volume goal movement. | Orchestrator |
| character_motivation_drift | Character goal changes without accepted state delta. | Renderer or scene task invents new motive. | Return to scene task and state delta review. | Scene Engine / StateManager |
| knowledge_state_disorder | Knowledge ledger conflicts with event evidence. | Reveal is treated as known too early. | Rebuild knowledge delta and blocker. | Reviewer / StateManager |
| relationship_debt_evaporation | Active debt has no manifestation, refresh, delay, or payoff. | Relationship pressure is forgotten between chapters. | Restore debt in hot ledger slice and chapter card. | Orchestrator |

## Standard Drift

| drift | detection_method | common_cause | response | return_to |
|---|---|---|---|---|
| foreshadow_forgotten | Prior seed has no status after expected window. | Ledger slice omits active seed. | Mark seed as active, delayed, or closed. | Reviewer |
| reader_expectation_break | Reader question after state contradicts previous question. | New hook ignores prior curiosity. | Refresh or close prior question explicitly. | Reviewer |
| world_rule_conflict | Event contradicts active world slice rule. | Renderer expands setting beyond slice. | Return blocker and revise world slice or chapter card. | Orchestrator |
