# Run003 Execution Plan

## Objective

Move from C Engine direction confirmation to an executable four-variant experiment that Hermes can run without further ad hoc instructions.

## Experiment Shape

Four variants use identical story input:

1. C0_current_c_anchor: current C style anchor, with stronger foreground leak bans.
2. C1_private_deep_fields: private author/character/scene/reader/stance fields, no exemplar pack.
3. C2_exemplar_distillation: fewer private fields, stronger good/bad craft exemplars.
4. C3_hybrid_harness: private deep fields plus exemplar pack and anti-technique review. This is the main candidate.

## Execution Steps

1. Hermes reads the unified input package.
2. Hermes runs variants in order C0, C1, C2, C3.
3. Hermes writes each variant output to a variant-specific output directory.
4. Hermes must keep private engine files separate from prose drafts.
5. Hermes runs LLM checklist-only gate after each variant.
6. Hermes anonymizes draft outputs for human blind pairwise evaluation.
7. Humans evaluate pairwise preference with hidden variant labels.
8. Aggregator computes C3 vs C0 thresholds.
9. Final verdict is produced from human preference plus checklist failures.

## Non-Goals

- No A/B/C rerun.
- No run002 rewrite.
- No official ledger creation.
- No state_delta acceptance.
- No raw corpus usage.
- No author imitation target.
- No skill-pack changes.

## Success Question

Does C3 beat C0 as readable fiction while preserving B chassis continuity and avoiding visible machinery?
