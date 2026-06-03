# Paper And Method Notes

调研日期：2026-06-03

本文件不堆论文摘要，只提炼对 Human Texture Engine 可执行的结论。

## 资料范围

重点参考：

- Dramatron / Co-Writing Screenplays and Theatre Scripts with Language Models。
- Wordcraft / Story Writing With Large Language Models。
- CoAuthor / Human-AI collaborative writing dataset。
- TaleBrush / sketch-based story generation。
- Verbalized Sampling / 用显式采样意图提升多样性。
- creative writing benchmark / pairwise story comparison。
- 行业编辑工具与 AI detector 的公开方法。

## AI 小说最常见的问题

1. 目标清楚但经历感弱：AI 能把“发生了什么”写明白，却常跳过人物如何承受。
2. 情绪被命名：文本直接说恐惧、愤怒、痛苦，而不是让它改变人物下一句怎么说、手怎么放、谁被疏远。
3. 信息过度显性：设定、规则、真相经常由系统、公告、长对白或权威人物直接交代。
4. 人物工具化：配角承担提示、质问、反对、作证、解释功能，却没有自己的尴尬、亏欠、误判、私心。
5. 场景像舞台：地点只为剧情服务，缺少“此地原本如何运转”的生活噪声。
6. 后果重置：受伤、失信、恐惧、羞耻出现后，下一段又回到推进情节。
7. 语言均匀：句子顺滑、逻辑整洁、转折有条理，但缺少真实说话和真实回忆中的毛边。
8. 结构过度服从钩子：每章都能吊读者，但人的余波经常被下一个设定爆点盖掉。

## 人类如何识别 AI 小说

人类通常不是因为某个词识别 AI，而是因为整套叙事行为不符合人类经验：

- 人物总在恰当时刻说出剧情需要的信息。
- 场景里的细节都“有用”，没有多余却真实的生活痕迹。
- 情绪总是被解释得太完整，没有沉默、误会、回避、嘴硬、事后补偿。
- 冲突结束太干净，关系不黏，伤害没有残留。
- 比喻和总结句像“主题阐释”，不是人物当下能感到的东西。
- 所有人都围绕主线移动，没有自己的小算盘。

因此 Human Texture 的判断单位不能只看句子，而要看：一场戏里人物是否有不便明说的欲望，关系是否被消耗，场景是否像本来就存在。

## AI 写作为什么容易同质化

可操作解释：

- 训练与对齐让模型偏向平均、清楚、无冒犯、逻辑完整的表达。
- prompt 往往奖励“把规则讲清楚”，不奖励“让人物在不完全理解中行动”。
- 单次生成缺少真实生活记忆，模型会用通用模板填补空白。
- 长篇 agent 为了维护一致性，会进一步收紧表达，把复杂人性压成可追踪字段。
- Reviewer 如果只评钩子、节奏、设定和爽点，会把文本推向更高效的机制展示。

Human Texture Engine 要反向引入“不完全”：人物不完全坦白，情绪不完全消化，关系不完全修复，信息不完全公告。

## 专业作者怎么编辑 AI 文本

可转化为工程步骤：

1. 先问“这场戏里谁最不想被看见什么”，而不是先改句子。
2. 给配角一个与主线不完全一致的小目标。
3. 把公告信息改成行动中被误读、偷听、交换、隐瞒、试探出来的信息。
4. 给代价安排后续账：身体账、关系账、声誉账、资源账、时间账。
5. 保留一个非工具细节，但让它贴着人物处境，不做散文化装饰。
6. 删除主题总结句，把判断交给场景动作。
7. 把“情绪名称”改成“情绪造成的错误选择或迟滞”。

这说明 Human Texture 不应是 Polisher 的 synonym rewrite，而应从 Planner 生成时就分配人物私心和后果。

## 人机共创系统怎么保留作者声音

从 Dramatron、Wordcraft、CoAuthor、TaleBrush 类系统得到的结论：

- AI 输出更适合当候选材料，而不是最终作者。
- 人类作者需要控制：角色选择、场景顺序、信息保留、哪些句子不说。
- 可视化/结构化草稿能帮助作者挑方向，例如情绪曲线、场景卡、人物关系账。
- 系统应记录作者接受/拒绝哪些改动，逐步形成项目内声音，而不是一次性模仿某位作者。

对本项目的落地：

- Human Texture Packet 应先由 AI 生成候选，再由 Reviewer/人工审查。
- 不做“作者风格复制”，而做“项目声音一致性”：人物怎样嘴硬，叙述怎样克制，网文爽点怎样不牺牲人味。

## 可操作评价维度

建议把评价拆成三层：

结构层：

- 人物是否有自己的私心和避讳。
- 代价是否造成后续账。
- 信息是否通过冲突、误解、物件、制度、旁观者自然露出。

场景层：

- 场景是否有生活功能，不只是剧情功能。
- 配角是否有个人 agenda。
- 情绪是否改变动作、选择、关系。

语言层：

- 是否存在过度总结句。
- 句式是否过于均匀。
- 是否有贴身但不过度装饰的细节。

本项目的完整 rubric 见 `human_texture_evaluation_rubric.md`。

## 对当前小说工程的启发

现有 Phase 8 已经证明 Planner / Writer / Reviewer 能稳定执行机制和爽点。下一步不是降低规则密度，而是在每个规则节点绑定一个人物层成本：

- 规则揭示必须有信息载体和误读风险。
- 破局必须消耗关系、身体、声誉或时间。
- 钩子之后必须留下人的余波。
- 配角出场必须带私心，不能只带功能。
- Reviewer 不能只判“有效”，还要判“是否像人在承受”。

## 主要来源

- Dramatron repo: https://github.com/google-deepmind/dramatron
- Dramatron paper: https://arxiv.org/abs/2209.14958
- CoAuthor paper: https://arxiv.org/abs/2201.06796
- TaleBrush paper: https://dl.acm.org/doi/10.1145/3491102.3501813
- Verbalized Sampling repo: https://github.com/CHATS-lab/verbalized-sampling
- Creative Story-Writing Benchmark: https://github.com/lechmazur/writing
