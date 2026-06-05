# Packet File Inventory

| file | purpose | required_for_execution | status | notes |
|---|---|---:|---|---|
| `README.md` | Defines packet purpose and default Lite mode. | yes | present | Consistent with no-generation boundary. |
| `status.yaml` | Records base, scope, and default mode. | yes | present | Uses all required false flags. |
| `v1_1_patch_notes.md` | Records small v1.1 cleanup scope. | no | present | Useful for review trace. |
| `execution_scope.md` | Defines what a future sample validates. | yes | present | Keeps sample narrow. |
| `world_slice_lite.template.yaml` | Minimal world context template. | yes | present | Needs human topic fill. |
| `single_book_story_lite.template.yaml` | Book-level spine template. | yes | present | Light enough for sample. |
| `volume_card_lite.template.yaml` | Volume-level goal and window template. | yes | present | Carries three-chapter pressure. |
| `chapter_card_lite_x3.template.yaml` | Three chapter card templates. | yes | present | Ch2 and Ch3 read previous delta. |
| `scene_agency_packet_tasks.template.yaml` | Scene-level agency task template. | yes | present | Prevents reaction-only character design. |
| `event_log_standard.template.yaml` | Evidence trace from scene task to delta. | yes | present | Supports state delta evidence. |
| `state_delta_v1.template.yaml` | Proposed / accepted / conflict delta contract. | yes | present | Accepted-only reducer rule is clear. |
| `hot_ledger_slice.template.yaml` | Minimal ledger context for Writer / Renderer. | yes | present | Max item cap is set to 12. |
| `spotlight_budget.template.yaml` | Controls scene burden and relationship debt manifestation. | yes | present | Owned by Orchestrator. |
| `orchestrator_lite_execution_boundary.md` | Defines Orchestrator inputs, outputs, and forbidden actions. | yes | present | Does not write prose. |
| `renderer_contract_v1_prompt_boundary.md` | Defines Renderer read scope and blocker behavior. | yes | present | Boundary is mostly hard enough. |
| `critical_standard_reviewer_gate.md` | Defines Critical + Standard review gates. | yes | present | Excludes Research checks. |
| `drift_detection_lite.md` | Defines minimal drift checks. | yes | present | Runs after review and delta. |
| `anti_feed_gate_lite.md` | Defines low-quality feed hard fails. | yes | present | Good stop layer. |
| `execution_artifact_flow.md` | Defines future artifact flow. | yes | present | Matches expected outputs. |
| `hermes_deepseek_readiness_checklist.md` | Human pre-run checklist. | yes | present | Still requires owner signoff. |
| `manual_review_checklist.md` | Human audit prompts. | yes | present | Needs scoring rubric, added in this review. |
| `no_go_conditions.md` | Blocks execution under unsafe conditions. | yes | present | Covers major risks. |
| `expected_outputs_if_later_executed.md` | Lists future artifacts only. | yes | present | Does not create run files. |
| `next_step_recommendation.md` | Recommends human review before sample. | no | present | Aligned with this review. |
