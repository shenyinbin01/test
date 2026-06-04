# Dry Run Result Report

日期：2026-06-04

## 总结论

6 字段精简版 Human Texture packet 通过 dry run。

5 个已验证片段中，5 个 B 版 Human Texture 平均分都 >= 3.8，全部保留原剧情功能，没有明显篇幅膨胀，也没有退化成风景、比喻、口语化或装饰性细节。

Reviewer gate 能明确定位 A 版失败应退回 Planner 还是 Writer；B 版结构均通过，Polisher 只需要处理语言显性和节奏压缩，不被要求救结构性空心。

## 1. 5 个片段 Focus Fields 摘要

| 片段 | Focus Fields | 选择理由 |
| --- | --- | --- |
| C4 柳青砚关系节点 | `shame_or_avoidance`, `relationship_debt_change`, `consequence_next_friction` | 关系节点的关键不是复检规则，而是苏衍撒谎后的羞耻、信任债和下一章摩擦。 |
| C3 饭堂 / 矿洞信息露出 | `scene_resistance`, `information_carrier`, `consequence_next_friction` | 主要问题是信息像系统源码，必须改成从场景阻力、载体和代价中拼出。 |
| C5 群体公告 / 规则公布 | `scene_resistance`, `information_carrier`, `consequence_next_friction` | 公告段不能取消规则公布，但要让“不走”成为群体压力下的选择，并让标记成为后果。 |
| C4 情绪残留 / 情绪代价 | `shame_or_avoidance`, `consequence_next_friction` | 情绪节点最容易膨胀，所以只保留两个字段：遮掩羞耻和后续摩擦。 |
| C4 章尾钩子压过人味 | `private_want`, `relationship_debt_change`, `consequence_next_friction` | 大钩子必须保留，但要让苏衍错过解释窗口这一关系债嵌入钩子发生时。 |

## 2. B 版平均分

| 片段 | A 平均分 | B 平均分 | 提升 |
| --- | ---: | ---: | ---: |
| C4 柳青砚关系节点 | 2.8 | 4.1 | +1.3 |
| C3 饭堂 / 矿洞信息露出 | 2.5 | 3.9 | +1.4 |
| C5 群体公告 / 规则公布 | 2.4 | 3.8 | +1.4 |
| C4 情绪残留 / 情绪代价 | 2.9 | 3.8 | +0.9 |
| C4 章尾钩子压过人味 | 2.8 | 4.0 | +1.2 |

整体 B 平均分：3.92。

## 3. 是否达到至少 4/5 有效

达到，并超过标准。

- 有效片段：5/5。
- B 版平均分 >= 3.8：5/5。
- 保留原剧情功能：5/5。

有效定义：B 版保留原剧情功能，平均分 >= 3.8，且改善来自选择、误读、关系、代价、场景阻力或信息载体。

## 4. 是否保留原剧情功能

保留。

- C4 关系节点仍完成复检通过、柳青砚指控、胖少年作证、证人规则、苏衍撒谎、白签到手。
- C3 信息节点仍完成饭堂线索、后山矿洞、阵眼、枯竭不是事故、周期筛选信息。
- C5 公告节点仍完成古镜、积分来源、苏衍曲线、三千年寿命、筛选与回收。
- C4 情绪节点仍完成分数链和测试石六十一。
- C4 章尾节点仍完成白签、天幕裂缝、元启降临、标记和回收标准。

## 5. 是否出现模板化

未明显出现，但有可控风险。

没有出现的问题：

- 没有逐项显性写出 6 个字段。
- 没有把字段写成正文标签。
- 没有靠风景、比喻、口语化假装有人味。

需要警惕的问题：

- `shame_or_avoidance` 容易落入“咬唇、低头、沉默”的动作重复。
- `consequence_next_friction` 容易固定成“某人不回头”或“关系更冷”。
- 情绪节点若每个情绪都给动作，会产生动作模板和篇幅压力。

控制建议：

- 正式 prompt patch 中继续要求每章只选 2-3 个 focus fields。
- 情绪节点默认只选 2 个字段。
- Reviewer 检查“字段是否改变选择/信息/后果”，不检查字段是否被逐字表达。

## 6. 是否出现篇幅膨胀

没有明显篇幅膨胀，但情绪节点有轻度风险。

本轮 B 版都是短改写，未复制两轮 MVP 的长版文本。C4 情绪代价节点仍是最容易膨胀的类型，因为分数链自带多个节拍，若每个节拍都展开，就会拖慢复检紧张感。

后续接入建议：

- 情绪代价节点每个情绪最多一个动作后果。
- 不解释每个情绪来源，除非它影响关系债。
- 整章接入时，Human Texture 增幅控制在 8-10%。

## 7. Reviewer Gate 是否能正确退回层级

能。

本轮 A 版 gate 分层：

| 片段 | A 版退回层级 | 理由 |
| --- | --- | --- |
| C4 柳青砚关系节点 | Writer | Beat 中已有关系冲突，但正文没有充分执行羞耻和关系债。 |
| C3 饭堂 / 矿洞信息露出 | Planner | 信息路径缺少 carrier 和代价，主角直接读源码。 |
| C5 群体公告 / 规则公布 | Planner | 公告段缺少选择压力、信息载体和检测后果设计。 |
| C4 情绪残留 / 情绪代价 | Writer | 烧积分功能明确，但情绪被写成燃料条。 |
| C4 章尾钩子压过人味 | Planner | 大钩子结构吞掉关系余波，缺少嵌入式 consequence。 |

B 版 gate 分层：

- 5 个 B 版均为 `pass_to_polisher`。
- Polisher 只允许压缩显性说明、调整节奏、保留已有余味。
- 没有任何 B 版需要 Polisher 新增私心、关系债、信息载体或后续摩擦。

## 8. 是否建议进入实验分支 Prompt Patch

建议进入实验分支 prompt patch，但不要直接修改正式 `skill-pack`。

建议创建实验分支：

```text
experiment/human-texture-skill-pack-v0
```

最小 patch 范围：

1. Planner：在 chapter beat 增加轻量 `human_texture` block，每章只选 2-3 个 focus fields。
2. Writer：增加 compact brief 执行规则，字段必须转成选择、误读、场景阻力或后果。
3. Reviewer：增加 Human Texture gate，并能退回 Planner / Writer / Polisher。
4. Polisher：增加边界，结构未通过时不得救场。

## 9. Dry Run 风险

1. 情绪节点仍是最容易膨胀的场景，需要更严压缩。
2. 公告节点仍保留一定系统展示感，但这是规则公布的网文功能，不应完全去掉。
3. 章尾 aftertaste 不能反复使用“不回头/退一步/白签折痕”等动作。
4. Dry run 仍是单评估者评分，进入实验分支后最好做一次盲评或双评。
5. 片段有效不等于长篇自动有效；关系债和 consequence 必须由 Planner ledger 继承。

## 最终判断

Human Texture compact packet design 可以进入下一阶段。

本轮证明：即使从 MVP 大 packet 压缩到 6 个字段，只要每章限制 2-3 个 focus fields，仍能稳定改善“AI 正文不像人”的核心问题，而且不会牺牲原有网文推进。下一步应做实验分支最小 prompt patch，而不是继续扩字段或让 Polisher 兜底。
