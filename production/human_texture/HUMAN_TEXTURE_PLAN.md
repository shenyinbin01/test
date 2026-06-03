# Human Texture Engine Plan

日期：2026-06-03

## 1. 这个项目要解决什么问题

当前小说工程已经能执行：

- 开章钩子。
- 规则展示。
- 认知优势。
- 规则破局。
- 代价。
- 设定揭示。
- 五章连续推进。

但当前 5 章验证样本显示，文本仍然像“系统展示故事机制”，而不是“人在经历故事”。Human Texture Engine 要解决的是叙事质感问题：

- 人物像功能件。
- 情绪被命名和系统化，没有真实后果。
- 场景只服务信息，不像有人生活。
- 设定像公告。
- 代价没有后续账。
- 关系缺少黏性。
- 语言顺滑但无余味。

项目目标不是让句子更花，而是让每个机制节点都被人物私心、羞耻、关系摩擦、生活阻力和后果账承载。

## 2. 为什么它不是普通“去 AI 味”

普通“去 AI 味”通常处理：

- 句式均匀。
- 词语重复。
- 转折太整齐。
- 口语化不足。
- AI detector 风险。

Human Texture 处理的是更底层的叙事行为：

- 谁不想被看见什么？
- 谁有私心但不敢说？
- 谁因为主角的选择被伤害或误解？
- 这个场景在主线之外如何运转？
- 信息为什么此刻露出，谁为此付出代价？
- 破局之后主角失去了什么，下一章哪里变难？

如果 Planner 没有分配这些东西，Polisher 再怎么改句子，也只是把空心文本改得更顺。

## 3. 行业内有哪些可借鉴方案

借鉴原则不是“谁名气大就抄谁”，而是看它是否解决了本项目的一个真实子问题。

可借鉴：

- Sudowrite / Novelcrafter / NovelAI：借鉴 Story Bible、Codex、Lorebook、Memory 的结构化上下文，不借鉴一键生成。
- Fictionary / AutoCrit / ProWritingAid：借鉴编辑审查问题，不借英文句法统计。
- Dramatron / Wordcraft / TaleBrush / CoAuthor：借鉴 human-in-the-loop 和 co-writing 定位，即 AI 生成候选，人类/Reviewer 做选择。
- Creative writing benchmark：借鉴 pairwise A/B 评价，不把 detector 分数当文学质量。
- AI detector / humanizer：只作为反面参照，提醒不要把目标变成“骗检测器”。

结论：

- 行业工具能提供 workflow 和上下文容器。
- 人味评价和中文网文嵌入必须自研。

## 4. GitHub 上有哪些可复用项目

本轮按 8 个筛选轴选择项目：任务相关性、代码可读性、长篇状态能力、agent 分工、人味相关信号、中文网文迁移性、可复现实验价值、活跃度与风险。

重点深读：

- [NovelGenerator](https://github.com/KazKozDev/NovelGenerator)：最值得借鉴 StoryContextDB、CharacterKnowledge、ReaderKnowledge、PlannedRevelation、anti-LLM prompt。它明确要求 personal agenda、micro detail、imperfect moment。
- [knowrite](https://github.com/knoai/knowrite)：最值得借鉴多阶段 novel engine、author/voice fingerprint、character memory、temporal truth、fitness evaluator、governance。
- [novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot)：最值得借鉴轻量 context/memory/skills 组织方式，适合作为实验项目。

补充借鉴：

- [NovelClaw](https://github.com/iLearn-Lab/NovelClaw)：借鉴 memory bank、storyboard、多 agent workspace。
- [Dramatron](https://github.com/google-deepmind/dramatron)：借鉴 co-writing 定位和层级生成。
- [pulpgen](https://github.com/muckelverk/pulpgen)：可做轻量可复现实验。
- [lechmazur/writing](https://github.com/lechmazur/writing)：借鉴 pairwise story comparison。

不建议直接 fork：

- 大型 UI/IDE 或平台类项目工程面太重。
- 通用 humanizer 项目不能解决本项目核心。

完整调研见 `research/github_project_survey.md`。

## 5. 我们是否应该自研

建议自研。

理由：

1. 当前工程已有 Planner / Writer / Reviewer / Polisher，不需要换底座。
2. 外部项目没有直接处理中文网文的核心矛盾：机制爽点必须保留，但人味不能被机制吞掉。
3. Human Texture 是叙事合同，不是通用生成器功能。
4. 当前失败样本已经足够定义第一版问题集，不需要全量 corpus。
5. 自研可以保持与 approved craft assets、Phase 8 skill injection、现有 reviewer 报告兼容。

自研不是从零造全套 agent，而是在现有工程上增加一层可审查的 Human Texture 合同。

## 6. 自研的话最小版本是什么

Human Texture MVP：

### 输入

- 当前 chapter plan。
- 上一章 summary / state。
- 相关 approved patterns。
- skill-pack Planner / Writer / Reviewer 输出。
- 当前 Human Texture rubric。

### 核心中间产物

`human_texture_packet`：

```yaml
human_texture_packet:
  chapter_id: ""
  pov_character:
    private_want: ""
    shame_or_avoidance: ""
    imperfect_choice: ""
  key_side_characters:
    - name: ""
      visible_function: ""
      private_agenda: ""
      relationship_debt_change: ""
  scene_texture:
    scene_life_function: ""
    scene_resistance: ""
    non_instrumental_detail: ""
  information_exposure:
    key_info: ""
    carrier: ""
    who_misreads_it: ""
    exposure_cost: ""
  consequence_ledger:
    inherited_cost: ""
    new_cost: ""
    next_chapter_friction: ""
  human_aftertaste_beat: ""
```

### 输出

- 给 Writer 的人味写作 brief。
- 给 Reviewer 的 10 维评分。
- 给 Polisher 的语言余味建议。
- 给下一章 Planner 的关系债 / 后果账。

### 不做

- 不自动重写整章。
- 不生成新 approved patterns。
- 不替换现有 Planner / Writer / Reviewer。
- 不读全量原文 corpus。

## 7. 如何嵌入现有 Planner / Writer / Reviewer / Polisher

Planner：

- 在现有 beat plan 后增加 `human_texture_packet`。
- 每个机制节点必须绑定人物选择、信息载体、代价后果。
- 每章继承至少一笔上一章后果。

Writer：

- 按 packet 写具体行为，不直接解释“他很痛苦/她很失望”。
- 把非工具性细节嵌进人物处境。
- 把公告信息改写成行动中露出。

Reviewer：

- 使用 10 维 rubric 打分。
- 对低分项明确退回层：Planner、Writer 或 Polisher。
- 如果系统展示感、代价后果、人物功能件任一项低于 3 分，不进入 Polisher。

Polisher：

- 只做语言光泽、句式重复、章尾余味。
- 如果缺人物私心、关系债、后果账，必须退回，不做硬救。

Detector：

- 现有 `detect_webnovel_ai_flavor` 可作为语言风险辅助，但 Human Texture rubric 是更高优先级。

完整嵌入方案见 `integration/integration_with_existing_skill_pack.md`。

## 8. 需要哪些样本库

第一阶段不需要全量原文 corpus，需要小而精准的样本库：

1. 人物私心样本库：主角/配角不便明说的欲望、羞耻、嘴硬、误判。
2. 关系债样本库：隐瞒、误会、救命、作证、背叛、补偿、试探。
3. 代价后果样本库：身体账、声誉账、资源账、时间账、心理账、关系账。
4. 场景生活质感样本库：饭堂、寝舍、宗门广场、矿洞、药圃、排队、杂役制度。
5. 信息自然露出样本库：公告被撕、谣言传错、饭桌偷听、制度漏洞、物件痕迹、旁观者误读。
6. 负样本库：系统展示、功能件人物、公告化信息、情绪命名、代价无后果。
7. 中文网文高密度爽点样本：确保人味不牺牲节奏。

每类 20-40 个片段即可启动 MVP，不需要全书原文。

## 9. 如何验证它真的让文本更像人

验证不要看 AI detector 分数，建议三层：

### Rubric 评分

- 对 baseline 与 Human Texture 版本分别用 10 维 rubric 打分。
- 关键指标：人物可信度、关系摩擦、信息自然度、代价后果、系统展示感。

### Pairwise 人审

- 同一章节给 A/B 两版。
- 盲评问题：哪一版更像人在经历故事？哪一版更有余味？哪一版仍像系统展示？

### 机制不降级检查

- 保留 Phase 8 原有指标：钩子、规则、破局、代价、章尾推动。
- Human Texture 版本不能为了“文学感”牺牲网文推进。

### 后果继承检查

- 检查下一章是否继承上一章至少一笔关系或身体后果。

## 10. 第一阶段应该做什么

建议第一阶段拆成 5 步：

1. 定稿 Human Texture rubric。
2. 用当前 5 章建立 baseline 标注：每章系统展示点、功能件人物、公告信息、潜力节点。
3. 建立小样本库，每类 20-40 条。
4. 做实验性 wrapper：输入 chapter plan，输出 `human_texture_packet`，不改 skill-pack。
5. 选 1-2 个片段做 A/B 验证，例如 C4 复检后柳青砚关系节点、C3 饭堂/矿洞信息露出节点。

阶段成功标准：

- Reviewer rubric 至少 7/10 维度提升。
- 人审多数选择 Human Texture 版本更像人在经历故事。
- 原有机制爽点不下降。

## 11. 哪些事情暂时不要做

暂时不要：

- 不要把 Human Texture 做成通用 humanizer。
- 不要直接 fork 外部大型项目。
- 不要上来改全套 skill-pack。
- 不要重写 5 章全稿。
- 不要启动 Polisher 试图救结构问题。
- 不要要求补传全量 corpus。
- 不要追求“文学化”而牺牲中文网文节奏。
- 不要用 AI detector 分数作为主指标。
- 不要新增 approved patterns，等 MVP 验证后再沉淀。

## 第一阶段交付物建议

- `human_texture_packet.schema.yaml`
- `human_texture_reviewer_prompt.md`
- `human_texture_writer_brief.md`
- `relationship_debt_ledger.yaml`
- `consequence_ledger.yaml`
- `sample_library/positive/*.md`
- `sample_library/negative/*.md`
- `ab_eval_report.md`

这些文件建议后续放在 `production/human_texture/experiment_mvp/`，本轮不创建，避免误以为已经进入实现阶段。
