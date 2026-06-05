# Planner Contract Draft

Planner 负责在 chapter beat 或 scene beat 阶段生成轻量 `scene_agency_packet`，并把本场景产生的后果写入 ledger 草案。

## Planner 应输出

每个关键场景最多输出一个 `scene_agency_packet`。如果场景只是过渡，不强制生成。

Planner 必须明确：

- 谁是 active_character。
- 该人物此刻的小目标是什么。
- 该人物如何误判或信息不完整。
- 他看见哪些选择。
- 他选择了什么策略。
- 这个选择留下什么 next_friction。

## Planner 不负责

- 不写正文。
- 不写完整心理细节。
- 不临时文学化。
- 不把人物目标写成抽象口号。
- 不让 Polisher 补行动主权。

## 与 Human Texture 的接口

Human Texture 解决私心、羞耻、关系债、场景阻力和信息载体。Character Agency 需要从这些字段中取可行动的压力，并转成选择和后果。

## 与 Work Voice 的接口

Work Voice 负责叙述站位，不负责决定人物怎么行动。Planner 不应把 narrator 的判断当成人物动机。
