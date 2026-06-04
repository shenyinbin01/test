# Minimal Integration Test Plan

本文件设计 Human Texture 进入 skill-pack 前的最小集成测试。当前只写测试设计，不修改正式 skill-pack。

## 测试目标

验证 6 字段 Human Texture packet 能否稳定嵌入现有 Planner / Writer / Reviewer / Polisher 工作流，并保持两类能力：

- 让正文更像人在经历故事。
- 不牺牲网文推进、钩子、规则破局、代价和设定揭示。

## 测试范围

纳入：

- 两轮 MVP 已验证的 5 个片段。
- 现有 5 章失败样本中的 chapter beat 或等价片段 brief。
- Human Texture rubric 的重点维度。
- Planner / Writer / Reviewer / Polisher 的边界检查。

不纳入：

- 不读取 `production/phase8/corpus/dachengqi/`。
- 不重写完整五章。
- 不启动 Polisher 正式链路。
- 不生成新的 approved_patterns。
- 不修改 Phase 8 craft assets。
- 不接入 NovelClaw 或其他外部项目。

## 阶段 0：设计包评审

目标：确认本目录 8 个文件足够支撑后续接入。

检查项：

- 6 字段 schema 是否足够轻。
- Planner / Writer / Reviewer / Polisher 职责是否不重叠。
- Reviewer 是否能判断退回层级。
- Polisher 是否没有越权。
- 是否明确禁止把 Human Texture 当普通去 AI 味。

通过标准：

- 设计包可直接转成实验分支的 prompt patch。
- 不需要在正式 skill-pack 中引入大型理论文本。

## 阶段 1：Dry Run，不改 skill-pack

目标：用现有材料模拟四层链路，但不修改正式 `SKILL.md`。

流程：

1. 选取 5 个已验证片段对应的原始 beat 或片段功能。
2. 人工生成轻量 `human_texture` block，每个片段只选 2-3 个 fields。
3. 按 `writer_brief_design.md` 写 B 版短改写。
4. 按 `reviewer_gate_design.md` 打 gate。
5. 记录哪些问题应该退回 Planner、Writer 或 Polisher。

输出：

```text
production/human_texture/skill_pack_design_test/dry_run/
  packets.yaml
  writer_outputs.md
  reviewer_gates.md
  result_report.md
```

通过标准：

- 5 个片段中至少 4 个 B 版 Human Texture 平均分 >= 3.8。
- 5 个片段均保留原剧情功能。
- 没有片段因 packet 导致明显篇幅膨胀。
- Reviewer 能明确定位失败层级。

## 阶段 2：实验分支 Prompt Patch

目标：在单独实验分支中给四个 skill 增加最小 prompt patch，但仍不进入正式合并。

建议分支：

```text
experiment/human-texture-skill-pack-v0
```

修改范围：

- Planner：增加 `human_texture` 输出块和 ledger 提醒。
- Writer：增加 brief 执行规则。
- Reviewer：增加 Human Texture gate。
- Polisher：增加边界禁止项。

严格限制：

- 每个 `SKILL.md` 只增加必要短段落。
- 不引入长篇论文式解释。
- 不改变现有 Phase 8 核心技法链路。
- 不新增 approved_patterns。

通过标准：

- `git diff` 能清楚看出是最小 prompt patch。
- 四个 skill 的职责边界仍与现有定义一致。

## 阶段 3：五片段回归测试

目标：确认正式嵌入前，自动链路仍能复现 MVP 效果。

测试片段：

| 片段 | 主要问题 | 预期 focus fields |
| --- | --- | --- |
| C4 柳青砚关系节点 | 撒谎、失望、信任破裂 | `shame_or_avoidance`, `relationship_debt_change`, `consequence_next_friction` |
| C3 饭堂 / 矿洞信息节点 | 信息公告化、场景空 | `scene_resistance`, `information_carrier`, `consequence_next_friction` |
| C5 群体公告节点 | 规则公布像公告 | `scene_resistance`, `information_carrier` |
| C4 情绪后果节点 | 情绪残留无行为后果 | `shame_or_avoidance`, `consequence_next_friction` |
| C4 章尾钩子节点 | 大钩子压过人 | `private_want`, `relationship_debt_change`, `consequence_next_friction` |

评分方式：

- A 版：原始失败片段。
- B 版：接入 Human Texture 后输出。
- 使用 `human_texture_evaluation_rubric.md` 的 10 个维度。
- 额外记录 webnovel function 是否保留。

通过标准：

- 5 个片段中至少 4 个明显优于 A 版。
- Human Texture 平均提升 >= 0.8。
- `system_display` 风险下降。
- `information_exposure` 和 `relationship_friction` 至少在相关片段提升 1 分。
- 不出现明显过度文学化。
- B 版篇幅相对 A 版增幅不超过 15%。

## 阶段 4：单章最小链路测试

目标：在不重写五章的前提下，选 1 章做“局部段落链路验证”。

流程：

1. Planner 仅为该章关键 2-3 个 beats 生成 Human Texture packet。
2. Writer 只改对应段落，不重写全章。
3. Reviewer 对这些段落跑 Human Texture gate。
4. Polisher 只在 gate 通过后处理语言显性问题。

通过标准：

- 原章剧情功能不丢失。
- 关系债或 consequence ledger 能进入下一章计划。
- Reviewer 至少一次正确阻止 Polisher 越权。
- 读感改善来自选择、误读、关系、代价和场景阻力，而不是文学化。

## 失败判定

出现以下任一情况，应暂停接入并回到设计：

- packet 让 Writer 开始逐项模板化执行字段。
- 每章都被迫写满 6 字段。
- 片段明显变慢，钩子或规则破局变弱。
- Reviewer 无法判断退回层级，只能笼统说“AI 味重”。
- Polisher 开始新增关系债、信息载体或后果。
- Human Texture 变成风景、比喻、口语化和装饰性细节。

## 最小数据记录

每次测试至少记录：

```yaml
test_case:
  source_chapter: ""
  source_fragment: ""
  original_function:
    - ""
  focus_fields:
    - ""
  packet_summary: ""
  writer_change_summary: ""
  reviewer_gate: ""
  returned_to: null
  scores:
    baseline_average: 0
    human_texture_average: 0
  webnovel_function_preserved: true
  length_delta_percent: 0
  risks:
    - ""
```

## 推荐下一步

建议下一步不是直接修改正式 `skill-pack`，而是先执行阶段 1 dry run。若 dry run 继续保持 5/5 或至少 4/5 有效，再开实验分支做最小 prompt patch。
