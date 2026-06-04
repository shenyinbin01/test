# Diff Notes

## Patch 性质

这是实验分支上的最小 prompt patch，不是正式合并版本。

Patch 只增加短段落和少量执行/验收检查，没有重排原有 skill 结构，没有改变 Phase 8 注入三字段、Writer 四条核心写作约束、Reviewer 十四维度或 Polisher 轻量增强定位。

## 为什么是最小 patch

本 patch 没有复制 Human Texture 设计文档全文，只把 dry run 已验证的 6 字段合同压缩进四个角色：

- Planner：生成 compact packet。
- Writer：执行 compact brief。
- Reviewer：gate 和退回层级。
- Polisher：边界和禁止越权。

## 关键 diff 摘要

### Planner

新增 `human_texture` YAML 模板和职责边界。最重要的限制是每章 `focus_fields` 最多 2-3 个，防止 Writer 逐项模板化。

### Writer

新增 `规则五`，强调字段必须转成正文中的行为、误读、场景阻力、选择或后果。保留网文推进优先，不允许把 Human Texture 写成慢速情绪戏。

### Reviewer

新增 `human_texture_review` 输出块和 gate 规则。Reviewer 现在能判断：

- 退回 Planner：缺字段、关系债无继承、信息无载体、钩子吞人。
- 退回 Writer：字段有规划但正文没执行、情绪无行为后果、字段显性模板化。
- 进入 Polisher：结构有效，只剩语言显性和节奏问题。

### Polisher

新增 gate 入口：`human_texture_review.gate` 不是 `pass_to_polisher` 时停止。Polisher 不补人物私心、关系债、信息载体或下一章摩擦。

## 未改内容

- 未修改 `production/phase8/craft_assets/`。
- 未修改 `production/phase8/skill_injection_minimal/validation_5ch/drafts/`。
- 未新增 `approved_patterns`。
- 未修改任何正文。
- 未运行 Polisher。
- 未接入外部项目。

## 预期影响

正向影响：

- Planner 不再只规划机制点，可在关键 beat 附加人味压力。
- Writer 有明确方法避免“逐项写字段”。
- Reviewer 能把失败定位到 Planner / Writer / Polisher。
- Polisher 不再被迫把结构性失败润色成顺滑失败。

风险：

- 如果 Planner 每章都输出 3 个字段，仍可能造成轻微模板化。
- 情绪节点仍容易篇幅膨胀，需要 Writer 和 Reviewer 严控。
- `human_texture_review` 输出块是新增合同，后续回归测试要验证它不会干扰既有十四维度。

## 回滚方式

本 patch 在独立实验分支上提交。若回滚，直接丢弃该分支或 revert 本提交即可，不影响 `main`。
