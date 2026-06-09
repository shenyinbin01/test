# Hermes Output Contract

Hermes must write outputs under:

```text
production/longform/run003_c_engine_variants_v0/results/hermes_run003/
```

## Required Per Variant

```text
<variant>/
  generation/
    chapter_001_draft.md
    chapter_002_draft.md
    chapter_003_draft.md
  private_engine/
  review/
    chapter_001_llm_checklist.md
    chapter_002_llm_checklist.md
    chapter_003_llm_checklist.md
  state/
    state_delta_ch001.yaml
    state_delta_ch002.yaml
    state_delta_ch003.yaml
    ledger_view_after_ch001.yaml
    ledger_view_after_ch002.yaml
    ledger_view_after_ch003.yaml
  reports/
    variant_completion_report.md
```

## Required Global Outputs

```text
human_blind_eval_materials/
  anonymized_samples/
  pair_map_private.yaml
reports/
  hermes_completion_report.md
  stop_report.md (only if needed)
```

State deltas must remain proposed. Ledger views must remain preview-only.
