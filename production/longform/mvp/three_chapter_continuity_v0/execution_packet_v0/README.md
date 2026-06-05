# Longform Three-Chapter Execution Packet v0

This packet prepares the input shape, execution boundaries, and review checks for a future Hermes / DeepSeek three-chapter continuity sample.

This task does not generate fiction, does not start Hermes or DeepSeek, and does not create a real IP universe or real longform outline. It only converts the accepted synthetic compression v1 direction into a small execution-ready packet.

## Default Mode

The default future execution mode is Lite:

- `chapter_card_lite`
- Critical + Standard reviewer gate
- hot ledger slice
- `state_delta_v1`
- spotlight budget
- Renderer blocker

Research fields stay out of the default execution chain. They may be used later only after a failure diagnosis or explicit owner approval.

## Intended Future Inputs

- `world_slice_lite.template.yaml`
- `single_book_story_lite.template.yaml`
- `volume_card_lite.template.yaml`
- `chapter_card_lite_x3.template.yaml`
- `scene_agency_packet_tasks.template.yaml`
- `event_log_standard.template.yaml`
- `state_delta_v1.template.yaml`
- `hot_ledger_slice.template.yaml`
- `spotlight_budget.template.yaml`

## Edge Rules

- Orchestrator Lite prepares contracts and constraints, not prose.
- Renderer can render only inside the contract and must return a blocker when structure is missing.
- Reviewer checks Critical + Standard gates before any state delta is accepted.
- Reducers accept only `state_delta.status: accepted`.
- Writer and Renderer read hot ledger slices, not full ledger history.
