# Renderer Boundary Audit

## Summary

Renderer boundary is strong enough for a controlled sample if the blocker rule is enforced. The main risk is Renderer silently repairing missing causality instead of returning blocker.

## Boundary Checks

| question | finding | risk | mitigation |
|---|---|---|---|
| Can Renderer still repair causality? | It is explicitly forbidden, but future prompt must repeat blocker behavior near output shape. | medium | Require blocker whenever causality is missing. |
| Can Renderer change who knows what? | It is explicitly forbidden and tied to knowledge state. | low | Reviewer checks knowledge consistency. |
| Can Renderer change relationship debt? | It is forbidden and debt is protected by hot ledger and spotlight budget. | low | Reviewer checks debt continuity. |
| Can Renderer turn Work Voice into lecture? | Placeholder exists, but no Work Voice execution contract is included. | medium | Keep Work Voice placeholder minimal in first run. |
| Can Renderer blocker return to the right layer? | Blocker has `return_to`, and examples imply Orchestrator or Reviewer. | low | Require `return_to` to be one of Orchestrator, Reviewer, or StateManager. |

## Verdict

Renderer boundary is usable, but the first real run should treat any unexplained structural repair as immediate stop.
