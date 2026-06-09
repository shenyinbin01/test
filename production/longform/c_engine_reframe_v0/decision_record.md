# Decision Record

## Decision ID

`C_ENGINE_REFRAME_V0`

## Date

2026-06-09

## Status

`proposed_by_architect / awaiting_owner_acceptance`

## Decisions

1. Retire A_baseline as an active architecture candidate.
2. Freeze B_longform_structure as the Longform Chassis.
3. Rebuild C_longform_engine as an Authorial Cognition Harness.
4. Redesign run_003 as a C-variant experiment: C0, C1, C2, C3.
5. Use human blind pairwise preference as the main evaluation layer.
6. Downgrade LLM reviewer to checklist helper, not final quality judge.

## Rationale

run_002 shows that B already carries most longform continuity value: chapter contracts, state_delta proposals, ledger previews, reader questions, consequence tracking, drift checks, and renderer boundary. C adds visible agency and orchestration, but the present form risks turning fiction into an engineering artifact. A does not supply enough longform control to justify continued investment.

The next useful question is not “does C have more fields than B?” The useful question is whether C can turn private structure into human-readable pressure without leaking the machinery.

## Non-Goals

- Do not execute run_003 in this package.
- Do not generate new fiction.
- Do not rerun run_002.
- Do not modify run_002 prose, state_delta, ledger previews, reviews, or reports.
- Do not mark proposed deltas as accepted.
- Do not create official ledger entries.
- Do not modify `skill-pack` or `production/phase8`.
- Do not save or use raw corpus.
- Do not imitate any specific author.

## Acceptance Authority

Only the project owner can accept this decision. Codex cannot mark this decision accepted and cannot convert any proposed state_delta into accepted state.
