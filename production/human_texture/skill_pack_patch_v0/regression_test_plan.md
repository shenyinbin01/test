# Regression Test Plan

## 目标

验证实验分支 prompt patch 是否能在不破坏现有 Phase 8 技法链路的前提下，让 Planner / Writer / Reviewer / Polisher 正确执行 Human Texture compact packet。

## 测试范围

使用 `production/human_texture/skill_pack_design_test/dry_run/` 中的 5 个片段：

1. C4 柳青砚关系节点
2. C3 饭堂 / 矿洞信息露出节点
3. C5 群体公告 / 规则公布节点
4. C4 情绪残留 / 情绪代价节点
5. C4 章尾钩子压过人味节点

不运行完整五章生成，不启动正式 Polisher 链路。

## 测试 1：Planner compact block

目的：验证 Planner 是否能生成轻量 `human_texture` block。

检查：

- 每个片段只选 2-3 个 `focus_fields`。
- 字段只来自 6 个允许字段。
- `relationship_debt_change` 和 `consequence_next_friction` 能进入下一章计划。
- `information_carrier` 不默认依赖权威公告或旁白说明。
- 输出不是“增加人味”“加强余味”等抽象口号。

通过标准：

- 5 个片段中至少 4 个 block 可直接给 Writer 使用。
- 没有片段超过 3 个 focus fields。

## 测试 2：Writer compact brief execution

目的：验证 Writer 是否能执行 brief 而不显性模板化。

检查：

- 字段是否转成行为、误读、场景阻力、选择或后果。
- 是否避免“他的私心是”“这是关系债”等字段说明句。
- 情绪节点是否做到每个情绪最多一个动作后果。
- 信息公告节点是否使用人、物、制度缝隙、误读或代价承载信息。
- 章尾钩子是否保留人物承受点。
- 是否保留原有网文推进、钩子、规则破局和节奏。

通过标准：

- 5 个片段均保留原剧情功能。
- 至少 4 个片段 Human Texture 平均分 >= 3.8。
- 没有明显篇幅膨胀或字段模板化。

## 测试 3：Reviewer gate

目的：验证 Reviewer 是否能 gate 并退回正确层级。

检查：

- 是否输出 `human_texture_review`。
- 是否检查 `focus_fields_checked`。
- 是否判断 `webnovel_function_preserved`。
- 是否识别系统展示风险和模板化风险。
- 是否能区分：
  - 缺字段 / 无继承 / 信息无载体 → Planner
  - 字段有规划但正文未执行 / 情绪无行为后果 → Writer
  - 结构有效但语言粗糙 → Polisher

通过标准：

- 5 个 baseline 片段的退回层级与 dry run 基本一致。
- 5 个 B 版片段不要求 Polisher 救结构性空心。

## 测试 4：Polisher boundary

目的：验证 Polisher 是否不越权。

检查：

- `human_texture_review.gate != pass_to_polisher` 时是否停止。
- 是否不补人物私心。
- 是否不补关系债。
- 是否不重排信息露出。
- 是否不补代价后果。
- 是否不重写场景生活逻辑。
- 是否不使用风景、比喻、口语化假装有人味。

通过标准：

- Polisher 只处理压缩显性说明、重复句式、已有章尾留白和语言光泽。
- 没有新增结构性 Human Texture 字段。

## 测试 5：非回归检查

目的：确认 patch 没有破坏原有链路。

检查：

- Planner 仍保留 `protagonist_cognitive_advantage` / `internalized_pressure` / `revelation_phases`。
- Writer 仍保留事件驱动开场、规则破局、认知优势展示、反模板化。
- Reviewer 仍保留十四维度。
- Polisher 仍保留 Phase 8 轻量增强规则与 ±10% 字数边界。

通过标准：

- 原有 Phase 8 技法链路不被 Human Texture 替代。
- Human Texture 只是补充 contract，不是新增大理论库。

## 明确不做

- 不运行完整五章生成。
- 不启动正式 Polisher 链路。
- 不读取 `corpus/dachengqi`。
- 不生成新 approved_patterns。
- 不修改 Phase 8 craft assets。
- 不修改正文。

## 进入下一阶段条件

满足以下条件时，可考虑将实验分支结果整理成 PR 或正式接入方案：

- 五片段回归至少 4/5 有效。
- Reviewer 能稳定退回正确层级。
- Polisher 没有越权。
- 没有明显篇幅膨胀。
- 没有字段模板化。
