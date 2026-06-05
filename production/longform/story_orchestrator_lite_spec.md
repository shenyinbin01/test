# Story Orchestrator Lite Spec

Story Orchestrator Lite（故事调度器轻量版）是长篇热路径的边界管理者。它不是 Writer，也不是隐藏作者。

## 它做什么

- 绑定卷目标、章节卡和当前账本。
- 生成下一章场景任务包。
- 决定哪些 reader debt（读者债 / 读者问题）必须刷新。
- 控制 spotlight（聚光预算），避免配角、设定或钩子吞掉人物承受点。
- 约束 reveal 顺序、高潮窗口和 hook 延迟。
- 判断 scene outcome（场景结果）是否仍在 `allowed_divergence_band` 内。
- 在偏航时触发局部 replan。

## 它不做什么

- 不写正文。
- 不替角色写内心。
- 不决定具体句法。
- 不越过 Reviewer 直接更新 canon。
- 不把场景变成机械任务清单。
- 不替角色做选择。

## 输入

- `single_book_story`
- `volume_card`
- 当前 `chapter_card`
- 当前热账本切片
- 上一章 `state_delta`
- 需要保留或刷新的一组 reader questions

## 输出

- 下一章或当前章的场景任务包。
- 必须读取的账本切片。
- spotlight budget。
- reveal / payoff / debt 窗口约束。
- drift warning，如有。

## 退回规则

| 失败 | 退回 |
|---|---|
| chapter_card 与 volume_goal 脱节 | Planner / Orchestrator |
| scene outcome 超出 allowed_divergence_band | Orchestrator 局部 replan |
| 人物选择被硬控 | Scene Engine |
| reader debt 过期无说明 | Chapter Card / Reader Question Ledger |
| Renderer 发现因果太薄 | Orchestrator / Scene Engine |

## 核心边界

Orchestrator 控制“允许空间”，不替角色写“具体选择”。如果它为了主线稳定把人物变成任务执行件，说明它失败，而不是 Writer 失败。
