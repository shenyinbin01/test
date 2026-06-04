# Minimal Patch Plan

This file lists future patch plans only. It does not modify `skill-pack`.

## General Patch Rules

- Patch must be on an experimental branch.
- Patch must not change Human Texture v0 semantics.
- Patch must not introduce `approved_patterns`.
- Patch must not expand Polisher authority.
- Patch must run dry run before A/B/C.

## Planner

File: `skill-pack/creation_skills/webnovel_planner/SKILL.md`

- `proposed_change_summary`: add optional Work Voice runtime packet input and scene-level `work_voice` output block.
- `exact_section_to_add_or_modify`: Inputs, Outputs, Execution Steps, Acceptance Criteria, Prohibited Behaviors.
- `new_contract_fields`: `scene_type`, `narrator_position`, `protagonist_distance`, `reader_relationship`, `world_attitude`, `allowed_interventions`, `forbidden_interventions`, `sentence_rhythm_hint`, `detail_bias`, `stable_flaw_to_keep`, `anti_ai_voice_focus`, `contamination_guard`.
- `backward_compatibility`: optional input; if absent, existing Planner behavior unchanged.
- `risk`: Planner may turn Work Voice into style checklist.
- `test_needed`: dry run with empty packet and synthetic packet; verify no正文 output and no source labels.

## Writer

File: `skill-pack/creation_skills/webnovel_writer/SKILL.md`

- `proposed_change_summary`: add optional `work_voice_brief` execution rules.
- `exact_section_to_add_or_modify`: Inputs, Writing Constraints, Execution Steps, Acceptance Criteria, Failure Handling.
- `new_contract_fields`: `narrator_position`, `reader_relationship`, `protagonist_distance`, `world_attitude`, `intervention_rules`, `rhythm_rules`, `detail_selection_rules`, `stable_flaws_to_keep`, `forbidden_voice_moves`, `anti_ai_voice_rules`, `contamination_forbidden`.
- `backward_compatibility`: if no brief, Writer uses existing beat + Human Texture rules.
- `risk`: Writer may explain fields in正文 or imitate source.
- `test_needed`: prompt dry run that checks expected brief shape without generating正文.

## Reviewer

File: `skill-pack/creation_skills/webnovel_reviewer/SKILL.md`

- `proposed_change_summary`: add Work Voice gate dimensions and return-layer policy.
- `exact_section_to_add_or_modify`: Inputs, Review Dimensions, Output YAML, Reviewer Responsibilities, Pass Criteria.
- `new_contract_fields`: `work_voice_gate`, failed dimensions, `return_to`, `polisher_allowed`, contamination result.
- `backward_compatibility`: existing fourteen dimensions remain unchanged.
- `risk`: Reviewer may check field presence instead of actual narrative effect.
- `test_needed`: dry run with placeholder review inputs; verify gate schema and return routing.

## Polisher

File: `skill-pack/creation_skills/webnovel_polisher/SKILL.md`

- `proposed_change_summary`: add explicit Work Voice non-rescue boundary.
- `exact_section_to_add_or_modify`: Usage, Prohibited Behaviors, Failure Handling, Acceptance Criteria.
- `new_contract_fields`: `work_voice_gate.polisher_allowed`, local polish instruction only.
- `backward_compatibility`: current light-enhancement rules remain unchanged.
- `risk`: Polisher may be asked to fix structural stance failure.
- `test_needed`: dry run with Reviewer report where `polisher_allowed: false`; confirm Polisher must stop.
