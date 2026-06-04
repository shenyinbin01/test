# Transferable Voice Assets Template

> 空模板。只记录可迁移的叙述策略，不记录原文和原作专属表达。

| 字段 | 填写 |
|---|---|
| `asset_id` |  |
| `source_observation_ids` |  |
| `scene_type` |  |
| `voice_rule` |  |
| `why_it_works` |  |
| `transfer_condition` |  |
| `misuse_risk` |  |
| `anti_copy_boundary` |  |
| `compatible_with_human_texture_fields` |  |
| `reviewer_check` |  |

## Field Notes

- `voice_rule`：必须是抽象叙述策略，例如“规则露出时先制造压迫，再让主角行动改变读者预期”。
- `why_it_works`：说明它如何让讲述者稳定存在。
- `transfer_condition`：说明什么 scene_type / beat 条件下可以使用。
- `misuse_risk`：说明误用后会不会变成仿写、端着、硬、旧派腔或普通文风 checklist。
- `anti_copy_boundary`：明确哪些元素不能带走。
- `compatible_with_human_texture_fields`：说明与 private_want、relationship_debt_change、scene_resistance 等字段是否兼容。
- `reviewer_check`：Reviewer 应如何判断该资产被正确使用。

## Empty YAML Shape

```yaml
asset_id:
source_observation_ids: []
scene_type:
voice_rule:
why_it_works:
transfer_condition:
misuse_risk:
anti_copy_boundary:
compatible_with_human_texture_fields:
  - private_want
  - shame_or_avoidance
  - relationship_debt_change
  - scene_resistance
  - information_carrier
  - consequence_next_friction
reviewer_check:
```
