# Ledger Hot Slice Design

Writer / Renderer 不读取全量 ledger。Orchestrator 从 ledger views 里抽取 hot ledger slice。

## Shape

```yaml
hot_ledger_slice:
  source_ledgers:
    - plot_ledger
    - character_state_ledger
    - relationship_debt_ledger
    - knowledge_ledger
    - reader_question_ledger
    - volume_progress_ledger
  included_items:
    - ledger:
      item_id:
      summary:
      latest_delta_ref:
  inclusion_reason:
    - "must affect current chapter choice"
    - "must affect next 1-3 chapters"
    - "must constrain knowledge, relationship, or volume progress"
  max_items: 12
  must_include:
    - current_volume_goal_progress
    - current_protagonist_pressure
    - active_relationship_debt
    - active_knowledge_boundary
    - active_reader_question
  excluded_items:
    - "resolved debts with no next manifestation"
    - "world facts not used in next 3 chapters"
    - "old resources with no choice impact"
  stale_items:
    - item_id:
      reason:
      last_delta_ref:
  retrieval_notes:
    - "prefer latest accepted delta"
    - "include stale item only if reviewer flags it"
```

## Rules

- Hot slice only includes current 1-3 chapter relevant content.
- Max item count is a cap, not a target.
- Renderer reads hot slice, not raw ledger history.
- Orchestrator owns hot slice selection.
- If hot slice omits required continuity item, Reviewer returns to Orchestrator.
