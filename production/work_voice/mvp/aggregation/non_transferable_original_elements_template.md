# Non-transferable Original Elements Template

> 空模板。所有不可迁移元素必须在进入 `voice_contract` 前被隔离。

## Element Types

- 原作专属设定
- 专属名词
- 专属口癖
- 专属句式
- 专属世界观表达
- 专属人物关系模式
- 可识别桥段
- 高风险修辞习惯

## Template

| 字段 | 填写 |
|---|---|
| `element_id` |  |
| `source_observation_ids` |  |
| `element_type` |  |
| `why_non_transferable` |  |
| `contamination_risk` |  |
| `forbidden_usage` |  |
| `safe_abstraction_if_any` |  |

## Empty YAML Shape

```yaml
element_id:
source_observation_ids: []
element_type:
why_non_transferable:
contamination_risk:
  level:
  reason:
forbidden_usage:
safe_abstraction_if_any:
```

## Review Rule

如果某元素无法明确判断是否可迁移，默认放入不可迁移清单。只有当 Reviewer 确认其已抽象为“叙述关系 / 讲述策略”时，才允许进入 transferable assets。
