# v0 Findings Summary

## 已跑通链路

v0 dry run 已验证以下结构链路可串联：

```text
World Slice
  -> Book Spine
  -> Volume Card
  -> Chapter Cards x3
  -> Scene Agency
  -> Event Log
  -> Renderer Input
  -> State Delta
  -> Reducers
  -> Gates
```

## 已完整 shape

- Renderer blocker shape 完整：`causal_thinness`、`embodied_consequence_missing`、`focalization_breach`、`exposition_clump`、`spotlight_imbalance`。
- Drift Detection shape 完整。
- Anti-feed Gate shape 完整。
- `state_delta -> ledger reducer -> ledger view` 能跑通。

## v0 发现的问题

1. `chapter_card` 偏重。
2. Reviewer gate 偏重。
3. schema 整体有过重风险。
4. `event_log` 字段命名需统一。
5. `state_delta` 缺 `status` / `conflict_report`。
6. `spotlight_targets` 需要预算。
7. reducers 需要冲突处理。
8. ledger 需要 hot slice，不能每次全量读取。
9. 重复骨架检测需要量化。
10. 需要 Lite / Standard / Research 三档。

## v1 目标

v1 不再证明链路是否能连上，而是证明链路是否能用更轻的默认形态连上。
