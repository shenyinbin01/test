# Template Gap Report

## Summary

The templates are usable for a controlled sample. They are deliberately sparse. The main risk is not missing fields, but under-filled fields during a future run.

| template | gap check | finding | severity | recommendation |
|---|---|---|---|---|
| `world_slice_lite` | Too narrow? | Narrow by design; enough if topic is small and institutional. | low | Keep Lite. Require `must_not_expand`. |
| `single_book_story_lite` | Missing end state? | Has `end_state_hint`, not full end state. | low | Accept for sample; do not expand into real outline. |
| `volume_card_lite` | Can carry three chapters? | Goal, escalation path, payoff window, and debt window are enough. | low | Require one explicit volume movement per chapter. |
| `chapter_card_lite_x3` | Controls continuity? | Ch2 and Ch3 read previous delta; fields cover state, reader question, and debt. | low | Fill `required_fields` for previous deltas before execution. |
| `scene_agency_packet_tasks` | Avoids reaction machine? | Includes local goal, belief, options, tactic shape, cost, blindspot, withheld plan. | pass | Keep one task per key scene. |
| `event_log_standard` | Supports delta? | Has source ids, outcome, consequence seed, affected fields, evidence ref. | pass | Require at least one event log per chapter. |
| `state_delta_v1` | Reviews conflict? | Has status, conflict report, rejected changes, provenance, evidence ref. | pass | Assign acceptance owner before execution. |
| `hot_ledger_slice` | Has max items? | `max_items: 12` is explicit. | pass | Human can lower cap if test feels heavy. |
| `spotlight_budget` | Executable? | Has focus tiers, scene steal ban, max focus count, relationship debt manifestation. | pass | Use it before Renderer, not after. |

## Minor Fixes If v0.1 Is Requested

- Add a one-line field note for `previous_delta_input.required_fields`.
- Add an explicit `accepted_by` owner in a run checklist.
- Add output path to packet status after owner approval.
