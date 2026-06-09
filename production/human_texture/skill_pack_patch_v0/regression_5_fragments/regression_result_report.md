# Regression Result Report

日期：2026-06-04

分支：`experiment/human-texture-skill-pack-v0`

## 1. 五片段是否达到通过标准

达到。

| 标准 | 结果 |
| --- | --- |
| 至少 4 个 B 版平均分 >= 3.8 | 5/5 达到 |
| 5 个片段均保留原剧情功能 | 达到 |
| Writer 未逐项显性写字段 | 达到 |
| 未出现明显篇幅膨胀 | 达到 |
| Reviewer 能正确定位退回层级 | 达到 |
| Polisher 未被要求补人物私心、关系债、信息载体或后果 | 达到 |
| patch 未干扰既有十四维度 Reviewer 判断 | 达到 |
| Human Texture 未退化成风景、比喻、口语化或装饰性细节 | 达到 |

整体 B 平均分为 3.92，有效片段为 5/5。

## 2. 哪些片段提升最稳定

最稳定的三类：

1. C3 饭堂 / 矿洞信息露出
   - B 平均分 3.9。
   - `scene_resistance` + `information_carrier` + `consequence_next_friction` 组合非常稳。
   - 信息不再由主角直接读源码，而是从饭堂秩序、旧牌、维护刻痕和残缺汇报中拼出。

2. C4 柳青砚关系节点
   - B 平均分 4.1。
   - `shame_or_avoidance` + `relationship_debt_change` + `consequence_next_friction` 能稳定把撒谎写成带关系后果的坏选择。

3. C4 章尾钩子压过人味
   - B 平均分 4.0。
   - 大钩子保留，同时让关系余波嵌入裂缝发生时，而不是尾段补总结。

## 3. 哪些片段仍有风险

1. C4 情绪残留 / 情绪代价
   - B 平均分 3.8，刚好达标。
   - 风险是分数链天然有多个节拍，容易让每个情绪都扩写成动作模板。
   - 当前 patch 中“每个情绪最多一个动作后果”是必要约束。

2. C5 群体公告 / 规则公布
   - B 平均分 3.8。
   - 规则公布仍有中等系统展示感，但不能完全去掉公告，否则会损失网文设定推进。
   - 需要继续控制元启说明句和古镜信息密度。

## 4. Planner block 是否足够轻

足够轻。

- 5 个片段全部只选 2-3 个 `focus_fields`。
- 没有超出 6 个允许字段。
- 没有“增加人味”“加强余味”等抽象口号。
- 每个 block 都有可继承的 `carry_forward.relationship_debt` 或 `carry_forward.consequence`。
- Planner 没有写正文、心理细节或临时文学化。

结论：Planner patch 可继续进入真实链路回归。

## 5. Writer 是否出现模板化

未明显出现。

本轮 Writer 输出没有：

- “他的私心是……”
- “这是关系债……”
- “这个信息载体……”
- “下一章摩擦是……”

人味主要来自：

- C4 关系节点：撒谎前的回避、胖少年未还人情、柳青砚收回台阶。
- C3 信息节点：送柴牌、旧牌、维护刻痕、残缺汇报和替班债。
- C5 公告节点：小杂役被拉住袖口、名字亮起、标记。
- C4 情绪节点：错看、错步、唇血和后续质问压力。
- C4 章尾节点：想解释但晚了一息，柳青砚不再给台阶。

风险：章尾和关系节点不能后续反复使用“退一步 / 不回头 / 不给台阶”同类动作。

## 6. Reviewer gate 是否有效

有效。

Reviewer 能稳定分层：

- `return_to_planner`
  - C3 baseline：缺信息载体和后续摩擦。
  - C5 baseline：公告缺选择压力和检测后果。
  - C4 章尾 baseline：钩子吞掉人物余波。
- `return_to_writer`
  - C4 关系 baseline：beat 中已有冲突，但正文没有执行羞耻和关系债。
  - C4 情绪 baseline：烧积分功能明确，但情绪仍像燃料条。
- `pass_to_polisher`
  - 5 个 B 版都结构通过，只剩语言显性、句势和局部余味可调。

Reviewer gate 没有替代十四维度，而是补充结构性 Human Texture 判断。

## 7. Polisher boundary 是否清晰

清晰。

Baseline gate 未过时：

- Polisher 全部停止，不接手结构性空心。

B 版 gate 通过后：

- Polisher 只允许压缩显性说明、调整句势、保留已有余味。
- Polisher 不补人物私心。
- Polisher 不补关系债。
- Polisher 不重排信息露出。
- Polisher 不补代价后果。
- Polisher 不重写场景生活逻辑。

结论：Polisher 没有越权。

## 8. 是否建议创建 PR 进入人工审查

建议创建 PR。

理由：

- 实验分支 patch 已完成。
- 五片段回归达标。
- 改动范围小，可回滚。
- 仍需要人工审查 prompt 是否过于约束、是否会影响真实长章生成。

建议 PR 标题：

```text
feat(human-texture): add experimental skill pack prompt patch
```

## 9. 是否建议合并 main

暂不建议直接合并 `main`。

建议先创建 PR 进入人工审查，而不是直接合并。

原因：

- 本轮是模拟回归，不是真实 Planner -> Writer -> Reviewer -> Polisher 链路运行。
- Reviewer gate 虽稳定，但仍需人工确认新增输出块不会影响现有审稿消费方。
- Writer patch 虽小，但真实模型可能把字段模板化，需要一次真实五片段链路复跑确认。

## 10. 如果不建议合并，需要列出阻塞项

阻塞项：

1. 未执行真实模型链路回归，只完成模拟回归。
2. 未验证 `human_texture_review` 输出块是否被下游工具安全忽略或消费。
3. 未验证真实 Writer 是否会把 `focus_fields` 显性写成字段说明。
4. 未进行人工 prompt 审查。
5. 未进行盲评或双评，当前评分仍由单评估者完成。

## 最终结论

Human Texture 实验分支最小 prompt patch 通过五片段模拟回归。

建议下一步：创建 PR 进入人工审查；PR 审查通过后，再做一次真实五片段链路回归。暂不建议直接合并 `main`。
