# Renderer Contract v1 Prompt Boundary

Renderer is contract-limited. It may render only what the accepted inputs permit. If the contract is missing causality, evidence, or knowledge boundaries, Renderer must return a blocker instead of repairing structure.

## Renderer Can Read

- `chapter_card_lite`
- `scene_agency_packet_tasks`
- `event_log_standard`
- `hot_ledger_slice`
- `human_texture_packet` placeholder
- `work_voice_contract` placeholder
- `spotlight_budget`

## Renderer Must Output

```yaml
renderer_output_shape:
  draft: placeholder_only
  render_report:
    source_chapter_card: ""
    source_event_logs: []
    hot_ledger_slice_used: []
    spotlight_budget_followed: true
    blockers: []
  blocker:
    blocker_type: ""
    severity: ""
    return_to: ""
```

## Renderer Forbidden

- Do not change causality.
- Do not change who knows what.
- Do not change relationship debt.
- Do not change resource state.
- Do not change accepted `state_delta`.
- Do not fix structural holes by itself.
- Do not imitate a specific author.
- Do not expand `background_only` spotlight into the main scene burden.

## Blocker Rule

Renderer must return a blocker if:

- A required event has no evidence reference.
- Character knowledge would exceed known state.
- Relationship debt is required but missing from hot ledger slice.
- The chapter card asks for an impossible payoff.
- Spotlight budget conflicts with scene agency.
