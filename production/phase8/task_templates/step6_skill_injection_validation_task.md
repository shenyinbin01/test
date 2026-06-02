# Phase 8 Step 6: Skill Injection & Forward Validation Task

## Objective

Validate whether Phase 8 approved craft patterns can measurably improve the Phase 7 multi-role creation pipeline, using sandbox overlay injection (no modification to production skill-pack).

## Inputs

- `production/phase8/craft_assets/approved_patterns/` — 20 approved craft asset cards
- `production/phase7/` — Phase 7 production skill-pack (READ ONLY)

## Outputs

- `production/phase8/forward_validation/README.md`
- `production/phase8/forward_validation/skill_injection_plan.md`
- `production/phase8/forward_validation/sandbox_overlay_prompts/`
  - `planner_overlay.md`
  - `writer_overlay.md`
  - `reviewer_overlay.md`
  - `polisher_overlay.md`
- `production/phase8/forward_validation/validation_inputs/`
  - `validation_brief.md`
  - `selected_patterns.md`
- `production/phase8/forward_validation/validation_outputs/`
  - `validation_story_bible.md`
  - `validation_chapter_beat.yaml`
  - `validation_draft.md`
  - `validation_review.md`
  - `validation_polished.md`
- `production/phase8/forward_validation/forward_validation_report.md`
- `production/phase8/forward_validation/forward_validation_report.json`

## Key Constraints

- NO modification to Phase 7 skill-pack
- NO new approved_patterns
- NO 《大乘期》 characters, settings, organizations, or plot elements
- NO old Step 3 artifacts
- NO original full-text chapters
- Sandbox overlay only
- Formal skill-pack modification requires Step 6 acceptance first

## Validation Criteria

The forward validation report must answer:
1. Which approved_patterns were used
2. Which role each pattern was injected into
3. Which patterns actually improved output
4. Which patterns were cosmetic only
5. Which patterns risk templating
6. Whether original contamination occurred
7. Whether improvement over Phase 7 baseline is significant
8. Whether to recommend formal skill-pack modification
9. If yes, which specific Skills to modify
10. If no, why not
