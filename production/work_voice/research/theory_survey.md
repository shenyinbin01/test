# Theory Survey

本文件把叙事学概念翻译成 Work Voice 可用的工程字段。核心问题不是“像谁写”，而是“叙述者站在哪里，以及他如何稳定地对待主角、世界和读者”。

## 1. Narrator / 叙述者

- 概念解释：叙述者是文本中负责讲述事件的声音或位置，不等于现实作者。
- 和“作者在哪里”的关系：它直接回答“谁在说话”。稳定叙述者能让长篇输出有持续的讲述人格。
- 工程字段：`narrator_position`、`intervention_style`、`reader_relationship`。
- 网文意义：避免文本成为无立场摄像头，增强开篇钩子、爽点解释和荒诞事件承托。
- 参考：[The Living Handbook of Narratology](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 2. Focalization / 聚焦 / 谁在看

- 概念解释：聚焦区分“谁在看”和“谁在说”。叙述者可以讲，主角可以看，读者可以被引导看。
- 和“作者在哪里”的关系：决定叙述距离主角多近，信息是否通过主角感知进入文本。
- 工程字段：`protagonist_distance`、`pov_scope`、`information_access`。
- 网文意义：贴主角可提升沉浸和代入，站在世界上方可增强设定压迫和命运感。
- 参考：[Focalization - LHN](https://www-archiv.fdm.uni-hamburg.de/lhn/node/18.html)。

## 3. Narrative Voice / 叙述声音

- 概念解释：叙述声音是文本中可感知的讲述习惯、态度、节奏和关系。
- 和“作者在哪里”的关系：声音让读者感觉“有人在讲”，而不是系统在播报。
- 工程字段：`voice_type`、`sentence_rhythm`、`detail_bias`、`stable_flaw`。
- 网文意义：能稳定区分“冷眼爽文”“贴身成长”“荒诞吐槽”“史诗规则叙述”等讲法。
- 参考：[Narratology concepts - LHN contents](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 4. Narrative Distance / 叙述距离

- 概念解释：叙述者与角色经验之间的距离，可近到贴身意识，也可远到全知评判。
- 和“作者在哪里”的关系：决定叙述者是和主角一起困住，还是在主角上方解释局势。
- 工程字段：`protagonist_distance`、`world_attitude`、`commentary_density`。
- 网文意义：不同场景需要不同距离，打斗和破局常贴近行动，设定揭示常拉远到世界规则。
- 参考：[Computational Narratology - LHN](https://www-archiv.fdm.uni-hamburg.de/lhn/node/43.html)。

## 5. Point of View / 视角

- 概念解释：视角规定事件从谁的知识、感知和限制中呈现。
- 和“作者在哪里”的关系：视角是叙述站位的制度边界，决定叙述者能否越过角色认知。
- 工程字段：`pov_scope`、`knowledge_boundary`、`reader_knowledge_delta`。
- 网文意义：长篇爽点依赖信息差，视角边界能防止提前解释、系统公告和全知剧透。
- 参考：[The Living Handbook of Narratology](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 6. Implied Author / 隐含作者

- 概念解释：隐含作者是读者从文本整体推断出的价值取向、选择逻辑和叙事秩序。
- 和“作者在哪里”的关系：它不是现实作者，而是作品背后的稳定价值组织者。
- 工程字段：`world_attitude`、`moral_temperature`、`payoff_logic`。
- 网文意义：让爽点、制度、荒诞事件和主角选择有一致的作品判断，而非临时技巧堆叠。
- 参考：Wayne C. Booth 的 implied author 概念；叙事学入口见 [LHN](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 7. Free Indirect Discourse / 自由间接引语

- 概念解释：第三人称叙述与角色意识短暂融合，让角色的判断渗入叙述语言。
- 和“作者在哪里”的关系：它让叙述者既能保持第三人称，又能短暂贴到角色身体里。
- 工程字段：`thought_blending_mode`、`protagonist_distance`、`intervention_style`。
- 网文意义：适合降低“解释感”，把信息、羞耻、怨气、爽感和误判嵌入角色经验。
- 参考：[Speech Representation - LHN contents](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 8. Reader Relationship / 叙述者与读者关系

- 概念解释：叙述者可把读者当同谋、旁观者、学生、见证人、审判者或被戏弄对象。
- 和“作者在哪里”的关系：读者关系决定叙述者是否插嘴、解释、卖关子、嘲讽或留白。
- 工程字段：`reader_relationship`、`hook_style`、`withholding_rules`。
- 网文意义：连载文本尤其依赖读者关系，章节钩子和爽点可见度都由它调度。
- 参考：[Narrative communication concepts - LHN](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 9. Authorial Stance / 作者立场

- 概念解释：作品对角色、世界、制度、暴力、喜剧和爽点的稳定态度。
- 和“作者在哪里”的关系：它回答叙述者站在人物旁边、世界规则背后，还是读者旁边。
- 工程字段：`world_attitude`、`humor_mode`、`showoff_mode`、`stable_flaw`。
- 网文意义：同样的情节，冷眼、热血、戏谑、史诗、日常讽刺会产生完全不同的阅读感。
- 参考：叙事学和文体学通用概念；工程化时不绑定现实作者身份。
