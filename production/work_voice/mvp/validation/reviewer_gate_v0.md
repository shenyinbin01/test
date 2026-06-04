# Reviewer Gate v0

Reviewer gate 用于判断 Work Voice MVP 输出是否具备稳定讲述者。本 gate 不替代文学终审，只提供工程化退回口径。

| 维度 | 检查问题 | 通过标准 | 失败表现 | 退回层级 |
|---|---|---|---|---|
| `narrator_position_stability` | 讲述者站位是否稳定可感？ | 多数段落能看出讲述者位置，scene_type 切换有规则 | 像无身体摄像头，忽近忽远 | Work Voice Contract / Writer |
| `protagonist_distance_control` | 讲述者离主角的距离是否受控？ | 行动、情绪、判断距离符合 contract | 过度替主角解释，或完全冷掉 | Contract / Writer |
| `reader_relationship_clarity` | 读者被当成什么角色？ | 同伙、旁听者、看热闹者等关系清楚 | 像系统向用户说明剧情 | Work Voice Contract |
| `world_attitude_consistency` | 叙述者怎么看世界是否一致？ | 世界态度能服务设定和爽点 | 一会儿热血，一会儿报告，一会儿旧派端着 | Contract / Planner |
| `intervention_timing` | 旁白插嘴、隐身、卖关子时机是否合适？ | 插嘴服务压迫、反差、爽点或留白 | 频繁总结动机，打断现场 | Writer / Contract |
| `scene_type_switching_correctness` | 不同 scene_type 的站位切换是否正确？ | 开篇、压制、规则露出、payoff、章尾等切换有设计 | payoff 时站错位置，章尾解释过满 | Planner / Contract |
| `anti_ai_voice_compliance` | 是否避免 AI 摄像头和评审报告腔？ | 不用总结句替代现场，不用情绪标签替代行为 | 人味技巧堆叠，旁白像 checklist | Writer，必要时 Contract |
| `no_author_imitation` | 是否避免具体作者模仿？ | 无作者名目标、无口癖仿写、无专属句法 | 输出像在追某具体作者口吻 | Fail，退回 Contract |
| `no_source_contamination` | 是否无来源污染？ | 无原文句子、专属名词、可识别桥段 | 出现来源作品元素或 raw corpus 痕迹 | Fail，退回污染清理 |
| `webnovel_momentum_preserved` | 是否保留网文推进？ | 事件推进、爽点、信息清晰度未被声音规则压坏 | 稳但慢，端着，硬，旧派腔 | Planner / Writer |
| `human_texture_compatibility` | 是否兼容 Human Texture？ | 人物私欲、关系债、后果摩擦仍在 | 只剩叙述姿态，人物又功能化 | Planner / Writer |

## 特别规则

- 如果缺少作者站位，不能交给 Polisher 救。
- 如果 `voice_contract` 本身模糊，退回 Work Voice Contract。
- 如果 `scene_type` 切换规则错误，退回 Planner / Contract。
- 如果 Writer 执行成具体作者模仿，直接判失败。
- 如果正文只是在套“人味技巧”，但讲述者不稳定，判失败。
- 如果只是句子不顺但站位正确，才允许 Polisher 做语言层处理。
