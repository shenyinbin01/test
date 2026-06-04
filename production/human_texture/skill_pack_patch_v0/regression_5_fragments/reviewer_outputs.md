# Patched Reviewer Simulation Outputs

本文件模拟 `webnovel_reviewer` 在实验 patch 下输出 `human_texture_review`。

测试重点：

- 能检查 `focus_fields` 是否执行。
- 能判断 webnovel function 是否保留。
- 能定位退回 Planner / Writer / Polisher。
- 不把结构性空心交给 Polisher。
- 不干扰既有十四维度 Reviewer 判断。

## Gate Summary

| 片段 | Baseline Gate | B Gate | B Focus Avg | 结构性空心交给 Polisher |
| --- | --- | --- | ---: | --- |
| C4 柳青砚关系节点 | `return_to_writer` | `pass_to_polisher` | 4.3 | 否 |
| C3 饭堂 / 矿洞信息露出 | `return_to_planner` | `pass_to_polisher` | 4.7 | 否 |
| C5 群体公告 / 规则公布 | `return_to_planner` | `pass_to_polisher` | 4.0 | 否 |
| C4 情绪残留 / 情绪代价 | `return_to_writer` | `pass_to_polisher` | 4.0 | 否 |
| C4 章尾钩子压过人味 | `return_to_planner` | `pass_to_polisher` | 4.3 | 否 |

## 1. C4 柳青砚关系节点

```yaml
baseline_review:
  human_texture_review:
    focus_fields_checked:
      - shame_or_avoidance
      - relationship_debt_change
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: 2
      relationship_debt_change: 3
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 2
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "medium"
    gate: "return_to_writer"
    required_fix:
      - "保留复检功能，但把苏衍撒谎写成羞耻和回避导致的坏选择。"
      - "让柳青砚给台阶被拒后形成可继承关系债。"
  fourteen_dimension_interference: false

b_version_review:
  human_texture_review:
    focus_fields_checked:
      - shame_or_avoidance
      - relationship_debt_change
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: 4
      relationship_debt_change: 5
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 4
    webnovel_function_preserved: true
    system_display_risk: "low"
    template_risk: "low"
    gate: "pass_to_polisher"
    required_fix:
      - "Polisher 仅可压缩显性句和微调句势，不新增关系债。"
  fourteen_dimension_interference: false
```

## 2. C3 饭堂 / 矿洞信息露出

```yaml
baseline_review:
  human_texture_review:
    focus_fields_checked:
      - scene_resistance
      - information_carrier
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: null
      relationship_debt_change: null
      scene_resistance: 3
      information_carrier: 2
      consequence_next_friction: 2
    webnovel_function_preserved: true
    system_display_risk: "high"
    template_risk: "medium"
    gate: "return_to_planner"
    required_fix:
      - "重新规划信息露出路径，避免主角直接读懂阵法底层源码。"
      - "补入信息载体和进入后山的后续摩擦。"
  fourteen_dimension_interference: false

b_version_review:
  human_texture_review:
    focus_fields_checked:
      - scene_resistance
      - information_carrier
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: null
      relationship_debt_change: null
      scene_resistance: 5
      information_carrier: 5
      consequence_next_friction: 4
    webnovel_function_preserved: true
    system_display_risk: "low"
    template_risk: "low"
    gate: "pass_to_polisher"
    required_fix:
      - "Polisher 可压缩生活锚点，不能新增信息载体或改变阵眼发现路径。"
  fourteen_dimension_interference: false
```

## 3. C5 群体公告 / 规则公布

```yaml
baseline_review:
  human_texture_review:
    focus_fields_checked:
      - scene_resistance
      - information_carrier
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: null
      relationship_debt_change: null
      scene_resistance: 2
      information_carrier: 2
      consequence_next_friction: 2
    webnovel_function_preserved: true
    system_display_risk: "high"
    template_risk: "medium"
    gate: "return_to_planner"
    required_fix:
      - "公告可以保留，但 Planner 必须把它变成强制选择现场。"
      - "补检测/标记的即时后果。"
  fourteen_dimension_interference: false

b_version_review:
  human_texture_review:
    focus_fields_checked:
      - scene_resistance
      - information_carrier
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: null
      relationship_debt_change: null
      scene_resistance: 4
      information_carrier: 4
      consequence_next_friction: 4
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "low"
    gate: "pass_to_polisher"
    required_fix:
      - "Polisher 可压缩公告句，不可新增检测规则或重排古镜信息。"
  fourteen_dimension_interference: false
```

## 4. C4 情绪残留 / 情绪代价

```yaml
baseline_review:
  human_texture_review:
    focus_fields_checked:
      - shame_or_avoidance
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: 3
      relationship_debt_change: null
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 3
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "medium"
    gate: "return_to_writer"
    required_fix:
      - "保留分数链，但让情绪碎片造成具体遮掩动作和后续质问压力。"
      - "每个情绪最多一个动作后果。"
  fourteen_dimension_interference: false

b_version_review:
  human_texture_review:
    focus_fields_checked:
      - shame_or_avoidance
      - consequence_next_friction
    scores:
      private_want: null
      shame_or_avoidance: 4
      relationship_debt_change: null
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 4
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "medium_low"
    gate: "pass_to_polisher"
    required_fix:
      - "Polisher 只可压缩动作密度，不可新增第三类情绪后果。"
  fourteen_dimension_interference: false
```

## 5. C4 章尾钩子压过人味

```yaml
baseline_review:
  human_texture_review:
    focus_fields_checked:
      - private_want
      - relationship_debt_change
      - consequence_next_friction
    scores:
      private_want: 2
      shame_or_avoidance: null
      relationship_debt_change: 3
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 2
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "medium"
    gate: "return_to_planner"
    required_fix:
      - "将关系余波嵌入天幕裂缝发生时，不能只在尾段总结。"
      - "补一个会进入下一章的个人摩擦，不削弱元启降临钩子。"
  fourteen_dimension_interference: false

b_version_review:
  human_texture_review:
    focus_fields_checked:
      - private_want
      - relationship_debt_change
      - consequence_next_friction
    scores:
      private_want: 4
      shame_or_avoidance: null
      relationship_debt_change: 5
      scene_resistance: null
      information_carrier: null
      consequence_next_friction: 4
    webnovel_function_preserved: true
    system_display_risk: "medium"
    template_risk: "low"
    gate: "pass_to_polisher"
    required_fix:
      - "Polisher 可调整章尾余味句，不可新增关系修复场或改变元启降临。"
  fourteen_dimension_interference: false
```

## Fourteen-Dimension Non-Interference Check

| 维度 | 是否被 Human Texture 替代 | 回归判断 |
| --- | --- | --- |
| plot_progress | 否 | 原剧情功能单独检查，未被 Human Texture 分数替代。 |
| character_consistency | 否 | Human Texture 只补充私心/关系债检查。 |
| logic_continuity | 否 | 所有 B 版均要求保留原事件与因果。 |
| pacing | 否 | 篇幅膨胀作为单独风险记录。 |
| ending_hook | 否 | 章尾钩子仍独立评估，Human Texture 只检查是否吞人。 |
| cool_point | 否 | 规则/爽点不被人味牺牲。 |
| information_density | 否 | Human Texture 补充信息载体，不替代密度判断。 |
| character_voice | 否 | 未改为声口评分。 |
| sentence_rhythm | 否 | 留给 Polisher 的语言层问题。 |
| ai_flavor | 否 | Human Texture 补结构展示感，不替代 ai_flavor 报告。 |
| style_consistency | 否 | 仍要求保持网文推进。 |
| hook_pacing | 否 | 钩子节奏仍独立。 |
| payoff_visibility | 否 | Human Texture 只补兑现后的承受点。 |
| template_risk | 否 | Human Texture 额外检查字段模板化。 |

结论：Human Texture gate 没有干扰既有十四维度 Reviewer 判断。
