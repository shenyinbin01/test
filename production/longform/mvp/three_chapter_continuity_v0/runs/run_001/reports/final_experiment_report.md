# Final Experiment Report

## Run Metadata

- run_id: run_001
- scenario: small organization advancement / assessment
- execution_scope: narrow three-chapter continuity sample
- output_root: `production/longform/mvp/three_chapter_continuity_v0/runs/run_001/`
- state_delta_acceptance: pending assigned reviewer

## Generated Outputs

- chapter_001: generated
- chapter_002: generated and reads chapter_001 state_delta preview
- chapter_003: generated and reads chapter_002 state_delta preview

## Review Summary

- Critical gate result: 0 failures across all three chapters
- Standard gate result: pass, with chapter_002 narrator-overreach risk scored 3
- Reviewer summary: usable proposed-delta sample

## State Delta Summary

| chapter | state_delta | status | reducer_entry |
|---|---|---|---|
| chapter_001 | `state_delta_ch001.yaml` | proposed | blocked |
| chapter_002 | `state_delta_ch002.yaml` | proposed | blocked |
| chapter_003 | `state_delta_ch003.yaml` | proposed | blocked |

No state_delta was marked `accepted` by Codex.

## Ledger Summary

- `ledger_view_after_ch001.yaml`: preview_from_proposed_delta
- `ledger_view_after_ch002.yaml`: preview_from_proposed_delta
- `ledger_view_after_ch003.yaml`: preview_from_proposed_delta

No formal accepted ledger merge occurred.

## Drift Summary

No critical drift detected. The sample stays inside the small organization assessment frame.

## Anti-Feed Summary

No hard anti-feed failure detected. Each chapter changes at least one meaningful state field.

## Manual Scores

| dimension | score |
|---|---:|
| three_chapter_continuity | 4 |
| mainline_progress | 4 |
| volume_goal_progress | 4 |
| character_agency | 4 |
| relationship_debt_inheritance | 4 |
| knowledge_state_consistency | 4 |
| reader_question_continuity | 4 |
| anti_feed_quality | 4 |
| renderer_boundary | 4 |
| state_delta_trust | 4 |
| engineering_artifact_feel | 3 |

- average_score: 3.91
- lowest_dimension: engineering_artifact_feel
- threshold_result: pass_for_experimental_signal

## Pass / Fail

- pass_fail: useful_signal
- reason: The sample demonstrates three-chapter inheritance, proposed state deltas, preview ledgers, and gate coverage without triggering failure stop rules.

## Lessons

- The compact packet is enough to carry resource, debt, knowledge, and reader-question continuity for three chapters.
- Proposed-delta preview ledgers are workable when accepted deltas are unavailable.
- Chapter 002 shows a mild risk of direct explanation; future Work Voice/Renderer pass should watch narrator overreach.
- The run remains non-production because no assigned reviewer accepted state deltas.

## Next Recommendation

Project owner or delegated reviewer should review proposed state deltas. If accepted, a separate task may create accepted reducer output. Codex should not perform that acceptance.
