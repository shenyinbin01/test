# Longform Reviewer Gate

Longform Reviewer Gate（长篇审稿门）用于判断三章连续是否真实成立，而不是只看单章是否顺滑。

## 检查维度

| dimension | 检查问题 | 失败退回 |
|---|---|---|
| `chapter_contract_compliance` | 正文 / artifact 是否执行 `chapter_card` 的状态变化合同。 | Planner / Orchestrator |
| `volume_goal_progress` | 本章是否推进、反转、延迟或扩大了卷目标压力。 | Orchestrator |
| `state_delta_traceability` | 每条 `state_delta` 是否有正文或事件证据。 | State Delta extractor |
| `relationship_debt_continuity` | 关系债是否继承、刷新、扩大或明确延期。 | State Delta / Relationship Ledger |
| `knowledge_state_consistency` | 谁知道什么、误会什么、被瞒什么是否一致。 | Knowledge Ledger / Chapter Card |
| `reader_question_continuity` | 读者问题是否被刷新、回收、新增或合理延期。 | Reader Question Ledger |
| `foreshadow_payoff_tracking` | 伏笔是否在窗口内兑现、延期或增加压力。 | Foreshadow Ledger / Chapter Card |
| `agency_clarity` | 关键场景是否由人物目标、误判、策略和代价推动。 | Scene Engine |
| `narrator_overreach` | 叙述者是否提前替读者、角色或因果下结论。 | Renderer / Work Voice Contract |
| `renderer_overreach` | Renderer 是否改了行动结果、信息状态、资源或关系事实。 | Renderer Contract |
| `anti_feed_quality` | 是否出现钩子工厂、免费爽点、空推进或账本虚构。 | Reviewer gate hard fail |
| `polisher_boundary` | 是否把结构性空心交给 Polisher。 | Hard fail |

## 输出块草案

```yaml
longform_review:
  chapter_id: ""
  scores:
    chapter_contract_compliance: null
    volume_goal_progress: null
    state_delta_traceability: null
    relationship_debt_continuity: null
    knowledge_state_consistency: null
    reader_question_continuity: null
    foreshadow_payoff_tracking: null
    agency_clarity: null
    anti_feed_quality: null
  gate: "pass_to_polisher|return_to_orchestrator|return_to_scene_engine|return_to_renderer|return_to_state_delta"
  required_fix: []
  polisher_allowed: false
```

## 硬门

- 结构性空心不得交给 Polisher。
- `state_delta` 无证据不得进入 reducers。
- Renderer 改因果必须 fail。
- `chapter_one_sentence` 不能替代章节卡。
