# Modified Sections Index

本文件记录本次实验 patch 修改了哪些 `SKILL.md` 段落。

## 1. webnovel_planner

文件：`skill-pack/creation_skills/webnovel_planner/SKILL.md`

新增段落：

- `## Human Texture beat 约束（实验 v0）`

修改段落：

- `## 执行步骤`
  - 在生成单章 beat 的步骤中增加可选 `human_texture` block 检查。
- `## 验收标准`
  - 增加 `human_texture` 字段必须不超过 2-3 个重点，且不得是抽象口号或正文模板。

作用：

- Planner 可在 chapter beat 中输出 Human Texture compact packet。
- Planner 负责关系债、后果账和信息载体，但不写正文。

## 2. webnovel_writer

文件：`skill-pack/creation_skills/webnovel_writer/SKILL.md`

新增段落：

- `### 规则五：Human Texture compact brief（实验 v0）`

修改段落：

- `## 执行步骤`
  - 在调用模型前检查 `human_texture.focus_fields` 是否不超过 3 个。
  - 在草稿检查中增加字段是否自然进入正文、未模板化显性写出的检查。
- `## 验收标准`
  - 增加如 beat 包含 `human_texture`，正文必须保留原剧情功能，且不得字段解释化或装饰化。

作用：

- Writer 把字段转成选择、误读、场景阻力、信息载体或后果。
- Writer 不得为了人味改 beat 或牺牲网文推进。

## 3. webnovel_reviewer

文件：`skill-pack/creation_skills/webnovel_reviewer/SKILL.md`

新增段落：

- `## Human Texture gate（实验 v0）`

修改段落：

- `## 输出 YAML 格式`
  - 增加 `human_texture_review` 输出块。
- `## Reviewer 职责`
  - 增加执行 Human Texture gate，并判断退回 Planner / Writer / Polisher。

作用：

- Reviewer 负责 gate 分层。
- 结构性空心不允许交给 Polisher。

## 4. webnovel_polisher

文件：`skill-pack/creation_skills/webnovel_polisher/SKILL.md`

新增 / 修改段落：

- `## 用途`
  - 增加 Human Texture gate 入口边界。
- `## 禁止行为`
  - 增加不得补 Human Texture 结构字段、gate 未过不得润色。
- `## 执行步骤`
  - 增加读取 Reviewer 报告后检查 `human_texture_review.gate`。
- `## 验收标准`
  - 增加如存在 `human_texture_review`，必须已通过 gate，且未新增结构性 Human Texture 字段。

作用：

- Polisher 只处理结构通过后的语言显性、节奏和已有余味。
- Polisher 不救 Planner / Writer 层失败。
