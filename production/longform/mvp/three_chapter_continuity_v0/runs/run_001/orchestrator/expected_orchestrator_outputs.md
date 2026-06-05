# Expected Orchestrator Outputs

If run_001 is approved, Orchestrator should produce:

- `chapter_001_orchestrator_packet`
- `chapter_002_orchestrator_packet`
- `chapter_003_orchestrator_packet`
- `scene_agency_packet_tasks`
- `spotlight_budget`
- `reader_question_refresh_plan`
- `reveal_constraints`
- `allowed_divergence_band`
- `replan_trigger`

## Output Rules

- Use `chapter_card_lite_x3.yaml` as the contract.
- Use only hot ledger slice context.
- Require chapter_002 to read chapter_001 accepted state_delta.
- Require chapter_003 to read chapter_002 accepted state_delta.
- Return blocker if prior accepted delta is missing.
