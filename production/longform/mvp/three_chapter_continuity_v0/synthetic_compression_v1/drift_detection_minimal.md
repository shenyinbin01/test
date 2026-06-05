# Drift Detection Minimal

v1 compresses drift detection into Critical / Standard / Research.

## Critical

Run by default.

| drift | minimal signal | return_to |
|---|---|---|
| 主线偏航 | `plot_change` no longer links to Book Spine or `volume_goal` | Orchestrator |
| 卷目标偏航 | chapter has no progress / delay / reversal / cost on volume goal | Orchestrator |
| 角色动机漂移 | character goal changes without accepted state_delta | Scene Engine / StateManager |
| 信息状态错乱 | `knowledge_ledger` conflicts with event evidence | Knowledge Ledger / Reviewer |
| 关系债蒸发 | active debt has no manifestation, refresh, or delay | Relationship Ledger |

## Standard

Run in normal three-chapter sample.

- 伏笔遗忘
- 读者期待断裂
- 世界规则冲突

## Research

Run only for long-range diagnostics.

- 重复骨架
- 长线节奏疲劳
- 人物 spotlight 曲线漂移

## Quantified Repeated Skeleton v1

Research mode may compare:

```yaml
repeated_skeleton_signature:
  plot_function: ""
  conflict_type: ""
  payoff_type: ""
  resource_change_type: ""
  reader_question_change_type: ""
```

If 3 consecutive chapters share 4 of 5 fields, flag as `template_pattern_drift`.
