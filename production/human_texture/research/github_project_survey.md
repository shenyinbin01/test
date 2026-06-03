# GitHub Project Survey

调研日期：2026-06-03

说明：star 数和更新时间来自本轮 GitHub 搜索/API 快照，后续可能变化。本轮重点看与 Human Texture Engine 相关的 workflow、prompt、memory、数据结构、评价器，而不是只读 README。

## 筛选方法：为什么是这些项目

本轮不是随机搜项目，而是先从 Human Texture Engine 的目标反推筛选轴。目标不是“找一个能写小说的 agent”，而是找到对当前工程有迁移价值的机制：长篇状态如何保存、Planner/Writer/Reviewer 如何协作、人物与关系如何被结构化、文本质量如何被评价、以及能否在中文网文节奏中落地。

筛选轴如下：

1. 任务相关性：必须与 longform fiction、novel writing agent、story generation、creative writing workflow、AI writing evaluation 至少一项强相关。
2. 工程可读性：不能只看 README；优先选择能看到 prompt、workflow、memory/state、quality evaluator 的项目。
3. 长篇状态能力：优先保留有 story memory、chapter state、character knowledge、world/codex、truth ledger、RAG 或上下文压缩的项目。
4. Agent 分工：优先保留有 planner / writer / editor / reviewer / evaluator / judge 其中多角色分工的项目，因为现有工程已经是 Planner / Writer / Reviewer / Polisher 架构。
5. 人味相关信号：优先深读明确处理 anti-AI pattern、humanizer、author voice、character agenda、micro detail、reader feedback、style fingerprint 的项目。
6. 中文网文迁移性：优先考虑能支持中文、或其机制能迁移到“钩子-规则-破局-代价-章尾”的项目；纯英文文学润色工具降权。
7. 可复现实验价值：至少保留 1-2 个能本地或轻量跑通的项目，用于后续验证 Human Texture Packet。
8. 活跃度与风险：活跃项目优先，但 star 高不是决定因素。若项目很热但主要是 UI/平台或模型本体，且缺少人味 workflow，就只做旁证。

因此，`NovelGenerator`、`knowrite`、`novel-bot` 被深读，不是因为 star 最高，而是因为它们分别覆盖了三种关键迁移价值：

- `NovelGenerator`：有 StoryContextDB 与 anti-LLM prompt，直接触碰“人物不要功能化、细节不要工具化”的问题。
- `knowrite`：有完整 novel engine 状态链，适合作为 Planner/Writer/Reviewer 之后如何接 memory、fitness、governance 的参考。
- `novel-bot`：结构轻，context/memory/skills 清晰，适合做本地可复现实验。

相反，`AI-Writer`、`MaliangAINovalWriter`、`vela` 等 star 更高或产品面更完整，但本轮只列入候选或旁证：它们更像写作平台、IDE 或模型应用，未在本轮有限时间内呈现出比上述三者更直接的人味工程结构。

## 筛选结论

最值得借鉴：

1. `KazKozDev/NovelGenerator`：StoryContextDB、宏观一致性检查、anti-LLM prompt，最接近“人味约束”。
2. `knoai/knowrite`：多阶段 novel engine、author/voice fingerprint、fitness evaluator、governance、memory/RAG/truth delta。
3. `xiaoxiaoxiaotao/novel-bot`：轻量本地 memory/context/skills 结构，适合作为可复现实验参考。

可复现实验：

- `muckelverk/pulpgen`：单体 Python CLI，依赖 Gemini API，容易跑小样本对照。
- `xiaoxiaoxiaotao/novel-bot`：本地 agent loop + workspace memory，适合测试 Human Texture Packet 如何进入上下文。

不建议直接 fork：

- 大型 UI/IDE 项目如 NovelClaw、vela、MaliangAINovalWriter，工程面太大，核心需求不一致。
- 纯 humanizer 或通用写作前端，对叙事层帮助不足。

## 候选项目总表

| 项目 | Stars / 更新快照 | 技术栈 | 本地运行 | Planner/Writer/Reviewer | 长篇状态管理 | 风格控制 | 人类反馈 | 评价体系 | 中文能力 | 代码结构可复用 | 启发 | 建议 |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| [iLearn-Lab/NovelClaw](https://github.com/iLearn-Lab/NovelClaw) | 314 / 2026-06-03 | Python / FastAPI | 可，本地应用 | 有 Plot/Character/World/Writer/Evaluator/Judge | 有 memory bank、storyboard、sessions | 有 style guide/language profile | 有人工 workspace | 有 evaluator/judge/reward | 可支持多语言，需测试中文 | 部分可借鉴，体量大 | 记忆工作台与多 agent 编排 | 借鉴，不 fork |
| [knoai/knowrite](https://github.com/knoai/knowrite) | 15 / 2026-05-29 | TypeScript | 可，本地 web/service | 有 planner/writer/editor/humanizer/proofreader/evaluator | 有 RAG、truth delta、character memory | 有 author/voice fingerprint | 有 reader feedback | 有 fitness/output governance | 可通过 prompt 支持中文，需改造 | 高 | novel engine 状态链条 | 深读，借鉴 |
| [KazKozDev/NovelGenerator](https://github.com/KazKozDev/NovelGenerator) | 133 / 2026-06-03 | TypeScript | 可，需模型 API | 有 structure/character/scene specialists + QC | 有 StoryContextDB | 有 tone/style guidance | 人工弱 | 有 QualityController、macro validation | 理论可中文，prompt 需翻译 | 高 | anti-LLM prompt 和 story context | 深读，借鉴 |
| [xiaoxiaoxiaotao/novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot) | 30 / 2026-05-27 | Python | 可，本地 CLI/agent | 有技能式 writer，reviewer 弱 | 有全局/章节/近期 memory | 有 skills/context | 有交互 loop | 评价弱 | 中文友好 | 中 | 轻量上下文拼装 | 深读，可实验 |
| [muckelverk/pulpgen](https://github.com/muckelverk/pulpgen) | 16 / 2026-03-17 | Python | 可，Gemini API | 有 outline/chapter/edit | XML book state | 风格弱 | 命令式人工介入 | 评价弱 | 未见专门中文 | 中 | 简洁可复现生成链 | 实验，不 fork |
| [Doriandarko/kimi-writer](https://github.com/Doriandarko/kimi-writer) | 571 / 2026-06-01 | Python | 可，Kimi API | 自主写作 loop | 有 token 压缩和文件工具 | 弱 | 命令式 | 弱 | 可中文 | 低-中 | 长上下文工具循环 | 借鉴压缩，不 fork |
| [mrigankad/Novel-OS](https://github.com/mrigankad/Novel-OS) | 11 / 2026-05-29 | Python | 可，本地 | 5-agent editorial pipeline | 有一定项目状态 | 未确认 | 未确认 | 未确认 | 未确认 | 待深读 | 多 agent 编辑管线 | 候选保留 |
| [HXSLtim/Nai](https://github.com/HXSLtim/Nai) | 12 / 2026-04-16 | Python | 可，本地平台 | 多 agent | 未深读 | 未深读 | 未深读 | 未深读 | 中文 | 待深读 | 中文多 agent 平台 | 候选保留 |
| [wzxsph/Novel-Claude](https://github.com/wzxsph/Novel-Claude) | 4 / 2026-06-03 | Python | 可，Claude/API | 微内核/插件/RAG/skills | 有 RAG 思路 | 未深读 | 未深读 | 未深读 | 中文网文友好 | 中 | skill/plugin 化 | 候选保留 |
| [Deng-m1/MaliangAINovalWriter](https://github.com/Deng-m1/MaliangAINovalWriter) | 783 / 2026-06-02 | Dart | 可，客户端 | 写作平台 | 有项目级管理 | 有 | 人工操作 | 弱 | 中文 | 低 | 中文 AI 小说平台 UX | 借鉴 UX，不 fork |
| [heider-x/vela](https://github.com/heider-x/vela) | 349 / 2026-06-03 | TypeScript | 可，本地 IDE | 写作 IDE | 有 RAG/本地模型思路 | 有 | 强 | 未确认 | 未确认 | 低-中 | 本地 AI 小说 IDE | 观察，不 fork |
| [zy-zmc/tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer) | 284 / 2026-06-03 | C# | 可 | 写作流程 | 有 15 维事实快照、状态门禁 | 未深读 | 未深读 | 有门禁思路 | 中文 | 中 | 事实快照/状态回写 | 借鉴状态门禁 |
| [BlinkDL/AI-Writer](https://github.com/BlinkDL/AI-Writer) | 3731 / 2026-06-03 | Python | 可 | 生成系统 | 未确认 | 弱 | 弱 | 弱 | 中文强 | 低 | 早期中文生成参考 | 放弃作为底座 |
| [google-deepmind/dramatron](https://github.com/google-deepmind/dramatron) | 研究项目 | Python/Colab | 可，需接 LLM sample | 分层生成：logline/characters/plot/locations/dialogue | 有层级结构 | 弱 | 强，人机共创 | 用户研究 | 英文为主 | 中 | 分层 co-writing | 方法借鉴 |
| [lechmazur/writing](https://github.com/lechmazur/writing) | 387 / 2026-06-01 | Benchmark | 非生成应用 | 无 | 无 | 无 | 人/LLM 评价 | pairwise comparison | 多语言未确认 | 中 | A/B 评价方法 | 借鉴评测 |

## 重点深读 1：knowrite

链接：https://github.com/knoai/knowrite

本轮阅读：

- `src/services/novel-engine.ts`
- `src/services/novel/chapter-planner.ts`
- `src/services/novel/chapter-writer.ts`
- `src/services/novel/fitness-evaluator.ts`
- `src/services/author-fingerprint*`
- `src/services/voice-fingerprint*`
- `src/services/character-memory*`
- `src/services/temporal-truth*`
- `prompts/`

代码结构：

- `novel-engine.ts` 负责编排整体生成。
- `chapter-planner.ts` 生成章节 beat / scene plan。
- `chapter-writer.ts` 串联 writer、editor、humanizer、proofreader、reader feedback、summarizer。
- 后续服务维护 RAG、truth delta、voice fingerprint、character memory、skill extraction、governance。

Workflow 观察：

1. outline/theme 生成。
2. 章节规划。
3. 输入 governance。
4. writer 生成 raw chapter。
5. editor loop。
6. humanizer。
7. proofreader。
8. reader feedback。
9. memory / truth / voice / character 状态更新。
10. fitness / output governance。

Prompt / humanizer 观察：

- Humanizer prompt 明确要求去除“AI 腔”、句式错落、对话非功能化、修辞具体化、每约 500 字加入微小细节。
- 优点：它知道 AI 文本常见问题，并把 humanizer 放入工作流。
- 局限：仍偏后置改写。若 Planner 没有给人物私心、关系债、代价余波，humanizer 只能把空心文本写得更自然。

数据结构观察：

- author fingerprint / voice fingerprint 值得借鉴为“项目声音账”。
- temporal truth / character memory 值得借鉴为“事实与人物关系状态账”。
- fitness evaluator / governance 值得借鉴为 Reviewer gate。

对中文网文适配：

- 可适配，但要把通用 humanizer 换成中文网文 Human Texture rubric。
- 需要加入“开章钩子不能吞掉人”“破局必须产生后果账”等本项目特有门禁。

建议：

- 不 fork。
- 借鉴多阶段状态链：`plan -> write -> human texture review -> revise -> memory update`。

## 重点深读 2：NovelGenerator

链接：https://github.com/KazKozDev/NovelGenerator

本轮阅读：

- `utils/agentCoordinator.ts`
- `utils/storyContextDatabase.ts`
- `utils/qualityController.ts`
- `utils/chapterWritingPrompt.ts`

代码结构：

- `agentCoordinator.ts` 管理 coordinated specialist generation。
- `storyContextDatabase.ts` 维护章节共享状态、既定事实、伏笔、角色知识、读者知识。
- `qualityController.ts` 做质量分析与修复建议。
- `chapterWritingPrompt.ts` 集中放章节 prompt 与反模板约束。

Workflow 观察：

1. context preparation。
2. specialist generation：structure / character / scene。
3. synthesis。
4. macro validation。
5. light polish。
6. repetition check / fix。
7. coherence update。

数据结构观察：

- `EstablishedFact`：已确立事实。
- `PlannedRevelation`：计划揭示。
- `ForeshadowingHint`：伏笔提示。
- `CharacterKnowledge`：角色知道什么。
- `ReaderKnowledge`：读者知道什么。
- `SharedChapterState`：章节共享状态。

这些结构直接启发 Human Texture 的三个账本：

- 关系账：谁欠谁、谁误会谁、谁避开谁。
- 后果账：身体、声誉、资源、时间、心理防线的损耗。
- 信息账：读者知道、角色知道、谁误读、谁隐瞒。

Prompt 观察：

`chapterWritingPrompt.ts` 中的 anti-LLM pattern prevention 很有价值，要求：

- 一个奇怪但有意义的个人细节。
- 一个不完美的时刻。
- 一个未解决元素。
- 一个出乎意料的结构选择。
- 一个 grounding detail。

配角也被要求具有 personal agenda、unexpected trait、speech pattern、hidden knowledge、personal problem。这是目前开源项目中最接近 Human Texture 的 prompt 设计。

局限：

- 它仍偏英文通用小说，不理解中文网文的机制爽点。
- 它的“奇怪细节”如果直接照搬，容易变成装饰性细节。

建议：

- 强烈建议借鉴数据结构和 prompt 原则。
- 不建议 fork；应将其思想转化为 `human_texture_packet`。

## 重点深读 3：novel-bot

链接：https://github.com/xiaoxiaoxiaotao/novel-bot

本轮阅读：

- `novel_bot/agent/loop.py`
- `novel_bot/agent/memory.py`
- `novel_bot/agent/context.py`
- `skills/chapter-writer/SKILL.md`

代码结构：

- `loop.py`：agent 交互循环，处理工具调用、session history、写文件/记忆调用压缩。
- `memory.py`：全局记忆、章节记忆、近期章节、写作进度。
- `context.py`：把 settings、characters、world、memory、recent summaries、story summary、skills、outline、progress 拼入上下文。
- `skills/chapter-writer/SKILL.md`：章节写作技能，强调感官沉浸、描写/对话比例、修辞、章尾余韵。

Workflow 观察：

- 它的价值不是复杂 agent，而是清楚地把“项目记忆 + 近期章节 + 技能”拼给 Writer。
- 对本项目而言，Human Texture Packet 可作为一种额外 context 注入，不必先重构整个系统。

局限：

- Reviewer 与 evaluation 较弱。
- 文学技能偏“写得漂亮”，不一定能解决关系后果。

建议：

- 可作为复现实验项目。
- 借鉴轻量 memory/context 形态，不直接复用创作技能。

## 补充深读：NovelClaw

链接：https://github.com/iLearn-Lab/NovelClaw

本轮阅读：

- README。
- GitHub connector 获取 `apps/novelclaw/workflow/executor.py` 关键结构。

观察：

- NovelClaw 是 FastAPI 写作工作台，包含 sessions、storyboards、manuscript、world、character、style、memory bank 等视图。
- executor 中出现 memory system、turning point tracker、consistency checker、realtime editor、PlotAgent、CharacterAgent、WorldAgent、RetrievalAgent、WriterAgent、EvaluatorAgent、JudgeAgent、RewardSystem。
- `CompositiveExecutor` 会维护 story premise、task briefs、style guide、language profile 等上下文。

价值：

- 很适合借鉴“可检查的记忆工作台”和 evaluator/judge 的位置。

局限：

- 项目体量大，本轮 clone 不稳定，且功能面超出当前 Human Texture MVP。

建议：

- 借鉴，不 fork。

## 补充深读：Dramatron

链接：https://github.com/google-deepmind/dramatron

本轮阅读：

- `README.md`
- `colab/dramatron.ipynb` 的结构标记与层级对象。

观察：

- Dramatron 从 logline 出发，层级生成 character descriptions、plot points、location descriptions、dialogue。
- 项目明确说它是 co-writing system，不是 autonomous full-play generator。
- 用户研究显示专业作者更愿意把它用于 worldbuilding、替代方案探索、灵感生成，而不是直接写完整剧本。

价值：

- Human Texture 不应追求全自动“写得像人”，而应生成可审查的人味候选：私心、关系债、场景阻力、后果账。

建议：

- 方法借鉴，不作为工程底座。

## 补充项目：pulpgen

链接：https://github.com/muckelverk/pulpgen

本轮阅读：

- 单体 Python CLI。
- 书籍 XML state、outline、chapter、edit、export markdown/epub/html。

价值：

- 足够轻，适合做小实验：把 Human Texture Packet 前后注入同一章节 prompt，比较输出。

局限：

- 评价器、关系状态和人物私心弱。

建议：

- 可复现实验，不 fork。

## 补充项目：kimi-writer

链接：https://github.com/Doriandarko/kimi-writer

本轮阅读：

- 工具式自主写作 loop。
- token 阈值上下文压缩、文件工具、项目创建/写入。

价值：

- 对长上下文压缩和工具循环有启发。

局限：

- Human Texture 相关约束弱。

建议：

- 只借鉴压缩和工具循环，不作为底座。

## 可复现实验建议

实验 1：`novel-bot`

- 目标：测试 `human_texture_packet` 作为 context 是否能让 Writer 改变人物与场景表现。
- 输入：当前第 4 章复检/柳青砚冲突片段。
- 对照：原 prompt vs 加入人物私心/关系债/后果账 prompt。
- 评价：使用本目录 rubric + 人审偏好。

实验 2：`pulpgen`

- 目标：测试单体生成链中，Human Texture Packet 在 outline 阶段 vs edit 阶段注入的差异。
- 输入：第 3 章矿洞发现片段。
- 对照：后置 humanizer vs 前置信息载体/场景生活/代价后果约束。
- 评价：看信息公告化是否降低，人物是否仍只是机制观察器。

## 总体建议

Human Texture Engine 应自研。外部项目能提供：

- `NovelGenerator`：数据结构和 anti-LLM prompt。
- `knowrite`：多阶段 workflow 与状态服务。
- `novel-bot`：轻量上下文拼装。
- `Dramatron`：人机共创定位。
- `lechmazur/writing`：pairwise 评价方法。

但没有一个项目可以直接解决中文网文中的核心矛盾：既要保留高密度机制爽点，又要让人物像人在承受规则、代价和关系。
