# Tiering Policy

## A. Lite

用于：

- synthetic dry run。
- 最小三章实验。
- 真实生成前的结构验证。

特点：

- 字段最少。
- 只保留必须影响下一章的字段。
- 适合默认链路。
- Writer / Renderer 只读 hot ledger slice。

## B. Standard

用于：

- 正常三章连续小样本。
- 有 Reviewer 人审。
- 有 `state_delta + reducers`。

特点：

- 字段完整但不研究化。
- 保留 reader question、relationship debt、knowledge state、resource / status。
- 可检查 volume goal progress 与 hook / payoff balance。

## C. Research

用于：

- 长线研究。
- Agentic Narrative Engine。
- 多 agent sandbox。
- 复杂偏航分析。

特点：

- 可以保留更细字段。
- 可以记录多章 pattern drift。
- 不进入默认生产链路。

## Tier Decision

下一次真实三章小样本建议使用 Lite chapter card + Standard reviewer gate，不跑 Research gate。
