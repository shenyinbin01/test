# Reviewer Gate Design

本文件设计 `webnovel_reviewer` 后续如何评估 Human Texture，并判断应退回 Planner、Writer，还是允许进入 Polisher。当前只写设计，不修改正式 `SKILL.md`。

## 设计目标

Reviewer 不是单纯判断“有没有 AI 味”，而是判断：

- 人物是否在机制压力下做了选择。
- 情绪是否造成行为和关系后果。
- 信息是否自然露出，而不是公告化。
- 场景是否对人物目标产生阻力。
- 代价是否进入下一章摩擦。
- 现有网文推进是否被保留。

Reviewer 必须能定位失败层级。结构性空心退回 Planner 或 Writer，不能丢给 Polisher。

## 建议输出块

```yaml
human_texture_review:
  focus_fields_checked:
    - relationship_debt_change
    - information_carrier
  scores:
    private_want: null
    shame_or_avoidance: null
    relationship_debt_change: 4
    scene_resistance: null
    information_carrier: 3
    consequence_next_friction: 4
  webnovel_function_preserved: true
  system_display_risk: "medium"
  template_risk: "low"
  gate: "pass_to_polisher"
  return_to: null
  required_fix:
    - "信息载体已有，但公告句仍偏重；Writer 可压缩公告并让罚牌承担更多信息。"
```

未被本章选为 `focus_fields` 的字段可以为 `null`，避免每章强行打满。

## 评分原则

使用 Human Texture rubric 的 1-5 分，但只对本章 focus fields 和关键风险项打分：

| 分数 | 含义 |
| --- | --- |
| 5 | 字段自然改变选择、关系、信息或后果，同时不牺牲推进。 |
| 4 | 字段有效，仍有少量可压缩说明。 |
| 3 | 字段存在但偏显性，或只影响局部语言，不足以改变场面。 |
| 2 | 字段多为口号、装饰或模板动作。 |
| 1 | 字段缺失，正文仍是机制展示或公告。 |

通过建议：

- focus fields 平均分 >= 4：可进入 Polisher。
- focus fields 平均分 3-3.9：退回 Writer，除非问题来自 Planner 缺字段。
- 任一 focus field <= 2：按失败类型退回 Planner 或 Writer。
- webnovel function 未保留：退回 Writer 或 Planner，不进入 Polisher。

## 退回层级判断

| 失败类型 | 表现 | 退回层级 |
| --- | --- | --- |
| Planner 缺字段 | 没有信息 carrier、没有 consequence、关系债无后续使用计划。 | Planner |
| Planner 字段抽象 | “增加信任裂痕”“更有人味”但不可写成动作。 | Planner |
| 字段和 beat 冲突 | 为了人味改变主线因果、削弱钩子或破局。 | Planner |
| Writer 未执行 | packet 有明确字段，但正文仍用旁白总结或公告。 | Writer |
| Writer 显性模板化 | 人物逐项低头、苦笑、握拳，字段像表格被写进正文。 | Writer |
| 信息公告化 | 关键信息仍由旁白或权威一次性解释，缺 carrier / cost。 | Planner 或 Writer |
| 情绪无后果 | 情绪被命名，但不改变选择、关系或下一章摩擦。 | Writer |
| 关系当场清零 | 冲突出现后立刻和解，relationship debt 无继承。 | Planner 或 Writer |
| 钩子压过人 | 章尾只剩系统级震撼，没有人物承受点。 | Planner |
| 语言粗糙但结构有效 | 字段已有效，只需压缩说明、调整句势、补一笔余味。 | Polisher |

## 与现有 14 维 Reviewer 的关系

Human Texture gate 不替代现有 14 维审稿，而是补充现有短板。

| 现有维度 | Human Texture 补充 |
| --- | --- |
| character_consistency | 检查人物是否有私心、羞耻、回避和关系债。 |
| information_density | 检查信息是否自然露出，而非公告堆密度。 |
| ai_flavor | 从结构上诊断系统展示感，不只看句子。 |
| ending_hook | 检查钩子是否保留人的承受点。 |
| cool_point | 检查爽点是否带来真实后果，而非零成本破局。 |
| template_risk | 检查 packet 是否被模板化执行。 |

## Hard Gate

以下情况不得进入 Polisher：

- `focus_fields` 未执行，平均分低于 3.5。
- 信息节点仍主要依赖公告和旁白解释。
- 关系节点出现“撒谎/误伤后立刻自然和解”。
- 情绪节点只有情绪名称，没有行为后果。
- 章尾大钩子完全吞掉人物反应。
- 为了人味牺牲了原有剧情功能、规则破局或节奏。

## Polisher Allowed 条件

只有当以下条件同时满足，Reviewer 才允许进入 Polisher：

- 原 chapter beat 的事件和功能完整。
- focus fields 至少有可见落点。
- 关系债或 consequence 已可继承。
- 没有结构性公告化或人物功能件问题。
- 剩余问题主要是句子显性、节奏松、局部语言缺光泽。

## Reviewer 输出示例

```yaml
decision: "return_to_writer"
reason: "Planner 已给出 scene_resistance 和 information_carrier，但正文仍由执事公告完整解释规则。"
human_texture_required_fix:
  - "保留公告的表层规则。"
  - "把关键漏洞改为从扣饭牌和老矿奴的停顿里露出。"
  - "主角只能拿到半截判断，并因此被监工看见。"
polisher_allowed: false
```

```yaml
decision: "return_to_planner"
reason: "章尾钩子是世界级异象，但 Planner 未指定任何 consequence_next_friction，Writer 无法自然补出后果。"
human_texture_required_fix:
  - "补一个会进入下一章的个人摩擦。"
  - "确认该摩擦不削弱钩子。"
polisher_allowed: false
```

```yaml
decision: "pass_to_polisher"
reason: "关系债和下一章摩擦成立；剩余问题是两句解释偏直白。"
human_texture_required_fix:
  - "压掉信任破裂的总结句。"
  - "保留柳青砚不接玉简的动作。"
polisher_allowed: true
```
