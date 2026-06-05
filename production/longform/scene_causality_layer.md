# Scene Causality Layer

Scene Causality（场景因果层）复用 Character Agency（角色主动感 / 行动主权）成果。它负责让人物在场景内自己推动局面，而不是被章节卡机械牵引。

## 场景行动包字段

| 字段 | 定义 |
|---|---|
| `local_goal` | 人物在本场景的具体可行动目标。 |
| `belief_about_situation` | 人物此刻以为局面是什么，允许错误或不完整。 |
| `available_options` | 人物看得到的 2-4 个选择。 |
| `chosen_tactic` | 人物实际采用的策略，必须带取舍。 |
| `perceived_cost` | 人物以为自己要付出的代价。 |
| `wrong_model_or_blindspot` | 人物的误判、盲点或低估。 |
| `withheld_plan` | 人物暂时不说出的计划或真实意图。 |
| `attention_target` | 人物注意力真正落点，帮助正文写行动而非解释。 |
| `next_friction` | 本选择给下一场景或下一章留下的具体摩擦。 |

## 与长篇车架的关系

章节卡给出状态变化合同，场景行动包负责让变化由人物选择自然发生。Story Orchestrator Lite 可以检查场景结果是否仍在 `allowed_divergence_band` 内，但不能替角色选策略。

## 失败信号

- 场景符合章节功能，但人物像执行任务。
- 人物选择没有误判、取舍或代价。
- 后果没有进入 `state_delta`。
- Orchestrator 为了卷目标压死人物主动感。
