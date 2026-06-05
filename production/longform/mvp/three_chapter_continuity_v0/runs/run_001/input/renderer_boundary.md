# Renderer Boundary

Renderer is contract-limited.

## Renderer Can Read

- `chapter_card_lite_x3.yaml`
- future `scene_agency_packet_tasks`
- future `event_log_standard`
- `hot_ledger_slice_initial.yaml` or refreshed hot slice
- Human Texture placeholder
- Work Voice placeholder
- `spotlight_budget_initial.yaml` or refreshed spotlight budget

## Renderer Can Write

- Contract-limited chapter output only after owner approval.
- `render_report`
- `blocker` with severity and return target.

## Renderer Must Not

- Change causality.
- Change who knows what.
- Change relationship debt.
- Change resource state.
- Change accepted `state_delta`.
- Repair structural holes.
- Imitate a specific author.
- Expand background-only items into main scene burden.

## Blocker Return Targets

- Orchestrator: missing causality, impossible chapter card, spotlight conflict.
- Reviewer: evidence trace unclear or gate cannot be judged.
- StateManager: accepted delta or ledger conflict.
