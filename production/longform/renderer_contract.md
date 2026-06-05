# Renderer Contract

Narrative Renderer（正文渲染器）负责把已批准的事件、状态和叙述合同转成正文。它不是结构修补器。

## Renderer 读取

- `chapter_card`
- `scene_agency_packets`
- `event_log`
- `human_texture_packet`
- `work_voice_contract`
- 当前热账本切片

## Renderer 写入

- `draft`
- `render_report`
- `blocker`，如果结构不足以渲染

## Renderer 不能改变

- 角色行动结果。
- 谁知道什么。
- 资源与关系账本事实。
- 已 accepted 的卷目标与章节合同。
- 因果决定。

## render_report 建议字段

```yaml
render_report:
  chapter_id: ""
  rendered_from:
    chapter_card: ""
    scene_agency_packets: []
    event_log: []
    hot_ledger_slice: []
  executed_constraints:
    human_texture: []
    work_voice: []
    reader_question: []
  blockers: []
  overreach_risk: low
```

## blocker 类型

| blocker | 说明 | 行动 |
|---|---|---|
| `causal_thinness` | 因果太薄，无法支撑本章状态变化。 | 退回 Orchestrator / Scene Engine。 |
| `embodied_consequence_missing` | 后果没有可见行为、关系或资源承载。 | 退回 Scene Engine。 |
| `focalization_breach` | 聚焦越界，叙述知道了角色不该知道的内容。 | 退回 Renderer Contract / Reviewer。 |
| `exposition_clump` | 信息露出堆成公告。 | 退回 Chapter Card / Renderer。 |
| `spotlight_imbalance` | 聚光失衡，钩子或设定吞掉人物承受点。 | 退回 Orchestrator。 |

## Polisher 边界

Renderer 通过后，Polisher 才能处理语言显性、句势和局部留白。Renderer blocker 未解决时，不得交给 Polisher。
