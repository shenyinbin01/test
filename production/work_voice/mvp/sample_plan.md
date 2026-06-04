# Sample Plan

本文件规划 Work Voice MVP 的受控样本采集方式。这里只规划观察样本，不填真实原文，不复制原作句子，不保存 raw corpus。

## Evidence 规则

允许的 evidence 形式：

- `source_work_id + chapter_or_position_ref + manual_note_id`
- 例：`WORK_A / ch_001 opening / note_03`
- 人工摘要可以写“发生了什么”，但不能记录原文句子。

禁止的 evidence 形式：

- 原文段落。
- 原句、专有比喻、专属口癖。
- raw corpus 文件路径。
- “像某作者一样写”的风格标签。
- 可识别桥段复述到足以还原原作。

## 样本规划字段

| 字段 | 说明 |
|---|---|
| `source_work_id` | 抽象作品 ID，不写作者名作为目标。 |
| `sample_id` | 样本 ID，例如 `WV-S001`。 |
| `scene_type` | 场景类型，用于分层采样。 |
| `chapter_or_position_ref` | 抽象位置引用，不含正文。 |
| `what_to_observe` | 本样本主要观察叙述站位、距离、读者关系等哪一项。 |
| `why_this_sample` | 为什么这个场景能暴露 Work Voice。 |
| `allowed_evidence_form` | 允许记录的证据形态。 |
| `forbidden_evidence_form` | 禁止记录的证据形态。 |
| `contamination_risk` | 污染风险等级和风险原因。 |
| `expected_output_card` | 预期生成的 observation card ID。 |

## scene_type 覆盖要求

| scene_type | 观察重点 | 为什么需要 |
|---|---|---|
| `opening_voice_setup` | 开篇建立叙述声音 | 看叙述者是否一开场就有位置。 |
| `protagonist_suppressed` | 主角吃亏 / 被压制 | 看叙述者是共情、冷眼、调侃还是压场。 |
| `world_rule_exposition` | 规则公布 / 世界设定露出 | 看设定是否由世界态度承载，而不是系统公告。 |
| `information_revelation` | 信息揭示 | 看叙述者何时卖关子、何时解释、何时隐身。 |
| `side_character_pressure_or_misread` | 配角压迫或误读 | 看旁人反应如何确认主角位置和世界规则。 |
| `payoff_delivery` | 爽点兑现 | 看爽点是旁白公告，还是动作后果和读者关系共同产生。 |
| `chapter_ending_hook` | 章尾钩子 | 看叙述者如何控制留白和期待。 |
| `emotional_aftermath` | 情绪余波 | 看是否用行为和关系后果替代情绪标签。 |
| `crowd_scene` | 群体场面 | 看叙述者是否站在群体、世界或读者旁边。 |
| `transition_or_time_jump` | 转场 / 时间跳跃 | 看叙述者如何压缩时间并保持声音稳定。 |

## 建议样本量

- MVP：单本成功作品 30-60 个观察点。
- 每个 scene_type 至少 2 个样本。
- 高风险 scene_type，如 `payoff_delivery`、`world_rule_exposition`、`chapter_ending_hook`，建议至少 4 个样本。
- 可选：加入失败样本的抽象诊断，不保存原文，用于识别 AI 摄像头感。

## 样本规划模板

```yaml
source_work_id:
sample_id:
scene_type:
chapter_or_position_ref:
what_to_observe:
why_this_sample:
allowed_evidence_form: "abstract reference only; no source text"
forbidden_evidence_form:
  - "source sentence"
  - "source paragraph"
  - "raw corpus path"
  - "specific author style label"
contamination_risk:
  level:
  reason:
expected_output_card:
```
