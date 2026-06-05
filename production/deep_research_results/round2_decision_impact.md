# Round 2 Decision Impact

第二轮 Deep Research 改变的不是“是否做长篇系统”，而是“从哪里启动、哪些层先进入主线、哪些层暂缓”。

## 对主线的影响

长篇车架进入主线规划，但完整 IP 宇宙暂缓。当前主线不再是持续扩展 Work Voice 或立刻进入完整多 agent，而是按以下顺序推进：

1. 先做发动机：角色主动感 / 行动主权（Character Agency）+ 后果继承账本（Consequence Ledger）。
2. 再接车架：Book Spine + Volume Card + Chapter Card + State Delta。
3. 再做 3 章连续实验，验证章节边界、状态继承、关系债、信息状态、读者问题和主线偏航。

## 对既有模块的重新定位

| 模块 | 新定位 | 决策影响 |
|---|---|---|
| Human Texture | 场景质感基础层 | 保留 v0，不继续扩字段；后续作为 scene causality 与 renderer contract 之间的质感约束。 |
| Work Voice | Narrative Renderer 的叙述合同子层 | 保留，但不作为发动机；不让它替角色因果、关系债和状态继承兜底。 |
| Character Agency | 场景发动机 | 前移为 P1；先用 `scene_agency_packet` 证明人物能自己推动局面。 |
| Consequence Ledger | 状态继承核心 | 与 `state_delta`、关系债账本一起前移，防止代价不继承。 |
| Reader Immersion | 章节卡 / 读者问题账本 / Reviewer gate | 不做 Writer prompt；用来检查读者问题、推断空间、期待延迟和回收窗口。 |
| Live Leakage | Human Texture 微观技法 | 不做独立大模块；只允许服务具体关系、信息或行动节奏。 |
| Agentic Narrative Engine | 长线 sandbox | 继续延后为 one-scene sandbox，不进入当前生产主链。 |
| IP Universe | 冷层资产 | 暂缓；只保留最小 `world_slice` 进入热路径。 |

## 新路线的判断

Round 2 把“长篇生产系统”从一个宏大瀑布，收窄成可验证闭环：

```text
World Slice
  -> Book Spine
  -> Volume Card
  -> Chapter Card
  -> Scene Agency Packet
  -> Event Log
  -> Narrative Renderer
  -> State Delta
  -> Ledger Reducers
  -> Next Chapter Retrieval
```

这个重排让项目能先回答一个更硬的问题：在不生成真实长篇、不修改正式 skill-pack 的前提下，三章连续是否能比逐章生成更稳地继承状态和读者期待。
