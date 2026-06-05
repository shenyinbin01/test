# Next Step Recommendation

## 三种后续选项

### A. 人工审长篇三章 MVP 设计包

不跑任何生成。项目负责人先审：

- 架构是否过重。
- schema 是否足够轻。
- Story Orchestrator Lite 是否边界清楚。
- Renderer Contract 是否能阻止末端补结构。
- 三章 MVP 是否值得进入 synthetic dry run。

### B. Codex synthetic dry run

只检查 schema 流转和 artifact shape，不生成正文。重点验证：

- `single_book_story -> volume_card -> chapter_card` 是否能连起来。
- `state_delta -> ledger_reducers` 是否可追溯。
- Reviewer gate 是否能识别退回层级。
- Renderer blocker 是否会在结构不足时阻断。

### C. Hermes / DeepSeek 三章连续小样本

获批后再跑真实三章连续小样本。它应只使用最小热路径，不接入完整 IP 宇宙，不上完整 multi-agent。

## 推荐顺序

```text
A -> B -> C
```

## 当前不要做

- 先不要做完整 IP 宇宙。
- 先不要做 1 卷 10 章。
- 先不要上完整 multi-agent。
- 先不要改正式 skill-pack。
- Work Voice 等后续作为 renderer contract 子模块收口。

## 需要项目负责人拍板

1. 是否认可 `state_delta` 作为唯一写后增量事实。
2. 是否认可完整 IP 宇宙暂缓。
3. 是否认可三章连续优先于一卷十章。
4. 是否认可 Renderer / Polisher 不处理结构洞。
5. 是否进入 Codex synthetic dry run。
