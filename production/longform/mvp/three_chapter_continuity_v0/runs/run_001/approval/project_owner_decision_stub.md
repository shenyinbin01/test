# Project Owner Decision Stub

The project owner must fill this before actual run_001 execution.

```yaml
decision:
  approve_run_001_execution: true
  assigned_reviewer: project_owner
  assistant_review_support: ChatGPT
  codex_can_accept_state_delta: false
  allow_hermes: true
  allow_deepseek: true
  output_path_confirmed: true
  failure_stop_rules_confirmed: true
  notes: "Approved for narrow run_001 execution only. Outputs must stay under runs/run_001/. No skill-pack changes, no approved_patterns changes, no raw corpus, no author imitation."
```

## Rule

This approval is limited to run_001. Codex may create execution artifacts, but cannot mark state_delta as accepted.
