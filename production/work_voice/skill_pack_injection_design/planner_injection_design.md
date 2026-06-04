# Planner Injection Design

## Planner Inputs

Future Planner may read:

- `work_voice_runtime_packet`
- chapter objective / outline / beat context
- Human Texture focus fields
- existing canon and reader_debts

Planner must not read raw corpus, source excerpts, observation cards, or `source_work_id` as a style label.

## Planner Output Block

Planner should add a compact block to chapter beat or chapter context:

```yaml
work_voice:
  scene_type:
  narrator_position:
  protagonist_distance:
  reader_relationship:
  world_attitude:
  allowed_interventions: []
  forbidden_interventions: []
  sentence_rhythm_hint:
  detail_bias:
  stable_flaw_to_keep:
  anti_ai_voice_focus: []
  contamination_guard: []
```

## Scene-Type Selection

Planner maps chapter scenes to Work Voice scene rules:

- `opening_voice_setup`: establish default stance without exposition.
- `protagonist_suppressed`: decide whether narrator is close, cold, biased, or detached.
- `world_rule_exposition`: allow stance above world rules, but ban system-report exposition.
- `payoff_delivery`: decide whether narrator hides, sticks close, or adds a short intervention after consequence.
- `chapter_ending_hook`: define withholding and reader relationship.

## Aligning Voice Contract With Chapter Plan

Planner should treat `voice_contract` as a constraint layer over scene beats:

1. Keep plot and canon decisions in the beat.
2. For each scene, select the applicable Work Voice stance rule.
3. Add only the scene-level fields Writer needs.
4. Preserve Human Texture focus fields as scene material, not narrator explanation.

## Avoiding Style Checklist Drift

Planner must not reduce Work Voice to adjectives, sentence length, or tone labels. Each `work_voice` block needs a stance relation: narrator to protagonist, narrator to reader, narrator to world, and allowed intervention timing.

## Human Texture Coordination

Human Texture focus fields define what must happen inside people and relationships. Work Voice defines how the narrator stands toward that material.

Planner should pair them:

| Human Texture focus | Work Voice coordination |
|---|---|
| `private_want` | Decide whether narrator reveals it directly, through action, or withholds it. |
| `shame_or_avoidance` | Decide protagonist distance: close enough to show avoidance, not so close it becomes explanation. |
| `relationship_debt_change` | Decide reader relationship and intervention timing around consequence. |
| `scene_resistance` | Use world_attitude to make resistance feel embodied. |
| `information_carrier` | Avoid system exposition; choose who carries information. |
| `consequence_next_friction` | Preserve narrative momentum and chapter hook. |

## Failure Returns

Reviewer should return to Planner when:

- scene_type is wrong for the beat.
- stance switching contradicts scene function.
- Human Texture focus and Work Voice stance conflict.
- Planner omitted `work_voice` for a scene that needs it.

Reviewer should return to Work Voice Contract when:

- runtime packet is too vague.
- allowed / forbidden interventions are missing.
- contamination guard is incomplete.

## Hard Boundaries

- Planner does not write正文.
- Planner does not imitate authors.
- Planner does not cite or embed source text.
- Planner does not use `source_work_id` as a style label.
- Planner only compresses contract rules into chapter / scene executable constraints.
