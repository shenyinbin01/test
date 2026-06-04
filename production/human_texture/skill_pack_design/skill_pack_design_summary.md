# Skill Pack Design Summary

## 一句话结论

建议进入 Human Texture 的 Skill Pack 嵌入实验，但先走独立实验分支和 dry run，不直接修改正式 `skill-pack`。

## 为什么可以进入下一步

Human Texture 调研、MVP Round 1、MVP Round 2 已形成一致结论：

- 第一轮 + 第二轮共 5 个片段，5/5 有效。
- 改善并非来自表层润色，而是来自私心、羞耻、误读、关系债、场景阻力、信息代价和下一章摩擦。
- 片段保留了原有剧情功能，没有牺牲网文推进。
- 最有效的字段可以压缩为 6 个核心字段，避免原始 packet 过大导致模板化。

## 6 个核心字段

| 字段 | 用途 |
| --- | --- |
| `private_want` | 让人物除了剧情任务外，还有不愿完全承认的小欲望。 |
| `shame_or_avoidance` | 让情绪变成回避和不完美选择，而不是情绪标签。 |
| `relationship_debt_change` | 让关系在段落前后发生可继承变化。 |
| `scene_resistance` | 让场景阻碍人物目标，而不是只当背景板。 |
| `information_carrier` | 让信息从人、物、制度缝隙、误读和代价中露出。 |
| `consequence_next_friction` | 让本章选择给下一章留下具体麻烦。 |

每章最多选 2-3 个主字段。字段是约束，不是正文模板。

## 四层职责

| 层级 | 应承担 | 不应承担 |
| --- | --- | --- |
| Planner | 选择 focus fields；维护关系债和后果账；指定信息 carrier；保证与 beat / hook / payoff / cost 兼容。 | 写正文、写心理细节、临时文学化。 |
| Writer | 把 packet 转成选择、误读、场景阻力和后果；保留网文推进。 | 改 beat、逐项显性写字段、新增未规划因果。 |
| Reviewer | 判断 Human Texture 是否通过；定位退回 Planner / Writer / Polisher。 | 只笼统说“AI 味重”；把结构问题交给 Polisher。 |
| Polisher | 在结构通过后压缩显性说明、调整节奏、保留已有余味。 | 新增私心、关系债、信息 carrier、下一章后果。 |

## 设计文件索引

- `README.md`：设计包目标和非目标。
- `human_texture_packet_schema.md`：6 字段 schema 和压缩规则。
- `planner_injection_design.md`：Planner 注入位置、字段选择和账本设计。
- `writer_brief_design.md`：Writer brief、执行规则和篇幅控制。
- `reviewer_gate_design.md`：评分、hard gate 和退回层级。
- `polisher_boundary_design.md`：Polisher 可做 / 不可做边界。
- `minimal_integration_test_plan.md`：后续 dry run、实验分支和回归测试计划。

## 最小可行嵌入方案

最小版本不需要完整 Human Texture Engine，只需要四个轻量 patch：

1. Planner 在 chapter beat 中新增 `human_texture` block，每章选 2-3 个 focus fields。
2. Writer 接收简化 brief，把字段转为行为和场景阻力，不逐项显性写出。
3. Reviewer 增加 Human Texture gate，并决定退回层级。
4. Polisher 增加边界声明，只处理结构通过后的语言问题。

## 建议的第一步

先执行 `minimal_integration_test_plan.md` 的阶段 1 dry run：

- 不修改正式 skill-pack。
- 复用两轮 MVP 的 5 个片段。
- 验证 6 字段压缩后是否仍能保持 5/5 或至少 4/5 有效。
- 检查 Reviewer 是否能稳定阻止 Polisher 越权。

若 dry run 通过，再创建实验分支做最小 prompt patch。

## 当前风险

- 字段过多时，Writer 容易逐项模板化。
- `scene_resistance` 容易变成装饰性生活细节。
- `relationship_debt_change` 容易被写成抽象“信任裂痕”，但下一章不继承。
- `information_carrier` 容易退化成路人闲聊讲设定。
- Polisher 若边界不清，会被迫修结构，导致越改越像普通去 AI 味。

## 最终建议

建议自研并进入 Skill Pack 嵌入实验，但保持轻量。Human Texture 的价值不是新增一套文学理论，而是给现有 Planner / Writer / Reviewer 增加一条可执行的检查链：每个关键机制点，都必须有人承受、有人误读、有人欠债，或有下一章摩擦。
