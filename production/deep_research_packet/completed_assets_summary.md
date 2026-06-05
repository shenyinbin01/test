# 已完成 / 进行中资产摘要

这是当前项目判断，不是外部研究结论。表中状态来自当前仓库路径检查；不存在的路径标注为 not found / pending，不自行发明完成状态。

| 资产 | 路径 | 状态 | 解决的问题 | 下一步 |
| --- | --- | --- | --- | --- |
| 人物质感（Human Texture）research / MVP | `production/human_texture/` | available | 诊断人物、信息、关系像功能件的问题，提出人物质感层 | 作为 Human Texture v0 收口和 patch 的基础 |
| 人物质感（Human Texture）skill-pack design | `production/human_texture/skill_pack_design/` | design completed | 提出 6 字段 compact packet 与 Planner / Writer / Reviewer / Polisher 职责 | 确认是否进入正式 base |
| 人物质感（Human Texture）dry run | `production/human_texture/skill_pack_design_test/` | dry run passed | 验证 6 字段压缩后仍能改善片段，且不明显膨胀 | 做盲评 / 双评或进入实验 patch |
| 人物质感（Human Texture）real chain validation | `production/human_texture/real_chain_validation_rerun/` | not found | 本应验证长链路有效性 | 项目负责人决定是否补做 |
| 人物质感（Human Texture）skill-pack patch | not found as production package | pending | 本应把 6 字段嵌入正式 skill-pack | 需另开工程 patch 分支 |
| 作品声音 / 作者站位（Work Voice）research | `production/work_voice/research/` | completed research package | 研究叙述者站位、叙述合同、相邻工具和风险 | 作为 MVP 和注入设计边界 |
| 作品声音 / 作者站位（Work Voice）MVP design | `production/work_voice/mvp/` | design completed | 定义 observation card、work voice map、voice contract、Reviewer gate | 需人工验收和 synthetic dry run |
| 作品声音 / 作者站位（Work Voice）skill-pack injection design | `production/work_voice/skill_pack_injection_design/` | design draft | 把 MVP 产物翻译成未来 Planner / Writer / Reviewer / Polisher 接口 | 人工审四个目标 skill diff 后再 patch |
| 作品声音 / 作者站位（Work Voice）experimental skill-pack patch | `production/work_voice/skill_pack_patch_v0/` | not found | 本应记录实验 patch 产物 | 当前 blocker 是 Human Texture base readiness |
| 项目长期路线图 | `production/project_roadmap/` | available | 统一长期框架、依赖图、资产归位和防跑偏原则 | 作为 Deep Research 上下文 |
| 内容价值观 | `production/project_roadmap/content_philosophy.md` | available | 定义工程化厨房、工业化真诚和反低质投喂约束 | 纳入后续 MVP acceptance criteria |
