# Ledger Reducer Conflict Handling

## Core Rules

- Reducers only process accepted `state_delta`.
- If `state_delta` conflicts with current ledger state, reducer generates `conflict_report`.
- If two accepted deltas conflict, automatic merge is blocked.
- If `evidence_ref` is missing, reducer rejects merge.
- If evidence and delta disagree, return to Reviewer / StateManager.
- Writer / Renderer do not directly edit ledger.

## Conflict Types

| conflict_type | example | response |
|---|---|---|
| `missing_evidence` | relationship debt change has no event evidence | reject merge |
| `ledger_conflict` | two deltas assign different resource status | block merge |
| `knowledge_conflict` | character knows fact before accepted reveal | return to Knowledge Ledger / Reviewer |
| `resource_conflict` | resource spent and active at same time | return to StateManager |
| `relationship_conflict` | debt resolved and active without explanation | return to Reviewer |
| `canon_conflict` | delta contradicts accepted canon | needs human review |

## Reducer Output Provenance

Every ledger item should include:

```yaml
provenance:
  latest_delta_ref: ""
  evidence_ref: []
  reducer_id: ""
  merge_status: "merged|blocked|needs_human_review"
```

## Auto-merge Boundary

Reducers can merge clean accepted changes. They cannot infer missing facts to make ledger coherent.
