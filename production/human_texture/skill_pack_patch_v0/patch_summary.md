# Human Texture Skill Pack Prompt Patch v0

分支：`experiment/human-texture-skill-pack-v0`

## 目标

本 patch 将 Human Texture compact packet 的最小合同接入 Planner / Writer / Reviewer / Polisher。

Human Texture 不是普通“去 AI 味”。它的目标不是让句子更花、更口语，而是让正文从“机制展示故事”变成“人在机制压力下做选择，并留下关系、情绪、场景和后果”。

## 修改范围

只修改 4 个正式 skill 文件：

- `skill-pack/creation_skills/webnovel_planner/SKILL.md`
- `skill-pack/creation_skills/webnovel_writer/SKILL.md`
- `skill-pack/creation_skills/webnovel_reviewer/SKILL.md`
- `skill-pack/creation_skills/webnovel_polisher/SKILL.md`

新增本说明目录：

- `production/human_texture/skill_pack_patch_v0/`

## Planner 最小接入

新增 `Human Texture beat 约束（实验 v0）`：

- chapter beat 可附加 `human_texture` block。
- 每章 `focus_fields` 最多 2-3 个。
- 可选字段限制为 6 个：
  - `private_want`
  - `shame_or_avoidance`
  - `relationship_debt_change`
  - `scene_resistance`
  - `information_carrier`
  - `consequence_next_friction`
- Planner 负责选字段、维护关系债/后果账、指定信息载体。
- Planner 不负责写正文、心理细节或临时文学化。
- 信息揭示不得默认依赖权威公告或旁白说明。
- 关系债与 consequence 必须能进入下一章计划。

## Writer 最小接入

新增 `规则五：Human Texture compact brief（实验 v0）`：

- Writer 接收 `human_texture` 后，不逐项显性解释字段。
- 字段必须转成行为、误读、场景阻力、选择或后果。
- 禁止靠风景、比喻、口语化或装饰性细节假装有人味。
- 情绪节点每个情绪最多一个动作后果。
- 信息公告节点优先使用人、物、制度缝隙、误读和代价作为信息载体。
- 章尾钩子必须保留人物承受点，但不能削弱钩子。
- 不得为了人味牺牲网文推进、规则破局、爽点、设定揭示和节奏。

## Reviewer 最小接入

新增 `Human Texture gate（实验 v0）`：

- 检查 `focus_fields` 是否执行。
- 检查 webnovel function 是否保留。
- 判断失败应退回 Planner / Writer / Polisher。
- 结构性空心不得交给 Polisher。
- 信息公告无代价，退回 Planner / Writer。
- 情绪代价无行为后果，退回 Writer。
- 章尾钩子吞掉人物余波，退回 Planner / Writer。
- 人物仍是功能件、关系债或后果无继承，退回 Planner。
- 语言粗糙但结构有效，才允许进入 Polisher。

## Polisher 最小接入

新增 Human Texture gate 边界：

- 如果 `human_texture_review.gate` 不是 `pass_to_polisher`，不得进入 Polisher。
- Polisher 可以压缩显性说明、调整重复句式、增强已有章尾留白、让已有动作和对话更贴人物状态。
- Polisher 不可以补人物私心、补关系债、重排信息露出、补代价后果、重写场景生活逻辑。
- Polisher 不得用风景、比喻、口语化假装有人味。
- Polisher 不得把结构性失败润色成顺滑失败。

## 非目标

- 不改 Phase 8 craft assets。
- 不新增 approved_patterns。
- 不修改正文。
- 不读取 `corpus/dachengqi`。
- 不启动正式 Polisher 链路。
- 不改变原有 Phase 8 技法链路。
- 不把 skill-pack 改成文学理论库。

## 建议下一步

进入五片段回归测试。测试只使用 dry run 中的 5 个片段，不运行完整五章生成，不启动正式 Polisher 链路。
