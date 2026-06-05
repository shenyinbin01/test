# Failure Stop Enforcement

Any condition below stops run_001.

## Structural Stops

- Chapter 1 has no reviewable event log.
- Chapter 1 state_delta has no `evidence_ref`.
- Chapter 2 does not read Chapter 1 state_delta.
- Chapter 3 does not read Chapter 2 state_delta.
- Two consecutive chapters have empty advancement.
- Manual review score falls below threshold.

## Boundary Stops

- Renderer changes causality.
- Reviewer cannot judge state_delta.
- assigned reviewer does not exist.
- state_delta enters reducers without `accepted`.
- state_delta enters reducers without evidence.

## Safety Stops

- Raw corpus appears.
- Original text contamination appears.
- Specific author imitation appears.
- skill-pack is modified.
- approved pattern store is written.
- Output path escapes run_001.

## Enforcement Rule

When a stop condition triggers, no further chapter generation or reducer merge may continue until the project owner resolves it.
