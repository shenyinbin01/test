# Synthetic Dry Run

这是 longform 三章连续 MVP 的 synthetic dry run，只验证结构流转。

本目录不验证文学质量，不生成正文，不调用 DeepSeek / Hermes，不运行 A/B/C 实验。所有内容均为抽象占位，用于检查：

- schema 字段是否能串起来。
- `state_delta` 是否能作为写后唯一增量事实。
- ledger views 是否能由 reducers 生成。
- Story Orchestrator Lite 是否只做边界管理。
- Renderer Contract 是否能返回 blocker，而不是补结构洞。
- Longform Reviewer Gate、Drift Detection、Anti-feed Gate 是否有可审 shape。

## 输入和输出

输入来自 `production/longform/` 的设计文档与 schema。输出是 synthetic artifact shape，不是故事成品。

## 禁止

- 不生成小说正文。
- 不创建真实 IP 宇宙。
- 不创建真实长篇大纲。
- 不使用 raw corpus。
- 不接入具体作者或作品。
- 不修改 `skill-pack`。
