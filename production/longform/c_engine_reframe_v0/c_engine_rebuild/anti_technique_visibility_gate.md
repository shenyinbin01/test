# Anti-Technique Visibility Gate

This gate hard-fails prose when the reader can see the engine instead of the story.

## Hard Fail Conditions

Fail the draft if any of these appear in foreground prose:

- Orchestrator notes appear.
- Terms such as `state_delta`, `ledger`, `agency_choice`, or `relationship_debt_change` appear.
- The prose directly explains relationship debt escalation instead of making it felt through action, avoidance, delay, concession, or consequence.
- The prose directly names a “third choice” as a structural move.
- The character feels like they are executing a chapter task.
- The scene reads like process description.
- The ending reads like a report summary.
- Technique is too visible.
- Choice lacks desire, fear, shame, misread, or cost.
- Reviewer rewards structural completeness instead of asking whether the reader wants to keep reading.

## Reviewer Questions

- Does the prose feel like people under pressure, or like artifacts satisfying fields?
- Can a reader infer the character's pressure without being told the design purpose?
- Is the scene hotter because tactics clash, not because labels say it is hot?
- Is the aftertaste carried by consequence, not by explanation?
- Would a human blind reader prefer this version over a lower-structure but cleaner scene?

## Gate Result

Use only:

- `pass_to_human_blind_eval`
- `return_to_c_engine`
- `return_to_renderer_v2`

LLM reviewer cannot declare the winning variant.
