# Human Texture Skill Pack Embedding Design

本目录是 Human Texture Engine 进入 skill-pack 之前的设计包。

本轮只做设计，不修改正式 `skill-pack`，不改 Planner / Writer / Reviewer / Polisher 的 `SKILL.md`，不重写正文，不启动 Polisher。

## 设计结论

Human Texture 不应作为普通“去 AI 味”后处理。两轮 MVP 共 5 个片段全部有效，原因不是句子被润色得更文学，而是正文新增了可验证的叙事压力：

- 人物有私心、羞耻、回避和不完美选择。
- 信息从人、场景、制度缝隙和误读中露出。
- 关系债与情绪后果会延续到下一章。
- 场景不再只是信息触发器，而会阻碍人物完成目标。
- 章尾钩子仍保留，但不吞掉人的反应和余味。

因此嵌入路径应前置到 Planner / Writer / Reviewer，而不是交给 Polisher 抢救。

## 文件说明

- `human_texture_packet_schema.md`：将 MVP 原始 packet 精简成 6 个核心字段，并定义字段边界。
- `planner_injection_design.md`：Planner 如何在 chapter beat 阶段生成 Human Texture 约束。
- `writer_brief_design.md`：Writer 如何把 packet 转成正文中的选择、误读、关系和阻力。
- `reviewer_gate_design.md`：Reviewer 如何判断 Human Texture 是否通过，以及该退回哪一层。
- `polisher_boundary_design.md`：Polisher 的边界，明确哪些结构性空心不能由润色层补救。
- `minimal_integration_test_plan.md`：后续最小接入测试方案。
- `skill_pack_design_summary.md`：面向立项推进的摘要。

## 非目标

- 不把 skill-pack 改成文学理论库。
- 不要求每章塞满所有字段。
- 不把“人味”写成风景、比喻、口语化和装饰性细节。
- 不牺牲网文推进、钩子、规则破局、代价和设定揭示。
- 不让 Polisher 承担 Planner / Writer / Reviewer 应承担的结构责任。
