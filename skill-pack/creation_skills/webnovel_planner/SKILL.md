---
name: webnovel_planner
description: "webnovel-hermes-wps 规划角色 Skill — 生成 Story Bible、前 N 章章节大纲、单章 chapter beat、维护读者期待债规划。不写正文，不审稿，不润色，不同步 WPS。"
tags: ["webnovel", "planner", "outline", "beat", "phase7", "phase8"]
---

# webnovel_planner Skill

## 用途

为创作链路提供剧情规划输入。Planner 的输出是 Writer 的唯一写作依据。

## 适用场景

1. 新项目启动时生成 Story Bible
2. 连载过程中生成新的前 N 章大纲
3. 每章开始前生成该章 chapter beat
4. 用户有剧情讨论需求时参与规划讨论
5. 维护 reader_debts 的规划部分（不直接修改文件）

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| project.yaml | `project.yaml` | ✅ |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | 可选 |
| runtime_canon | `.story-system/runtime_canon.yaml` | 可选 |
| reader_debts | `.story-system/reader_debts.yaml` | 可选 |
| 已有 outline | `outlines/chapters_001_030.yaml` | 可选 |
| 已有 beats | `outlines/beats/` | 可选 |
| 用户任务说明 | Hermes 传入 | ✅ |

## 输出

| 输出 | 路径 |
|------|------|
| Story Bible | `.story-system/MASTER_SETTING.yaml` |
| 前 N 章大纲 | `outlines/chapters_001_030.yaml` |
| 单章 beat | `outlines/beats/chapter_XXX.yaml` |
| 章节上下文 | `.webnovel/context/chapter_XXX_context.yaml`（可选） |

## 允许读取路径

- `project.yaml`
- `.story-system/`
- `outlines/`
- `.webnovel/context/`（如存在）
- `templates/prompts/`（仅读取 Prompt 模板）

## 允许写入路径

- `.story-system/MASTER_SETTING.yaml`
- `outlines/`
- `.webnovel/context/`

## Story Bible 增强字段（Phase 8 注入）

生成 Story Bible 时，必须包含以下三个新增字段。它们是让主角有"发动机"的核心结构。

### 1. protagonist_cognitive_advantage（认知优势）

**定义**：主角相对世界、敌人、配角、读者预期的高维认知优势。主角在某个具体领域比他人多知道一层真相（系统规则、世界机制、上层博弈逻辑）。

**格式**：
```yaml
protagonist_cognitive_advantage:
  domain: ""           # 优势领域（如：规则本质、历史真相、力量本源）
  advantage: ""        # 具体优势描述（主角知道什么别人不知道的事）
  revelation_plan: ""  # 如何在剧情中逐步展示（不写成旁白解释）
```

**要求**：
- 优势只覆盖特定领域，主角在其他方面可以无知甚至犯错
- 优势不是"全知全能"，是有边界的
- 展示方式通过动作、决策、对话中的"反常选择"，不旁白解释

### 2. internalized_pressure（内在代价）

**定义**：主角能力、身份、优势或选择带来的内在代价。代价必须是能力的同源产物，不是外部敌人制造的困难。

**格式**：
```yaml
internalized_pressure:
  source: ""          # 代价源（能力的副作用 / 身份的撕裂 / 选择的不可逆代价）
  manifestation: ""   # 代价如何具体体现（选择受限 / 情感矛盾 / 身体代价 / 关系代价）
  escalation: ""      # 代价如何在剧情中渐进加深
```

**要求**：
- 代价必须影响剧情选择，不能是口号式的"他感觉累"
- 代价不能是无关附加物（如"他很强但他妈妈病了"——除非能力本身就来自母亲牺牲）
- 代价让爽点更有重量，不是削弱爽点

### 3. revelation_phases（世界观揭秘阶段）

**定义**：世界观、规则、真相、敌人系统如何分阶段揭示。每阶段有一个核心谜面和一个核心谜底，谜底揭示时必须伴随剧情转折。

**格式**：
```yaml
revelation_phases:
  - phase: 1
    mystery: ""       # 本阶段核心谜面（让读者好奇的问题）
    answer: ""        # 本阶段核心谜底
    trigger: ""       # 揭示触发条件（伴随什么剧情转折）
    deeper_mystery: "" # 揭示后带出的更深层谜面
  - phase: 2
    # ...
```

**要求**：
- 每卷至少 1 个谜面 + 1 个谜底
- 最长谜面不超过 2 卷（否则读者忘记谜面）
- 最后一次揭示必须是故事高潮的一部分
- 最大秘密在最高冲突点揭晓

---

## Human Texture beat 约束（实验 v0）

Human Texture 不是普通"去 AI 味"，目标是让机制压力落到人物选择、关系、场景和后果上。生成单章 chapter beat 时，可附加一个轻量 `human_texture` block：

```yaml
human_texture:
  focus_fields: [] # 每章最多 2-3 个
  private_want: ""
  shame_or_avoidance: ""
  relationship_debt_change: ""
  scene_resistance: ""
  information_carrier: ""
  consequence_next_friction: ""
  carry_forward:
    relationship_debt: []
    consequence: []
```

**字段限制**：`focus_fields` 只能从 `private_want` / `shame_or_avoidance` / `relationship_debt_change` / `scene_resistance` / `information_carrier` / `consequence_next_friction` 中选择，每章最多 2-3 个，不强行写满。

**Planner 职责**：
- 选择本章最关键的 Human Texture 字段，并让它们服务 beat / hook / payoff / rule-breaking / cost
- 维护可继承的关系债与后果账；没有下一章用途的关系变化不要写入
- 为重要信息揭示指定 `information_carrier`，避免默认依赖权威公告或旁白说明

**Planner 不负责**：写正文、写心理细节、临时文学化、替 Writer 生成具体句子。

---

## 禁止行为

1. 不写正文
2. 不审稿
3. 不润色
4. 不更新 runtime_canon
5. 不生成 chapter_commit
6. 不同步 WPS
7. 不跳过用户确认直接写入已有的 MASTER_SETTING
8. 不修改已有 chapter_commits
9. 不编辑已有 draft / final
10. 不决定章节是否通过验收

## 执行步骤

1. Hermes 传入任务说明（新项目 / 续写 / 剧情讨论）
2. 读取所有可选输入（如存在）
3. 如为新项目，生成 Story Bible：
   a. 调用 DeepSeek，传入 project.yaml + 设定上下文，生成 Story Bible JSON
   b. **必须包含 protagonist_cognitive_advantage（认知优势）、internalized_pressure（内在代价）、revelation_phases（揭秘阶段）三个字段**
   c. 校验 JSON 结构完整性（project / story_synopsis / characters / world / outline / protagonist_cognitive_advantage / internalized_pressure / revelation_phases）
   d. 转写为 MASTER_SETTING.yaml 格式
   e. 检查 canon_check（无内部矛盾、无禁词、符合约束）
   f. 写入 `.story-system/MASTER_SETTING.yaml`
4. 如需要生成大纲，调用 DeepSeek 生成前 N 章 outline → 写入 `outlines/chapters_001_030.yaml`
   - 大纲的卷/阶段设计必须体现 revelation_phases 的分阶段揭示
5. 如需生成单章 beat，读取 outline + runtime_canon + reader_debts，调用 DeepSeek 生成 chapter beat → 写入 `outlines/beats/chapter_XXX.yaml`
   - 每个 chapter beat 必须标注：
     - `cognitive_advantage_triggered`: 本章是否触发主角认知优势（true/false）
     - `pressure_deepened`: 本章是否加深内在代价（true/false）
     - `revelation_progress`: 本章是否推进一个揭秘点（true/false + 描述）
   - 如本章存在关系破裂、信息揭示、情绪代价、规则公告或章尾大钩子，可附加 `human_texture` block；其中 `focus_fields` 最多 2-3 个，且 `relationship_debt_change` / `consequence_next_friction` 必须能进入下一章计划
6. 如需生成上下文，写入 `.webnovel/context/chapter_XXX_context.yaml`
7. 向 Hermes 报告输出文件路径

## 失败处理

1. project.yaml 不存在 → 停止并报告，要求创建
2. 生成 beat 但 outline 不存在 → 先建议生成 outline，不强制
3. DeepSeek 输出截断 → 重试最多 1 次
4. 写入路径不存在 → 自动创建目录

## 验收标准

1. MASTER_SETTING.yaml 包含可用设定，**且包含 protagonist_cognitive_advantage、internalized_pressure、revelation_phases 三个字段**
2. outline 有完整主线路线图，且体现 revelation_phases 的分阶段设计
3. chapter beat 包含 4-6 个场景，**且标注 cognitive_advantage_triggered / pressure_deepened / revelation_progress**
4. 所有输出与已有 canon 无冲突
5. 未写入任何正文内容
6. 未修改任何已有正文文件
7. 如输出 `human_texture`，字段不超过 2-3 个重点，且不是抽象口号或正文模板

## 与其他 Skill 的关系

- **webnovel_writer**: Planner 的输出 beat 是 Writer 的唯一写作输入
- **webnovel_state_manager**: Planner 不替代 StateManager 的职责，不更新 runtime_canon
- **detect_webnovel_ai_flavor / webnovel_reviewer / webnovel_polisher**: Planner 的 beat 供 Reviewer 判断章节是否按规划执行
- **webnovel_wps_sync**: Planner 不同步 WPS
