# State Delta Acceptance Policy

## Status Values

- `proposed`
- `accepted`
- `rejected`
- `conflict`
- `needs_human_review`

## Reducer Rules

- `proposed` does not enter reducers.
- `conflict` does not enter reducers.
- `needs_human_review` does not enter reducers.
- `rejected` does not enter reducers.
- Only `accepted` may enter reducers.
- `accepted` must include `evidence_ref`.
- `accepted` must include assigned reviewer approval.
- Codex cannot self-approve `accepted`.

## Missing Reviewer Rule

If assigned reviewer is missing or unclear, all state deltas remain non-mergeable.
