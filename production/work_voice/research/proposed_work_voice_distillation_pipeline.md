# Proposed Work Voice Distillation Pipeline

## 阶段 0：调研结论

前人已经做到：

- 叙事学可以描述 narrator、focalization、narrative distance、reader relationship。
- Stylometry / writeprint 可以识别表层文体和作者差异。
- 商业工具提供 story bible、memory、lorebook、style guide、author note 等容器。
- 开源项目提供长篇状态、上下文装配、quality controller、generation gate、evaluator。

仍需自研：

- 面向中文网文的 Work Voice 字段。
- 不读取 raw corpus、不复刻作者的观察卡流程。
- `work_voice_map` 到 `voice_contract` 的转换。
- A/B/C 验证 rubric。

## 阶段 1：样本规划

MVP 不需要全量语料。建议在项目负责人批准下，只使用受控、脱敏、最小化样本观察，不记录原文。

- 单本成功作品：30-60 个片段观察点。
- scene_type：opening_hook、daily_transition、conflict、revelation、payoff、relationship_scene、world_rule_exposition、chapter_ending、humor_or_absurdity、setback。
- 是否需要多本作品：MVP 可先单本，第二轮加入 2-3 本同类型成功作品对照。
- 是否需要同作者多作品：不作为首轮必须项，避免把项目误导成作者识别。
- 是否需要失败作品对照：建议至少加入当前失败样本的抽象诊断，不放原文，用于识别 AI 摄像头感。

## 阶段 2：voice_observation_card

卡片只记录抽象观察和 `evidence_ref`，不保存原文。

```yaml
sample_id: WV-S001
source_work_id: WORK-A
chapter_id: ch_001
scene_type: opening_hook
what_happens: "主角遭遇制度性压迫并被迫作出选择"
narrator_position: "贴近主角行动，但在关键句拉到世界规则上方"
protagonist_distance: "close_action / medium_judgment"
reader_relationship: "把读者当提前知道荒诞规则的同谋"
world_attitude: "冷眼承认制度残酷，但允许主角用行动撬开缝隙"
intervention_style: "少量短评，不解释情绪标签"
humor_mode: "干冷、反差、制度荒诞"
showoff_mode: "让主角通过行动暴露优势，不提前公告天赋"
sentence_rhythm: "短行动句推进，关键判断句略长"
detail_bias: "偏道具、动作后果、旁人反应"
stable_flaw: "偶尔故意不解释，让读者先感到不适"
transferable_voice_rule: "爽点前先让世界规则显得不可撼动"
non_transferable_original_element: "角色名、设定名、专属术语、原作桥段"
evidence_ref: "internal-approved-sample-id-only"
confidence: 0.72
```

## 阶段 3：work_voice_map

聚合观察卡后生成声音地图：

- 主要叙述站位是什么。
- 次要叙述站位是什么。
- 哪些 scene_type 会切换站位。
- 作者什么时候贴主角。
- 什么时候站在世界上方。
- 什么时候站在读者旁边。
- 什么时候隐身。
- 什么时候插嘴。
- 这种声音如何服务本书卖点。

建议输出结构：

```yaml
work_voice_map:
  source_work_id: WORK-A
  primary_stance: "close_action_with_world-rule_overlook"
  secondary_stances:
    - scene_type: "humor_or_absurdity"
      stance: "reader-side_deadpan"
    - scene_type: "revelation"
      stance: "world-rule_overlook"
  stance_switch_rules:
    - "破局前贴主角行动，破局后拉远解释世界反应"
  sellpoint_support:
    - "先让制度显得硬，再让主角行动产生裂缝"
  non_transferable:
    - "专有设定名"
    - "高辨识度原作桥段"
```

## 阶段 4：voice_contract

`voice_contract` 是给 Writer 的可执行合同。

```yaml
voice_contract:
  voice_type: "冷眼贴身爽文叙述"
  narrator_position: "多数时候贴近主角行动，关键解释时站到世界规则上方"
  reader_relationship: "读者是同谋，不是学生；少解释，多让读者提前闻到荒诞"
  protagonist_distance: "行动近，情绪不贴标签，判断中距离"
  world_attitude: "承认制度残酷和滑稽，但不替主角哭诉"
  intervention_rules:
    - "每个场景最多 1-2 次叙述者短评"
    - "短评必须服务压迫、反差或爽点可见度"
  humor_rules:
    - "幽默来自制度荒诞和行动反差，不来自插科打诨"
  showoff_rules:
    - "主角优势先以动作后果呈现，再让旁人反应确认"
  detail_selection_rules:
    - "优先选择道具、动作痕迹、旁人反应、空间阻力"
  sentence_rhythm_rules:
    - "推进段短句密，判断段可略拉长"
  stable_flaws_to_keep:
    - "允许少量冷硬和不解释，保留叙述者的偏执"
  forbidden_original_elements:
    - "来源作品角色名、势力名、专属设定、原文句式、标志性比喻"
  anti_ai_voice_rules:
    - "禁止先总结情绪再举例"
    - "禁止把人味技巧显性公告出来"
    - "禁止连续用同一种解释句收束段落"
```

## 阶段 5：A/B/C 验证

A = old baseline。

B = Human Texture v0。

C = Human Texture v0 + Work Voice Contract。

验证目标：

- C 是否比 B 更像一个稳定讲述者写的。
- C 是否减少技巧化人味。
- C 是否有更清晰作者位置。
- C 是否没有复刻来源作品。
- C 是否保留网文推进。

建议评价表：

| 维度 | 评分 |
|---|---|
| 稳定讲述者可感 | 1-5 |
| 叙述站位清晰 | 1-5 |
| 与主角距离合适 | 1-5 |
| 读者关系稳定 | 1-5 |
| Human Texture 不技巧化 | 1-5 |
| 网文推进和爽点可见 | 1-5 |
| 未复刻来源作品 | pass/fail |
| 无 raw corpus / 原文风险 | pass/fail |

## MVP 最小路径

1. 选 1 本成功作品做受控观察，不读取或入库 raw corpus。
2. 填 30-60 张 `voice_observation_card`。
3. 聚合 `work_voice_map`。
4. 生成 1 份 `voice_contract`。
5. 对同一 chapter beat 跑 A/B/C。
6. Reviewer gate + 人审判断 C 是否更稳定。
7. 若 C 有效，再决定是否将 Work Voice schema 固化到工程。
