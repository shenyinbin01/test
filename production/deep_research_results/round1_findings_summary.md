# Deep Research 第一轮关键结论摘要

本摘要只记录项目负责人已经确认可进入工程讨论的第一轮结论，不新增外部研究判断。

## 1. 当前分层有价值，但类型混杂

Human Texture、Work Voice、Reader Immersion、Live Leakage、Character Agency、Agentic Narrative Engine 等概念都指向真实问题，但它们不在同一层级。有些是因果发动机，有些是场景质感，有些是叙述合同，有些是评价治理。

## 2. 建议重组为四层

第一层：因果主权层
- 角色主动感 / 行动主权（Character Agency）
- 后果继承账本（Consequence Ledger）
- 关系债账本
- 信息状态变化

第二层：场景质感层
- 人物质感（Human Texture）
- 活人浅痕作为微观实现
- 信息载体
- 场景阻力

第三层：叙述合同层
- 作品声音 / 作者站位（Work Voice）
- 叙述距离
- 读者关系
- 反老练讲课

第四层：评价治理层
- 读者代入感 / 读者解压 rubric
- 反低质投喂门槛
- 模板风险
- Polisher 边界

## 3. 角色主动感应前移

角色主动感 / 行动主权（Character Agency）应被前移，因为它决定人物是否能基于自己的目标、判断、误判、取舍和代价推动局面。没有这一层，Human Texture 和 Work Voice 容易变成局部补丁。

## 4. 最小实现不是直接多 agent

第一轮建议的最小实现是 scene-level decision packet + consequence ledger，而不是直接上 full multi-agent。原因是当前生产链需要可审查、可回滚、可小样本验证的 contract。

## 5. Work Voice 仍成立，但不应替代发动机

Work Voice 解决“讲故事的人是否稳定存在”，不解决“人物是否自己推动局面”。它仍然有价值，但不应继续无限扩展，也不应被当作角色因果发动机。

## 6. Reader Immersion 更像评价层

Reader Immersion 不宜先做 Writer patch。它更适合作为 Reviewer rubric 或读者体验审查层，用来判断读者是否有参与判断、脑补和期待空间。

## 7. Live Leakage 更像微观技法

Live Leakage 更适合归入 Human Texture 的微观实现，而不是独立大模块。它应服务于人物质感和场景阻力，不能变成“多加细节”。

## 8. Agentic Narrative Engine 是长线研究轨道

Agentic Narrative Engine 值得研究，但应先做 one-scene sandbox，不应马上接管生产主链。

## 9. 反低质投喂应作为硬验收

工程化不应滑向内容农场、套路密度优化或点击操控。后续 MVP 都应设置反低质投喂 gate。
