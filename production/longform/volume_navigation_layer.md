# Volume Navigation Layer

Volume Card（卷卡）负责当前卷的阶段目标和回收窗口。它比整书更具体，比章节更稳定。

## 最小字段

| 字段 | 定义 |
|---|---|
| `volume_id` | 当前卷编号。 |
| `volume_one_sentence` | 本卷一句话承诺。 |
| `volume_goal` | 本卷必须推进或完成的阶段目标。 |
| `volume_antagonistic_force` | 本卷主要阻力，可以是反派、制度、资源短缺、误判或关系压力。 |
| `midpoint_turn` | 本卷中段翻面点，说明局势如何变质。 |
| `escalation_path` | 本卷压力如何逐步升级。 |
| `payoff_window` | 本卷必须兑现或阶段性兑现的问题。 |
| `debt_window` | 本卷必须刷新、扩大或结清的关系债 / 后果债。 |
| `ending_state` | 本卷结束时应达到的状态。 |
| `next_volume_seed` | 留给下一卷的种子。 |

## 与章节卡的关系

每张 `chapter_card` 必须链接当前 `volume_goal`，并说明本章对卷目标是推进、延迟、反转、代价扩大、伏笔回收，还是制造下一章压力。

卷卡不写正文，不替代章节卡，也不直接安排人物台词。
