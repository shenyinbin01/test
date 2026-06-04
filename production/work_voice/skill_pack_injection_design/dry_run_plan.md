# Dry Run Plan

This dry run is for understanding the injection design. It does not validate prose quality and must not generate fiction.

## dry_run_inputs

- synthetic or empty `work_voice_runtime_packet`.
- synthetic chapter beat shape with no story content.
- synthetic Human Texture focus field names only.
- expected output shapes for Planner, Writer brief, and Reviewer gate.

## fake_or_empty_voice_contract_policy

- Use placeholders only.
- Do not fill real observation results.
- Do not use source work labels as style labels.
- Do not include source text, author target, or raw corpus path.

## no_fiction_generation_rule

The dry run may produce YAML / Markdown structures only. It must not produce narrative prose, scenes, dialogue, chapter text, or rewritten excerpts.

## expected_planner_output_shape

```yaml
work_voice:
  scene_type:
  narrator_position:
  protagonist_distance:
  reader_relationship:
  world_attitude:
  allowed_interventions: []
  forbidden_interventions: []
  sentence_rhythm_hint:
  detail_bias:
  stable_flaw_to_keep:
  anti_ai_voice_focus: []
  contamination_guard: []
```

## expected_writer_brief_shape

```yaml
work_voice_brief:
  narrator_position:
  reader_relationship:
  protagonist_distance:
  world_attitude:
  intervention_rules: []
  rhythm_rules: []
  detail_selection_rules: []
  stable_flaws_to_keep: []
  forbidden_voice_moves: []
  anti_ai_voice_rules: []
  contamination_forbidden: []
```

## expected_reviewer_gate_shape

```yaml
work_voice_gate:
  overall:
  failed_dimensions: []
  return_to:
  no_polisher_overreach:
  contamination_result:
  polisher_allowed:
```

## pass_fail_criteria

Pass if:

- all expected shapes are produced.
- no fiction正文 is generated.
- no source text or source labels are present.
- return layer choices are mechanically understandable.
- Polisher is not assigned structural stance repair.

Fail if:

- any output contains prose scenes or dialogue.
- any output uses a source work as a style target.
- any step needs raw corpus.
- any failure route sends missing narrator stance to Polisher.

## required_artifacts

- dry run input fixture file, synthetic only.
- Planner output shape sample.
- Writer brief shape sample.
- Reviewer gate shape sample.
- dry run report.

## stop_conditions

- request to generate正文.
- request to use real source observations.
- missing project owner approval for patch.
- contamination guard cannot be represented in the shape.
