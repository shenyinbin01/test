# Orchestrator Lite v1 Contract

Story Orchestrator Lite v1 is a boundary manager. It does not write prose and does not choose for characters.

## Inputs

- `book_spine`
- `volume_card`
- `chapter_card_lite_or_standard`
- `hot_ledger_slice`
- `previous_state_delta`
- `reviewer_feedback_if_any`

## Outputs

- `next_chapter_card`
- `scene_agency_packet_tasks`
- `spotlight_budget`
- `reader_question_refresh_plan`
- `reveal_constraints`
- `allowed_divergence_band`
- `replan_trigger`

## Output Shape

```yaml
orchestrator_lite_v1_output:
  next_chapter_card_mode: Lite
  scene_agency_packet_tasks:
    - scene_id:
      active_character:
      required_choice_pressure:
      forbidden_resolution:
  spotlight_budget:
    primary_focus: []
    secondary_focus: []
    background_only: []
    forbidden_to_steal_scene: []
    max_scene_focus_count: 3
  reader_question_refresh_plan:
    must_refresh: []
    may_delay: []
  reveal_constraints:
    allowed_reveals: []
    forbidden_reveals: []
  allowed_divergence_band: []
  replan_trigger:
    - "scene outcome violates must_not_happen"
    - "state_delta status becomes conflict"
```

## Forbidden

- 不写正文。
- 不替角色选择具体行动。
- 不修改 accepted ledger。
- 不越过 Reviewer。
- 不变成隐藏作者。

## v1 Adjustment

Orchestrator now owns `spotlight_budget` and hot ledger slice selection. It must keep default mode Lite unless the Reviewer or project owner requests Standard / Research.
