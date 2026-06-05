# Longform Architecture

## 架构总览

可选冷层：

```text
IP Universe / Series Codex / World Asset Pool
```

热路径：

```text
World Slice
  -> Book Spine
  -> Volume Card
  -> Chapter Card
  -> Scene Agency Packet
  -> Event Log
  -> Narrative Renderer
  -> State Delta
  -> Ledger Reducers
  -> Next Chapter Retrieval
```

## 关键定义

IP Universe（IP 宇宙）是冷层资产，不是热路径入口。当前只需要 World Slice（世界切片），也就是本次三章连续实验必须用到的最小世界约束。

Book Spine（单书脊梁）是热启动入口。它确定一本书的核心承诺、主对抗、类型承诺、情绪承诺和终局方向。

Chapter Card（章节卡）不是剧情摘要，而是状态变化合同。它必须说明本章之前和之后，人物状态、关系压力、知识状态、资源 / 身份状态、读者问题和下一章种子如何变化。

State Delta（状态增量）是写后唯一增量事实。所有账本更新都必须能追溯到它，不能由 Writer 或 Renderer 直接手改账本。

Ledger Reducers（账本归并器）负责把 `state_delta` 转为剧情、角色、关系、信息、资源、声誉、读者问题、伏笔和卷目标进度等运行时视图。

Narrative Renderer（正文渲染器）不能改因果。它只能把已批准的章节卡、场景行动包、事件日志、人物质感包和叙述合同渲染成正文；发现结构问题时返回 blocker。

Story Orchestrator Lite（故事调度器轻量版）控制边界，不替角色做选择。它负责绑定卷目标、章节卡和当前账本，检查场景结果是否仍在允许偏差内。

## 闭环而非瀑布

长篇系统不是：

```text
设定越完整 -> 大纲越完整 -> 正文自然稳定
```

而是：

```text
热路径规划 -> 场景行动 -> 正文渲染 -> 状态增量 -> 账本视图 -> 下一章检索与偏航检查
```

每一章完成后，系统必须通过 `state_delta` 写回变化，再由账本影响下一章。连续性不能寄托给一个越来越长的 summary。
