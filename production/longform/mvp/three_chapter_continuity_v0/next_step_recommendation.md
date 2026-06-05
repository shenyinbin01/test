# MVP Next Step Recommendation

## 推荐路径

1. 人工审查本设计包。
2. 通过后做 Codex synthetic dry run。
3. synthetic dry run 通过后，再让 Hermes / DeepSeek 跑三章连续小样本。

## 为什么不是直接生成

当前还没有验证：

- 这些 schema 是否能顺畅流转。
- `state_delta` 是否能被 reducer 稳定归并。
- Reviewer gate 是否能定位失败层级。
- Renderer blocker 是否会按边界工作。

直接生成正文会让问题归因变混：可能是模型问题、prompt 问题、schema 问题、审核问题，也可能只是三章输入太重。

## 暂不建议

- 不建议先做完整 IP 宇宙。
- 不建议先做 1 卷 10 章。
- 不建议先上完整 multi-agent。
- 不建议先改正式 skill-pack。

## 推荐结论

先人工审，再 synthetic dry run，再真实三章小样本。只有三章小样本证明长篇车架有效后，才进入实验分支 prompt patch 或更大章节数验证。
