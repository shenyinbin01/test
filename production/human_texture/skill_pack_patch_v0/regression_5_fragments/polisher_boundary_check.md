# Polisher Boundary Check

本文件模拟 `webnovel_polisher` 在实验 patch 下对五片段 Reviewer gate 的响应。

被测边界：

- `human_texture_review.gate != pass_to_polisher` 时不得进入 Polisher。
- `pass_to_polisher` 后，只允许压缩显性说明、调整重复句式、增强已有章尾留白、让已有动作和对话更贴人物状态。
- 不允许补人物私心、补关系债、重排信息露出、补代价后果、重写场景生活逻辑。

## Baseline Gate 未过时

| 片段 | Baseline Gate | Polisher 行为 | 是否越权 |
| --- | --- | --- | --- |
| C4 柳青砚关系节点 | `return_to_writer` | 停止；退回 Writer 执行羞耻和关系债。 | 否 |
| C3 饭堂 / 矿洞信息露出 | `return_to_planner` | 停止；退回 Planner 补信息载体和后续摩擦。 | 否 |
| C5 群体公告 / 规则公布 | `return_to_planner` | 停止；退回 Planner 把公告变成强制选择现场。 | 否 |
| C4 情绪残留 / 情绪代价 | `return_to_writer` | 停止；退回 Writer 给情绪残留行为后果。 | 否 |
| C4 章尾钩子压过人味 | `return_to_planner` | 停止；退回 Planner 把关系余波嵌入钩子。 | 否 |

结论：gate 未过时，Polisher 不接手结构性空心。

## B 版 Gate 通过后

| 片段 | B Gate | 允许 Polisher 做 | 禁止 Polisher 做 |
| --- | --- | --- | --- |
| C4 柳青砚关系节点 | `pass_to_polisher` | 压缩“太轻、太脏”等显性说明；调整句势。 | 新增柳青砚原谅/补关系债/改复检结果。 |
| C3 饭堂 / 矿洞信息露出 | `pass_to_polisher` | 压缩生活锚点密度；减少重复说明。 | 新增信息载体、改阵眼发现路径、改矿洞机制。 |
| C5 群体公告 / 规则公布 | `pass_to_polisher` | 压缩元启说明句；调整群体反应节奏。 | 新增检测规则、重排古镜信息、取消公告功能。 |
| C4 情绪残留 / 情绪代价 | `pass_to_polisher` | 压缩动作密度；避免情绪动作重复。 | 新增第三类情绪后果、改分数链、改测试石读数。 |
| C4 章尾钩子压过人味 | `pass_to_polisher` | 调整章尾余味句；压缩关系说明。 | 新增关系修复场、改变元启降临、削弱回收标准。 |

## 越权检查

| 禁止项 | 是否发生 | 说明 |
| --- | --- | --- |
| 补人物私心 | 否 | 私心均由 Planner block 给出，Writer 已执行。 |
| 补关系债 | 否 | 关系债由 Planner/Writer 完成，Polisher 只保留已有落点。 |
| 重排信息露出 | 否 | C3/C5 信息载体已由 Planner/Writer 决定。 |
| 补代价后果 | 否 | `consequence_next_friction` 已在 B 版存在。 |
| 重写场景生活逻辑 | 否 | 场景阻力已成立，Polisher 只可压缩。 |
| 用风景/比喻/口语化假装有人味 | 否 | B 版人味来自选择、误读、关系和代价。 |
| 把结构性失败润色成顺滑失败 | 否 | Baseline gate 未过时均停止。 |

## Boundary Result

Polisher boundary 清晰有效。

本轮 5 个 baseline 片段均不会被 Polisher 接手，避免“结构性空心被润成顺滑失败”。5 个 B 版 gate 通过后，Polisher 也只拿到语言层和节奏层小修任务，没有被要求补私心、关系债、信息载体或后果。
