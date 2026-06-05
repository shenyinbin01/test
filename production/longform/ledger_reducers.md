# Ledger Reducers

Ledger Reducers（账本归并器）负责从 `state_delta` 生成运行时账本视图。

## 核心原则

- Writer 不直接改 ledger。
- Renderer 不直接改 ledger。
- Ledger 更新必须可追溯到 `state_delta`。
- 如果 `state_delta` 与正文证据不一致，必须失败。
- Reducer 不能创造新事实，只能归并 accepted delta。

## 输入

```yaml
state_delta:
  delta_id: ""
  chapter_id: ""
  evidence_refs: []
  plot_delta: []
  character_state_delta: []
  relationship_debt_delta: []
  knowledge_delta: []
  resource_or_status_delta: []
  reader_question_delta: []
  next_chapter_seed: ""
```

## 输出视图

| reducer | 输出账本 | 归并依据 |
|---|---|---|
| plot_reducer | `plot_ledger` | `plot_delta`、`next_chapter_seed` |
| character_state_reducer | `character_state_ledger` | `character_state_delta` |
| relationship_debt_reducer | `relationship_debt_ledger` | `relationship_debt_delta` |
| knowledge_reducer | `knowledge_ledger` | `knowledge_delta` |
| resource_reducer | `resource_ledger` | `resource_or_status_delta` |
| reputation_identity_reducer | `reputation_identity_ledger` | `resource_or_status_delta` 或专门声誉 delta |
| reader_question_reducer | `reader_question_ledger` | `reader_question_delta` |
| foreshadow_payoff_reducer | `foreshadow_payoff_ledger` | 伏笔 / 回收 delta |
| volume_progress_reducer | `volume_progress_ledger` | `plot_delta` 与 `volume_goal_link` |

## 失败处理

| 失败 | 处理 |
|---|---|
| delta 缺证据 | 不归并，退回 State Delta extractor。 |
| delta 与正文冲突 | hard fail，退回 Reviewer。 |
| reducer 需要新增事实才能补齐账本 | hard fail，说明上游缺失。 |
| 多账本互相冲突 | 标记 conflict report，退回 State Manager / Reviewer。 |
| 账本更新过细 | 压缩，只保留影响后续选择或读者期待的事实。 |

## 下一章检索

下一章只读取热账本切片，不读取全部历史：

- 当前卷目标进度。
- 与本章相关的 3-5 条角色状态。
- 必须显影的关系债。
- 必须遵守的信息边界。
- 本章必须刷新或回收的读者问题。
- 近期伏笔和回收窗口。
