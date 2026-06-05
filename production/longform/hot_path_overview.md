# Hot Path Overview

热路径是三章连续 MVP 真正会用到的最小闭环。

```text
World Slice
  -> Single Book Story
  -> Volume Card
  -> Chapter Card
  -> Scene Agency Packet
  -> Event Log
  -> Renderer Contract
  -> State Delta
  -> Ledger Reducers
  -> Next Chapter Retrieval
```

## 热路径原则

1. 从单书开始，不从完整 IP 宇宙开始。
2. 从一个当前卷开始，不先做完整卷群。
3. 从三个连续章节开始，不先做 10 章或完整卷。
4. 每章必须产生可验证 `state_delta`。
5. 下一章只能读取被 reducers 归并后的热账本切片。
6. 任何账本变化必须能回连到正文证据或事件日志。

## 热路径入口

当前入口是：

- `world_slice`：最小世界约束。
- `single_book_story`：整书承诺。
- `volume_card`：当前卷目标。
- `chapter_card`：三章连续合同。

## 热路径出口

当前出口不是正文，而是设计与验证产物：

- 三组 A/B/C 实验输入输出合同。
- 三章状态增量格式。
- 多账本物化视图。
- Reviewer gate 与 drift report。
