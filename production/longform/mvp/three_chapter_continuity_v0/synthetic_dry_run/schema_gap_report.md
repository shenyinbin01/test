# Schema Gap Report

## world_slice

Finding: shape is usable, but can widen quickly.

Gap:

- Needs a max scope rule, such as "only facts required by the next 3 chapters."
- Needs a field distinguishing hard rule from texture context.

## chapter_card

Finding: powerful but heavy.

Gap:

- `chapter_one_sentence` is correctly demoted, but `chapter_card` may need Lite / Standard variants.
- `spotlight_targets` needs budget and cap.
- `allowed_divergence_band` needs replan threshold.

## state_delta

Finding: traceability works.

Gap:

- Task uses `evidence_ref`; schema uses `evidence_refs`. Dry run kept both.
- Needs `conflict_report` shape for delta vs evidence mismatch.
- Needs accepted / rejected status field before reducers read it.

## ledger reducer

Finding: reducer flow works at shape level.

Gap:

- Needs conflict handling when two deltas update the same fact differently.
- Needs compression rule for hot ledger slice.
- Needs reducer output provenance field per ledger item.

## event_log

Finding: usable bridge from scene agency to state delta.

Gap:

- Schema uses `source_scene_id`; task asks `source_scene_agency_packet`. Dry run kept both.
- Needs explicit distinction between visible event and inferred hidden intention.

## renderer blocker

Finding: five blocker types are enough for v0.

Gap:

- Needs mandatory behavior: blocker prevents Polisher entry.
- Needs mapping from blocker severity to return path.

## drift detection

Finding: shape is reviewable.

Gap:

- Repeated skeleton detection needs concrete artifact metric.
- Reader expectation break needs link to `reader_question_ledger` deadlines.

## anti-feed gate

Finding: gate is auditable at artifact level.

Gap:

- Narrator overreach and prose liveliness remain untestable without generated prose.
- Needs a hard pass/fail format for future reviewer output.
