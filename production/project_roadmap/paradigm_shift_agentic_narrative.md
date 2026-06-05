# Paradigm Shift: Agentic Narrative Engine

## Old Paradigm

旧范式大致是：

世界观 / 大纲 -> 章节规划 -> Writer 生成正文 -> Reviewer 修。

这个范式仍然可用，也仍然是当前生产主线。它的优势是可控、容易接入现有 skill-pack、可直接服务章节产出。它的局限是角色主动性往往在正文阶段被补救，容易出现“剧情需要角色这么做”的痕迹。

## New Paradigm

新范式是：

IP 宇宙 -> 世界状态 -> 角色 agents -> 场景仿真 -> 事件日志 -> 叙述渲染 -> 审核。

在这个范式里，角色不再只是正文里的描写对象。角色是有目标、认知边界、误判、关系、资源和策略的 agent。角色在场景中根据自己的信息和压力行动，事件日志记录行动与后果，然后 Narrative Renderer 只把运行结果写成正文。

## Author Position

作者强的地方，不是一直站出来解释，而是能同时做上帝和角色代入。

作为上帝，作者负责类型承诺、主线方向、节奏、爽点和审美边界。作为角色代入，作者要理解角色此刻不知道什么、误会什么、怕失去什么、能动用什么资源，以及为什么会做一个不完美但属于自己的选择。

## Required Orchestrator

Agentic Narrative Engine 必须有 Story Orchestrator。

Story Orchestrator 不直接替角色行动，但要保证：

- 类型承诺不丢。
- 主线不散。
- 场景目标清楚。
- 冲突强度可控。
- 爽点和后果能回收。
- 角色 agent 不自由跑飞。

## Renderer Boundary

Narrative Renderer 只把事件日志渲染成正文。它不负责凭空发明角色主动性，不负责新增重大剧情，不负责修改世界状态。它的能力是叙述、节奏、段落、语气和读者体验。

## Engineering Boundary

工程上不能一开始做自由多 agent。第一步必须是有边界的 scene simulation：

- 固定 scene brief。
- 固定角色列表。
- 固定可见信息。
- 固定冲突目标。
- 固定输出 event log。
- 固定 Reviewer gate。

只有当 1-scene MVP 能稳定产出可解释的事件日志，才考虑扩展到多场景或章节级链路。

## Minimal 1-scene MVP

Scene brief：主角被当众羞辱，地上少了一枚碎银。

Characters：

- 主角 agent
- 欺辱者 agent
- 旁观者 agent
- 暗中观察者 agent

Each agent should include:

- current goal
- private pressure
- known information
- wrong assumption
- relationship leverage
- available resource
- likely strategy

Validation target：

同一个 scene brief，先跑 agent simulation，再让 Writer 渲染。对照直接让 Writer 生成，判断是否更有角色主动感、信息摩擦和行动后果。这个 MVP 只验证范式可能性，不进入正式生产。
