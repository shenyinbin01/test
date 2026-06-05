# Reducer Acceptance Rules

Reducer input is blocked unless all conditions pass.

## Never Merge

- `status: proposed`
- `status: conflict`
- `status: needs_human_review`
- `status: rejected`
- any delta without `evidence_ref`
- any delta without assigned reviewer acceptance

## Merge Only If

- `status: accepted`
- accepted by assigned reviewer
- `accepted_changes` has evidence references
- conflict report is `none`
- source event log is reviewable

## Stop Rule

If Reviewer cannot judge the state delta, stop the run and return to the responsible layer.
