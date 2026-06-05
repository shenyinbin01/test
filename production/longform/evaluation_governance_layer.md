# Evaluation Governance Layer

评价治理层负责判断长篇闭环是否真实有效，而不是只看单章是否顺滑。

## 组成

- `longform_reviewer_gate`：长篇章节通过门，检查合同、状态、关系、信息、读者问题、伏笔和边界。
- `drift_detection`：偏航检测，发现主线、卷目标、角色动机、知识状态和世界规则漂移。
- `anti_feed_quality_gate`：反低质投喂门禁，阻止钩子工厂、免费爽点、关系蒸发和账本虚构。
- `reader_question continuity`：读者问题连续性，检查问题是否刷新、回收或明确延期。
- Polisher / Renderer 边界：结构不过关不能交给末端润色。

## Reviewer 退回层级

| 问题 | 退回 |
|---|---|
| 章节合同不成立 | Orchestrator / Planner |
| 场景人物没有主动选择 | Scene Engine |
| 信息状态错乱 | Chapter Card / Knowledge Ledger |
| 关系债无继承 | State Delta / Relationship Debt Ledger |
| Renderer 改因果 | Renderer Contract |
| 语言粗糙但结构有效 | Polisher |
| 结构性空心 | 不得交给 Polisher |

## 通过标准

一章通过不代表长篇通过。三章连续必须同时看：

- 状态是否继承。
- 关系债是否显影。
- 信息状态是否一致。
- 读者问题是否被管理。
- 伏笔是否有窗口。
- 主线是否仍朝 Book Spine 和 Volume Card 推进。
