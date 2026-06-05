# Next Step Recommendation

## Option A: 人工审 synthetic dry run 结果

不生成正文。重点审：

- 是否接受 Lite / Standard / Research 三档。
- 是否接受 `state_delta` 必须带 accepted status 和 conflict report。
- 是否接受 `spotlight_budget` 进入 chapter card or Orchestrator check。

## Option B: 第二轮 synthetic dry run，压缩过重字段

不生成正文。目标：

- 压缩 chapter_card。
- 压缩 reviewer gate。
- 定义 hot ledger slice。
- 定义 reducer conflict report。

## Option C: Hermes / DeepSeek 三章连续小样本

获批后再跑。仍然不要：

- 完整 IP 宇宙。
- 一卷十章。
- 完整 multi-agent。
- 正式 skill-pack 修改。

## Recommended Order

```text
A -> B -> C
```

## Current Recommendation

Do Option A first. If owner accepts the complexity risks, do Option B to create a compressed dry-run v1 before any generated sample.
