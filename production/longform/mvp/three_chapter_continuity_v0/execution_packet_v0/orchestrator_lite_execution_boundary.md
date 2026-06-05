# Orchestrator Lite Execution Boundary

Story Orchestrator Lite is a boundary manager for future execution. It prepares chapter contracts, scene tasks, ledger retrieval, and review-facing constraints.

## Inputs

- `world_slice_lite`
- `single_book_story_lite`
- `volume_card_lite`
- `previous_state_delta`
- `hot_ledger_slice`
- `reviewer_feedback_if_any`

## Outputs

- `next_chapter_card_lite`
- `scene_agency_packet_tasks`
- `spotlight_budget`
- `reader_question_refresh_plan`
- `reveal_constraints`
- `allowed_divergence_band`
- `replan_trigger`

## Forbidden

- Do not write prose.
- Do not choose a specific action for the character.
- Do not edit accepted ledger entries.
- Do not bypass Reviewer.
- Do not become a hidden author.

## Replan Trigger

Return to Orchestrator if:

- `state_delta.status` becomes `conflict`.
- The next chapter cannot read required previous delta fields.
- Relationship debt disappears without evidence.
- Knowledge state becomes impossible.
- Renderer reports missing causality or missing evidence.
