# Human Texture Interaction Design

Human Texture and Work Voice are separate layers that must cooperate.

## Human Texture Handles

- `private_want`
- `shame_or_avoidance`
- `relationship_debt_change`
- `scene_resistance`
- `information_carrier`
- `consequence_next_friction`

Human Texture makes people, information, and relationships feel lived.

## Work Voice Handles

- `narrator_position`
- `protagonist_distance`
- `reader_relationship`
- `world_attitude`
- `intervention_style`
- `sentence_rhythm`
- `stable_flaw`

Work Voice makes the storyteller feel stable.

## Coordination In One Chapter

Planner should place Human Texture focus fields and Work Voice scene stance in the same scene plan:

```yaml
scene:
  scene_type:
  human_texture_focus_fields: []
  work_voice:
    narrator_position:
    protagonist_distance:
    reader_relationship:
    world_attitude:
```

Writer should first preserve the scene's actual choice, conflict, information carrier, and consequence. Then Work Voice decides how narration stands toward those materials. In practice, neither layer comes first as a checklist; plot action must make both visible.

## Reviewer Distinction

| Failure | Likely layer |
|---|---|
| Character has no private want, relationship consequence, or scene resistance | Human Texture |
| Narration has no stable position or reader relationship | Work Voice |
| Information is dumped by narrator instead of carried by a person / event | Human Texture + Work Voice |
| Text has life details but still feels like a technique demonstration | Work Voice / Writer |
| Voice is stable but people are functional pieces | Human Texture / Writer |

## Return Rules

- Missing private want or relation debt -> return to Planner / Writer with Human Texture focus.
- Missing stable narrator -> return to Work Voice Contract / Planner / Writer.
- Wrong scene stance -> return to Planner / Contract.
- Decorative life details replacing consequence -> return to Writer.
- Local rough sentence after both gates pass -> Polisher.

## Anti-Collision Rules

- Work Voice must not turn Human Texture into旁白解释.
- Human Texture must not flatten Work Voice into life-detail stacking.
- Neither layer belongs to Polisher.
- Writer must make both serve plot momentum, not output two visible rule lists.
