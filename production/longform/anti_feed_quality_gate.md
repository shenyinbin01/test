# Anti Feed Quality Gate

反低质投喂门禁用于阻止系统变成“更高级的预制内容”。它不反对网文推进、钩子和爽点，但反对没有因果、代价和继承的机械投喂。

| gate | 失败表现 | 判定 | 处理 |
|---|---|---|---|
| 章节空推进 gate | 本章有事件和钩子，但主线、卷目标、关系债、信息状态都没有变化。 | hard_fail | 退回 Chapter Card / Orchestrator。 |
| 钩子工厂 gate | 每章只扩大悬念，不兑现、不延期、不付代价。 | hard_fail | 检查 reader question 和 foreshadow ledgers。 |
| 免费爽点 gate | 主角得到资源、胜利或信息，但没有代价或后续限制。 | hard_fail | 退回 Scene Engine / State Delta。 |
| Narrator 抢戏 gate | 叙述者替角色解释选择、替读者下结论。 | fail | 退回 Renderer / Work Voice contract。 |
| 关系蒸发 gate | 冲突、失望、亏欠在下一章消失。 | hard_fail | 退回 Relationship Debt Ledger。 |
| 设定膨胀 gate | 本章主要在堆规则、势力、背景，不改变行动空间。 | fail | 收窄 world_slice / information_carrier。 |
| Spotlight 失衡 gate | 钩子、反派、设定或配角吞掉主角承受点。 | fail | 退回 Orchestrator spotlight budget。 |
| 重复骨架 gate | 三章推进结构明显重复。 | fail | 调整 plot_function / payoff_type。 |
| Polisher 越权 gate | Polisher 被要求补私心、关系债、信息载体、后果。 | hard_fail | 阻止进入 Polisher。 |
| 账本虚构 gate | ledger 出现正文或 event_log 无证据的事实。 | hard_fail | 退回 State Delta / Reducer。 |

## 通过条件

一个章节或三章样本不能只靠“顺、快、钩子强”通过。至少要证明：

- 人物行动有主权。
- 后果能继承。
- 信息露出有载体和代价。
- 关系债没有蒸发。
- 读者问题被管理。
- Renderer / Polisher 没有修结构洞。
