# Reusable Projects Shortlist

日期：2026-06-03

## 结论

没有发现适合直接 fork 成 Human Texture Engine 的项目。建议自研核心，但借鉴 5 类外部能力：

1. 长篇状态账本。
2. Planner / Writer / Reviewer / Evaluator workflow。
3. anti-AI / anti-template prompt。
4. 轻量 memory/context 注入。
5. pairwise 评价方法。

## 推荐借鉴项目

### 1. NovelGenerator

链接：https://github.com/KazKozDev/NovelGenerator

可借鉴：

- `StoryContextDB`。
- `EstablishedFact`、`PlannedRevelation`、`ForeshadowingHint`、`CharacterKnowledge`、`ReaderKnowledge`。
- chapter prompt 中的 anti-LLM pattern prevention。
- 配角 personal agenda、unexpected trait、hidden knowledge、personal problem。

不复用原因：

- 英文通用小说语境，不适配中文网文节奏。
- prompt 思路好，但需要转化为本项目的 Human Texture Packet。

建议：

- 借鉴数据结构和 prompt 原则。
- 不 fork。

### 2. knowrite

链接：https://github.com/knoai/knowrite

可借鉴：

- `novel-engine.ts` 的多阶段编排。
- `chapter-planner.ts` / `chapter-writer.ts` 的职责分层。
- author fingerprint、voice fingerprint。
- character memory、temporal truth、RAG、fitness evaluator、governance。

不复用原因：

- humanizer 偏后置去 AI 腔。
- 工程链条与现有 skill-pack 重叠，直接 fork 会破坏当前架构。

建议：

- 借鉴状态更新链：写作后更新 voice、character、truth、fitness。
- 不 fork。

### 3. novel-bot

链接：https://github.com/xiaoxiaoxiaotao/novel-bot

可借鉴：

- `context.py` 把 settings、characters、world、memory、recent summaries、skills、outline 拼接为上下文。
- `memory.py` 的全局/章节/近期记忆结构。
- 技能式写作 prompt。

不复用原因：

- Reviewer 和评价体系弱。
- 人味约束偏文学表达，不够关系/后果导向。

建议：

- 作为 Human Texture Packet 注入实验对象。
- 不 fork。

### 4. NovelClaw

链接：https://github.com/iLearn-Lab/NovelClaw

可借鉴：

- memory bank / storyboard / manuscript / world / character / style workspace。
- PlotAgent、CharacterAgent、WorldAgent、WriterAgent、EvaluatorAgent、JudgeAgent 的协作位置。
- turning point tracker、consistency checker、reward system 的设计方向。

不复用原因：

- 体量大，偏完整写作平台。
- 本项目当前只需要 Human Texture MVP。

建议：

- 借鉴工作台和可检查 memory surfaces。
- 不 fork。

### 5. Dramatron

链接：https://github.com/google-deepmind/dramatron

可借鉴：

- logline -> characters -> plot points -> locations -> dialogue 的层级 co-writing。
- 明确把 AI 输出定位为素材，供作者选择、编辑、重写。

不复用原因：

- 剧本系统，不是中文网文长篇系统。
- 结构层启发大于代码复用。

建议：

- 借鉴 co-writing 方法论。

### 6. pulpgen

链接：https://github.com/muckelverk/pulpgen

可借鉴：

- 轻量 Python CLI。
- XML book state。
- outline/chapter/edit/export 简单链条。

不复用原因：

- 评价、人味、关系状态都弱。

建议：

- 作为 A/B prompt 注入实验对象。

### 7. lechmazur/writing

链接：https://github.com/lechmazur/writing

可借鉴：

- 同一 creative brief 下做 pairwise story comparison。
- 双顺序比较降低位置偏差。
- 用偏好图而不是绝对分数排名。

不复用原因：

- 是短篇 benchmark，不是工程写作系统。

建议：

- 借鉴 A/B 人审框架。

## 暂不建议投入的项目类型

### 大型写作 IDE

例：`vela`、`MaliangAINovalWriter`。

原因：

- 主要价值在 UI、项目管理和本地模型集成。
- 当前问题不是缺写作 IDE，而是缺 Human Texture 叙事合同。

### 模型/生成演示项目

例：`AI-Writer`。

原因：

- star 高，但与现有 Planner/Writer/Reviewer 工程对接价值有限。

### 通用 humanizer

原因：

- 只能改表层句式。
- 容易把目标带偏到 detector avoidance。

## 推荐复用策略

短期：

- 用 `NovelGenerator` 的思路设计 `human_texture_packet`。
- 用 `novel-bot` 或 `pulpgen` 做小实验。
- 用 `lechmazur/writing` 的 pairwise 方法做 A/B 评价。

中期：

- 从 `knowrite` 借鉴 voice/character/truth state 更新。
- 从 `NovelClaw` 借鉴可检查的 memory workspace。

长期：

- 将 Human Texture Packet、Relationship Debt Ledger、Consequence Ledger 融入现有 skill-pack。
- 形成项目内 approved human texture patterns，但必须等实验通过后再做。
