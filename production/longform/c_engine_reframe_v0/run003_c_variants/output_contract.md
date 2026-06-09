# Run 003 Output Contract

Each variant must output the same artifact categories.

## Per Variant

```
generation/
  chapter_001_draft.md
  chapter_002_draft.md
  chapter_003_draft.md
private_engine/
  chapter_001_author_intent.yaml
  chapter_001_scene_pressure.yaml
  chapter_001_reader_decompression.yaml
  chapter_001_narrative_stance.yaml
  chapter_002_author_intent.yaml
  chapter_002_scene_pressure.yaml
  chapter_002_reader_decompression.yaml
  chapter_002_narrative_stance.yaml
  chapter_003_author_intent.yaml
  chapter_003_scene_pressure.yaml
  chapter_003_reader_decompression.yaml
  chapter_003_narrative_stance.yaml
review/
  chapter_001_checklist.md
  chapter_002_checklist.md
  chapter_003_checklist.md
state/
  state_delta_ch001.yaml
  state_delta_ch002.yaml
  state_delta_ch003.yaml
  ledger_view_after_ch001.yaml
  ledger_view_after_ch002.yaml
  ledger_view_after_ch003.yaml
```

## Boundary

Private engine artifacts must not enter prose prompts raw. They may only be compiled into natural-language scene briefs, stance briefs, safe continuity summaries, and rights-clear exemplars.

State deltas remain proposed. Ledger views remain previews from proposed deltas.
