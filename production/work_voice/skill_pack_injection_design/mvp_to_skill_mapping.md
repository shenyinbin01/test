# MVP To Skill Mapping

## Mapping Table

| MVP artifact | Future consumer | Purpose | Injected as | Risk | Reviewer check |
|---|---|---|---|---|---|
| `voice_observation_card` | Upstream curator / Hermes, not Writer | Record abstract stance observations without source text | Upstream research asset only | If pushed into Writer, may overload context or leak source-specific signals | Cards must not contain source text or author imitation target |
| `work_voice_map` | Hermes / future Contract compiler | Aggregate repeated stance rules by scene_type | Input to contract generation, not runtime prompt | May confuse genre convention with voice rule | Check transferable vs non-transferable separation |
| `transferable_voice_assets` | Contract compiler / Planner design | Identify reusable narrative stance rules | Contract candidate rules | Too abstract becomes unusable; too specific becomes copying | Each asset needs scene_type, transfer condition, anti-copy boundary |
| `non_transferable_original_elements` | Contract compiler / Reviewer | Block source-specific names, bridge, phrasing, world terms | `forbidden_original_elements` and contamination guard | Missing items can contaminate generation | Any source-specific element in runtime output is fail |
| `voice_contract` | Planner, Writer, Reviewer | Define executable Work Voice constraints | Compiled into compact runtime packet | Can degrade into tone checklist or hidden imitation target | Must include narrator_position, reader_relationship, world_attitude, contamination guard |
| `contamination_checklist` | Reviewer | Hard gate against source copying and imitation | Reviewer checklist | If optional, C group may pass contaminated output | Any fail item blocks acceptance |
| `reviewer_gate` | Reviewer | Decide pass/fail and return layer | Added gate dimensions in review report | Reviewer may only check field presence, not effect | Check body-level stance stability and no Polisher overreach |
| `abc_validation_plan` | Hermes / project owner / Reviewer | Compare A baseline, B Human Texture, C Work Voice | Validation protocol after patch approval | Running too early may test unstable prompts | Must use same beat and conditions; no raw corpus or source text |

## Role-Specific Rules

- Planner consumes `voice_contract` or compact runtime packet, never raw corpus.
- Writer consumes compact `work_voice_runtime_packet` / scene brief, not full observation cards.
- Reviewer consumes `voice_contract`, reviewer gate, and contamination checklist.
- Polisher consumes only local polish boundaries and does not repair narrator stance.
- Observation cards and aggregation outputs are upstream assets; they should not be inserted wholesale into Writer prompts.

## Design Consequence

Future patch should add a small Work Voice block to existing role contracts, not a large new workflow. The runtime chain should see only the distilled, reviewed, contamination-checked abstraction.
