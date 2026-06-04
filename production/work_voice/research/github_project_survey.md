# GitHub Project Survey

调研目标是寻找 fiction generation、长篇状态管理、voice/style/persona 控制、planner/writer/reviewer/evaluator 相关开源项目。GitHub 匿名 API 在调研时出现 rate limit，star 精确值未作为结论依据；表内 star / 活跃度沿用本仓库 Human Texture 调研快照并结合本轮页面与代码读取，进入 MVP 前应复核。License 以本轮读取到的 LICENSE 文件或页面状态标注。

## 15 个候选项目

| 项目 | 链接 | stars / 活跃度快照 | license | 目标 | voice/style/persona | 长篇状态 | planner/writer/reviewer | 复用判断 |
|---|---|---:|---|---|---|---|---|---|
| NovelGenerator | [KazKozDev/NovelGenerator](https://github.com/KazKozDev/NovelGenerator) | 133 / 2026-06-03 | BSL 1.1，2029 后 Apache-2.0 | AI novel generation | 有 humanization、quality、story context | 有 reader/character knowledge | 有 agent coordinator | 重点借鉴结构，不直接复用 |
| knowrite | [knoai/knowrite](https://github.com/knoai/knowrite) | 15 / 2026-05-29 | AGPL-3.0 | long-form AI writing system | README 描述 voice fingerprint / author fingerprint | 三层记忆 | Writer/Editor/Humanizer/Reader 等 | 概念强，license 谨慎 |
| novel-bot | [xiaoxiaoxiaotao/novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot) | 30 / 2026-05-27 | MIT | 小说生成 bot | 通过 settings/skills/context 控制 | workspace/chapter memory | agent context + memory | 可借鉴轻量上下文拼装 |
| NovelClaw | [iLearn-Lab/NovelClaw](https://github.com/iLearn-Lab/NovelClaw) | 314 / 2026-06-03 | MIT | complex long-form story workflow | 多 Agent 间接支持 | MemorySystem/Retriever | Planner-like agents + evaluator | 可借鉴 executor 和 gate |
| Dramatron | [google-deepmind/dramatron](https://github.com/google-deepmind/dramatron) | 研究项目 / 需复核 | Apache-2.0 | co-writing scripts | 不以 voice 为核心 | 层级生成 | logline -> characters -> plot -> dialogue | 可借鉴层级 co-writing |
| pulpgen | [muckelverk/pulpgen](https://github.com/muckelverk/pulpgen) | 16 / 2026-03-17 | MIT | CLI pulp fiction generator | 可通过 prompts 控制 | XML state/patch | outline -> draft -> revise | 可借鉴实验 harness |
| kimi-writer | [Doriandarko/kimi-writer](https://github.com/Doriandarko/kimi-writer) | 571 / 2026-06-01 | MIT with attribution requirement | AI writing workflow | 需复核 | token 压缩和文件工具 | autonomous loop | 候选，不作为 MVP 依赖 |
| lechmazur writing | [lechmazur/writing](https://github.com/lechmazur/writing) | 387 / 2026-06-01 | 未找到 LICENSE，需复核 | creative writing benchmark | 评价而非生成 | 无 | benchmark | 可借鉴评测形式 |
| Novel-OS | [mrigankad/Novel-OS](https://github.com/mrigankad/Novel-OS) | 11 / 2026-05-29 | MIT | AI novel OS | 需复核 | 可能有项目状态 | 5-agent editorial pipeline | 候选 |
| Nai | [HXSLtim/Nai](https://github.com/HXSLtim/Nai) | 12 / 2026-04-16 | 未找到 LICENSE，需复核 | AI novel writing related | 需复核 | 需复核 | 多 Agent | 候选 |
| Novel-Claude | [wzxsph/Novel-Claude](https://github.com/wzxsph/Novel-Claude) | 4 / 2026-06-03 | GPL-3.0 | Claude 小说写作 | prompt-driven | RAG 思路 | microkernel/plugin/skills | 候选 |
| MaliangAINovalWriter | [Deng-m1/MaliangAINovalWriter](https://github.com/Deng-m1/MaliangAINovalWriter) | 783 / 2026-06-02 | Apache-2.0 | AI novel writer | 有平台式风格控制 | 项目级管理 | 写作平台 | 借鉴 UX，不 fork |
| vela | [heider-x/vela](https://github.com/heider-x/vela) | 349 / 2026-06-03 | GPL-3.0 | writing / AI assistant | 有写作 IDE 控制 | RAG / 本地模型思路 | IDE + 人工操作 | 观察，不 fork |
| tianming-novel-ai-writer | [zy-zmc/tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer) | 284 / 2026-06-03 | 未找到 LICENSE，需复核 | 长篇小说工程系统 | 通过协议和 gate 控制 | fact snapshot / ledger | generation gate | 重点借鉴 gate |
| AI-Writer | [BlinkDL/AI-Writer](https://github.com/BlinkDL/AI-Writer) | 3731 / 2026-06-03 | Apache-2.0 | AI writing | 需复核 | 需复核 | 生成系统 | 历史参考 |

## 5 个重点项目

### 1. NovelGenerator

深读代码：

- `utils/storyContextDatabase.ts`
- `utils/qualityController.ts`
- `utils/chapterWritingPrompt.ts`
- `utils/agentCoordinator.ts`

发现：

- `SharedChapterState` 把 established facts、planned revelations、foreshadowing hints、character knowledge、reader knowledge 分开管理。
- `qualityController` 有 emotional curve、pacing、repetition、show vs tell、revelation、stakes、micro details 等评价维度。
- `chapterWritingPrompt` 有避免 AI 味和增加具体细节的检查。
- `agentCoordinator` 支持上下文准备、专家生成、综合、轻润色、重复检查和一致性更新。

可借鉴：`readerKnowledge` / `characterKnowledge` 分离，可迁移到 Work Voice 的 `knowledge_boundary` 和 `reader_relationship`。不适合之处：英文项目，质量维度偏通用，不能直接解决中文网文叙述站位。

### 2. knowrite

深读范围：README 和项目公开结构说明。

发现：

- README 描述 Writer、Editor、Humanizer、Proofreader、Reader、Summarizer、Fitness 多角色。
- 描述三层记忆、character episodic memory、temporal truth、input/output governance、voice fingerprint 等概念。
- License 为 AGPL-3.0，复用代码会引入合规复杂度。

可借鉴：多层记忆、输入输出治理、角色分工和 voice governance。风险：其 terminology 中包含 author/fingerprint 方向，本项目只能借鉴治理框架，不能采用“作者复刻”目标。

### 3. novel-bot

深读代码：

- `novel_bot/agent/context.py`
- `novel_bot/agent/memory.py`

发现：

- context 由 settings、characters、world、global memory、recent summaries、skills、outline、progress 组合。
- memory 区分 workspace memory、chapter memory、recent chapters、progress。

可借鉴：轻量上下文装配方式，可作为 `voice_contract` 注入 Writer 的参考。不适合之处：更像生成 bot，不提供 Work Voice 抽取和评价闭环。

### 4. NovelClaw

深读代码：

- `apps/novelclaw/workflow/executor.py`

发现：

- `CompositiveExecutor` 协调 LLMClient、Retriever、MemorySystem、ConsistencyChecker、TurningPointTracker、RealtimeEditor、PlotAgent、CharacterAgent、WorldAgent、WriterAgent、EvaluatorAgent、JudgeAgent、RewardSystem。

可借鉴：长篇生成应有独立 memory、retriever、consistency checker 和 evaluator。Work Voice MVP 不应一开始复制大型系统，只借鉴 evaluator/gate 思路。

### 5. tianming-novel-ai-writer

深读代码：

- `Services/Modules/ProjectData/Implementations/Generation/GenerationGate/GenerationGate.PublicMethods.cs`
- `Services/Modules/ProjectData/Implementations/Tracking/FactSnapshotExtractor/FactSnapshotExtractor.VolumeSnapshot.cs`

发现：

- GenerationGate 检查协议、CHANGES、ledger consistency、unknown entities、design element presence、POV character presence、规则约束。
- FactSnapshotExtractor 在卷末提取角色、冲突、伏笔、地点、阵营、物件、时间线等快照。

可借鉴：把 Work Voice 作为 gate 检查项，在接受 Writer 输出前判断叙述站位是否漂移、是否违反禁用元素。

## 其他项目简评

- Dramatron：参考 [paper](https://arxiv.org/abs/2209.14958)。其层级 co-writing 对 Planner -> Writer 有启发，但偏剧本结构。
- pulpgen：MIT、CLI、XML state/patch audit trail，适合借鉴小型实验 harness。
- lechmazur/writing：适合做 creative writing benchmark 参考，不是生成系统。

## 2-3 个可借鉴工程结构

1. Knowledge boundary：借 NovelGenerator 的 reader/character knowledge，把“叙述者知道什么、读者知道什么、主角知道什么”拆开。
2. Contract injection：借 novel-bot 的 context 组装和 NovelAI/Novelcrafter 的控制槽位，把 `voice_contract` 放进 Writer 前置上下文。
3. Gate before acceptance：借 tianming 的 GenerationGate 和 NovelClaw 的 evaluator，把 Work Voice Reviewer gate 放在 draft 接受前。

## 是否能直接复用

没有发现可直接复制到当前项目的成熟 Work Voice 蒸馏系统。可复用的是结构和方法，不是代码：样本分层、上下文合同、知识边界、评价门禁、长篇状态快照。
