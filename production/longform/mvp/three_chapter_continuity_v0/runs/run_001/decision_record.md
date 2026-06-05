# Run 001 Decision Record

Project owner decisions now recorded:

- scenario: C, small organization advancement / assessment.
- output_path: `production/longform/mvp/three_chapter_continuity_v0/runs/run_001/`
- reviewer_gate: Critical + Standard.
- Research gate: disabled.
- state_delta review: human review only.
- reducer rule: only `state_delta.status: accepted` marked by assigned reviewer can enter reducers.
- blocked delta statuses: `proposed`, `conflict`, `needs_human_review`, and `rejected`.
- manual threshold: average score >= 3.8, state_delta trust >= 4, every dimension >= 3, no Critical failure.
- failure stop rules: accepted from `execution_review_v0/failure_stop_rules.md`.
- Hermes / DeepSeek: not approved yet.

## Current Run Permission

This commit may create scaffold and input files only. It may not create chapter output files or call any model.
