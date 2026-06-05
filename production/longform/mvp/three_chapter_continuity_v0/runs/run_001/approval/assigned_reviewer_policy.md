# Assigned Reviewer Policy

## Authority

- The project owner is the final assigned reviewer by default.
- ChatGPT may assist with review.
- Codex may organize files, run checks, and report evidence.
- Codex cannot mark any `state_delta` as `accepted`.

## Acceptance Rule

A `state_delta` may be marked `accepted` only by:

- the project owner, or
- a reviewer explicitly delegated by the project owner.

If no assigned reviewer exists, all `state_delta` files are blocked from reducers by default.

## Codex Boundary

Codex may:

- prepare review files
- check YAML and Markdown
- verify path boundaries
- summarize reviewer evidence

Codex may not:

- self-approve run execution
- self-approve state delta acceptance
- bypass project owner review
- enter proposed, conflict, rejected, or needs-human-review deltas into reducers
