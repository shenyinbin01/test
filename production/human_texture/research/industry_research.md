# Industry Research: Human Texture Engine

调研日期：2026-06-03

本文件关注行业方案对“像人写”的处理方式。结论先行：现有工具大多在三类问题上成熟：长篇上下文管理、风格/设定记忆、表层润色与检测；但它们很少把“人物私心、羞耻、犹豫、关系债、代价余波、非工具性细节”做成可执行的叙事合同。因此 Human Texture Engine 不宜复用通用 humanizer，应自研核心叙事评价与注入层。

## 调研选择依据

本轮行业调研不是按市场知名度罗列，而是按当前失败样本暴露的工程缺口选型：

- 长篇上下文缺口：选择 Sudowrite、Novelcrafter、NovelAI，观察 Story Bible / Codex / Lorebook / Memory 能否承载角色、设定、关系和后果。
- 编辑评价缺口：选择 Fictionary、AutoCrit、ProWritingAid，观察成熟编辑工具如何把“场景、冲突、节奏、重复、讲述过多”转成检查项。
- Agent workflow 缺口：选择 NovelClaw、knowrite、NovelGenerator、novel-bot、Dramatron，观察 planner/writer/reviewer/evaluator 如何分工。
- 表层 humanizer 风险：选择 Undetectable AI、Originality.ai 等，明确哪些方案只改句式，不能解决人物和关系。
- 风格控制缺口：选择 NovelAI、Novelcrafter、Sudowrite、knowrite，观察 voice / author note / codex 类结构能否迁移成项目声音账。
- 评价方法缺口：选择 GPTZero、Originality.ai、creative writing benchmark，判断检测器和 pairwise 评价各自能做什么。

因此，本文件的关注点不是“哪款工具最好”，而是“哪个外部方案能补上 Human Texture 的哪一个部件，以及它在哪一层失效”。

## 1. AI 小说写作工具

代表产品 / 项目：

- [Sudowrite](https://www.sudowrite.com/) / Story Bible / Rewrite / Describe。
- [Novelcrafter](https://www.novelcrafter.com/) / Codex / scene drafting。
- [NovelAI](https://novelai.net/) / Memory / Lorebook / Author's Note。
- [Squibler](https://www.squibler.io/) 等书籍生成与章节续写工具。

解决什么问题：

- 快速生成章节、续写、改写、扩写。
- 管理角色、设定、世界观、风格提示。
- 缓解长篇写作时的上下文遗忘。

它们怎么解决“像人写”：

- 主要靠风格提示、作者声音、Rewrite、Describe、Memory、Lorebook、Codex 等上下文约束。
- 部分工具会要求场景目标、角色动机、冲突、情绪线，但多数仍停留在“提示模型写得更自然”。

表层润色还是叙事层改造：

- Sudowrite 的 Rewrite / Describe 偏表层与局部表达增强。
- NovelAI 的 Memory / Lorebook 偏上下文约束。
- Novelcrafter 的 Codex 更接近叙事层，因为它把角色、物品、组织、设定结构化，但并不天然保证人物有私心和关系后果。

是否可借鉴到中文网文：

- 可借鉴：Story Bible / Codex / Lorebook 形态适合中文网文的境界、势力、规则、伏笔、人物关系管理。
- 不足：中文网文节奏更强，若只增加描写，会拖慢爽点；Human Texture 必须嵌入破局、代价和关系，而不是额外插入“文学感段落”。

是否值得复用：

- 不建议直接复用产品形态。
- 值得复用“结构化上下文容器”：角色记忆、关系账、设定账、场景账、信息露出账。

## 2. AI 辅助创作 / 编辑工具

代表产品 / 项目：

- [ProWritingAid](https://prowritingaid.com/)
- [AutoCrit](https://www.autocrit.com/)
- [Fictionary](https://fictionary.co/)
- Grammarly、Hemingway Editor 等通用编辑工具。

解决什么问题：

- 句子清晰度、重复词、节奏、可读性。
- 小说编辑维度：场景目标、冲突、人物弧光、情节结构、叙述比例。
- 找出弱动词、陈词滥调、过度解释、节奏松散。

它们怎么解决“像人写”：

- 通过编辑清单和统计提示，帮助作者意识到重复、讲述过多、情绪命名过多、场景目标不明。
- Fictionary/AutoCrit 的价值在于“编辑视角”，不是模型自动重写。

表层润色还是叙事层改造：

- ProWritingAid 更偏语言层。
- AutoCrit 介于语言层与 genre editing。
- Fictionary 更偏叙事层和场景层，但仍需要作者判断。

是否可借鉴到中文网文：

- 可借鉴“审查问题”形式，例如：这场戏谁想要什么？谁失去了什么？场景信息是否通过行动出现？
- 不宜照搬英文写作统计，如句长、被动语态等。

是否值得复用：

- 值得复用为 Reviewer rubric 的问题模板。
- 不建议作为核心引擎。

## 3. Longform Fiction Agent / Story Generation Agent

代表产品 / 项目：

- [NovelClaw](https://github.com/iLearn-Lab/NovelClaw)
- [knowrite](https://github.com/knoai/knowrite)
- [NovelGenerator](https://github.com/KazKozDev/NovelGenerator)
- [novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot)
- [Dramatron](https://github.com/google-deepmind/dramatron)

解决什么问题：

- 长篇章节规划、上下文压缩、记忆管理、多 agent 协作。
- Planner / Writer / Reviewer / Evaluator 编排。
- 跨章一致性、角色状态、伏笔回收、世界设定维护。

它们怎么解决“像人写”：

- `NovelGenerator` 会在 prompt 中强制要求“奇怪个人细节、不完美时刻、未解决元素、接地细节、配角个人 agenda”。
- `knowrite` 有 humanizer、author fingerprint、voice fingerprint、fitness evaluator、governance 等流程。
- `Dramatron` 明确定位为 human co-writing，生成角色、plot points、location、dialogue，供作者编辑重写。

表层润色还是叙事层改造：

- `knowrite` 的 humanizer 仍偏后置去 AI 腔，但整体 novel engine 是叙事层工作流。
- `NovelGenerator` 的 StoryContextDB 和 anti-LLM prompt 进入了 scene / character 层，最接近 Human Texture。
- `Dramatron` 是结构层 co-writing，不追求自动成稿。

是否可借鉴到中文网文：

- 可以借鉴 agent 编排和状态管理。
- 需要替换为中文网文特有的节奏合同：开章钩子、规则压迫、破局、代价、章尾悬念，同时加入人味约束。

是否值得复用：

- 建议借鉴，不建议直接 fork。
- 外部项目的数据结构和 workflow 可拆作参考；核心 rubric 与中文网文写作合同必须自研。

## 4. AI Humanizer

代表产品 / 项目：

- [Undetectable AI](https://undetectable.ai/)
- [Originality.ai Humanizer](https://originality.ai/)
- QuillBot、Surfer AI Humanizer 等。

解决什么问题：

- 改写 AI 文本以降低检测器命中。
- 改变句式、词汇、节奏、局部冗余。

它们怎么解决“像人写”：

- 主要改变表层可检测特征，例如句长分布、词语选择、口语化程度、困惑度/突发度。

表层润色还是叙事层改造：

- 几乎全是表层润色。
- 对“人物为什么在此刻闭嘴”“为什么撒谎造成关系债”“信息为什么从饭桌传出来”帮助很小。

是否可借鉴到中文网文：

- 不建议作为目标函数。
- 只能借鉴“检测风险不是文学质量”的反面经验。

是否值得复用：

- 不建议复用。
- Human Texture Engine 应避免把文本改得更乱、更口语化，却仍然空心。

## 5. Style Transfer / Author Style Control

代表产品 / 项目：

- NovelAI 的 Memory / Lorebook / Author's Note。
- Novelcrafter 的 Codex。
- Sudowrite 的 Story Bible 与风格改写。
- 开源项目 `knowrite` 的 author fingerprint / voice fingerprint。

解决什么问题：

- 保持语气、设定词、人物称谓、叙述习惯。
- 控制作者声音或类型风格。

它们怎么解决“像人写”：

- 通过上下文样本、风格说明、禁用词、偏好句式、叙述视角约束，让模型模仿某类表达。

表层润色还是叙事层改造：

- 介于语言层和叙事层之间。
- 风格控制可以让句子更像某个作者，但不能自动生成真实后果。

是否可借鉴到中文网文：

- 可借鉴为“声音账本”：主角叙述习惯、配角口头禅、关系称呼变化。
- 不应直接做作者模仿；本项目要做的是人味机制，不是仿写某位作者。

是否值得复用：

- 值得复用上下文组织方式。
- 不建议把 Human Texture 定义成 author style transfer。

## 6. Human-in-the-loop Writing Workflow

代表产品 / 项目：

- [Dramatron](https://github.com/google-deepmind/dramatron)：以剧作家共创为定位。
- Wordcraft：Google PAIR 的人机故事写作系统。
- TaleBrush：让用户用曲线/草图控制故事情绪或情节走向。
- Novelcrafter / Sudowrite 的章节计划与局部重写工作流。

解决什么问题：

- 让作者掌握取舍权，而不是让模型一次性自动定稿。
- 支持作者在角色、场景、情绪线、替代方案之间选择。

它们怎么解决“像人写”：

- 不把 AI 输出当终稿，而当候选材料。
- 通过人类作者的选择、删改、重写保留意图和声音。

表层润色还是叙事层改造：

- 这是流程层改造。
- 对 Human Texture 最重要的启发是：人味经常来自“选择了不说什么、谁尴尬地绕开什么、哪件小事被保留”，这些需要在 workflow 中显式暴露。

是否可借鉴到中文网文：

- 很适合。中文网文生产也需要快速试错，但必须保留主创对爽点、人设和读者预期的控制。

是否值得复用：

- 值得复用“候选方案 + 人审 rubric + 小范围回写”的流程。

## 7. AI Writing Evaluation / AI Fiction Detection

代表产品 / 项目：

- [GPTZero](https://gptzero.me/)
- [Originality.ai](https://originality.ai/)
- Turnitin AI writing detection。
- `lechmazur/writing` creative writing benchmark。

解决什么问题：

- 检测文本是否可能由 AI 生成。
- 比较模型在同一创意约束下的故事质量。
- 发现重复、平均化、模板化、位置偏差。

它们怎么解决“像人写”：

- 检测器通常看统计特征，不等于文学判断。
- 创意写作 benchmark 更接近质量比较，但仍以短篇和成对偏好为主。

表层润色还是叙事层改造：

- AI detector 偏表层统计。
- 创意写作 benchmark 偏评价方法，不提供直接修复。

是否可借鉴到中文网文：

- 可借鉴成对 A/B 人审：同一章节 baseline vs Human Texture 版本，比较“人物是否像人在经历故事”。
- 不建议把 detector 分数当优化目标。

是否值得复用：

- 值得复用 pairwise evaluation 和维度化 reviewer prompt。
- 不建议复用检测器作为主指标。

## 结论

行业方案给 Human Texture Engine 的启发不是“把文本润色得像人”，而是四个工程组件：

1. 结构化上下文：角色、关系、场景、设定、信息、后果都要有账本。
2. 叙事层 reviewer：检查人物是否有私心、关系是否有债、代价是否有后续。
3. 人机共创流程：AI 给候选，作者/Reviewer 按 rubric 取舍。
4. Pairwise 验证：用 baseline 和改造版本做盲评，而不是看检测器分数。

Human Texture Engine 应自研核心能力，外部项目只借鉴架构、数据结构和评估方法。

## 主要来源

- Sudowrite: https://www.sudowrite.com/
- Novelcrafter: https://www.novelcrafter.com/
- NovelAI docs: https://docs.novelai.net/
- ProWritingAid: https://prowritingaid.com/
- AutoCrit: https://www.autocrit.com/
- Fictionary: https://fictionary.co/
- GPTZero: https://gptzero.me/
- Originality.ai: https://originality.ai/
- Undetectable AI: https://undetectable.ai/
- Dramatron: https://github.com/google-deepmind/dramatron
- Dramatron paper: https://arxiv.org/abs/2209.14958
- NovelClaw: https://github.com/iLearn-Lab/NovelClaw
- knowrite: https://github.com/knoai/knowrite
- NovelGenerator: https://github.com/KazKozDev/NovelGenerator
- novel-bot: https://github.com/xiaoxiaoxiaotao/novel-bot
