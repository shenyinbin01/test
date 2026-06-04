# Voice Contract v0 Template

> 空模板。不填具体作品内容，不写具体作者目标，不复制原文。

## Metadata

- `version`: v0
- `status`: draft / reviewed / approved_for_test / rejected / retired
- `based_on_work_voice_map_id`:
- `created_by`:
- `created_at`:

## Voice Type

`voice_type`:

填写提示：用一句话描述本作品声音，例如“冷静贴主角 + 偶尔站在世界规则上方补刀”。不要写成某作者风格。

## Narrator Position

```yaml
narrator_position:
  default:
  scene_switches:
    - scene_type:
      position:
      allowed_intervention:
      forbidden_intervention:
```

填写提示：回答讲述者默认站在哪里，以及哪些 scene_type 会切换。

## Reader / Protagonist / World

- `reader_relationship`:
- `protagonist_distance`:
- `world_attitude`:

填写提示：这三项决定“讲故事的人”和主角、读者、世界的稳定关系。

## Rules

- `intervention_rules`:
- `humor_rules`:
- `showoff_rules`:
- `detail_selection_rules`:
- `sentence_rhythm_rules`:
- `scene_type_switching_rules`:

填写提示：每条规则必须可被 Writer 执行，也必须可被 Reviewer 检查。

## Stable Flaws

- `stable_flaws_to_keep`:

填写提示：保留让声音像一个稳定讲述者的毛病，例如嘴硬、偏心、冷幽默、过度克制。不要写具体作者人格。

## Forbidden Original Elements

- `forbidden_original_elements`:

填写提示：列出所有不可迁移原作专属元素。此项不能为空。

## Anti-AI Voice Rules

默认建议：

- 不要用总结句替代现场。
- 不要用情绪标签替代情绪行为。
- 不要每段都显性解释动机。
- 不要让旁白像评审报告。
- 不要为了人味而硬塞生活细节。

## Human Texture Interaction

- `compatible_fields`:
- `conflict_resolution`:

填写提示：Work Voice 控制叙述距离和声音，Human Texture 控制人物、信息、关系材料。缺少叙述站位时不能交给 Polisher 救。

## Reviewer Gate

- `required_dimensions`:
- `fail_policy`:

填写提示：写明失败时退回哪一层。
