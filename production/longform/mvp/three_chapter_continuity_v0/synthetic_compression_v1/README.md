# Synthetic Compression v1

这是 longform 三章连续 MVP 的 synthetic compression v1。

v0 证明链路能通。v1 要证明链路能轻。

## Goals

- 保留 v0 已跑通的结构链路。
- 降低 `chapter_card`、Reviewer gate、ledger 读取复杂度。
- 增加 `state_delta` 审核状态、冲突报告、溯源。
- 增加 `spotlight_budget`。
- 统一 `event_log` 字段命名。
- 给后续真实三章小样本准备更轻的输入形态。

## Scope

本轮仍然不生成正文，不跑 DeepSeek / Hermes，不运行 A/B/C，不修改正式 `skill-pack`。

## Compression Direction

默认链路使用 Lite。正常三章小样本使用 Critical + Standard gate。Research 字段只用于架构研究和失败诊断，不进入默认链路。
