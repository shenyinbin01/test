# 长篇叙事生产系统第二轮深度研究报告

## 执行摘要

这套“长篇叙事生产系统”值得继续，但**不应该按“IP 宇宙先行、然后一路向下流水线式地做完”**。更合理的判断是：它已经找到了正确的问题——长篇失真通常不是句子不通，而是**车架缺失**，也就是卷目标、章节导航、状态继承、读者债、关系债、知识分布、后果余波没有被工程化管理；但它现在最危险的地方也正是这里——如果把这些问题误解成“多填几层表”或“上完整多 agent”，系统会非常快地滑向**伪控制感、重型官僚 prompt、昂贵但不好看的日志系统**。citeturn18view0turn32view0turn30view0turn28view0turn29view1turn46search8turn46search17turn46search20

我对你的新构想的总判断是：**方向对，排序要改，层次要重排，IP 宇宙要降级，状态回写要前移，故事调度器要做成“边界管理者”而不是“隐藏作者”**。项目当前仓库已经有章节级前向链路和写后回写：Planner 产出 beat，Writer 写稿，Reviewer 审稿，Polisher 轻增强，StateManager 再把 accepted 结果写回 runtime canon 和 reader debts；Phase 8 也已经明确“整本书是最小有效认知单位”“Polisher 不是救稿角色”“多书技法库必须分层”。这说明项目已经具备走向长篇系统的基础，但现有 `chapter_beat`、`chapter_commit`、`runtime_canon` 结构仍然太粗，无法承载真正的卷—章—场景连续控制。citeturn18view0turn19view0turn30view0turn28view0turn29view1turn45view0

最大机会不在“把 Writer 再训得更会写”，也不在“立刻做完整 IP 宇宙”，而在**把单书级承诺、卷级推进、章节卡、场景行动包、状态增量和偏航检测接成闭环**。最大风险则是：**你以为自己在做长篇控制，实际上只是在堆一个更复杂的大纲模板机**；或者反过来，**你以为自己在做角色主动感，实际上只是把主线控制交给了成本极高的自由涌现系统**。互动叙事和 drama management 研究早就反复证明，强自治角色和好故事不是同一件事；真正可用的系统通常都在“强情节控制”和“强角色自治”之间，加入一个经验管理层或故事调度层。citeturn44search2turn37search1turn44search18turn37search4turn37search16

因此，最该先验证的不是“1 卷 10 章”，更不是“多书 IP 宇宙工程”，而是一个**单书故事骨架 + 1 个卷卡 + 3 个连续 chapter cards + state delta 写回 + Story Orchestrator Lite** 的最小实验。这个实验已经足够暴露长篇系统最关键的问题：主线偏航、关系债蒸发、知识状态错乱、卷目标断裂、爽点兑现机械化，以及“章节单看都还行，连起来死掉”的典型失败。citeturn34view0turn45view0turn46search19turn41search19

## 资料依据与长篇生产架构总评

### 资料依据与局限

你指定的 `planning/deep-research-github-entry-v0` 入口页分支未能直接读取到，因此本报告没有按那一份入口包顺序继续下钻；项目侧证据主要来自当前公开 `main` 分支中可读取的相关文档，以及你在本轮问题中给出的第一轮 Deep Research 总结。我把你给出的第一轮结论视为**项目当前假设**，而不是外部研究结论；凡是下文被当作“外部支持”的部分，均以仓库文档或外部资料单独引用。

当前可读仓库里，最关键的项目依据包括：Phase 7 多角色创作链路、Phase 6A StateManager 结果、Phase 8 单书闭环与 lessons learned、Human Texture 研究包与嵌入方案、Work Voice 研究包与 summary，以及现有 `chapter_beat`、`chapter_commit`、`runtime_canon` schema。它们已经足够让我判断：项目已经从“只会写一章”进到了“知道要管状态”的阶段，但还没进入真正的“长篇运行时系统”阶段。citeturn18view0turn19view0turn32view0turn45view0turn22view0turn26view0turn31view0turn30view0turn28view0turn29view1

### 当前仓库已经做到哪里

仓库当前的正式主链并不是自由式 agent 创作，而是一条**强门禁的章节流水线**：Planner → Writer → 句式节奏分析 → AI 味检测 → Reviewer → Polisher → StateManager → WPS Sync；其中 Hermes 在每一步验收，失败则停止或回退。这个设计在工程上是清醒的，因为它承认“正文生成”只是中段，不是闭环终点。citeturn18view0

更重要的是，StateManager 已经不是摆设：仓库文档明确写到它会在 accepted commit 后更新 `runtime_canon`、`reader_debts`、`.webnovel/state.yaml`、projection 和 audit log。与此同时，Human Texture 的集成方案已经提出**Relationship Debt Ledger** 和 **Consequence Ledger**，并强调“每个低分项必须退回对应层修，不许把结构空洞丢给 Polisher 硬救”。这说明项目实际上已经摸到了长篇系统的两个关键方向：**状态继承**和**责任分层**。citeturn18view0turn19view0turn26view0

但这套基础设施还停在“章节文件回写”层，不是“长篇叙事控制”层。当前 `chapter_beat` 只要求场景序号、叙事功能、POV、目标情绪、冲突类型、对话占比、关键台词和章尾钩子；当前 `chapter_commit` 只记录 plot events、character updates、world updates、dialogue signatures 和 affected elements；当前 `runtime_canon` 只包含 timeline、character states 和 active threads。对单章管理来说，这些字段够用；对三章连续以上的长篇控制来说，它们明显缺少**谁知道什么、谁欠谁什么、资源如何继承、声誉如何变化、本卷目标推进到哪、哪些读者债已经过期**等关键对象。citeturn30view0turn28view0turn29view1

### 对新构想的总判断

你的“IP 宇宙 → 单书故事 → 卷 → 章 → 场景 → 发动机 → 正文 → 状态回写”的方向是成立的，但**它不应该被实现成一条单向瀑布流**。更准确的形态应该是：**资产层、导航层、运行时层、持久化层和治理层组成一个有反馈的图结构**。否则会出现两个典型误区：一是把上层做成越来越厚的大纲表格，压死角色主动感；二是把下层做成越来越自由的 agent 运行，最后得到成本很高但失去故事力度的 event log。互动叙事领域对“强情节控制—强角色自治”之间张力的总结，正好说明这不是一个可以靠单层解决的问题。citeturn44search18turn44search2turn37search5

我对各层的判断如下。表中的结论是我的综合推理建议，依据来自仓库现状与外部方法对标。

| 层 | 我的判断 | 当前主要问题 | 处理建议 |
|---|---|---|---|
| IP 宇宙层 (IP Universe Layer，跨书复用的世界资源池) | **保留，但降级为可选冷层** | 很容易在前期变成设定堆砌和资产幻觉 | 先做 `world_slice`，不要让整套系统依赖完整宇宙才能启动 |
| 单书故事层 (Book Spine Layer，一本书的核心承诺与冲突) | **最高优先级** | 目前仓库更强的是 chapter beat，不是 book promise | 先固化整书一句话、反力量、终局方向、转变类型 |
| 卷结构层 (Volume Structure Layer，阶段性推进与兑现) | **必要** | 最容易退化成“升级表” | 加卷目标、卷反力、卷中点翻面、卷尾欠账/兑现窗口 |
| 章节链层 (Chapter Navigation Layer，章节导航与承诺) | **必要，但必须升级** | `chapter_one_sentence` 不够 | 用 `chapter_card` 管前后状态、读者债、卷链接、允许偏差 |
| 场景发动机层 (Scene Causality Layer，角色在局面里的因果行动) | **必要** | 无边界就会跑飞；边界太硬又会木偶化 | 用 scene agency packet + allowed divergence band |
| 正文渲染层 (Narrative Rendering Layer，把事件讲成正文) | **必要，但从属** | 最容易越权“替角色补动机” | 只负责讲述与信息分配，不负责改因果决定 |
| 状态回写层 (State Persistence Layer，把变化写回系统) | **必须前移** | 现有 schema 粗而泛 | 改成 `state_delta` + reducers + 多账本物化视图 |

### 最核心的批判

如果只允许我挑一个最大概念错误，我会说：**把 IP 宇宙放在热路径入口，是目前这套长篇构想里最容易把项目拖慢的设计。** Phase 8 自己的下一阶段建议，优先级其实也是“新书拆解流水线产品化”和“第二本书验证”，而不是先做一个全能的跨书宇宙总控层；同时它还明确要求多书技法库分层，避免每拆一本到处直接改 Skill Pack。换成正向生产系统，这个逻辑同样成立：在没有证明“单书—卷—章—状态继承”的 forward loop 稳定之前，先做 IP 宇宙，只会把**资产管理问题**提前到**叙事控制问题**之前。citeturn34view0turn45view0

## 与外部方法的对标

### 顶层写作法、连载实践与游戏叙事能借什么

下面这张表给出的是**可借鉴部分**与**不能照搬部分**。表内“不能照搬”的部分很重要，因为你这个项目最危险的失败方式，不是缺理论，而是把异领域的方法机械移植成更复杂的模板机。

| 外部方法 | 可借鉴什么 | 不能照搬什么 | 对本项目最有用的层 | 来源 |
|---|---|---|---|---|
| 雪花写作法 (Snowflake Method，一句话逐层扩展成更细设计) | 适合把“整书一句话 → 段落摘要 → 人物 → 场景列表”做成**单书故事层**与**卷层**的递进展开 | 它解决的是规划展开，不解决运行时状态继承和写后回写 | 单书故事层、卷结构层 | citeturn35search0 |
| 三幕式 / 英雄旅程 / 救猫咪 (Three-Act Structure / Hero’s Journey / Save the Cat，宏观节奏与转折钉子) | 适合给整书和卷提供**承诺、翻面、高潮、回报**的宏观节奏检查 | 这类方法偏电影与单体作品，直接下沉到网文章节会过硬、过匀、过公式化 | 单书故事层、卷结构层 | citeturn35search3turn35search1turn36search6 |
| Story Grid（以 story grid 方式检查故事单位与起草流程） | 它很适合把“写作方法”翻成“可检查的单元合同”，尤其适合章节卡与 reviewer gate | 它不是运行时引擎，也不会自动给你角色主动感 | 章节链层、评价治理层 | citeturn35search2turn35search6 |
| 编剧室流程 (Writers’ Room，协作拆季拆集的房间式开发) | 最值得借的是“房间文档”：season/episode 级目标、角色 spotlight、揭示顺序、连续性讨论 | 人类编剧室有大量口头 tacit knowledge，不能假装几份 YAML 就等于 writers’ room | 卷结构层、章节链层、故事调度层 | citeturn36search11 |
| 连载小说规划 (Serial Fiction Planning，以场景—章节—弧线分块推进连载) | 场景是基本单位、章节和 plot arc 是上层嵌套，这一观察非常适合你的“章—场景—状态回写”体系 | 连载经验往往靠作者直觉和读者互动回调，不能直接程序化成静态模板 | 章节链层、场景发动机层 | citeturn36search8 |
| 任务链与跑团战役思维 (Quest / Campaign Thinking，以局部任务嵌套阶段目标) | 很适合借“局部目标—阻碍—失败后转向—下一任务 seed”的链式设计思维 | 游戏任务面向玩家选择，小说面向被设计的阅读体验；不能把章节写成任务清单 | 卷结构层、章节链层、场景发动机层 | citeturn43search1turn36search8 |
| 故事圣经 / 设定词典 / Lorebook / Codex（按需检索的世界与角色资料） | 非常适合做 `world_slice`、`series_codex`、按需上下文注入，而不是全量长上下文灌入 | Lorebook 只是检索容器，不是故事调度器，更不等于连续性本身 | 资产层、状态检索层 | citeturn41search4turn41search5turn41search13turn41search0 |
| Plan-and-Write / Dramatron（先有结构再扩写的层级生成） | 强烈支持你做“书 → 卷 → 章 → 场景”的**层级正向生成**，而不是直接从 premise 写正文 | 层级生成能提升一致性，但不自动解决读者债与关系债继承 | 单书故事层、卷结构层、章节链层 | citeturn46search19turn41search19turn41search3 |
| 涌现叙事 (Emergent Narrative，由自主体互动生成故事) | 支持“角色运行后再渲染”的研究方向；也提醒你角色行为可以是故事素材来源 | 研究界一直承认它在作者控制上技术与概念上都很难，不能直接拿来接管生产主链 | 场景发动机研究轨道 | citeturn37search4turn37search16 |
| 戏剧管理 / 自动故事导演 (Drama Management / Automated Story Director，在不完全剥夺行动自由的前提下导向更好的故事体验) | 这正是 Story Orchestrator 的最强参照：它控制**目标体验与约束**，而不是替角色讲台词 | 不要把它做成“暗箱作者”，否则角色主动感会被吃掉 | 故事调度层 | citeturn44search2turn37search1turn44search18 |
| AI Director（像 Left 4 Dead 那样在预设可能空间内动态调度） | 很适合借“**作者先给可能空间，调度器再做动态选取**”的思想；这比纯自由涌现更可控 | 它管理的是强度、节奏和资源分布，不是文学文本本身 | 故事调度层、节奏治理层 | citeturn37search2turn37search10 |
| 开源 AI 写作引擎（NovelGenerator、knowrite、novel-bot） | 说明行业已经在摸索 autonomy、memory、truth DB、filesystem memory 等结构 | 这些项目大多展示“能跑通自动链路”，不等于“能跑出你要的长篇质量”；不要把“自动化程度”误当成“叙事质量” | 工程参照层 | citeturn42search0turn44search9turn42search2 |

### 读者理论、叙述理论与长篇控制的关系

叙述理论最能给你帮助的地方，不是“风格多高级”，而是**把讲述的控制点说清楚**。Living Handbook of Narratology 对**聚焦 (Focalization，叙事信息经由谁的经验被限制与分配)** 和 **隐含读者 (Implied Reader，文本预设的接收位置与理解路径)** 的界定，正好说明：Renderer 不是纯“润色器”，它实际上在控制**谁先知道、谁后知道、读者与讲述者之间保持什么距离**。因此，Renderer 在你的系统里应该从属于“叙述合同层”，而不是被当作最后的文风包装器。citeturn38search2turn40search6turn31view0

读者侧理论也同样关键。交通沉浸 (Transportation，读者被卷入叙事世界的吸收状态) 研究强调，沉浸不是“多写心理”这么简单，它涉及注意力集中、情绪参与和意象建构；叙事参与 (Narrative Engagement，读者在理解、情感、在场感上的组合性参与) 研究则把它拆成可以测量的维度。与此同时，叙事张力研究指出，好看的故事不是只靠 surprise，**curiosity、suspense、retrospection** 在阅读推进中一起工作。换成工程语言，就是：**Reader Immersion 不应该先做 Writer patch，而应该进入 chapter card 的 reader-question 字段、payoff 窗口、信息揭示顺序和 reviewer gate**。citeturn38search12turn38search1turn39search1turn39search4turn39search8

### 为什么这会推翻一部分直觉

这轮最重要的外部对标结论其实很简单：**长篇系统真正需要的不是“更大上下文”，而是“更可审计的层级展开 + 更可追责的状态继承 + 更克制的动态调度”。** 一方面，LongWriter、LongGenBench、NovelQA 等研究都说明，长上下文模型依然会在超长生成、复杂指令遵循、100K 级细节理解和多跳推理上暴露明显短板；另一方面，Dramatron、Plan-and-Write、Automated Story Director 这一路的方法都在提醒，真正能工作的往往是**分层生成和中间管理层**，不是一口气生成，也不是纯自由 agent。citeturn46search8turn46search20turn46search17turn41search19turn46search19turn44search2

## 推荐的系统重组

### 我建议的长篇分层

我建议把你的长篇系统重组为下面六层，而不是把 IP 宇宙放在整条热路径的入口。

```text
可选冷层
  IP Universe
    └─ Series Codex / World Asset Pool

热路径入口
  World Slice
    └─ Book Spine
        └─ Volume Cards
            └─ Chapter Cards
                └─ Scene Agency Packets
                    └─ Event Log
                        └─ Narrative Renderer
                            └─ State Delta
                                └─ Ledger Reducers / Drift Gates
                                    └─ Next Chapter Retrieval
```

这个重排的核心含义是：**IP 宇宙是冷层资产，不是热层入口；单书故事才是热启动入口。** 这样才能避免“先修一个巨大的世界数据库，再发现三章连续都跑不稳”的常见项目性浪费。项目自己的 Phase 8 文档已经把“整本书视角”“多书分层技法库”“不直接全量注入 Skill Pack”写得很清楚，所以把 IP 宇宙降级为可选冷层，其实不是否定项目，而是顺着仓库现有治理逻辑把它推到更合理的位置。citeturn32view0turn34view0turn45view0

### 各层的职责边界

我建议各层这样定义。

| 层 | 对象性质 | 应该负责什么 | 不该负责什么 |
|---|---|---|---|
| 资产层 (Asset Layer，储存可复用世界与系列材料) | 冷数据 | 世界规则、势力、制度、历史、禁忌、系列共用角色与事件摘要 | 指挥当前章节怎么写 |
| 单书脊梁层 (Book Spine Layer，一本书的主承诺) | 热规划 | 整书一句话、主对抗线、终局方向、类型承诺、核心转变 | 具体场景动作 |
| 卷与章节导航层 (Volume / Chapter Navigation Layer，阶段推进与章节承诺) | 热规划 | 卷目标、卷反力、章节功能、章节前后状态、reader debt 变化窗口 | 具体措辞和微动作 |
| 场景因果层 (Scene Causality Layer，角色在局面中行动的层) | 运行时 | 角色目标、判断、选项、战术、盲点、行动结果、下一摩擦 | 文风、叙述距离 |
| 叙述合同层 (Narrative Contract Layer，事件如何被讲述) | 运行时 | Work Voice、聚焦、叙述距离、Human Texture 槽位、信息分配 | 改写既定因果 |
| 持久化与治理层 (Persistence & Governance Layer，写回、检测、门禁) | 审核/记忆 | state delta、账本物化、偏航检测、反套路 gate、Polisher 边界 | 代替创作层做美学决定 |

### `chapter_one_sentence` 为什么不够

“每章一句话”很有用，但它只解决了**方向**，没有解决**约束**。它适合用作导航锚点，不适合单独充当 chapter chain 的主合同。仓库现有 `chapter_beat` 已经证明了这一点：只有场景功能、POV 和情绪目标时，系统仍然不知道这一章**具体必须推进哪笔卷级承诺、必须继承哪笔旧债、结束后哪些状态必须改变**。citeturn30view0

因此，我建议把 `chapter_one_sentence` 保留为卡片顶部字段，但真正可执行的是 `chapter_card`。下面这组字段是我建议的最小可执行版本。

| 字段 | 用途 | 类型建议 |
|---|---|---|
| `chapter_one_sentence` | 一句导航锚点，防止跑偏 | 必填 |
| `volume_goal_link` | 这章服务哪个卷目标 | 必填 |
| `plot_function` | 推进、反转、对价、兑现、埋伏、缓冲、收束中的哪一种 | 必填 |
| `required_conflict` | 这章必须发生的冲突类型与对象 | 必填 |
| `required_reveal` | 本章必须揭示什么，或者必须不揭示什么 | 必填 |
| `required_payoff_or_debt` | 本章要兑现哪笔旧债，或新增哪笔新债 | 必填 |
| `character_state_before` | 主角与关键角色进入本章前的状态摘要 | 必填 |
| `character_state_after` | 本章结束后必须形成的状态变化 | 必填 |
| `relationship_pressure_change` | 哪条关系债被加压、缓和、冻结或转向 | 必填 |
| `knowledge_state_change` | 谁新增知道、误知道、被隐瞒了什么 | 必填 |
| `resource_or_status_change` | 资源、名望、身份、限制的变化 | 重要 |
| `reader_question_before` | 读者带着什么问题进入本章 | 必填 |
| `reader_question_after` | 本章结束时读者应带走什么新问题或新判断 | 必填 |
| `spotlight_targets` | 本章谁必须占前景，谁只能侧身出现 | 重要 |
| `allowed_divergence_band` | 场景发动机可以自由发挥到什么程度 | 必填 |
| `must_not_happen` | 本章绝对不能破坏的 canon、节奏或曝光顺序 | 必填 |
| `next_chapter_seed` | 下一章的起动种子，不是 hook 文案，而是因果种子 | 必填 |

关键点在于：**章节卡写的是“状态变化合同”，不是“剧情摘要扩写版”。** 这也是我为什么认为你这轮思路里真正有价值的部分，不是“层数变多了”，而是开始把章节理解成**一个可检查的变化单元**。这和 Story Grid、Plan-and-Write、Dramatron 之类方法最值得借的地方是一致的。citeturn35search2turn46search19turn41search19

### 你现有几个核心模块在长篇车架里的落点

人物质感 (Human Texture，人物在关系、私心、阻力和后果中呈现出来的场景质感) 不该单飞成“独立大坝”，它应该落在**场景因果层**和**叙述合同层**之间：一部分是 scene packet 的输入，一部分是 renderer 的讲述约束，一部分通过关系债与后果账本跨章继承。仓库里的 Human Texture 集成方案已经是往这个方向走的。citeturn26view0turn22view0

作品声音 / 作者站位 (Work Voice / Narrative Stance，讲述者稳定地站在哪里讲话) 则应是**叙述合同层**的一部分，而不是主导长篇规划的上游总控。Work Voice 研究包本身也已经明确，它解决的是“讲故事的人是否稳定存在”，不是“人物有没有人味”。所以我建议在长篇车架里：**先把它做成 renderer contract + reviewer gate，不要让它直接主导 scene planning**。citeturn31view0

角色主动感 / 行动主权 (Character Agency，角色如何按自己的判断在局面里选择) 则是长篇系统里最需要放在**场景因果层**的东西。它不是“主角永远主动”，而是**每个关键转折都要能回溯到角色在局面中的选择、误判与代价**。单章里它提升活性，长篇里它最大的价值是防止章节只在执行大纲。你第一轮把它前移，我认为是对的；第二轮应该继续前移，但要加上章节卡和卷目标边界。

读者代入感 / 读者解压 (Reader Immersion，给读者留下判断、期待和情绪参与空间) 在长篇系统里不应先做成 Writer patch，而应落在**章节卡字段 + 读者问题账本 + reviewer gate**。此前 Human Texture 和 Work Voice 文档都已经隐含了一个结论：**早期让 Writer 直接“替读者设计感觉”很容易变成说教或过度解释**。外部的 transportation、narrative engagement、reader-response 理论也支持这一点。citeturn26view0turn31view0turn38search12turn38search1turn40search1

## 状态账本与运行时设计

### 我建议的总原则是 Delta First

如果你真的去做账本，我最强烈的建议不是“多建几个 YAML”，而是**先把写回对象改成 `state_delta`，再用 reducer 生成各账本的 current view**。

原因很简单。当前仓库虽然已经有 `chapter_commit`、`runtime_canon` 和 `reader_debts`，但它们还是偏“章节总结文件”思路。长篇系统真正需要的是：

- 先有**章节接受后的增量事实**；
- 每条增量都带**来源 chapter / scene / evidence**；
- 然后由 reducer 更新 plot、character、relationship、knowledge 等物化视图；
- 再由下一章检索器按需取热上下文。citeturn18view0turn19view0turn28view0turn29view1

这样做有三个好处。第一，它让“自动回写错误”更容易追责；第二，它避免每个 agent 直接改一堆总表而把系统写乱；第三，它能天然支持审计日志、回滚和 drift detection。考虑到 NovelQA 和 LongGenBench 这类研究都显示模型在超长细节保持上仍不可靠，**你不应该把长篇连续性寄托给一个越来越大的 summary 文件**。citeturn46search17turn46search20

### 建议账本结构

下面这张表是我建议的账本设计。为了回应你的问题，我把你点名的九类都列出来，并明确哪些属于 MVP 必需，哪些应该延后。

| 账本 | 核心字段 | 谁写入 | 谁读取 | 更新时间 | 不维护会怎样 | MVP 是否必需 |
|---|---|---|---|---|---|---|
| 剧情账本 (Plot Thread Ledger，主线与支线的线程状态) | `thread_id`、`scope`、`status`、`last_turn`、`next_obligation`、`antagonistic_force` | StateManager reducer | Orchestrator、Planner Lite、Reviewer | 每章 accepted 后 | 主线偏航、支线消失、重复铺垫 | 是 |
| 角色状态账本 (Character State Ledger，角色当前外部状态与内部压力) | `character_id`、`current_goal`、`current_strategy`、`pressure`、`blindspot`、`wounds_or_fatigue`、`unresolved_cost` | Scene engine propose，StateManager accept | Orchestrator、Renderer、Reviewer | 每章 accepted 后；必要时场景内暂存 | 主角像重置，配角动机漂移 | 是 |
| 关系债账本 (Relationship Debt Ledger，谁欠谁、误会谁、躲谁、拖累谁) | `pair_or_group_id`、`debt_type`、`debtor`、`creditor`、`visibility`、`temperature`、`next_manifestation` | Reviewer/StateManager | Chapter planner、Renderer、Reviewer | 每章 accepted 后 | 关系蒸发、情感线断裂、配角成工具件 | 是 |
| 资源账本 (Resource Ledger，钱、时间、物品、权限、体力等可耗资源) | `resource_id`、`owner`、`delta`、`scarcity_level`、`deadline` | StateManager | Orchestrator、Scene engine | 每章 accepted 后 | 资源前后不一致、代价无继承 | 类型相关；建议做 |
| 信息账本 (Knowledge Ledger，谁知道什么、误知道什么、被瞒着什么) | `fact_id`、`known_by`、`believed_by`、`withheld_from`、`reliability`、`reveal_status` | Scene engine propose，StateManager accept | Renderer、Orchestrator、Reviewer | 每章 accepted 后 | 信息状态混乱、反转失效、剧透顺序错位 | 是 |
| 声誉 / 身份账本 (Reputation / Identity Ledger，外界如何认知这个人) | `identity_claim`、`public_status`、`trust_map`、`institutional_restriction` | StateManager | Orchestrator、Renderer | 每章 accepted 后 | 名声变化不继承、身份冲突不成立 | 视题材而定；建议做 |
| 伏笔 / 回收账本 (Foreshadow / Payoff Ledger，线索与兑现窗口) | `setup_id`、`setup_chapter`、`expected_window`、`payoff_status`、`delay_reason` | Planner、Reviewer、StateManager | Orchestrator、Reviewer | 章前计划 + 章后更新 | 伏笔遗忘、兑现机械、回收失约 | 是 |
| 读者问题账本 (Reader Question Ledger，读者当前被吊着的问题与判断空间) | `question_id`、`opened_at`、`intensity`、`expected_payoff_window`、`last_refresh` | Planner + Reviewer | Orchestrator、chapter planner | 章前设定、章后修正 | 读者期待断裂、只剩事件没有牵引 | 是 |
| 卷目标进度账本 (Volume Progress Ledger，当前卷的承诺推进度) | `volume_id`、`goal_state`、`antagonism_stage`、`midpoint_state`、`distance_to_climax` | Orchestrator + StateManager | Orchestrator、Reviewer | 每章 accepted 后 | 卷目标断裂、卷尾像拼出来的 | 是 |

### Story Orchestrator 应该做什么

故事调度器 (Story Orchestrator，负责全局叙事边界管理的中层控制器) **是必要的**，但它不应该是“另一个 Writer”。它最合理的身份，是互动叙事里的 drama manager、Automated Story Director，和 Left 4 Dead 那种 AI Director 的混合体：**不是代替角色做事，而是管理允许空间、推进窗口和体验节奏。**citeturn44search2turn37search1turn37search10

我建议它的职责边界如下。

| Story Orchestrator 应做 | Story Orchestrator 不应做 |
|---|---|
| 绑定卷目标、章节卡和当前账本，生成下一章的场景任务包 | 直接写正文 |
| 决定哪些 reader debt 必须刷新，哪些可以延迟 | 直接给角色写内心独白 |
| 控制 spotlight 预算，避免配角抢戏或被消失 | 决定具体句法、比喻和修辞 |
| 约束 reveal 顺序、高潮窗口、hook 延迟 | 临场改写已 accepted 的因果结果 |
| 判断 scene outcome 是否仍在 `allowed_divergence_band` 内 | 越过 reviewer 直接更新 canon |
| 在偏航时触发局部 replan，而不是强行继续 | 把每个场景变成机械的任务清单 |

这意味着 Orchestrator 的输出，不应该是“下一章正文 prompt”，而应该是：

- 当前卷的推进约束；
- 下一章 `chapter_card`；
- 每个关键 scene 的 `scene_agency_packet`；
- 允许偏差带；
- 必须回收与禁止破坏项；
- 读者问题刷新计划；
- 写后验收检查表。

这样做的好处是：**它控制主线，不压死角色。**

### 如何避免它压死角色主动感

这里最重要的不是“少控制”，而是**控制正确的东西**。
我建议你把章节级控制拆成三层：

- **硬约束 (Hard Constraints，绝不能破坏的边界)**：canon 一致性、卷目标窗口、必须延迟的真相、不可越过的角色底线、禁止的 narrator 抢戏。
- **软约束 (Soft Constraints，优先满足但可替代的规划)**：希望在哪一章刷新哪笔 reader debt，希望谁占 spotlight，希望本章转折偏向外部冲突还是内部误判。
- **自由区 (Free Play Zone，允许角色凭局面出招的部分)**：具体战术、误判形式、谁多说一句、谁先发现异常、行动如何失败。

这跟 Riedl 与 Stern 所说的“不是强故事，也不是强自治，而是在中间做 narrative control”的思路是一致的。角色主动感真正需要的不是“没人管”，而是**角色在硬边界内对战术路径有真实选择权**。citeturn44search2turn44search18

### Narrative Renderer 应该做什么

正文渲染器 (Narrative Renderer，把事件、状态和叙述合同转成正文的模块) 的定义也要更严格。它不该是“最后一个大模型，顺手把所有前面没解决的问题都补掉”。正相反，项目自己的 Phase 8 和 Human Texture 文档都已经证明：**晚层修补结构，是错位劳动**。citeturn45view0turn26view0

我建议 Renderer 的职责边界如下：

| Renderer 读什么 | Renderer 写什么 | Renderer 不能改什么 |
|---|---|---|
| `chapter_card` | 正文 draft | 角色行动结果 |
| `scene_agency_packets` | 段落级叙述分配 | 谁知道什么 |
| `event_log` | focalization / distance 的具体落点 | 资源与关系账本事实 |
| `human_texture_packet` | 信息露出顺序 | 已 accepted 的卷目标与章节合同 |
| `voice_contract` | 微动作、活人浅痕、余味位置 | 叙述外的因果补洞 |
| 当前热账本切片 | render report：暴露哪些结构问题 | reviewer gate 结论 |

如果 Renderer 发现 event log 不好看，它不应该偷偷修改角色行动，而应该返回一个**render blocker**。我建议 blocker 至少分五种：

- `causal_thinness`：事件成立，但因果过薄；
- `embodied_consequence_missing`：发生了事，但后果没有落到身体、关系或资源上；
- `focalization_breach`：叙述越权，知道了不该知道的事；
- `exposition_clump`：信息堆在一起，失去读者参与空间；
- `spotlight_imbalance`：人物前景/背景调度失衡。

然后它把问题退回给 Orchestrator 或 scene engine，而不是自己硬救。Renderer 的真正高级之处，不是越权，而是**知道什么时候不能越权**。Living Handbook 对 focalization 与 implied reader 的界定，正好支持这种边界。citeturn38search2turn40search6

### 长篇偏航检测应该怎么做

偏航检测 (Drift Detection，发现长篇在连续生成中偏离承诺的机制) 不应只靠“读起来怪不怪”。我建议至少做八类检测。

| 偏航类型 | 检测方法 | 常见成因 | 响应方式 |
|---|---|---|---|
| 主线偏航 | 检查章节 delta 是否推进了本卷或整书主线程 | scene 漂亮但不服务主线 | Orchestrator 重写 chapter card |
| 卷目标偏航 | 连续 N 章未缩短 `distance_to_climax` 或未改变卷级冲突态 | 章节被局部爽点绑架 | 卷层 replan |
| 角色动机漂移 | 当前目标/策略变化没有对应原因 delta | Writer 或 renderer 自行补动机 | 退回角色状态账本与 scene packet |
| 信息状态错乱 | 两个章节对同一 `fact_id` 的 `known_by` / `reveal_status` 冲突 | 回写粗糙、summary 幻觉 | 阻塞合并，人工校正 |
| 伏笔遗忘 | `expected_window` 超期无 payoff 或无延期理由 | 只顾开坑不管旧债 | 强制 chapter card 优先回收 |
| 关系债蒸发 | 相关角色再次同场时 debt 不体现且无解释 | 章节局部写得好，跨章没继承 | 退回关系债账本 |
| 世界规则冲突 | 事件与 `world_slice` / 规则表不一致且无 exception entry | 设定热启动不完整 | world exception 审核 |
| 读者期待断裂 | 读者问题账本开坑过多、刷新过少、问题类型重复 | 章节钩子工厂化 | 压缩新坑，优先兑现旧债 |

这些检测要分层做。**自动检查**负责 schema、冲突、超期、未读条目；**人工审**负责角色活性、爽点机械感、讲述者抢戏、读者参与空间被解释掉等更含审美判断的东西。近期关于创意写作评估的研究本身也说明，LLM evaluator 是在探索中的工具，不适合做唯一裁判，所以这里不应迷信“全自动审”。citeturn46search14

## 最小长篇 MVP 与反低质约束

### 最小长篇 MVP 应该选哪一个

如果只能推荐一个最小可验证方案，我明确推荐：

**单书故事 + 1 个卷卡 + 3 个连续 chapter cards + per-chapter state delta + Story Orchestrator Lite。**

也就是你列的几个候选里，最接近“**1 本书 + 1 卷 + 3 章连续**”，但我会把 IP 宇宙砍成一个极薄的 `world_slice`，而不是完整宇宙工程。

原因如下。

| 方案 | 能验证什么 | 最大盲点 | 结论 |
|---|---|---|---|
| 1 卷 10 章 | 能看到卷级节奏、疲劳与注水风险 | 成本太高，失败后难定位根因 | 先不要做 |
| 3 章连续 | 能测试状态继承、reader debt 连续、关系债和主线偏航 | 还看不到完整卷尾 | **最优先** |
| 1 章多场景 | 能测试 scene engine 局部有效性 | 看不到跨章连续性 | 作为前置微实验可以做 |
| 1 个卷大纲 + 5 个 chapter cards | 能测试规划质量 | 没有正文和写后回写 | 只能做 preflight |
| 1 个 IP 宇宙 + 1 本书 + 1 卷 + 3 章 | 能测试层次齐不齐 | IP 资产噪音太大，容易误判系统成败 | 第二阶段再做 |

为什么是 3 章，不是 1 章，也不是 10 章？因为长篇真正致命的错误，大多发生在**章节边界**：第一章立得住，第二章开始忘，第三章开始漂。三章已经足够暴露这些问题，但还没贵到无法迭代。citeturn46search8turn46search17turn18view0

### 推荐的最小实验设计

我建议你用同一套输入做三组对照，但实验范围只限 3 章连续。

| 项目 | 设计 |
|---|---|
| 实验目标 | 验证“章节卡 + 状态回写 + Orchestrator Lite”是否能显著提升三章连续的主线稳定、角色连续性和读者债继承 |
| 输入 | `single_book_story`、`world_slice`、cast roster、1 个 `volume_card`、3 个 `chapter_seeds` |
| 对照组 A | 现有链路：仅基于当前 `chapter_beat` 逐章生成，靠 `runtime_canon` 和 `reader_debts` 粗回写 |
| 实验组 B | A + 升级后的 `chapter_card` + `state_delta` + 多账本 reducers，不做 scene agency packet |
| 实验组 C | B + `scene_agency_packet` + Story Orchestrator Lite + render blocker 回退机制 |
| 中间产物 | `volume_card`、3 个 `chapter_card`、scene packets、event logs、3 份 `state_delta`、9 类账本视图、drift report |
| 输出 | 3 章正文、账本快照、偏航检测报告、人审评分、自动冲突报告 |
| 评价指标 | 连续性、角色动机稳定、后果继承、读者问题连续、关系债可感、爽点是否机械、hook/payoff 平衡、文本偏好 |
| 通过标准 | B 或 C 相对 A，在“连续性”“后果继承”“reader debt 记忆”“主线稳定”四项上人审平均提升至少 1 分；硬性 canon 冲突率低于 5%；三章内至少 70% 的旧债被刷新或明确延期 |
| 失败信号 | 章节单看更工整，但读起来更像工程产物；账本正确但正文无生气；scene log 很丰富但主线更散；自动回写与正文相互矛盾 |
| 为什么足够小 | 它已经跨过两个章节边界，能测连续性；同时只做一个卷切片，不会被完整长篇成本吞掉 |

### 评价指标应该怎么落地

我建议把评价维度拆成“硬性”“半硬性”和“审美性”三类。

| 维度 | 类型 | 测法 |
|---|---|---|
| canon 冲突率 | 硬性 | 自动检测 |
| 信息状态一致性 | 硬性 | 自动检测 + reviewer spot check |
| 卷目标推进度 | 半硬性 | volume progress 账本 + reviewer |
| 关系债继承率 | 半硬性 | relationship ledger 与正文证据交叉 |
| 读者问题连续性 | 半硬性 | reader question ledger + 人审 |
| 角色主动感可追溯性 | 半硬性 | scene packet 是否存在明确选项、代价、盲点 |
| 爽点机械感 | 审美性 | 人审 rubric |
| 讲述者抢戏程度 | 审美性 | 人审 rubric |
| 文本活性与现场感 | 审美性 | 双盲偏好测试 |

### 反低质投喂 / 反预制菜 gate

你这套系统要想不滑成“更高级的套路生成器”，必须把反套路做成**结构 gate**，而不是价值观口号。仓库 Phase 8 已经建立了一些很好的治理基础：Writer 不接触原文，candidate 技法不能直接注入，Polisher 不能救结构，多书技法必须分层，最小注入优于全量塞卡。这些原则应该直接继承到长篇系统。citeturn32view0turn45view0

在此基础上，我建议新增下面这些 gate：

| Gate | 阻塞条件 | 目的 |
|---|---|---|
| 章节空推进 gate | 本章新增大量 setup，但没有改变任何既有状态 | 防止注水 |
| 钩子工厂 gate | 连续两章只制造新 hook，不刷新旧 `reader_question` | 防止“吊着不给” |
| 免费爽点 gate | 重大胜利没有资源、关系、声誉或信息代价 | 防止机械爽文糖水化 |
| Narrator 抢戏 gate | 叙述者直接替读者下判断、讲道理、总结主题，而非经由场景与角色显现 | 防止“老灯说教” |
| 关系蒸发 gate | 关键关系债在相关角色再相遇时无任何体现 | 防止人物只为剧情服务 |
| 设定膨胀 gate | 新增设定条目数显著高于有效状态变化数 | 防止设定堆砌机 |
| Spotlight 失衡 gate | 配角连续抢走主角关键承担，或相反连续沦为工具人 | 防止戏份结构失真 |
| 重复骨架 gate | 近三章 `plot_function + hook_type + payoff_type` 明显重复 | 防止模板循环 |
| Polisher 越权 gate | Polisher 试图补动机、补主线、重排 reveal | 防止后置假修复 |
| 账本虚构 gate | 写回账本中出现正文没有证据的变化 | 防止状态系统自说自话 |

“工程化厨房”真正该追求的，不是每章都稳定产出“像网文的东西”，而是：**每章都能被追问：这次爽点是谁争来的、付了什么、留下了什么、下一章为什么必须继续。** 如果这几个问题追不下去，再漂亮的 YAML 都会把系统推向内容农场。

## 风险、反方意见与路线图

### 产品化、工程化与创作风险

| 风险类别 | 具体风险 | 为什么会发生 | 缓解建议 |
|---|---|---|---|
| 用户使用风险 | 前期填表过重，作者根本不愿维护 | 当前链路已经有 8 步，多加长篇层后复杂度会爆炸 | 提供 Lite / Standard / Research 三档模式 |
| 复杂度风险 | 系统层数正确，但人类操作成本过高 | 把所有研究概念都落地成必填 schema | 只把热路径字段做成必填，其余按需展开 |
| 成本风险 | token 与返工成本过高 | 多层 planning + scene + render + review + writeback | 先做 3 章连续，不做 10 章；scene packet 只用于关键场景 |
| 状态维护风险 | 账本越多，越容易互相打架 | 自动回写会幻觉，且 reviewer 很难全查 | delta-first + reducer + evidence_ref |
| 审核风险 | reviewer 判不出账本真伪 | 账本可能变成“看似合理的第二套小说” | 强制正文证据映射 |
| 质量验证风险 | 连续性提升但可读性下降 | 系统过度优化一致性，忽略现场感 | 把双盲文本偏好列为一等指标 |
| 创作风险 | 上层规划过硬，人物变成木偶 | 章节卡过细、allowed divergence 太窄 | 用“结果约束”，不用“动作处方” |
| 创作风险 | 过度工程化，读起来像产品文档 | 状态正确但叙述没有呼吸 | Renderer 保留 voice / focalization / human texture 合同 |
| 产品风险 | 看上去功能很多，但每章质量提升不明显 | 核心瓶颈可能在模型审美与训练，不在架构 | 先用 MVP 验证，不要大规模工程投入 |
| 伦理 / 内容质量风险 | 系统更高效地批量复制套路 | 只优化 hook、节奏、完读率代理指标 | 加反预制菜 gate，限制新坑膨胀和免费爽点 |

### 我站在反方时，会怎么批这个项目

第一种反方意见会说：**你做的不是写作系统，而是“管理系统幻觉”**。
这种批评有相当强的杀伤力。因为确实有可能出现这种情况：一切账本都很漂亮，chapter card 也很完整，但正文依然只是“被管理过的无聊文本”。如果发生这种事，说明系统优化的是**文档一致性**，不是**阅读活性**。

第二种反方意见会说：**网文读者并不需要这么重的因果车架，他们更在意单章快感和节奏**。
这不是空话。很多连载型内容确实靠场景强度、连载钩子和角色魅力往前跑，而不是靠严丝合缝的宏观结构。你如果把资源过早砸在卷账本和 IP 宇宙上，可能会错过真正影响读者体感的更低层问题。

第三种反方意见会说：**角色主动感引擎未必提升正文质量，反而会制造又臭又长的 event log。**
这类担心有充分依据。涌现叙事、强自治代理和多 agent 仿真长期都面对一个问题：角色行为更“真实”，不等于故事更“好看”。最近的 multi-agent story writing 论文之所以仍然保留 narrative plan 和 rewrite 步骤，正说明 agent 运行本身不是终点。citeturn37search11turn44search2

第四种反方意见会说：**模型真正缺的不是层级，而是语料、审美、偏好训练与裁判。**
这也是可能的。LongWriter、NovelQA 一类研究表明，模型在长文本生成与理解上的能力边界仍然很现实；如果底层模型本身对中文长篇叙事的审美和概率分布支持不足，再精巧的车架也可能只能把 mediocre 稳定下来，而不能把 mediocre 变成好看。citeturn46search8turn46search17

第五种反方意见会说：**IP 宇宙根本是高级拖延。**
我认为这条批评对当前阶段尤其成立。没有先证明“单书骨架 + 3 章连续 + 状态继承”能创造肉眼可见的提升之前，IP 宇宙很容易只是让团队获得一种“我们在搭大系统”的幻觉。

### 可回流到仓库的产物建议

下面这些文件，我认为都值得回流仓库。其中优先级已经按“先实验、后扩展”的原则排过序。

| 文件 | 用途 | 优先级 |
|---|---|---|
| `production/longform/longform_architecture.md` | 定义长篇系统各层、热路径与冷层资产 | 最高 |
| `production/longform/longform_terms.md` | 冻结术语，避免“宇宙/世界/单书/卷/章/场景/账本/债”再混 | 最高 |
| `schemas/world_slice.schema.yaml` | 取代“完整 IP 宇宙先行”的最小世界切片 | 最高 |
| `schemas/single_book_story.schema.yaml` | 整书一句话、反力量、终局方向、类型承诺 | 最高 |
| `schemas/volume_card.schema.yaml` | 卷目标、卷反力、卷中点、卷尾兑现窗口 | 最高 |
| `schemas/chapter_card.schema.yaml` | 章节前后状态、reader debt、allowed divergence、must_not_happen | 最高 |
| `schemas/scene_agency_packet.schema.yaml` | local goal、belief、options、tactic、blindspot、cost、next friction | 最高 |
| `schemas/event_log.schema.yaml` | scene engine 输出的可渲染事件日志 | 高 |
| `schemas/state_delta.schema.yaml` | 写后回写的唯一源事实格式 | 最高 |
| `schemas/plot_ledger.schema.yaml` | 剧情线程物化视图 | 高 |
| `schemas/character_state_ledger.schema.yaml` | 角色状态物化视图 | 高 |
| `schemas/relationship_debt_ledger.schema.yaml` | 关系债物化视图 | 高 |
| `schemas/knowledge_ledger.schema.yaml` | 信息状态物化视图 | 高 |
| `schemas/resource_ledger.schema.yaml` | 资源继承 | 中 |
| `schemas/reputation_identity_ledger.schema.yaml` | 声誉与身份继承 | 中 |
| `schemas/reader_question_ledger.schema.yaml` | 读者问题与兑现窗口 | 高 |
| `schemas/volume_progress_ledger.schema.yaml` | 卷目标推进度 | 高 |
| `production/longform/story_orchestrator_spec.md` | 调度器职责边界、输入输出、stoplight 约束 | 最高 |
| `production/longform/renderer_contract.md` | Renderer 读写边界与 blocker 类型 | 最高 |
| `production/longform/longform_reviewer_gate.md` | 长篇 reviewer 的硬 fail / soft fail 规则 | 高 |
| `production/longform/drift_detection_rules.md` | 主线偏航、世界冲突、关系蒸发等检测规则 | 高 |
| `production/longform/mvp/three_chapter_continuity_v0.md` | 三章连续 MVP 方案与验收标准 | 最高 |

除此之外，我建议把三类旧假设在仓库里显式标记状态：

- “**完整 IP 宇宙应先于单书长篇架构**” → 标记为 **待验证 / 暂缓**。
- “**chapter_one_sentence 足以控制 chapter chain**” → 标记为 **已否决**。
- “**Renderer / Polisher 可以在末端补足结构**” → 标记为 **已否决**。

### 路线图建议

| 阶段 | 立即做什么 | 先不要做什么 | 理由 |
|---|---|---|---|
| 立即阶段 | 冻结术语；写 `longform_architecture.md`；补 `single_book_story`、`volume_card`、`chapter_card`、`state_delta` 四个 schema；搭 3 章连续实验 harness | 不做完整 IP 宇宙，不做 10 章 benchmark | 先抓热路径最硬问题 |
| 短期阶段 | 做 Story Orchestrator Lite；做 reducers 和 drift detection；把 Human Texture / Work Voice 接到 renderer contract 与 longform reviewer gate | 不做完整多 agent 生产接管 | 先验证“结构控制 + 状态继承”是否有实效 |
| 中期阶段 | 做 1 个卷沙盒；引入 `world_slice` / `series_codex`；做 Lite / Standard / Research 三档产品模式 | 不把所有账本都暴露给最终用户 | 兼顾稳定性与可用性 |
| 长期阶段 | 研究角色驱动叙事沙盒；做可选 IP 宇宙层与系列复用；做跨书 pattern library 与篇章级评估体系 | 不把自由多 agent 聊天当成故事系统本体 | 长线研究应服务主链，而不是吞掉主链 |

我的最终优先级结论很明确：

**先做单书架构 MVP，不先做完整 IP 宇宙。**
**先做 3 章连续，不先做 1 卷 10 章。**
**先做 state delta + chapter card + orchestrator lite，不先上完整多 agent。**
**先把 Renderer 限权，不幻想它能救结构。**

## 参考来源

### 项目侧依据

本报告有关“项目当前链路、现有 schema、现有治理原则”的判断，主要依据当前公开仓库中的以下文档：Phase 7 多角色创作工作流、Phase 6A StateManager 结果、Human Texture 研究包与集成方案、Work Voice 研究包、Phase 8 README、Phase 8 单书闭环 completion report、next stage recommendation、lessons learned，以及现有 `chapter_beat`、`chapter_commit`、`runtime_canon` schema。citeturn18view0turn19view0turn22view0turn26view0turn31view0turn32view0turn33view0turn34view0turn45view0turn30view0turn28view0turn29view1

### 外部资料支持的关键结论

本报告有关“分层生成优于单次长生成”“长上下文与超长输出仍有能力边界”“故事调度器必要”“自由 agent 不会自动变成好故事”“读者沉浸应转成字段与 gate”“叙述合同是信息分配合同而非纯文风”的判断，主要依据 Snowflake、Save the Cat、Hero’s Journey、Story Grid、serial fiction planning、Living Handbook of Narratology、transportation / narrative engagement / reader-response 研究、Plan-and-Write、Dramatron、emergent narrative、Automated Story Director、Left 4 Dead AI Director、LongWriter、LongGenBench、NovelQA，以及若干写作工具与开源系统文档。citeturn35search0turn35search1turn35search2turn35search3turn36search8turn38search2turn40search6turn38search12turn38search1turn39search1turn39search8turn46search19turn41search19turn37search4turn44search2turn37search1turn37search10turn46search8turn46search20turn46search17turn41search4turn41search5turn41search13turn41search0turn42search0turn44search9turn42search2

### 我的推理建议

本报告中所有**具体 schema 重排、delta-first 写回方案、账本拆分方式、Story Orchestrator 边界、Renderer 限权规则、3 章连续 MVP 排序、反预制菜 gate 与路线图优先级**，都属于我的综合推理建议。它们是基于项目现状与外部研究交叉得出的工程判断，不应被误读为“仓库已验证事实”或“外部学界共识”。