# Character Agency MVP Design

角色主动感 / 行动主权（Character Agency）解决的是：人物是否自己推动局面，而不是被剧情推着走。

它不是：

- 主角永远主动出击。
- 主角永远正确。
- 主角永远强势。
- 多写动作。
- 多写心理解释。
- 自由多 agent 聊天。

本设计包只做 MVP contract、schema、ledger 和 reviewer gate 草案，不生成小说正文，不修改 `skill-pack`，不运行 Hermes / DeepSeek。

## 文件说明

- [status.yaml](status.yaml): 设计包状态。
- [problem_statement.md](problem_statement.md): 问题定义。
- [scene_agency_packet.schema.yaml](scene_agency_packet.schema.yaml): 场景级行动主权 packet。
- [consequence_ledger.schema.yaml](consequence_ledger.schema.yaml): 后果继承账本。
- [relationship_debt_ledger.schema.yaml](relationship_debt_ledger.schema.yaml): 关系债账本。
- [planner_contract_draft.md](planner_contract_draft.md): Planner 合同草案。
- [writer_contract_draft.md](writer_contract_draft.md): Writer 合同草案。
- [reviewer_gate_draft.md](reviewer_gate_draft.md): Reviewer gate 草案。
- [one_scene_mvp_plan.md](one_scene_mvp_plan.md): 一场景 MVP 计划。
- [acceptance_criteria.md](acceptance_criteria.md): 验收标准。
- [anti_misuse_rules.md](anti_misuse_rules.md): 防误用规则。
- [next_step_recommendation.md](next_step_recommendation.md): 下一步建议。
