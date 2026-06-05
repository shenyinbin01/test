# Compatibility With Existing Pipeline

## Current Boundary

当前不改 `skill-pack`，不改 Planner / Writer / Reviewer / Polisher 的正式 SKILL.md，不启动 Hermes / DeepSeek。

## Possible Future Placement

| Existing role | Future compatibility |
|---|---|
| Planner | Could create `world_slice`, `single_book_story`, `volume_card`, and `chapter_card` before chapter beat. |
| Longform Planner / Story Orchestrator Lite | May be added as a thin layer between Planner and scene-level Writer brief. It should manage boundary, not write prose. |
| Writer | Future Writer should read `renderer_input` or sanctioned scene brief, not all raw ledgers. |
| Reviewer | Needs longform gate for chapter contract, state_delta traceability, drift, and anti-feed checks. |
| StateManager | Future upgrade should move from rough `chapter_commit` to `state_delta + reducers`. |
| Polisher | Still cannot fill structural holes, character agency, state ledger gaps, or missing information carrier. |

## Integration Shape

```text
Planner
  -> Longform hot path cards
  -> Story Orchestrator Lite checks
  -> Scene Agency Packet
  -> Event Log
  -> Renderer Input
  -> Draft, if later generated
  -> Reviewer Gate
  -> State Delta
  -> Ledger Reducers
  -> Next Chapter Retrieval
```

## Compatibility Risks

- Existing `chapter_commit` may not carry enough evidence refs.
- Writer may be overloaded if asked to read every ledger.
- Reviewer gate may need Lite mode to avoid manual burden.
- StateManager needs reducer behavior before production use.
