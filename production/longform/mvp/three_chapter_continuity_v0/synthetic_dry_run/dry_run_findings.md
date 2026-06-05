# Dry Run Findings

## What Connected

1. `world_slice -> single_book_story -> volume_card -> chapter_card` connects cleanly as a hot path.
2. Three `chapter_card` files can carry cross-chapter state using explicit `reads_state_delta`.
3. `scene_agency_packet` can keep protagonist choice visible without turning into prose.
4. `event_log` can provide evidence for `state_delta`.
5. `state_delta -> ledger_reducer_flow -> ledger_views_after_ch3` works as an artifact chain.
6. Renderer Contract can define allowed reads and forbidden changes.
7. Reviewer, Drift Detection, and Anti-feed gates can all be represented without generated text.

## What Felt Heavy

1. `chapter_card` has many required fields; it may need Lite / Standard modes.
2. Reviewer gate has 12 dimensions; full manual review every chapter may be costly.
3. Ledger views after ch3 are useful but can become bulky quickly.
4. Renderer inputs should not include all ledgers, only a hot slice.

## Missing Or Ambiguous Fields

1. `spotlight_targets` exists, but no explicit spotlight budget rule.
2. `allowed_divergence_band` exists, but no severity threshold for when replan triggers.
3. `state_delta` has evidence refs, but conflict report shape is not yet defined.
4. `event_log` naming differs between schema and task wording.
5. Drift detection lacks a concrete repeated skeleton metric.

## Boundary Risks

1. Orchestrator could become hidden author if it specifies tactics instead of boundaries.
2. Renderer could overreach if blocker is optional rather than mandatory.
3. StateManager must not invent ledger facts when reducer input is incomplete.

## Overall Result

Synthetic dry run completed. The schema flow connects, but next step should compress over-heavy fields before real generation.
