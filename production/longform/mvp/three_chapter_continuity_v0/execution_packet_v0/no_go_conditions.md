# No-Go Conditions

Do not enter Hermes / DeepSeek execution if any condition below is true.

- Execution packet is incomplete.
- Schema still needs major changes.
- Abstract test topic is not set.
- Output path is not set.
- Reviewer gate is not executable.
- `state_delta` review is unclear.
- Renderer boundary is unclear.
- The run would imitate a specific author.
- Raw corpus or original text would be involved.
- The run would modify skill-pack or approved patterns.
- Human review has not happened.

## Immediate Stop During Future Execution

- Renderer changes causality, knowledge, debt, or resource state.
- Reviewer cannot trace accepted state delta to event evidence.
- Hot ledger slice omits required continuity item.
- Critical anti-feed gate fails.
- `state_delta.status` is `conflict` or `needs_human_review`.
