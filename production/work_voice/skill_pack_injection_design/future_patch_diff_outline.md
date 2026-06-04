# Future Patch Diff Outline

This is a future PR outline only. It does not patch any `skill-pack` file in this round. Future PR must be explicitly approved by the project owner.

## File: `skill-pack/creation_skills/webnovel_planner/SKILL.md`

Planned change:

- Add optional Work Voice runtime packet input.
- Add scene-level `work_voice` output block to chapter beat / context.
- Add prohibition against author imitation, source text, and `source_work_id` as style label.
- Add failure routing when `voice_contract` is vague or scene_type stance conflicts with beat.

## File: `skill-pack/creation_skills/webnovel_writer/SKILL.md`

Planned change:

- Add optional `work_voice_brief` input.
- Add execution rules for narrator position, reader relationship, protagonist distance, world attitude, interventions, rhythm, details, stable flaws, and anti-AI voice.
- Add prohibition against explaining fields in正文.
- Add contamination guards and no author imitation rule.
- Add failure handling for missing stable narrator and source contamination.

## File: `skill-pack/creation_skills/webnovel_reviewer/SKILL.md`

Planned change:

- Add Work Voice gate dimensions.
- Add output block `work_voice_gate`.
- Add hard fail rules for author imitation and source contamination.
- Add return-to layer policy.
- Add `no_polisher_overreach` check.

## File: `skill-pack/creation_skills/webnovel_polisher/SKILL.md`

Planned change:

- Add explicit Work Voice boundary section.
- Allow only local tone / rhythm polishing after structural approval.
- Prohibit fixing missing narrator position, reader relationship, vague contract, or Planner scene_type errors.
- Require stop when Reviewer marks `polisher_allowed: false`.

## Future PR Guardrails

- Patch only after project owner approval.
- Patch on experimental branch only.
- Do not modify Human Texture v0 semantics.
- Do not add `approved_patterns`.
- Do not widen Polisher authority.
- Run dry run before A/B/C.
