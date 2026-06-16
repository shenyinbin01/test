# Extracted Generic Deltas - ch001_batch_01

Sources:
- `candidates/candidate_01.md` through `candidate_10.md`
- `score_matrix.md`
- `top3.md`
- `recommended_output.md`
- `recommendation_reason.md`
- external/editor audit direction from `cases/ch001/03_editor_critique.md` and `cases/ch001/04_skill_delta.md`

Purpose:
Extract reusable Renderer Skill lessons from the batch run without importing case-specific story elements into the generic skill.

## Delta 1: 人物鲜活来自身份约束下的判断

1. Observed Pattern：
高分候选不是靠更多情绪词、尴尬反应或俏皮话让主角变活，而是让主角在压力中持续做符合身份的判断：先确认异常，再核验边界，再决定下一步。

2. Case Evidence：
candidate_05、candidate_08、candidate_10 都让江离通过追问、核验、保留物证、规划判定路径呈现性格。candidate_02 的轻幽默有效，但也暴露出语气过轻时会稀释大场面压力。

3. Generic Rule：
人物鲜活感应优先来自“这个人会如何判断、取舍、克制和行动”，而不是来自额外添加的生活化动作、现代吐槽或旁人尴尬。角色反应必须受身份、经验、当前压力约束。

4. Scope：
generic_skill_candidate

5. Risk：
合入后可能把所有主角都写成冷静推理型，削弱本来应该外放、冲动或情绪化的人物声音。

6. Regression Test Idea：
给 Renderer 一个荒诞任务或高压反差种子，检查正文是否至少包含一次“符合主角身份的判断或选择”。同时检查是否用通用尴尬、小动作、顺口吐槽替代判断。

## Delta 2: 旧资源要证明价值，不要只做道具清单

1. Observed Pattern：
礼包段有效时，不是因为列出了低阶物品，而是证明了这些物品“当年有重量、现在已过时、但仍能作为任务证据或情绪锚点”。无效风险是变成库存盘点或怀旧说明。

2. Case Evidence：
candidate_06 的礼包段最强，因为它把聚气丹、止血散、基础掌法和五百年前的处境连上。recommended_output 保留了“每一样都没用 / 每一样又都曾经有用”的结构方向，并进一步让礼包成为系统识别五百年前的证据。

3. Generic Rule：
当剧情出现迟到、过期、错位或低阶资源时，Renderer 应写出资源的三层功能：过去为什么有价值、现在为什么错位、它如何推动当前选择。不能只罗列资源名和品阶。

4. Scope：
generic_skill_candidate

5. Risk：
可能诱导每个道具都配一段回忆，造成节奏拖慢、解释膨胀。

6. Regression Test Idea：
给定“过期奖励 / 迟到信物 / 低阶装备”类种子，检查正文中每个重点资源是否服务于人物判断或任务推进。若只列物品、品阶、数量而不改变选择，则判为误用。

## Delta 3: 旧冲突要同时成立“当时重量”和“当前错位”

1. Observed Pattern：
旧仇有效时，不是把旧敌人重新拔高成大反派，也不是把旧事轻飘飘抹掉，而是让读者理解：它当年确实压过主角，现在却和主角当前层级形成荒诞错位。

2. Case Evidence：
candidate_08、candidate_10 能让江一星既不是新主线大 Boss，也不是纯笑话。candidate_09 低解释很干净，但自评指出情绪厚度不足，说明旧冲突若只保留任务功能，会缺少人物重量。

3. Generic Rule：
处理“旧敌、旧债、旧失败”时，要同时交代过去的压迫尺度和现在的层级变化。旧冲突的现在价值来自错位，而不是重新膨胀旧敌强度。

4. Scope：
generic_skill_candidate

5. Risk：
合入后可能导致所有旧冲突都插入回忆段，拖慢章首推进；也可能过度强调过去，削弱当前主线压力。

6. Regression Test Idea：
给定“多年后重遇旧敌 / 迟来的复仇任务”种子，检查正文是否同时有过去压力和当前错位。若只写旧恨、不写当前层级；或只写荒唐、不写旧事重量，均判为不足。

## Delta 4: 荒唐任务要认真执行

1. Observed Pattern：
最有效的钩子来自角色把荒唐任务当成真实规则来拆解，而不是把荒唐任务当段子消费。读者兴趣来自“他会怎么合法完成这个不可能目标”。

2. Case Evidence：
candidate_07 的钩子得分最高，因为它把坟、牌位、族谱、旧演武场都变成可测试锚点。candidate_10 的综合版进一步保留“摆擂 / 坟前备用方案”，让荒唐落在可执行步骤上。

3. Generic Rule：
当任务、规则或目标荒唐时，人物应严肃寻找可执行路径。喜剧感应来自认真执行和规则边界试探，而不是来自角色只吐槽任务离谱。

4. Scope：
generic_skill_candidate

5. Risk：
可能把章节写成规则解谜，降低动作场面、情绪爆发和网文爽点密度。

6. Regression Test Idea：
给定荒唐任务种子，检查章尾是否形成清晰下一步行动，而不是停在“这很离谱”的感慨。另检查过程是否保留人物压力，不把任务完全变成智力题。

## Delta 5: 规则载体少解释，错位由人物发现

1. Observed Pattern：
系统越像客服，错位越被解释掉；系统越只给任务、条件和有限反馈，人物越有空间展示判断。有效候选让江离通过追问发现规则缝隙。

2. Case Evidence：
candidate_05 的问答节奏被评为“系统不客服，错位由江离问出来”。recommended_output 保留系统短、硬、少信息的回答方式。上一轮审计也指出系统主动诊断和补救会把荒诞变成流程排障。

3. Generic Rule：
当信息载体是系统、公告、规则、榜单、考试或权威通知时，默认不要让它过早解释自身错位或主动给替代方案。错位应优先由人物追问、核对、试探或行动失败暴露。

4. Scope：
generic_skill_candidate

5. Risk：
可能误伤“智能系统拟人协商”“毒舌器灵”“导师型 AI”等题材，让本该主动互动的角色变哑。

6. Regression Test Idea：
检查信息载体在本章设定中是否具备人格和主动协商功能。若没有，禁止其自我诊断、主动补偿、列替代完成路径；若有，则要求主动解释也必须制造新冲突，而不是直接消解冲突。

## Delta 6: 防摆锤继承要显式保留旧优点

1. Observed Pattern：
本轮成功不在于单点增强“人物鲜活”，而在于 candidate_10 同时保住压力开场、礼包落差、系统僵硬、任务目标、章尾钩子。低分风险多来自新反馈挤压旧优点。

2. Case Evidence：
score_matrix 中 candidate_10 的“防摆锤”为 10，推荐理由明确指出旧优点没有被新反馈打爆。candidate_02、candidate_03 虽更活或更轻巧，但分别有压力被稀释、喜剧压过世界危机的风险。

3. Generic Rule：
每次根据新反馈重写时，应先识别并锁定上一版有效资产，再只对目标问题做局部增益。新增优点不能牺牲核心剧情任务、既有压力尺度和已验证的钩子。

4. Scope：
generic_skill_candidate

5. Risk：
可能让 Renderer 过于保守，只会小修小补，缺少必要的大幅重构。

6. Regression Test Idea：
对比重写前后，检查核心事件、压力来源、人物目标、章尾承诺是否仍存在。若新稿解决了单一反馈但删除旧稿的主要爽点或钩子，判为摆锤失败。

## Delta 7: 支撑角色只能加压或折射，不能替作者解释

1. Observed Pattern：
张前辈作为外部反应位有效时，可以折射江离状态和世界压力；过量时会变成解释工具或抢走主线注意力。

2. Case Evidence：
candidate_02 自评指出张前辈桥段略抢。recommendation_reason 也提示下一轮要防止张前辈变成解释工具。candidate_10 中他主要承担反应、追问和确认风险，未取代江离判断。

3. Generic Rule：
配角在高概念开章中应承担加压、误读、折射身份、推动下一步这类功能。不能让配角替作者解释设定、替主角总结主题，或靠旁人尴尬制造人味。

4. Scope：
generic_skill_candidate

5. Risk：
可能削弱群像和社交场景，使章节过度单人化。

6. Regression Test Idea：
抽查配角对白：每句是否改变压力、信息、选择或关系状态。若只是复述设定、解释主角心理、重复读者已知信息，则判为误用。

## Delta 8: 低解释有效，但必须保留情绪证据

1. Observed Pattern：
低解释能提升自然度和推进速度，但如果缺少能证明情绪重量的具体证据，人物会显得干。

2. Case Evidence：
candidate_09 自评为“推进干净”，但问题是情绪厚度较少。candidate_06 的礼包证据增强了人物重量，但又有推进偏慢风险。recommended_output 采用折中：保留少量关键旧物证据，再回到任务推进。

3. Generic Rule：
减少解释时，不等于删除人物反应。Renderer 应用少量可验证的场景证据承载情绪，再尽快回到行动。

4. Scope：
generic_skill_candidate

5. Risk：
可能被误用成“每段都要放一个象征物”，导致刻意和做作。

6. Regression Test Idea：
检查低解释稿是否仍有至少一个具体证据能支撑人物反应。若只剩任务流程，无过去重量、当前代价或选择后果，则判为干稿。

## Delta 9: 案例方案不得直接通用化

1. Observed Pattern：
“坟、牌位、族谱、坟前跳舞、新手礼包打死人”等方案在本案有效，是因为本章特定种子绑定了五百年前旧仇、目标死亡、系统迟到和任务判定。

2. Case Evidence：
candidate_07、candidate_10 的章尾方案强，但强在“江一星已死且系统仍要求战胜”的特例。如果把这些元素直接写入通用 Skill，会污染其他题材。

3. Generic Rule：
通用 Skill 只能沉淀“用可识别锚点测试规则边界”“荒唐任务认真执行”这类抽象原则，不沉淀具体执行物：坟、牌位、族谱、舞步、江一星、新手礼包等。

4. Scope：
case_specific_only

5. Risk：
若误合入 Skill，会导致后续 Renderer 在无关题材中机械复用坟墓、牌位、象征性战胜等桥段。

6. Regression Test Idea：
后续审核 Skill Delta 时扫描是否出现本案专名或具体桥段。如果出现“坟头跳舞”“牌位摆擂”“江一星”等案例执行物，应退回为案例笔记，不进通用 Skill。

## Delta 10: “鲜活感 = 更多玩笑或现代吐槽”应拒绝

1. Observed Pattern：
少量冷幽默能增加人物光泽，但一旦人物主要承担吐槽功能，就会稀释压力和身份感。

2. Case Evidence：
candidate_02 的人味强，但自评提示轻松语气可能稀释飞升压力。上一轮审计也明确反对用俏皮收尾、旁人尴尬替代人物判断。

3. Generic Rule：
不能把“人物鲜活”理解为增加现代吐槽、段子反应、可爱小动作或旁人尴尬。幽默必须建立在人物判断、身份错位或行动方案上。

4. Scope：
reject

5. Risk：
如果合入为正向规则，会把高压开章改成段子表演，使主角脱离世界观语境。

6. Regression Test Idea：
检查新增幽默句是否改变判断、推进任务或强化身份错位。若删掉该句不影响行动，且只提供现代口吻或轻浮感，应判为误用。

