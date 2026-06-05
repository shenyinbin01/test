# Three Chapter Continuity MVP v0

这是长篇三章连续 MVP 设计包，不生成正文，不跑 DeepSeek，不读取 raw corpus。

## 目标

验证“单书故事 + 卷卡 + 章节卡 + 状态增量 + Story Orchestrator Lite（故事调度器轻量版）”是否能比现有逐章生成更好地保持连续性。

## 要验证的问题

- 三章之间主线是否更稳定。
- 关系债是否能跨章继承。
- 信息状态是否一致。
- 读者问题是否被刷新、回收或明确延期。
- `state_delta` 是否能追溯到正文证据或事件日志。
- Renderer（正文渲染器）是否保持限权，不修补结构洞。

## 当前阶段

当前只做设计：

- 不生成真实小说正文。
- 不创建真实长篇小说大纲。
- 不使用具体作者。
- 不使用 raw corpus。
- 不启动 Hermes / DeepSeek。
- 不修改 `skill-pack`。
