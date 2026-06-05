# Project Dependency Map

## Dependency Rules

| Item | Dependency | Reason | Start Condition |
| --- | --- | --- | --- |
| Work Voice v0 | Human Texture v0 has entered the base | Work Voice needs a stable human-texture packet or it becomes a free-floating narrator rule | Human Texture fields are present in the formal skill-pack or an approved patch base |
| Character Agency MVP | Work Voice patch is closed enough to preserve narrator boundary | Agency can start before A/B/C fully succeeds, but must not interrupt Work Voice closure | Work Voice diff is reviewed and its unresolved risks are known |
| Live Leakage MVP | Character Agency has baseline judgment | Without agency, live leakage becomes performed human flavor or detail padding | Character Agency can identify who acts, why, and under what constraint |
| Reader Immersion MVP | Character Agency plus Work Voice | Without agency and narrator stance, immersion becomes author-forced reader instruction | Characters act from their own pressure, and narration can leave room for the reader |
| Agentic Narrative Engine Research | Can run in parallel with Mainline A | It is a long-term paradigm study, not a production replacement | Research artifacts stay isolated from production pipeline changes |
| Agentic 1-scene MVP | Preferably after Character Agency MVP | Scene simulation needs agent goals, misjudgment and action ownership | A bounded scene brief and minimal agent card schema exist |

## Current Blocking Point

The local repository does not contain `experiment/work-voice-skill-pack-patch-v0` or `production/work_voice/skill_pack_patch_v0/`. The available latest work branch is `experiment/work-voice-skill-pack-injection-design-v0`, which records the Work Voice injection design but does not patch the formal skill-pack.

This means the immediate blocker is not concept design. It is base readiness: the formal creation skills currently do not include the Human Texture v0 fields that the Work Voice patch expects.

## Parallelization Guidance

- Human Texture closure and Work Voice patch closure should stay on the main engineering lane.
- Character Agency design can begin as a document-only MVP after Work Voice diff review, but should not touch production skills until Work Voice v0 has a closure report.
- Agentic Narrative Engine research can run as an isolated research package, but must not change `.story-system`, `.webnovel`, production skill-pack, WPS sync, or approved pattern storage.

## Stop Conditions

- If a subproject cannot produce a bounded artifact, it should remain research.
- If a validation result is negative, keep the failed artifact and record what boundary it exposed.
- If a new concept requires rewriting earlier accepted assets, stop and request project-owner review.
