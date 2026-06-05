# Drift Detection Rules

偏航检测不是看“读起来怪不怪”，而是检查长篇闭环是否偏离单书承诺、卷目标、角色状态和读者问题。

| drift | detection_method | common_cause | response | return_to |
|---|---|---|---|---|
| 主线偏航 | 检查 `state_delta.plot_delta` 是否仍链接 Book Spine 或当前 `volume_goal`。 | 场景漂亮但不服务主线。 | 重写或收窄 `chapter_card`。 | Orchestrator |
| 卷目标偏航 | 连续章节没有推进、反转、延迟或扩大卷目标压力。 | chapter hook 独立成瘾。 | 强制下一章绑定 `volume_goal_link`。 | Orchestrator |
| 角色动机漂移 | `character_state_ledger.current_goal` 改变但没有 delta 证据。 | Writer 或 Renderer 自行补动机。 | 回到 scene agency 和角色状态账本。 | Scene Engine |
| 信息状态错乱 | `knowledge_ledger` 中 known_by / withheld_from 与正文证据冲突。 | 聚焦越界或公告式解释。 | 修正知识状态或重排信息载体。 | Chapter Card / Knowledge Ledger |
| 伏笔遗忘 | `foreshadow_payoff_ledger.expected_payoff_window` 超期无回收或延期理由。 | 只开坑不管旧债。 | 下一章优先刷新、兑现或明确延期。 | Chapter Card |
| 关系债蒸发 | `relationship_debt_ledger.next_manifestation` 未出现且无延期。 | 单章和解或配角工具化。 | 强制关系压力进入下一章。 | Relationship Ledger / Scene Engine |
| 世界规则冲突 | `world_slice.active_rules` 与事件结果冲突。 | 临时爽点绕过规则。 | 退回章节卡或世界切片。 | Orchestrator |
| 读者期待断裂 | `reader_question_ledger` 的问题被遗忘、被强行公告或无理由改写。 | 叙述者提前喂答案。 | 重建 reader question before/after。 | Reviewer / Chapter Card |
| 重复骨架 | 近三章 `plot_function + hook_type + payoff_type` 高度相似。 | 模板化推进。 | 调整章节功能和 spotlight budget。 | Orchestrator |

## 使用原则

偏航检测只能触发局部 replan 或 gate fail，不能让 Orchestrator 直接写正文。
