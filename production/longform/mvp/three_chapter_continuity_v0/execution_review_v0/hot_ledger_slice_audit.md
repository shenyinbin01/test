# Hot Ledger Slice Audit

## Summary

Hot ledger slice is the right default. It lowers context load while preserving active state, debt, knowledge, reader questions, and volume progress.

## Checks

| question | finding | result |
|---|---|---|
| Avoids full ledger context overload? | Renderer and Writer are explicitly barred from full ledger. | pass |
| Could miss key relationship debt? | Yes, if Orchestrator selects slice poorly. | medium risk |
| Needs forced must-include items? | Already includes active relationship debt, knowledge boundary, reader question, and volume progress. | pass |
| Needs stale items? | Present, useful when Reviewer flags forgotten continuity. | pass |
| Needs retrieval notes? | Present, and points to latest accepted delta. | pass |
| Needs human confirmation? | Yes for first run, because retrieval quality is untested. | human decision |

## Recommendation

Keep `max_items: 12` for run_001. Require human review of initial hot ledger slice before Chapter 1 and after each accepted state delta.
