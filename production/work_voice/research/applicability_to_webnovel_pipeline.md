# Applicability To Current Webnovel Pipeline

## 当前链路

当前项目已有 `skill-pack`、Planner / Writer / Reviewer / Polisher、Human Texture v0、Phase 8 craft_assets、GitHub 真源、Hermes 调度、DeepSeek 真实生成、DeepCode 工程辅助。`.story-system` 是故事真源，WPS 只是输出和人工编辑载体。

## 1. Work Voice 应该放在哪里

推荐顺序：

1. Planner 前：选择原创作品的目标叙述站位方向。
2. Planner 中：把站位进入 Story Bible、章节大纲和 beat。
3. Writer 前：生成 `voice_contract` 注入 Writer。
4. Reviewer 中：做 Work Voice gate。

不建议只放在 Polisher，因为 Polisher 只能改语言，无法修复“叙述者站错地方”。

## 2. 是否应该成为独立 Skill

MVP 阶段建议先不改 `skill-pack`，以外部 research contract 形式运行。通过 A/B/C 验证后，再考虑创建独立 `webnovel_work_voice` Skill 或合入 Planner / Reviewer 的接口。

## 3. 是否作为 voice contract 注入 Writer

是。Writer 是正文生成点，`voice_contract` 必须在 Writer 前进入，而不是生成后再润色。合同应短、明确、可执行，并包含禁用项。

## 4. 和 Human Texture v0 是否冲突

不冲突。Human Texture 解决“场景里的人是否像人”，Work Voice 解决“整本书的叙述者是否像同一个人”。两者可并行输入 Writer，Reviewer 分别检查。

## 5. 是否会导致过拟合、仿写、版权风险

会有风险。风险来自样本过窄、使用具体原文、保留专有设定、追求某作者口吻。规避方式是只记录抽象字段，不记录原文，不使用作者名做 prompt，不迁移角色名、设定名、独特比喻、专属句法。

## 6. 如何避免复刻具体作者

- 主概念统一为 Work Voice / Narrative Stance。
- 不使用作者姓名作为生成目标。
- 不读取 raw corpus，除非项目负责人另行批准且只用于内部受控观察。
- 每张观察卡必须写 `non_transferable_original_element`。
- Reviewer gate 检查“是否像具体来源作品”。

## 7. 如何服务原创作品

Work Voice 服务的是原创作品的叙述策略选择：例如“贴主角的行动偏执叙述”“站在世界规则背后的冷眼叙述”“把读者当同谋的荒诞叙述”。这些策略可服务原创设定、原创人物和原创爽点。

## 8. 如何判断声音可迁移

可迁移特征通常是关系和策略：

- 叙述者与主角距离。
- 叙述者与读者关系。
- 信息隐藏和揭示规则。
- 世界态度。
- 爽点展示方式。
- 细节选择偏好。

这些特征换成新设定、新角色、新事件后仍能工作。

## 9. 如何判断原作专属，不能迁移

不可迁移元素包括：

- 原作角色、势力、设定、物件、地名。
- 高辨识度专属比喻、口头禅、句法。
- 特定情节结构和桥段组合。
- 只依赖原作世界观才成立的叙述判断。

这些应进入 `forbidden_original_elements`。

## 10. 如何让输出像稳定讲述者

- 在每章 beat 前明确本章 `narrator_position`。
- 在 Writer 前注入 `voice_contract`。
- 在段落层控制 `protagonist_distance` 与 `intervention_style`。
- 在 Reviewer 中检查站位漂移。
- 在多章后用 `work_voice_map` 检查长篇一致性。

## 推荐集成路线

第一阶段只做研究外壳：

`work_voice_map` -> `voice_contract` -> Writer 临时 prompt block -> Reviewer 临时 rubric -> A/B/C 验证。

第二阶段再工程化：

新增 contract schema、Reviewer gate、日志与回归样例。等 PR #1 合并并稳定后，再决定是否改 `skill-pack`。
