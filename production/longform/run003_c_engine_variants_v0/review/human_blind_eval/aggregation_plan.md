# Human Evaluation Aggregation Plan

## Required Pairings

- C3 vs C0
- C3 vs C1
- C3 vs C2
- C1 vs C0
- C2 vs C0

## Primary Thresholds

C3 vs C0 must reach:

- reader_pull win rate >= 65%
- anti_ai_surface win rate >= 65%
- character_alive win rate >= 60%
- scene_heat win rate >= 60%
- technique visibility complaints reduced by >= 30%

## Aggregation

1. Count pairwise preferences by hidden variant.
2. Decode private pair map only after evaluation is complete.
3. Compute dimension win rates.
4. Record confidence-weighted notes, but do not let confidence override preference.
5. Produce `human_eval_summary_template.md`.

## Final Rule

If C3 does not beat C0, C Engine rebuild is not accepted regardless of LLM checklist cleanliness.
