# Reviewer Gate Tiering

Longform Reviewer Gate v1 分为 Critical / Standard / Research。真实三章小样本先跑 Critical + Standard，不跑 Research gate。

## Critical Gate

一票否决或必须退回的结构门。

| gate | purpose | return_to |
|---|---|---|
| `chapter_contract_compliance` | 检查章节是否执行最小状态变化合同。 | Orchestrator / Planner |
| `state_delta_traceability` | 检查 delta 是否有 evidence_ref。 | StateManager / Reviewer |
| `relationship_debt_continuity` | 检查关系债是否继承、刷新或明确延期。 | State Delta / Relationship Ledger |
| `knowledge_state_consistency` | 检查谁知道什么是否一致。 | Knowledge Ledger / Chapter Card |
| `renderer_overreach` | 检查 Renderer 是否改因果、资源、知识或关系事实。 | Renderer Contract |
| `polisher_boundary` | 检查是否把结构洞交给 Polisher。 | Hard fail |
| `anti_feed_hard_fail` | 检查空推进、免费爽点、账本虚构等硬失败。 | Reviewer |

## Standard Gate

真实三章小样本建议同时运行。

| gate | purpose | return_to |
|---|---|---|
| `volume_goal_progress` | 检查本章是否服务当前卷目标。 | Orchestrator |
| `reader_question_continuity` | 检查读者问题是否刷新、兑现或延期。 | Reader Question Ledger |
| `agency_clarity` | 检查关键选择是否由人物目标、误判和代价推动。 | Scene Engine |
| `foreshadow_payoff_tracking` | 检查伏笔窗口和兑现状态。 | Chapter Card |
| `narrator_overreach` | 检查叙述者是否替读者或角色下结论。 | Renderer / Work Voice |
| `hook_payoff_balance` | 检查钩子和阶段兑现是否平衡。 | Orchestrator / Reviewer |

## Research Gate

只用于失败诊断或长线研究。

| gate | purpose |
|---|---|
| `template_pattern_drift` | 检查多章结构模板漂移。 |
| `spotlight_distribution_over_time` | 检查人物聚光曲线。 |
| `prose_liveliness_if_later_generated` | 生成后再看阅读活性。 |
| `longrange_reader_emotion_curve` | 长线读者情绪曲线，当前三章不默认使用。 |

## v1 Decision

真实三章小样本先跑 Critical + Standard。Research gate 不进入默认链路，避免 Reviewer 变成大型研究仪表盘。
