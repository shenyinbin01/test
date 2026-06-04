# Integration Flow

## Future Flow

Step 1: source work observation, outside generation chain.

- Status: MVP has sample planning templates.
- Human review: required.
- Raw corpus入库: forbidden.

Step 2: observation cards.

- Status: MVP has schema and templates.
- Human review: required.
- Generation chain: not involved.

Step 3: aggregation into `work_voice_map`.

- Status: MVP has template.
- Human review: required.
- Purpose: identify stable stance patterns by scene_type.

Step 4: extract transferable assets and remove non-transferable elements.

- Status: MVP has both templates.
- Human review: required.
- Raw source elements: forbidden.

Step 5: create `voice_contract`.

- Status: MVP has schema and empty templates.
- Human review: required before runtime use.
- Not this round: no real contract is created here.

Step 6: compile compact runtime packet.

- Status: designed in this package.
- Next patch: add compiler expectations / prompt input contract.
- Raw cards and source work labels: forbidden.

Step 7: Planner injects scene-level `work_voice` block.

- Status: this package designs future fields.
- Next patch: update Planner skill only after approval.
- Planner does not write正文.

Step 8: Writer executes compact brief.

- Status: this package designs future brief.
- Next patch: update Writer skill only after approval.
- Writer must not explain fields in正文.

Step 9: Reviewer applies Human Texture + Work Voice gates.

- Status: MVP gate exists; this package designs injection.
- Next patch: add gate dimensions to Reviewer.
- Human review remains required.

Step 10: Polisher only handles local polish if structurally approved.

- Status: this package reinforces boundary.
- Next patch: add explicit Work Voice non-rescue rule.
- Polisher cannot fix missing storyteller.

Step 11: A/B/C validation.

- Status: MVP plan exists.
- Not this round: do not run validation.
- Must happen after approved patch and dry run.

## What This Round Adds

This round adds the design bridge from MVP artifacts to future skill-pack edits. It does not patch skills, generate text, or validate C group output.
