# Hermes Return Format

Hermes must return:

```yaml
run003_return:
  run_id: run003_c_engine_variants_v0
  executor: hermes
  status: completed|failed|need_human
  variants_executed:
    C0_current_c_anchor: true
    C1_private_deep_fields: true
    C2_exemplar_distillation: true
    C3_hybrid_harness: true
  prose_generated: true
  state_delta_acceptance: none
  official_ledger_created: false
  raw_corpus_used: false
  author_imitation_target: false
  stop_report_created: false
  output_root: production/longform/run003_c_engine_variants_v0/results/hermes_run003/
  key_files:
    - ""
  risks:
    - ""
  next_required_action: human_blind_eval
```
