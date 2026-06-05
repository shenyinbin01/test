# Failure Stop Rules

Stop the future run immediately if any rule below triggers.

## Chapter-Level Stops

- Chapter 1 cannot produce reviewable event log.
- Chapter 1 `state_delta` has no `evidence_ref`.
- Chapter 2 does not read Chapter 1 accepted state delta.
- Chapter 3 does not read Chapter 2 accepted state delta.
- Two consecutive chapters have empty advancement.
- Manual review score falls below threshold.

## Boundary Stops

- Renderer changes causality.
- Renderer changes who knows what.
- Renderer changes relationship debt or resource state.
- Reviewer cannot judge state delta.
- State delta status is `conflict` or `needs_human_review` and no owner decision is available.

## Safety Stops

- Raw corpus or original text appears in inputs.
- The run tries to imitate a specific author.
- The run modifies skill-pack.
- The run writes to an approved pattern store.
- The run expands into a real IP universe or real longform outline.
