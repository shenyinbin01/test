# Run003 C Engine Variants v0

Run003 is the formal C Engine four-variant experiment package. It is ready for Hermes to execute prose generation, collect outputs, and return results for human blind evaluation.

This package does not generate fiction. It defines shared inputs, C0/C1/C2/C3 variant contracts, Hermes execution instructions, human blind pairwise evaluation, LLM checklist-only review, validation scripts, and report templates.

## Positioning

- A is retired as active architecture and kept only as historical baseline.
- B is frozen as Longform Chassis.
- C is the active research line.
- Run003 compares four C variants on the same input.
- The main evaluation is human blind pairwise preference.
- LLM reviewer is checklist-only and must not choose the winner.

## Directory Map

- `input/`: unified input package shared by all variants.
- `variants/`: C0/C1/C2/C3 execution contracts and renderer/private-engine templates.
- `hermes_execution_packet/`: instructions for Hermes formal generation.
- `review/`: human blind evaluation and LLM checklist-only review packages.
- `validation/`: readiness and forbidden-action checks.
- `reports/`: result templates for Hermes and final verdict.

## Current State

Run003 is ready for Hermes execution after project owner review. Codex has not generated prose, has not changed run002 artifacts, and has not modified skill-pack or phase8 assets.
