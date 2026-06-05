# Chapter Navigation Layer

Chapter Card（章节卡）不是一章一句话，而是状态变化合同。

`chapter_one_sentence` 有用，但它只能提供导航锚点。真正可执行的是本章前后状态、信息变化、关系压力、读者问题和下一章种子。

## 最小字段

| 字段 | 定义 |
|---|---|
| `chapter_id` | 章节编号。 |
| `chapter_one_sentence` | 章节导航锚点，不是完整合同。 |
| `volume_goal_link` | 本章如何关联当前卷目标。 |
| `plot_function` | 本章的剧情功能，如推进、反转、揭示、兑现、设置代价。 |
| `required_conflict` | 必须发生的冲突。 |
| `required_reveal` | 必须露出的信息及其载体。 |
| `required_payoff_or_debt` | 必须兑现、延期或新建的债。 |
| `character_state_before` | 主要人物进入本章前的状态。 |
| `character_state_after` | 本章结束后必须改变的状态。 |
| `relationship_pressure_change` | 关系压力如何变化。 |
| `knowledge_state_change` | 谁知道、误知道、被瞒着或开始怀疑什么。 |
| `resource_or_status_change` | 资源、身份、权限、时间、体力或声誉变化。 |
| `reader_question_before` | 本章前读者带着哪些问题。 |
| `reader_question_after` | 本章后哪些问题被刷新、回收、新增或延期。 |
| `spotlight_targets` | 本章重点照亮的人物、关系或问题。 |
| `allowed_divergence_band` | 允许场景执行偏离的范围。 |
| `must_not_happen` | 本章绝不能发生的破坏性漂移。 |
| `next_chapter_seed` | 下一章必须接住的摩擦或问题。 |

## 失败信号

- 一章单看顺，但下一章接不上。
- 本章有钩子，却没有状态变化。
- 信息露出只服务公告，不改变谁能做什么。
- 关系变化没有进入下一章压力。
- `chapter_one_sentence` 被当成完整章节合同。
