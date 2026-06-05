# Longform Narrative Production

长篇叙事生产系统解决的不是“单章怎么写得像人”，而是：如何从一个单书故事稳定生产连续章节，并保证主线、卷目标、角色状态、关系债、信息状态、读者期待和伏笔回收不崩。

本目录是设计包，不生成小说正文，不调用 DeepSeek，不启动 Hermes，不修改正式 `skill-pack`。

## 核心目标

- 让单书故事能向卷、章、场景逐层展开。
- 让章节不是孤立输出，而是带前后状态变化的合同。
- 让写后变化先进入 `state_delta`（状态增量），再由 reducers（账本归并器）生成运行时账本。
- 让 Story Orchestrator Lite（故事调度器轻量版）管理边界，而不是替角色做选择。
- 让 Narrative Renderer（正文渲染器）只渲染已批准的事件和状态，不修补结构洞。

## 当前范围

当前只做长篇三章连续 MVP 的设计准备：

- 冷层资产与热路径分离。
- 单书脊梁、卷卡、章节卡、场景行动包、事件日志和状态增量 schema。
- 多类账本 schema 与 reducer 规则。
- Orchestrator、Renderer、Reviewer gate、偏航检测和反低质投喂门禁。
- 三章连续 A/B/C 实验设计。

## 不做的事

- 不创建真实 IP 宇宙。
- 不创建真实长篇小说大纲。
- 不生成正文。
- 不读取 raw corpus。
- 不修改 `skill-pack/creation_skills/`。
- 不修改 `production/phase8/`。
- 不新增 `approved_patterns`。
