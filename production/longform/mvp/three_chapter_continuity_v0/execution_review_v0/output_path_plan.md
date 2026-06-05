# Output Path Plan

If a future run is approved, use this path:

```text
production/longform/mvp/three_chapter_continuity_v0/runs/run_001/
```

This task does not create `run_001`. It only plans the path.

## Future Directory Shape

```text
input/
  world_slice_lite.yaml
  single_book_story_lite.yaml
  volume_card_lite.yaml
  chapter_card_lite_x3.yaml
  hot_ledger_slice_initial.yaml

orchestrator/
  chapter_001_orchestrator_packet.yaml
  chapter_002_orchestrator_packet.yaml
  chapter_003_orchestrator_packet.yaml

generation/
  chapter_001_draft.md
  chapter_002_draft.md
  chapter_003_draft.md

review/
  chapter_001_reviewer_report.md
  chapter_002_reviewer_report.md
  chapter_003_reviewer_report.md

state/
  state_delta_ch001.yaml
  state_delta_ch002.yaml
  state_delta_ch003.yaml
  ledger_view_after_ch003.yaml

reports/
  drift_report.md
  anti_feed_report.md
  final_experiment_report.md
```

## Path Rules

- Do not write generated outputs into `execution_packet_v0`.
- Do not write generated outputs into `execution_review_v0`.
- Keep run artifacts under `runs/run_001`.
- Store inputs separately from generation and review artifacts.
- Do not create production assets from this run unless separately approved.
