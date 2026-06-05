# Reducer Entry Policy

Reducers may read only accepted state deltas.

## Reject Merge If

- `state_delta.status` is not `accepted`.
- `state_delta.evidence_ref` is missing or empty.
- accepted changes have no evidence reference.
- state delta conflicts with chapter evidence.
- reviewer report conflicts with state delta.
- assigned reviewer has not confirmed acceptance.
- Codex is the only source of acceptance.

## Conflict Handling

If reviewer report and state delta conflict, mark the delta `conflict` and stop reducer entry.

If evidence cannot be traced, mark the delta `needs_human_review`.

If assigned reviewer is unavailable, leave the delta outside reducers.
