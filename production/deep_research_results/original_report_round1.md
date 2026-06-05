# 工程化网文创作系统深度审计报告

## 执行摘要与资料边界

你给定的入口页 URL 没有在当前浏览流程中成功解析，因此我无法按该入口页宣告的“资料包顺序”逐份核验。下面这份报告，基于我能直接读取的公开 `main` 分支材料完成，包括：项目总纲 `AGENTS.md`、`skill-pack`、Phase 7 多角色工作流、Phase 8 技法蒸馏与验证、`production/human_texture/`、`production/work_voice/research/`，再结合你在本轮任务说明里提出的较新概念标签来做外部对标与批判性重组。换句话说，这是**基于可访问公开仓库与题设摘要的 best-effort 审计**，不是对你那份失联入口页的原样复述。citeturn42view0turn43view0turn44view0turn27view0turn34view0turn40view0

我的总体判断是：这个项目**有价值，而且方向感比一般“AI 写小说工具”更成熟**，因为它已经明确区分了结构能力、审稿门禁、原作污染风险、状态真源与正文生成，也已经通过 Phase 8 做出了一批受控验证；但你当前的“分层”并不严格，混杂了**场景层合同、叙述层合同、读者侧结果、运行时架构、产品治理原则**五种不同性质的对象。Human Texture 与 Work Voice 是成立的两个合同层；Reader Immersion 更像评价目标而不是生成层；Live Leakage 更像 Human Texture 的一种微观证据；Agentic Narrative Engine 是架构范式，不是与前几者同级的“层”；Industrial Sincerity 则是治理原则。citeturn19view0turn35view0turn36view0turn40view0turn45view3turn27view0

如果只问“哪一个最该先解决，才能让 AI 网文不像套路机器而像有人认真写过”，我给出的答案不是 Work Voice，也不是立刻上多 agent，而是**角色主动感（Character Agency，指角色在局面中有自己的判断、误判、取舍与下一步算法）加后果继承账本**。叙事理论与互动叙事研究都反复暴露同一个事实：当角色没有可信的目标—选择—代价回路时，系统只能靠解释去补，结果很容易变成“作者代角色说话”；相反，当角色先在因果上站住，叙述声音才不必靠说教来制造存在感。仓库当前 Human Texture 文档其实也在朝这个方向走，只是它现在把“私心、羞耻、关系债、场景阻力、信息载体、后果摩擦”更多表述成 texture，而不是显式的行动主权层。citeturn36view0turn39view0turn48search0turn48search7turn50search8turn51search16

长线的 Agentic Narrative Engine 我认为**值得做，但现在只能作为研究轨道，不应直接接管生产主链**。Façade、experience management、Left 4 Dead 的 AI Director、emergent narrative、以及近年基于 LLM 的 generative agents 和 multi-agent story generation，都说明“让角色运行，再由上层导演/调度器约束，再把事件轨迹渲染为文本”是可行方向；但它们同样说明，**高 agency 与高 coherence 的矛盾不会自己消失**。没有 scene-level orchestrator，这条路大概率不是“更自由”，而是“更贵、更散、更无聊”。citeturn46search2turn46search8turn48search2turn48search16turn50search0turn50search11turn50search5

## 项目框架总评

### 当前框架成立的部分

公开仓库已经清楚显示：这个项目不是在做一个“一键写整本书”的玩具，而是在做一个**有状态真源、角色分工、质检门禁、技法审计和污染隔离**的创作管线。`AGENTS.md` 把 Hermes、DeepCode、DeepSeek、Python、`.story-system` 和 WPS 的边界划得很硬；Phase 7 给出了 Planner→Writer→Reviewer→Polisher→State Manager→WPS Sync 的完整流程；Phase 8 又把“approved craft assets 才能进入正式链路”“Writer 不得接触原文和未审核技法”写成了制度。这些都说明“工程化厨房”不是口号，而是已经落到组织结构上的东西。citeturn42view0turn43view0turn44view0turn27view0

Human Texture 与 Work Voice 作为两个相邻但不同的合同层，是这个项目最有洞见的部分。前者处理“场景里的人是否像人，是否有私心、羞耻、关系债、阻力、信息代价与后果账”；后者处理“讲故事的人站在哪里，如何稳定地对待主角、世界和读者”。仓库里这两套文档都明确拒绝把事情做成“去 AI 味润色”或“作者指纹复刻”，而是要把它们转成可审查字段、brief、review gate 和 A/B/C 验证。这个方向，与 narratology 中 narrator / focalization / implied author / implied reader 的区分是一致的，也和现代写作工具把 lorebook、codex、memory、scene metadata 作为上下文容器的做法相一致。citeturn34view0turn35view0turn40view0turn41view2turn46search6turn46search15turn46search0turn47search4turn49search1turn49search2

### 重叠、错层与顺序问题

你当前的“分层”最大的问题，不是内容错，而是**层级类型不统一**。Human Texture 与 Work Voice 是创作合同；Character Agency 是因果驱动层；Live Leakage 是微观写作手法；Reader Immersion 是读者侧效果指标；Agentic Narrative Engine 是运行时架构；Industrial Sincerity 是治理与产品哲学。把这些并列，容易导致讨论看似全面，实际却互相打架：比如 Reader Immersion 会被误做成写作 prompt，Live Leakage 会被误做成主模块，Agentic Engine 会被误以为是 Human Texture 的上位替代。citeturn35view0turn39view0turn40view0turn45view3turn46search1turn47search7turn48search0

更具体地说，**Live Leakage 与 Human Texture 有明显重叠**。如果“活人浅痕”只是指不邀功、不追光的细微活人漏痕，那它更像 Human Texture 的一种低振幅实现方式，而不是独立层。**Reader Immersion 也不该被当成前置生成层**，因为 reader-response、transportation、narrative engagement 研究关心的是文本如何为读者保留推断位、情绪站位与知识差，这更适合做 reviewer rubric 和实验指标，而不是一个单独 writer patch。citeturn51search15turn51search8turn51search9turn46search1turn47search7turn47search4

顺序上，我认为**“角色主动感晚于 Work Voice”的风险很大**。仓库当前 Work Voice 研究把它放成 Human Texture 之后的上层合同，这在“叙述站位”这个问题本身上没错；但如果角色在 scene 中没有自己的决策算法，Work Voice 很容易退化成叙述者替角色做理解、替读者先下判断、替剧情解释为什么它合理，于是你担心的“老灯说教”就不再是偶发 bug，而会变成系统性代偿机制。互动叙事研究一直把 high agency 与 coherent plot 的平衡看成核心难题；仓库另一头的 Human Texture 文档也已经发现：如果 Planner 没有分配这些人味压力，Polisher 只能把空心文本改得更顺。我的结论是：**行动主权应前移，但先前移到 scene-level contract，不是直接前移到 full multi-agent runtime**。citeturn34view0turn36view0turn40view0turn48search0turn48search7turn50search8

### 当前框架缺失的关键层

缺失得最明显的一层，是**因果主权层（Causal Agency Layer，指角色目标、局部信念、可见选项、选中策略、误判与后果继承的结构层）**。仓库现有链路里，读者债、runtime canon、chapter commit、Human Texture packet、Phase 8 的认知优势/内在代价/揭秘阶段，其实已经散落着这层的零件；但项目概念里还没有把它显式地树成“这是一切人味、声音、代入之前的因果发动机”。citeturn44view0turn27view0turn30view0turn36view0turn39view1

同样缺失的，还有**故事调度层（Story Orchestrator，指在角色局部自主与全局叙事目标之间做限幅、配额、终止条件和镜头焦点分配的导演层）**。项目级已经有 Hermes 作为工程总调度，但那是仓库/脚本/技能调用层的 orchestrator，不是 scene runtime 的 orchestrator。Façade 的 drama manager、Valve 的 AI Director、experience management 文献都说明：一旦你真的让多个代理运行，必须有一个不写正文、但负责 pacing、spotlight、beat sequence、reveal timing 和 failure containment 的中间层。没有它，多 agent 不会自动变成好故事，只会变成高成本日志。citeturn42view0turn46search2turn46search8turn48search2turn48search9turn50search8

### 我建议的重组方式

我建议把你现在的概念重组成四层，而不是把所有东西都叫“层”。第一层是**因果主权层（Agency Layer，角色在局面中的决策与后果回路）**；第二层是**场景质感层（Scene Texture Layer，Human Texture + consequence + information carrier + relationship debt）**；第三层是**叙述合同层（Narrative Stance Layer，Work Voice + focalization + reader relationship）**；第四层是**评价与治理层（Evaluation and Governance Layer，Reader Immersion rubric + anti-template gate + industrial sincerity rules）**。至于 Live Leakage，放到第二、三层的具体写法规则里；至于 Agentic Narrative Engine，放到**可选上游运行时**，不要与前三层并列。这个重组，既更符合 narratology 的概念边界，也更符合仓库本身已经存在的 Planner/Writer/Reviewer/Polisher/State Manager 分工。citeturn42view0turn44view0turn36view0turn40view0turn45view3turn46search6turn46search15turn47search4turn48search0

如果必须给出一条最直接的优先级判断：**最关键的一层是角色主动感；它应该提前；但它的最小实现形态不是多 agent 仿真，而是 scene-level decision packet + consequence ledger**。这是我对你最核心问题的直接回答。citeturn48search0turn48search7turn50search8turn36view0turn39view1

## 模块逐项审计

### 人物质感

**人物质感（Human Texture，指人物与场景共同承担私欲、羞耻、关系摩擦、信息漏出与后果账的叙事合同）**是公开仓库里目前定义最清楚、也最接近真正问题根部的模块。仓库对它的诊断很准：当前链路已经会写钩子、规则、认知优势、规则破局、内在代价和五章推进，但文本仍像“系统展示故事机制”；问题不是句子不顺，而是人物像功能件、情绪被命名而缺少行为后果、场景只为信息服务、关系债不持续。这个判断不是空泛抱怨，而是和 indirect characterization、embodied event、角色行为塑造这些外部理论相吻合：人物不是靠“被解释成什么样”成立，而是靠选择、动作、迟滞、误读与可继承后果被读者间接推断出来。citeturn34view0turn35view0turn51search15turn51search8turn51search16

**相邻工程实践**也很清楚：仓库已经把 Human Texture 压成可执行字段，并进一步收缩成 6 个核心字段，强调每章最多激活 2–3 个，避免 packet 过大导致模板化；Writer brief 也明确反对把它写成风景、口语、比喻或心理标签。这是正确的，因为真正危险的不是“字段太少”，而是“字段太多导致每章都像完成表格”。**价值**在于它能直接攻击系统展示感；**风险**在于它一旦被后置到 Polisher，或者被做成“一章必须有 6 个人味细节”的 checklist，就会立刻退化成人味表演。**是否保留**：强烈保留。**下一步 MVP**：不要再扩字段，而是冻结 6 字段版 schema，在实验分支里做 1–2 个 scene 的 blind A/B，并让 Reviewer 明确判断“结构空心是否仍在”。citeturn36view0turn39view0turn39view3turn39view2

### 作品声音与作者站位

**作品声音（Work Voice / Narrative Stance，指文本中的讲述者站位、叙述距离、读者关系与稳定偏态）**作为问题命名是成立的。仓库这一包最有价值的一点，在于它明确区分了 narrator、focalization、narrative distance、implied author、reader relationship、free indirect discourse，并把这些概念翻译成工程字段，而不是把“声音”偷换成“学某作者的句子”。这一点非常重要，因为 narratology 本来就强调 narrator 不等于现实作者，implied author 是读者从文本整体推断出的价值组织者，而 focalization 处理的是“谁在看”，不只是“谁在说”。citeturn40view0turn41view1turn46search6turn46search15turn46search0turn46search3

我对这个模块的批判，不是反对它，而是反对它**被过早地当成解决正文空心的主要手段**。当角色没有可信行动主权时，叙述者就会被迫出场解释，所以 Work Voice 的确可能滑向“作者抢戏”。它和“老灯说教”的边界，关键不在于叙述者是否存在，而在于它是否**越过了 focalization 的知识边界、提前替读者完成理解、或反复用显性评判取代场面本身的因果与情绪**。换句话说，讲述者可以在场，但应该优先通过 detail selection、distance control、withholding rule、free indirect blending 来显影，而不是通过总结和训解来显影。**是否保留**：保留。**下一步 MVP**：继续用 `voice_observation_card -> work_voice_map -> voice_contract -> Writer 注入 -> Reviewer gate` 这条线，但要把它排在 scene-level agency contract 之后，且必须设置“commentary_density / knowledge_boundary / forbidden_original_elements”三条硬门。citeturn45view3turn41view2turn41view3turn45view0turn45view2

### 角色主动感与行动主权

**角色主动感（Character Agency，指角色是否在局面里基于自己的目标、信念、误判与代价推进情势）**，在你目前的概念里是最该前移的模块。公开仓库还没有把它做成独立包，但外部文献给出的方向已经足够清楚：interactive narrative 的核心难题一直是如何在 plot coherence 和 character/user agency 之间取平衡；narrative planning 文献则把“让角色显得在为自己的目标行动”视为高质量故事生成的关键，而不是额外装饰。Façade 的 drama manager、Automated Story Director、experience management 都不是为了减少 agency，而是为了让 agency 在**受控情境中变得可叙事**。citeturn48search0turn48search7turn46search2turn46search8turn50search8

我赞成你“没有行动主权时，作者站位容易滑向讲课，读者也难以代入”的判断，但要加一个硬限制：**这里的 agency 不能被误解为“主角永远主动出击”或“角色自由聊天”**。真正可工程化的，是 scene-level 的六件事：`local_goal`、`belief_about_situation`、`available_options`、`chosen_tactic`、`perceived_cost`、`wrong_model_or_blindspot`；再加一项 `next_friction` 记录后果如何进入下一场。这样做的价值，是把“人味”从修辞层拉回因果层。**风险**是两种：一是把每个角色都写成算盘精，二是以为有 state card 就等于有戏。**是否保留**：不仅保留，而且上升为首要层。**下一步 MVP**：先不要上 agent；先在 Planner 输出与 Writer 输入之间插一个 `scene_agency_packet`，只要求主角和 1–2 个关键配角各自给出一条局部算法，再做 blind A/B。citeturn51search16turn36view0turn39view1turn44view0

### 活人浅痕与活人漏痕

**活人浅痕（Live Leakage，指不邀功、不追光、低振幅地泄露人物状态的动作、迟疑、物理反应与关系边界变化）**，我认为是**有效概念，但不是独立层**。它最接近的外部锚点，不是“大量细节”，而是 indirect characterization、embodied events、gesture style、micro-gesture 等研究：人物很多时候不是通过说明书显出活性，而是通过不完全自觉的身体动作、短促修正、对物件的处理方式、站位变化、信息保留方式来被读者推断。文学叙事研究也反复强调，虚构人物的可感性往往建立在 embodied actions，而不是抽象心理陈述上。citeturn51search15turn51search8turn51search16turn51search1turn51search9

它的最大价值，是避免 Human Texture 变成“解释性人味”；它的最大风险，则是迅速滑成“人味表演”，也就是统一套用一批库存动作：摸鼻子、抿嘴、移开视线、攥衣角。只要变成库存动作库，它就不再是 leakage，而成了戏精标签。我的结论是：**保留这个名字可以，但把它降格为 Human Texture 与 Work Voice 的微观实现规则**。Reviewer 的标准应当非常苛刻：每个活人漏痕都必须改变关系、信息流或行动节奏中的至少一项；如果删掉这句，段落功能没有变化，那它就是假漏痕。**下一步 MVP**：把 Writer 约束写死为“每个主字段最多一个 leakage 落点、每 scene 总量不超过两个、不得重复 stock gesture”，而不是扩展一个单独模块。citeturn39view3turn37view0turn51search9turn51search15

### 读者代入感与读者解压

**读者代入感（Reader Immersion，指文本是否为读者保留判断位置、期待空间、情绪站位和推断缝隙）**从理论上是成立的，但从工程上它更像**评价层**。reader-response 理论中的 implied reader，本来就关心文本如何预设接受位置；transportation theory 关心读者是否被吸入叙事世界；narrative engagement 量表则把理解、情绪卷入、叙事在场与注意聚焦拆成可测维度；关于 suspense、curiosity 和 surprise 的研究则进一步说明，读者并不是被“解释得越多越沉浸”，而是被**恰当的信息差、未完成推断、可预期又不封死的局势**牵引。citeturn47search4turn47search7turn47search11turn46search1turn46search19turn47search6turn47search10

所以，这一层不应该落成“多写心理、多替读者解释”的写作 patch，而应落成 reviewer 和 orchestrator 的检查项。我建议直接工程化成这些字段：`reader_knowledge_delta`、`open_question_type`、`withholding_reason`、`prediction_slots`、`inference_slack`、`emotional_position_options`、`payoff_deadline`、`exposition_preemption_risk`。其中最关键的是两个负面门禁：一是**叙述者是否提前替读者完成了道德/情绪/因果解释**，二是**信息隐藏是否有场面内原因，而不是系统刻意吊着不说**。**是否保留**：保留，但改为评价层。**下一步 MVP**：先不给 Writer 新 patch，只给 Reviewer 新 rubric，在 1-scene 实验里专门让评委回答“哪一版更给你留判断空间”。citeturn36view0turn45view3turn46search1turn47search6

### 角色驱动叙事引擎

**角色驱动叙事引擎（Agentic Narrative Engine，指先运行受边界约束的角色—世界状态，再把事件轨迹渲染成正文的运行时架构）**是有研究价值的新范式，但它现在不该被说成“更根本、因此应立刻接管主链”。外部参照里，Aylett 的 emergent narrative、Riedl 等人的 interactive narrative / narrative planning、Façade 的 drama manager、Valve 的 AI Director、以及近年的 generative agents 与 multi-agent long story generation，都共同支持一件事：**让局面先发生，再把它叙述出来**，确实能减少“作者硬掰剧情”的痕迹；但这些案例同样都依赖上层导演、beat sequencing、player/character model、state constraint 与 quality selection。citeturn48search16turn48search0turn46search2turn46search8turn48search2turn48search9turn50search0turn50search11turn50search5

我对这一模块的判断是：**保留，但只作为长线研究轨道**。近年的 LLM multi-agent 论文也恰好说明，长篇故事仍然被 discourse coherence 与 narrative complexity 卡住，所以它们往往还是引入 outline agent、planning agent、narrative plan 或 story graph，而不是彻底交给一群自治角色自己想办法。你的正确方向不是“更自由”，而是“更可控的局部涌现”：先把它限定在一个 scene，两个到四个 agent，一个 orchestrator，一个 narrator/renderer。**价值**是更强的角色因果与局面感；**风险**是剧情跑飞、爽点失控、配角抢戏、token 爆炸、状态维护困难，以及“行为更真实但更不好看”。**下一步 MVP**：做 one-scene sandbox，而不是 chapter-level 甚至 novel-level sandbox。citeturn50search11turn50search1turn50search5turn48search0turn50search8

### 工业化真诚与工程化厨房

**工业化真诚（Industrial Sincerity，指承认类型文需要产能、节奏、钩子与稳定性，但用工程制度保护人物活性、叙事诚实与内容上限）**不是文艺口号，而是这个项目最应该长期坚持的治理框架。仓库里最接近这一点的成熟做法，恰恰不是生成 prompt，而是：`.story-system` 作为唯一真源、approved craft assets 进入正式链路、Writer 不接触原文、Reviewer 和 gate 在 Polisher 之前拦结构问题、Polisher 只做轻增强、以及污染风险与模板风险被显式审查。商业工具侧，Sudowrite、Novelcrafter、NovelAI 之类真正可借鉴的也不是“一键出文”，而是 codex、lorebook、memory、story bible、scene metadata 这样的组织能力。citeturn42view0turn27view0turn33view1turn33view2turn49search0turn49search1turn49search2

这个模块必须保留，但要防止自己骗自己。工程化厨房的真正敌人，不是工业化，而是**把工业化只理解成 throughput 优化**。一旦 KPI 变成“日更量、钩子密度、爽点密度、低 ai_flavor 分”，系统就会不可避免地向更高级的套路生成器滑落。**是否保留**：必须保留，而且要上升到顶层治理原则。**下一步 MVP**：立刻补一份 `anti_feed_quality_gate.md`，规定 throughput、爽点和 reviewer score 不能单独通过，必须同时经过 agency、consequence、voice、reader slack 四道门。citeturn43view0turn27view0turn35view0turn49search1turn49search2

## 外部理论与工程参照

### 叙事学与读者理论

**The Living Handbook of Narratology（LHN，叙事学在线手册；用于把 narrator、focalization、implied author、implied reader 等概念转成工程字段）**最适合支撑 Work Voice 和 Reader Immersion。可借的是概念边界：谁在说、谁在看、叙述距离、隐含作者、读者位置；不能照搬的是纯理论术语堆砌，因为它不会自动给你 scene-level prompt 结构。citeturn46search6turn46search15turn46search0turn46search3turn47search4

**Busselle 与 Bilandzic 的 Narrative Engagement（叙事卷入；用于把“代入感”从玄学变为可量测维度）**可借的是多维结构：理解、情绪卷入、在场感、注意聚焦；不能照搬的是把量表直接当中文网文审稿表，因为你的任务不是做媒体心理实验，而是做写作工程 gate。citeturn46search1turn46search4turn46search19

**Green 与 Brock 的 Transportation Theory（叙事运输；用于理解读者为何被带入故事）**可借的是“沉浸来自故事世界吸收，而不是来自解释密度”的思想，因此它适合反对过度说明；不能照搬的是把 persuasion 框架原样套到类型网文上，因为你关心的是阅读参与，不是态度劝服。citeturn47search7turn47search11turn47search15

**Loewenstein 的 Curiosity Theory（信息差好奇；用于构造 reader decompression 的知识缺口）**与叙事情境中的 suspense / curiosity / surprise 研究结合后，非常适合定义 `open_question_type`、`withholding_reason`、`prediction_slots`。可借的是“信息差必须可被感知、可被追索”；不能照搬的是把所有章节都写成 clickbait，因为那会摧毁公平性与兑现质量。citeturn47search10turn47search6turn47search18

### 互动叙事、游戏叙事与多 agent 仿真

**Aylett 的 Emergent Narrative（涌现叙事；角色交互生成故事，不依赖完全预写情节）**可借的是“故事可从受限互动中长出来”；不能照搬的是对自由涌现的浪漫化，因为原论文同样提醒了 episodic 与 boring bits 的问题。citeturn48search16turn48search4

**Riedl 与 Bulitko 的 Interactive Narrative / Narrative Planning（交互叙事与叙事规划；平衡故事控制与角色/玩家 agency）**与你的 Character Agency、Story Orchestrator 和 Agentic Engine 最相关。可借的是“agency 需要 narrative control”；不能照搬的是把交互系统的玩家位直接替换成网文章节生产，因为你这里没有真人玩家，而是作者/系统在提前布置体验。citeturn48search0turn48search7turn50search8

**Mateas 与 Stern 的 Façade（交互戏剧；character + drama management + beat sequencing 的经典案例）**最值得借的是“角色局部自主 + 上层 beat 管理”的双层结构，以及“高 agency 仍需导演”。不能照搬的是它的内容组织规模与实时对话结构，因为你的目标是网文 scene prose，不是实时玩家舞台。citeturn46search2turn46search8turn46search11

**Valve 的 Left 4 Dead AI Director（AI 导演；用导演层在作者预设空间内调度遭遇与节奏）**比 generative agents 更接近你真正需要的 story orchestrator。可借的是“在 author-defined possibility space 内做动态选取”，以及“用导演打破固定套路，提高重复游玩中的不确定性与悬念”；不能照搬的是直接把敌人刷怪逻辑类比成剧情，因为网文需要因果、角色立场与兑现，不只是 encounter variety。citeturn48search2turn48search9

**Generative Agents（生成式代理；memory + reflection + planning 的社会行为仿真）**证明了 LLM agent 可以通过记忆、反思和计划产生可感的社会行为与协调事件。可借的是 observation / reflection / planning 的三段式循环，以及环境状态驱动；不能照搬的是把“社会上合理发生”误当成“文学上值得写”，因为 believable social behavior 不等于 high-drama high-payoff narrative。citeturn50search0turn50search14

**StoryWriter 与 Multi-Agent Based Character Simulation for Story Writing（近年的多 agent 长篇与角色模拟研究；证明 scene-level/plan-level 多代理写作正在成型）**可借的是“根据 narrative plan 做角色运行，再产出文本”的研究框架；不能照搬的是直接相信多 agent 自然优于单 writer，因为这些论文本身就是在解决 coherence 和 long-form complexity 两个持续难题。citeturn50search11turn50search1turn50search5

### 商业工具与工程工作流

**Novelcrafter Codex（故事圣经/世界构建容器；适合作为长期状态与条目进化参考）**可借的是 codex 与 progressions 的组织方式；不能照搬的是把它当成正文质量解决方案，它解决的是检索与组织，不是“谁在讲故事”和“谁在承担后果”。citeturn49search1turn49search5

**NovelAI Lorebook（知识注入容器；适合作为 narrative elements 的上下文仓）**可借的是 lorebook 作为上下文注入机制，以及条目级 API 与 quick access；不能照搬的是把 lorebook 当成叙事发动机，因为它本质仍是 context repository。citeturn49search2turn49search14turn49search10

**Sudowrite（面向小说作者的 AI 协作工具；适合作为 co-writing 产品定位参照）**可借的是“AI as writing partner”这个定位，而不是“一键代写”；不能照搬的是其成品依赖的英语工作流和产品体验逻辑，你更需要的是可审计合同与 reviewer gate，而不是产品 UI。citeturn49search0

### 仓库研究包已经筛出的工程候选

公开仓库自己的 Human Texture 与 Work Voice 调研，已经把 **NovelGenerator、knowrite、novel-bot、NovelClaw、Dramatron、pulpgen** 列为值得继续跟踪的对象。这里我建议你的仓库处理方式是：把它们放进“候选模式与实验底座”而不是“计划直接 fork 的对象”。仓库文档本身也已经得出相同结论：这些项目可借 context/memory/quality controller/agent coordinator 等结构，但不适合整套照搬。citeturn34view0turn35view0turn40view0

## 风险、反对意见与反低质投喂约束

### 最大风险清单

**工程风险（Engineering Risk，指系统在实现上变得过重、过散、不可验证）**的核心不是“做不出来”，而是“每加一层都只是在 prompt 外再包一层 prompt”。当前仓库已经有 Planner/Writer/Reviewer/Polisher/State Manager、Phase 8 craft asset 注入、Human Texture、Work Voice；如果再直接上 Agentic Engine，而不先冻结 schema、baseline 和 blind eval，噪音会高到无法归因。多 agent 路线还会引入成倍的状态管理和 token 成本。citeturn42view0turn44view0turn27view0turn36view0turn40view0turn50search0turn50search11

**创作风险（Creative Risk，指文本被更复杂的系统制造得更像系统）**主要有四个：第一，Human Texture 被装饰化；第二，Work Voice 变成说教；第三，agent 仿真生成“真实但不好看”的日常；第四，配角因为更完整而抢走主角戏。interactive narrative 与 emergent narrative 早就表明，agency 提高不等于戏剧性自动提高；Valve 的 AI Director 之所以有效，恰恰是因为它在“可发生的集合”里做导演，而不是让一切自由生长。citeturn48search16turn48search0turn46search2turn48search2turn48search9

**产品风险（Product Risk，指系统的 KPI 逼着内容向模板化滑移）**在于：一旦你把 reviewer 中最容易量化的东西——钩子、节奏、章节推进、ai-flavor——当成主战绩，而把 agency、consequence、reader slack、voice drift 当成“高阶加分项”，团队就会自然把资源投向更高产的套路生成。仓库本身已经在 Human Texture 和 Work Voice 里多次提醒“不做通用 humanizer、不把 detector 当文学质量、不让 Polisher 补结构洞”，这些提醒如果不上硬 gate，最终只会沦为写在文档里的自我安慰。citeturn34view0turn35view0turn39view2turn40view0turn41view3

**伦理与内容质量风险（Ethics and Quality Risk，指项目滑成仿写、污染或内容农场）**主要有三类：仿写具体作者、原作内容污染、以及工业化逻辑对“像人认真写过”目标的反向侵蚀。Work Voice 文档已经明确把“把作品声音误判成作者本人”“把类型套路误判成作品声音”列为开放风险；Phase 8 也明确禁止 Writer 接触原文和 candidate 技法。这些都是正确的，但还不够，因为真正的滑坡通常不发生在明面违规时，而发生在“我没有抄，但我把效果学成了更高效的投喂模板”时。citeturn41view3turn27view0turn45view3

**验证风险（Validation Risk，指你误把风格变化当质量提升）**非常高。仓库当前已经采用 pairwise A/B、blind human judgment、保留机制指标不降级的思路，这比 detector 好得多；但只要实验样本太小、baseline 同时在变、prompt 每周重写一次，就仍然会出现“什么都像有提升，最后不知道是什么真的有效”的情况。citeturn36view0turn40view0

### 反低质投喂审核标准

我建议你把“反低质投喂 / 反套路化”写成一套**一票否决式 gate**，而不是写成价值宣言。

- **行动主权门**：每个 scene 必须能指出主角的 `local_goal`、`chosen_tactic` 与 `perceived_cost`；如果冲突只是作者替角色安排结果，没有角色自己的判断链，则不通过。这个门是为了防止系统只在增强操控。citeturn48search0turn48search7turn39view1
- **后果继承门**：每章必须继承上一章至少一笔关系账、资源账、身体账或声誉账；如果代价本章用完即蒸发，不通过。这个门是为了防止“爽点一过，世界归零”。citeturn36view0turn39view0
- **信息公平门**：每个关键揭示都要标明 `information_carrier` 与 `withholding_reason`；如果信息只是系统/权威/旁白整块公告，不通过。这个门是为了防止读者失去参与空间。citeturn36view0turn37view0turn47search4
- **说教拦截门**：如果 narrator 的评论在没有新增信息、没有制造反讽、也没有改变距离控制的情况下，直接替读者解释“人物其实怎样”“读者应该怎么想”，不通过。这个门就是专门拦“老灯说教”。citeturn46search6turn46search15turn46search0
- **模板风险门**：连续两章以上使用同一种冲突解法、同一种认知显摆模式、同一种章尾钩子组织方式，则 reviewer 必须标红；仓库现有 `template_risk` 维度应继续保留并升级。citeturn30view0turn33view0
- **活人漏痕门**：每个 scene 最多允许两个 leakage 落点，且必须改变行动或关系，不允许 stock gesture 堆叠。这个门是为了防止人味表演。citeturn39view3turn51search9turn51search15
- **Polisher 边界门**：Polisher 不得新增主角发动机、不得新增爽点、不得替结构问题硬救；仓库第二批轻量注入报告已经给了可执行先例。这个门是为了防止末端加工把系统推成预制菜工厂。citeturn33view1turn33view2
- **产能红线门**：任何声称提高产能的 patch，只有在 hook/pacing 不下降、agency/texture/voice/reader slack 至少两项显著上升时才允许合并；否则一律算“高效投喂优化”，不算“质量提升”。这是我的推理性建议，但它完全符合你仓库已有的 approved-pattern / reviewer-gate 治理方向。citeturn27view0turn39view2turn40view0

### 反对意见与失败可能

最应该正视的反方意见有五条。**第一，角色 agent 不一定提高正文质量**。它更可能先提高 event trace 的合理性，却把 prose 质量、节奏密度和阅读快感拉低；Façade、emergent narrative、generative agents 都能支持这个担心。citeturn46search2turn48search16turn50search0

**第二，网文读者未必需要高复杂度的角色主动感**。仓库自己的 5 章验证已经说明，结构、钩子、规则与 payoffs 可以在“机制展示感仍强”的情况下拿到不低评分；这意味着市场端未必会奖励你全部叙事升级。换句话说，高 agency 可能是上限改善，不一定是底盘生死线。citeturn32view0turn33view0turn35view0

**第三，过度工程化确实可能杀死现场感**。当每章都要经过 packet、contract、ledger、gate、voice map、orchestrator，再到 renderer，写作流很容易从“创作中的限制”变成“报表中的限制”。工具越多，不代表现场感越强。这个反对意见成立，所以我主张强制收口 schema，而不是继续加模块名。citeturn39view0turn36view0turn40view0

**第四，模型真正缺的也许不是结构，而是审美、语料与训练目标**。这一点不能被工程自信掩盖。仓库当前已经把许多结构问题收拢清楚，但如果基础模型在中文长篇叙述的语感、动作经济、价值温度上本来就不够，工程最多是把缺陷更稳定地暴露出来。这个判断是推理，但从多 agent 长篇研究仍把 coherence 当主问题，也能得到侧面支持。citeturn50search11turn50search1

**第五，Work Voice 可能被高估**。有些读者感受到的“像有人认真写过”，并不来自稳定 narrator，而来自角色因果、节奏控制、关系摩擦和兑现力度；如果基础行动层还是空的，再精致的 voice contract 也可能只是“更有风格的讲解器”。这也是我坚持先做 agency packet 再做 voice 合同的原因。citeturn36view0turn40view0turn48search0

## MVP优先级、1-scene实验与路线图

### 建议的 MVP 优先级

我的排序是：**先做 scene-level 行动主权 packet，再收口 Human Texture，再把 Reader Immersion 做成 reviewer rubric，然后做 Work Voice 的小样本 contract，最后才做 Story Orchestrator 与 Agentic Narrative Engine 的 one-scene sandbox**。这个顺序和仓库现有 Human Texture / Work Voice 文档略有不同，但我认为更稳，因为它先解决“谁在局面里推进”和“后果怎么继承”，再解决“谁在讲”。citeturn36view0turn40view0turn45view3turn48search0turn50search8

更直白地说：**当前 skill-pack 增强路线仍然值得继续，但只在它产出的是可复用 contract、schema、ledger、rubric、benchmark；如果它继续主要表现为 prompt patch 叠加，那就应该停。** Human Texture 的 6 核心字段、Work Voice 的 `voice_contract`、Polisher 的边界规则、Reviewer 的 gate，都能回流到新范式里；它们不是死补丁，前提是你把它们做成“接口”而不是“灵感”。citeturn39view0turn39view2turn40view0turn45view3

### 1-scene MVP 设计

**实验目标（Goal，验证行动主权与角色驱动运行时是否真的提升“文本活性”而不损失类型推进）**：比较三条生成路径在单 scene 上的表现，重点看 agency、因果、reader slack 与模板风险，而不是只看文句顺滑。这个设计沿用了仓库已经采用的 A/B/C 与 pairwise 思路。citeturn36view0turn40view0

**输入材料（Input，所有组共用）**：同一份 scene brief，内容只包含世界状态、主角当前目标、一个配角的对立目标、上一场遗留的一笔关系债、一个必须露出的关键信息、一个不可逆选择、字数上限与节奏要求；禁止提供正文样例，禁止提供作家参照。支持文件建议包括：`scene_state.yaml`、`character_state.yaml`、`reader_debt_snapshot.yaml`、`forbidden_exposition_list.yaml`。这个输入体量足够小，也与仓库当前 `.story-system`、Phase 8、Human Texture 文档兼容。citeturn42view0turn44view0turn27view0turn36view0

**对照组（A，Direct Writer）**：直接让 Writer 根据 scene brief 生成。
**实验组一（B，Texture + Voice）**：在 A 的基础上，额外注入 `human_texture_brief` 与 `voice_contract`。
**实验组二（C，Agentic Scene）**：先运行受限 scene simulation：2–4 个角色 agent + 一个 story orchestrator，在 6–10 个离散回合内产出 `event_trace`、`belief_updates`、`consequence_ledger`，再交给 narration renderer 输出正文。C 组必须把 orchestrator 与 renderer 分开，不允许 renderer 读取 agent 的自由 chatter 全量日志，只读整理后的 sanctioned trace。这个分工参考了 drama management、AI Director 与生成式代理研究。citeturn45view3turn46search2turn48search2turn50search0turn50search5

**中间产物（Artifacts）**建议固定如下。A 组只有 `draft.md`。B 组增加 `human_texture_brief.yaml`、`voice_contract.yaml`。C 组增加 `agent_cards.yaml`、`scene_orchestrator_rules.yaml`、`event_trace.yaml`、`selected_events.yaml`、`consequence_ledger.yaml`、`render_contract.yaml`。这样才能让你以后知道“好坏到底来自哪里”，而不是只比较成文。这个要求也是为了防止多 agent 方案变成黑箱。citeturn39view1turn39view2turn45view3turn50search8

**评价维度（Evaluation）**我建议分成九项：`agency_clarity`、`causal_coherence`、`human_texture`、`live_leakage_authenticity`、`voice_stability`、`reader_inference_space`、`hook_and_payoff_preservation`、`template_risk`、`runtime_cost`。前八项做 1–5 分盲评，最后一项记录 token、延迟和失败率。评委不看组别，只回答“哪一版更像人物自己把局面推出来”“哪一版更像有人认真写过”“哪一版更像系统在展示机制”。这与仓库对 Human Texture 和 Work Voice 所倡导的 blind pairwise / A/B/C 逻辑一致，也符合 narrative engagement 与 reader-response 的关注点。citeturn36view0turn40view0turn46search1turn47search4turn47search7

**通过标准（Pass）**建议设得很具体：B 或 C 在 `agency_clarity` 与 `reader_inference_space` 上对 A 至少提升 1 分；`hook_and_payoff_preservation` 不得下降超过 0.5 分；`template_risk` 不得变差；盲评中至少三分之二的评委选择 B 或 C 更像“有人认真写过”；如果是 C 组，还要满足平均成本不超过 A 组的 2 倍，否则它只说明“更贵”，不说明“更可用”。这些阈值是我的建议，不是仓库既有结论。citeturn32view0turn33view0turn36view0

**失败信号（Failure Signal）**必须预先写明：如果 C 组事件更合理但 prose 更差；如果配角显著抢戏；如果 orchestrator 常常强行收束导致文本变硬；如果 B 组已经接近或超过 C 组，那就说明 full agentic engine 还不该进入中期路线，而 scene-level contract 已经足够。**为什么这个实验足够小**：因为它只测一个 scene、一次不可逆选择、极少数角色、单回合 consequence inheritance；它不测全章、不断代、长记忆和世界观拓展，所以能把归因收拢。citeturn48search0turn50search11turn50search5

### 三阶段路线建议

**立即要做的事**：冻结当前实验噪音。具体包括：新增 `scene_agency_packet.schema.yaml`、`consequence_ledger.yaml`、`relationship_debt_ledger.yaml`；把 Human Texture 收口到 6 核心字段；给 Reviewer 增加 reader slack / info fairness / anti-lecture 检查；Work Voice 继续保留研究态，但不先改正式 skill-pack。这个阶段的关键词不是“再发明模块”，而是“把最小字段和最小验收定住”。citeturn39view0turn39view1turn39view2turn40view0turn45view3

**接下来要做的事**：做 1-scene benchmark 套件和 blind eval harness。这里建议把 B 组定义为“Agency + Human Texture + Reader Immersion rubric”，而不是只做“Human Texture + Work Voice”；Work Voice 可以在另一个相邻实验里加入，避免把两个变量绑死。这个阶段也可以允许实验分支里出现一个轻量 `webnovel_story_orchestrator` 草案，但它只服务 sandbox，不进主链。citeturn36view0turn40view0turn48search2turn50search8

**长线要做的事**：只有在 one-scene 证明 C 真正提升正文活性，而且不会明显损伤类型推进时，才进入 bounded agentic narrative engine 研究。那时的首要产物，不是更大的 prompt，而是 story orchestrator 的职责说明：scene objective、allowed action space、spotlight budget、reveal quotas、termination rule、state mutation policy、renderer input contract。换句话说，长线不是“自由多 agent 聊天”，而是“导演约束下的局部涌现”。citeturn46search8turn48search2turn50search8turn50search0

## 可回流到仓库的产物与来源说明

### 建议新增或修订的仓库产物

我建议直接向仓库回流以下文档与 schema。**新增** `production/architecture/stack_reframe.md`，把当前“模块并列图”重写成“因果主权层 / 场景质感层 / 叙述合同层 / 评价治理层”。**新增** `production/agency/scene_agency_packet.schema.yaml`、`production/agency/story_orchestrator_spec.md`、`production/agency/consequence_ledger.yaml`、`production/agency/relationship_debt_ledger.yaml`。**新增** `production/quality/reader_immersion_rubric.md` 与 `production/quality/anti_feed_quality_gate.md`。这些都是当前公开仓库中最缺、但又最能把你新概念落地的空位。citeturn42view0turn44view0turn36view0turn40view0

同时，**修订** `production/human_texture/` 与 `production/work_voice/research/` 的路线表述。Human Texture 文档里应新增“它不是因果主权本身，而是其场景显影合同”；Work Voice 文档里应新增“它依赖 scene-level agency，不应作为空心文本的主要补丁”；Phase 8 相关注入文档则应增加一个总原则：所有新 patch 必须说明自己复用到未来 orchestrated runtime 的方式，否则一律视为局部补丁。citeturn34view0turn39view0turn40view0turn45view3

再往下，**给 MVP 新增 acceptance criteria**。Human Texture MVP 当前已经强调 blind pairwise、后果继承和机制不降级；现在应再加两条：一条是 `agency_clarity`，一条是 `reader_inference_space`。Work Voice MVP 当前建议 A/B/C，但最好把“commentary_density 不可替代 causality”写成显式失败条件。Polisher 的 acceptance criteria 也应继续保留“不得新增发动机、不得新增爽点、不得替结构洞兜底”这一类边界。citeturn36view0turn40view0turn33view1turn33view2

最后，有几条旧假设我建议直接标记为**待验证或降级**。一是“Live Leakage 是独立层”——我认为不成立，应降为技法层。二是“Reader Immersion 是生成层”——我认为不成立，应改为评价层。三是“Work Voice 在 Human Texture 之后即可进入正式工程化”——我认为不稳，应先补 agency packet。四是“Agentic Narrative Engine 是长线更根本的新范式，所以可以提前拉动现有主链”——我认为现在证据不足，只能作为 research track。citeturn35view0turn40view0turn48search0turn50search11

### 来源与引用说明

**仓库公开文档支持的判断**，主要包括：当前项目已有 7 个创作 Skill 与明确的 Phase 7 流程；Phase 8 已有 approved-pattern gating、最小正式注入和 5 章连续验证；Human Texture 已被定义成一层合同并收口为 6 核心字段；Work Voice 已被定义成 `voice_contract` 式研究 MVP，而非作者仿写工程。citeturn43view0turn43view1turn44view0turn27view0turn28view0turn30view0turn32view0turn34view0turn35view0turn39view0turn40view0turn45view3

**外部资料支持的判断**，主要包括：narrator / focalization / implied author / implied reader 能为 Work Voice 与 Reader Immersion 提供稳定概念边界；transportation、narrative engagement、curiosity/suspense 能为“读者解压”提供可操作字段；emergent narrative、drama management、AI Director、generative agents、recent multi-agent story generation 能为 Agentic Narrative Engine 与 Story Orchestrator 提供真实对标；embodied events、characterization 与 micro-gesture 研究能为 Live Leakage 提供更精确的理论落点。citeturn46search6turn46search15turn46search0turn47search4turn47search7turn46search1turn47search6turn47search10turn48search16turn46search2turn48search2turn50search0turn50search11turn51search15turn51search8turn51search9

**我自己的推理建议**，主要包括三点：第一，把“角色主动感 + 后果继承账本”提升为最优先层；第二，把 Live Leakage 和 Reader Immersion 从“模块”降到“技法/评价层”；第三，把 Agentic Narrative Engine 限定为 one-scene sandbox 研究，而不是直接接管产线。这三点不是仓库现有结论，而是我根据公开仓库状态与外部文献作出的审计性重排。citeturn36view0turn39view0turn40view0turn48search0turn50search8turn50search11

### 参考来源

**项目公开资料**：`AGENTS.md`、`skill-pack/README.md`、`skill-pack/mapping.md`、`docs/phase7_multirole_creation_workflow.md`、`production/phase8/README.md`、`production/phase8/forward_validation/README.md`、`production/phase8/skill_injection_minimal/skill_injection_report.md`、`production/phase8/skill_injection_minimal/validation_5ch/cross_chapter_validation_report.md`、`production/phase8/polisher_light_injection/validation/polisher_light_validation_report.md`、`production/human_texture/HUMAN_TEXTURE_PLAN.md`、`production/human_texture/summary.md`、`production/human_texture/integration/integration_with_existing_skill_pack.md`、`production/human_texture/skill_pack_design/*.md`、`production/work_voice/research/*.md`。citeturn42view0turn43view0turn43view1turn44view0turn27view0turn28view0turn30view0turn32view0turn33view1turn34view0turn35view0turn37view0turn39view0turn40view0turn41view2turn41view3

**外部理论资料**：The Living Handbook of Narratology 关于 Narrator、Focalization、Implied Author、Implied Reader 的条目；Busselle 与 Bilandzic 关于 narrative engagement；Green 与 Brock 关于 transportation；Loewenstein 关于 curiosity；以及关于 suspense / uncertainty 的后续研究。citeturn46search6turn46search15turn46search0turn46search3turn47search4turn46search1turn46search19turn47search7turn47search11turn47search10turn47search6turn47search18

**外部互动叙事与 agent 资料**：Aylett 的 emergent narrative；Riedl 与 Bulitko 的 interactive narrative / narrative planning；Mateas 与 Stern 的 Façade；Valve 的 Left 4 Dead AI Director；Park 等人的 Generative Agents；以及 2025 年关于 StoryWriter 与角色仿真的多 agent 研究。citeturn48search16turn48search0turn48search7turn46search2turn46search8turn48search2turn48search9turn50search0turn50search14turn50search11turn50search5

**外部工具与工作流资料**：Sudowrite 官方站、Novelcrafter Codex 官方页与帮助文档、NovelAI Lorebook 官方文档。citeturn49search0turn49search1turn49search5turn49search2turn49search14