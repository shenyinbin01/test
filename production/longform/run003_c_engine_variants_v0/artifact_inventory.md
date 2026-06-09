# Artifact Inventory

## Root

- `README.md`: package overview and directory map.
- `run003_execution_plan.md`: formal execution plan.
- `run003_status.yaml`: machine-readable status.
- `artifact_inventory.md`: file inventory.

## Input

- `input/unified_world_slice.yaml`: shared world and assessment mechanism.
- `input/unified_book_spine.yaml`: shared longform spine.
- `input/unified_volume_card.yaml`: shared three-chapter window.
- `input/unified_chapter_cards.yaml`: shared chapter contracts.
- `input/unified_character_seed.yaml`: shared character seed.
- `input/unified_initial_state.yaml`: shared initial state.
- `input/unified_reader_question.yaml`: shared reader-question seed.
- `input/unified_forbidden_list.md`: shared forbidden list.
- `input/input_contract.md`: rules ensuring all variants share one source.

## Variants

Each variant contains a `variant_contract.md`, `prompt_contract.md`, `renderer_input_template.md`, and `expected_outputs.md`. C1 and C3 also include private engine YAML templates. C2 and C3 include exemplar packs.

## Execution And Review

- `hermes_execution_packet/`: Hermes run instructions, order, output contract, forbidden actions, return format, stop rules.
- `review/human_blind_eval/`: pairwise human evaluation package.
- `review/llm_checklist_only/`: checklist-only LLM review package.
- `validation/`: scripts and readiness checklist.
- `reports/`: report templates.
