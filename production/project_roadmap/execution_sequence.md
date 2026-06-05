# Execution Sequence

## Phase A: 收口当前 Work Voice

Phase A 的目标是把现有 Work Voice research / MVP / injection design 推到可验收状态，而不是扩展新概念。

1. 审 Work Voice patch diff。
2. 解决 Human Texture v0 base readiness。
3. 运行 synthetic dry run 加强版。
4. 经项目负责人批准后，再做小样本 A/B/C。
5. 写 Work Voice v0 收口报告。

Phase A 的停止条件是：如果 runtime packet 过长、Reviewer 无法识别叙述者缺失、Polisher 开始越权，先修正边界，不进入大样本验证。

## Phase B: 补齐角色生命感

Phase B 在 Work Voice 有可审查边界之后启动。它不应打断 Work Voice 收口。

1. Character Agency MVP：确认人物行动主权。
2. Live Leakage MVP：确认低显著活人痕迹。
3. Reader Immersion MVP：确认读者补全空间和解压路径。

每个 MVP 都要小闭环：文档设计、最小样例、Reviewer gate、失败信号和下一步判断。失败也要留下产物和边界，不允许因为失败就丢掉记录。

## Phase C: 长线范式探索

Phase C 是研究线，不是生产线替换。

1. Agentic Narrative Engine Research。
2. Agent card schema。
3. Scene simulation loop。
4. 1-scene MVP。
5. 与现有 Renderer / Reviewer 对接可能性评估。

Phase C 的所有产物都应保持隔离，不能修改当前 production pipeline，不能修改 `.story-system` 真源结构，不能直接接入 WPS 输出。

## Operating Rules

- 当前不要同时启动太多正文验证。
- 每个 MVP 都要小闭环。
- 失败也要留下产物、风险和判断。
- 不允许因为新范式出现就废弃已有成果。
- 任一阶段要进入 skill-pack 修改，必须另开工程任务和审计分支。
