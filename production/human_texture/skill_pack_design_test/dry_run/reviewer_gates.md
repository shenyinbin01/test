# Reviewer Gates

评分与 gate 依据：`production/human_texture/skill_pack_design/reviewer_gate_design.md`

规则摘要：

- 只检查本片段 `focus_fields`，未选字段不强行打分。
- focus fields 平均分 >= 4：结构通过，可进入 Polisher 做轻量语言处理。
- focus fields 平均分 3-3.9：通常退回 Writer。
- 任一 focus field <= 2：按失败类型退回 Planner 或 Writer。
- Polisher 不负责补私心、关系债、信息载体或下一章摩擦。

## Gate Summary

| 片段 | A 版失败应退回 | B focus avg | B gate | Polisher 是否被要求救结构 |
| --- | --- | ---: | --- | --- |
| C4 柳青砚关系节点 | Writer | 4.3 | pass_to_polisher | 否 |
| C3 饭堂 / 矿洞信息露出 | Planner | 4.7 | pass_to_polisher | 否 |
| C5 群体公告 / 规则公布 | Planner | 4.0 | pass_to_polisher | 否 |
| C4 情绪残留 / 情绪代价 | Writer | 4.0 | pass_to_polisher | 否 |
| C4 章尾钩子压过人味 | Planner | 4.3 | pass_to_polisher | 否 |

## 1. C4 柳青砚关系节点

```yaml
baseline_gate:
  decision: "return_to_writer"
  reason: "关系节点已经有柳青砚给台阶和苏衍撒谎，但正文把失望命名后即通过复检，羞耻与关系债未充分执行。"
  failure_type:
    - "Writer 未执行具体 shame_or_avoidance"
    - "relationship_debt_change 停留在失望命名"
  polisher_allowed: false

compact_b_gate:
  focus_fields_checked:
    - shame_or_avoidance
    - relationship_debt_change
    - consequence_next_friction
  scores:
    shame_or_avoidance: 4
    relationship_debt_change: 5
    consequence_next_friction: 4
  focus_average: 4.3
  webnovel_function_preserved: true
  system_display_risk: "low"
  template_risk: "low"
  gate: "pass_to_polisher"
  return_to: null
  polisher_allowed: true
  polisher_boundary: "只能压缩显性句和调整节奏，不新增关系债。"
```

## 2. C3 饭堂 / 矿洞信息露出节点

```yaml
baseline_gate:
  decision: "return_to_planner"
  reason: "原片段虽有饭堂线索，但核心设定靠主角直接读懂阵法和记忆洪流完成，缺少稳定 information_carrier 与 consequence_next_friction。"
  failure_type:
    - "Planner 缺少信息露出路径"
    - "信息公告化 / 直接读源码"
    - "后山行动代价没有进入下一章摩擦"
  polisher_allowed: false

compact_b_gate:
  focus_fields_checked:
    - scene_resistance
    - information_carrier
    - consequence_next_friction
  scores:
    scene_resistance: 5
    information_carrier: 5
    consequence_next_friction: 4
  focus_average: 4.7
  webnovel_function_preserved: true
  system_display_risk: "low"
  template_risk: "low"
  gate: "pass_to_polisher"
  return_to: null
  polisher_allowed: true
  polisher_boundary: "可压缩粥与积分的类比句；不可新增信息载体或改变阵眼发现路径。"
```

## 3. C5 群体公告 / 规则公布节点

```yaml
baseline_gate:
  decision: "return_to_planner"
  reason: "元启和古镜承担了几乎全部规则公布，群体选择和检测代价没有被规划成信息载体。"
  failure_type:
    - "Planner 缺少 scene_resistance"
    - "Planner 缺少 consequence_next_friction"
    - "公告式设定说明过重"
  polisher_allowed: false

compact_b_gate:
  focus_fields_checked:
    - scene_resistance
    - information_carrier
    - consequence_next_friction
  scores:
    scene_resistance: 4
    information_carrier: 4
    consequence_next_friction: 4
  focus_average: 4.0
  webnovel_function_preserved: true
  system_display_risk: "medium"
  template_risk: "low"
  gate: "pass_to_polisher"
  return_to: null
  polisher_allowed: true
  polisher_boundary: "可压缩元启说明句；不可把公告重写成新剧情或新增检测规则。"
```

## 4. C4 情绪残留 / 情绪代价节点

```yaml
baseline_gate:
  decision: "return_to_writer"
  reason: "Planner 的烧积分功能明确，问题在正文把情绪碎片写成燃料条，缺少由羞耻和残留导致的行为后果。"
  failure_type:
    - "情绪无足够行为后果"
    - "代价主要服务分数下降"
  polisher_allowed: false

compact_b_gate:
  focus_fields_checked:
    - shame_or_avoidance
    - consequence_next_friction
  scores:
    shame_or_avoidance: 4
    consequence_next_friction: 4
  focus_average: 4.0
  webnovel_function_preserved: true
  system_display_risk: "medium"
  template_risk: "medium_low"
  gate: "pass_to_polisher"
  return_to: null
  polisher_allowed: true
  polisher_boundary: "可压缩动作密度；不可新增第三类情绪后果或改分数链。"
```

## 5. C4 章尾钩子压过人味节点

```yaml
baseline_gate:
  decision: "return_to_planner"
  reason: "章尾钩子很强，但关系余波被大事件吞掉，人物承受点主要靠尾段总结补写。"
  failure_type:
    - "钩子压过人"
    - "consequence_next_friction 未嵌入钩子发生时"
    - "relationship_debt_change 后置成总结"
  polisher_allowed: false

compact_b_gate:
  focus_fields_checked:
    - private_want
    - relationship_debt_change
    - consequence_next_friction
  scores:
    private_want: 4
    relationship_debt_change: 5
    consequence_next_friction: 4
  focus_average: 4.3
  webnovel_function_preserved: true
  system_display_risk: "medium"
  template_risk: "low"
  gate: "pass_to_polisher"
  return_to: null
  polisher_allowed: true
  polisher_boundary: "可调整章尾余味句；不可新增关系修复场或改变元启降临钩子。"
```

## Reviewer 分层结论

Reviewer 能明确分层：

- A 版中，信息公告和章尾钩子问题主要退回 Planner，因为缺少信息载体、场景选择压力或后续摩擦设计。
- A 版中，关系节点和情绪节点主要退回 Writer，因为 beat 里已有冲突/代价，但正文执行停留在命名或燃料化。
- B 版中，5 个片段均不需要 Polisher 救结构。Polisher 只允许做压缩显性说明、句子节奏和余味保留。
