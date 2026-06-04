# Reviewer Gate Injection Design

Reviewer should add a Work Voice gate after existing plot / rhythm / AI-flavor checks. The gate does not replace literary judgment; it decides whether output can proceed or must return to a specific layer.

| dimension | check_question | pass_standard | fail_signals | return_to | severity |
|---|---|---|---|---|---|
| `narrator_position_stability` | Does the draft feel told from a stable position? | Stance is visible and scene switches match the brief. | Camera-like narration, random distance, no storyteller body. | Work Voice Contract / Writer | high |
| `protagonist_distance_control` | Is narrator distance from protagonist controlled? | Distance matches contract and scene function. | Over-defends protagonist, over-explains feelings, or turns cold randomly. | Planner / Writer | medium |
| `reader_relationship_clarity` | Does narration treat reader as a defined role? | Reader relationship is felt without being announced. | Sounds like system instruction, report, or generic exposition. | Work Voice Contract | high |
| `world_attitude_consistency` | Does narration hold a stable attitude toward the world? | World attitude supports rules, pressure, and payoff. | Alternates between old-style solemnity, report tone, and random jokes. | Contract / Planner | medium |
| `intervention_timing` | Are narrator intrusions timed correctly? | Interventions serve pressure, contrast, payoff, or withholding. | Frequent motive summaries; punchlines before consequence; explanatory interruptions. | Writer / Contract | medium |
| `scene_type_switching_correctness` | Are stance switches correct for scene_type? | Opening, suppression, exposition, payoff, and ending use planned stance. | Payoff overexplained, ending overclosed, exposition becomes report. | Planner / Contract | high |
| `anti_ai_voice_compliance` | Does draft avoid AI-camera and checklist narration? | Scene carries meaning through action, consequence, and reader relation. | Generic humanizer details, emotion labels, repeated summaries. | Writer | high |
| `no_author_imitation` | Is there no specific author imitation? | No author target, catchphrase, signature syntax, or style label. | Draft appears to chase a specific author voice. | Work Voice Contract | critical |
| `no_source_contamination` | Is there no source contamination? | No source sentences, source terms, raw corpus traces, or recognizable bridge. | Any source-specific carryover. | Reviewer / Work Voice Contract | critical |
| `webnovel_momentum_preserved` | Does Work Voice preserve webnovel propulsion? | Conflict, payoff, hooks, and information clarity remain strong. | Stable but slow, stiff, old-fashioned, or over-literary. | Planner / Writer | high |
| `human_texture_compatibility` | Does voice support Human Texture rather than explain it? | People, relationships, and consequences remain embodied. | Narrator explains private_want or debt instead of staging them. | Planner / Writer | medium |
| `no_polisher_overreach` | Is failure correctly routed away from Polisher? | Polisher only gets local sentence / rhythm issues after structural pass. | Structural voice failure sent to Polisher. | Reviewer | high |

## Fixed Rules

- 缺少稳定讲述者，不能交给 Polisher 救。
- `voice_contract` 模糊，退回 Work Voice Contract。
- `scene_type` 切换规则错误，退回 Planner / Contract。
- Writer 执行成具体作者模仿，直接判失败。
- 出现原文污染，直接判失败。
- 只是套人味技巧但讲述者不稳定，判失败。
- 如果只是局部句子节奏不顺，才允许交给 Polisher。

## Output Shape

Future review report may add:

```yaml
work_voice_gate:
  overall: pass | fail | needs_revision
  failed_dimensions: []
  return_to:
  no_polisher_overreach: true
  contamination_result:
  rewrite_instructions: []
  polisher_allowed: false
```
