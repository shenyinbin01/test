# Anti-feed Gate Minimal

v1 compresses Anti-feed Gate into Critical / Standard / Research.

## Critical Hard Fail

These gates run by default.

| gate | fail condition | return_to |
|---|---|---|
| 章节空推进 | no plot, relationship, knowledge, resource, or reader-question change | Chapter Card / Orchestrator |
| 钩子工厂 | only adds hooks, no payoff or explicit delay | Reviewer / Chapter Card |
| 免费爽点 | reward or reveal has no cost, limit, or consequence | Scene Engine / State Delta |
| Narrator 抢戏 | narrator explains decisions or reader emotion before scene evidence | Renderer / Work Voice |
| 关系蒸发 | active debt disappears without delta | Relationship Ledger |
| 账本虚构 | ledger item lacks accepted state_delta evidence | StateManager / Reducer |
| Renderer / Polisher 越权 | late layer fills causality, debt, resource, or knowledge gaps | Hard fail |

## Standard

Run in normal three-chapter sample.

- 设定膨胀
- spotlight 失衡
- 重复骨架

## Research

Run only after failure or in long-range analysis.

- 多章模板漂移
- 长线情绪曲线
- 跨卷结构重复

## v1 Decision

Critical gates are enough to prevent low-quality feed in Lite. Standard gates should run for the three-chapter human review. Research gates stay out of default prompts.
