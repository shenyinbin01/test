# A/B/C Validation Plan

本轮只写验证计划，不实际跑验证。

## Groups

- A = old baseline
- B = Human Texture v0
- C = Human Texture v0 + Work Voice Contract

## 验证目标

- C 是否比 B 更像一个稳定讲述者写的。
- C 是否减少技巧化人味。
- C 是否有更清晰的叙述站位。
- C 是否没有复刻来源作品。
- C 是否保留网文推进。
- C 是否没有变成端着、装、硬、十几年前网文腔。
- C 是否没有牺牲爽点、节奏和信息清晰度。

## test_sample_ids

```yaml
test_sample_ids:
  - test_id:
    scene_type:
    beat_ref:
    human_texture_packet_ref:
    voice_contract_ref:
```

## input_brief_requirements

每个测试样本必须包含：

- 同一 chapter beat。
- 同一 Human Texture packet。
- 同一字数范围。
- 同一禁用项。
- C 组额外包含同一 `voice_contract`。

## generation_conditions

- 同模型、同温度范围、同生成轮次。
- 不提供 raw corpus。
- 不提供来源作品原文。
- 不提供作者姓名作为风格目标。
- A、B、C 输出必须标记来源条件，便于盲评时打乱。

## forbidden_inputs

- 原文句子或段落。
- raw corpus 文件。
- 具体作者风格要求。
- 来源作品专属名词。
- 可识别桥段。
- 已被列入 `forbidden_original_elements` 的任何内容。

## reviewer_dimensions

- narrator_position_stability
- protagonist_distance_control
- reader_relationship_clarity
- world_attitude_consistency
- intervention_timing
- scene_type_switching_correctness
- anti_ai_voice_compliance
- no_author_imitation
- no_source_contamination
- webnovel_momentum_preserved
- human_texture_compatibility
- payoff_visibility
- information_clarity

## scoring_scale

| 分数 | 含义 |
|---|---|
| 1 | 明显失败 |
| 2 | 偶尔成立，但不稳定 |
| 3 | 基本可用，有明显问题 |
| 4 | 稳定成立，小问题可修 |
| 5 | 强成立，可进入下一步 |

污染维度使用 pass/fail，不用 1-5 分。

## pass_fail_threshold

C 组通过最低标准：

- `no_author_imitation` = pass
- `no_source_contamination` = pass
- `narrator_position_stability` >= 4
- `reader_relationship_clarity` >= 4
- `webnovel_momentum_preserved` >= 4
- `human_texture_compatibility` >= 3
- C 组在“稳定讲述者可感”上必须显著优于 B 组。

## contamination_check

每个 C 组样本必须附带 `contamination_checklist.md` 的检查结果。任何污染项为 fail，则整组失败。

## required_outputs

- A/B/C 三组文本输出引用，不在本设计包中生成。
- Reviewer scorecard。
- contamination checklist。
- pass/fail 结论。
- 失败退回层级。
- 下一轮 contract 修订建议。

## rerun_conditions

需要重跑的情况：

- C 组出现污染风险。
- C 组叙述站位稳定但牺牲爽点。
- C 组只像文风润色，没有稳定讲述者。
- B 组和 C 组差异不足。
- Reviewer 对核心维度分歧大于 1 分。
