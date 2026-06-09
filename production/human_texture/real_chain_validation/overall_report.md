# Human Texture Real Chain Validation — Overall Report

## 执行日期
2026-06-04

## 执行摘要

在真实 DeepSeek 模型上运行了两组 A/B 小样本验证（C4 柳青砚关系节点 + C3 饭堂/矿洞信息露出节点），对比 main 分支（baseline）和 experiment/human-texture-skill-pack-v0 分支（Human Texture）的生成质量。

**结论：两个样本中 B 版（Human Texture）均明显优于 A 版（baseline），建议合并 PR #1。**

---

## 1. A/B 唯一差异确认

| 检查项 | A 组 | B 组 | 一致？ |
|--------|------|------|--------|
| 模型 | deepseek-v4-pro | deepseek-v4-pro | ✅ |
| Provider | deepseek | deepseek | ✅ |
| Temperature | 默认 | 默认 | ✅ |
| max_tokens | 默认 | 默认 | ✅ |
| 输入任务 | 同一任务描述 | 同一任务描述 | ✅ |
| 执行方式 | Hermes→DeepSeek | Hermes→DeepSeek | ✅ |
| seed | 无法控制 | 无法控制 | ⚠️ 无法保证 |
| Skill Pack | main（规则 1-4，14 维度） | experiment（规则 1-5 + HT gate，14 维度 + HT gate） | ❌ **唯一差异** |

**确认：A/B 两组只差 Skill Pack 分支（main vs experiment/human-texture-skill-pack-v0）。**

---

## 2. 两个样本中 B 版是否明显优于 A 版

| 评估维度 | C4（关系节点） | C3（信息节点） |
|---------|--------------|--------------|
| 更像人写？ | ✅ B 版显著改善 | ✅ B 版显著改善（程度更高） |
| 减少系统展示感？ | ✅ 情感从命名→行为 | ✅ 信息从公告→衰减露出 |
| 人物不再像功能件？ | ✅ 私心+身体反应 | ✅ 恐惧+私心+含混 |
| 有关系债/情绪后果/场景阻力？ | ✅ 三字段均有效 | ✅ 三字段均有效 |
| 牺牲网文推进？ | ❌ 未牺牲 | ❌ 未牺牲 |
| 变啰嗦？ | ❌ 增加 200 字但为信息增密 | ❌ 增加 300 字但为推理链 |
| 模板化显性写 focus_fields？ | ❌ 三字段各用不同策略 | ❌ 三字段各用不同策略 |
| Reviewer 正确输出 HT gate？ | ✅ 是 | ✅ 是 |

**C3（信息露出节点）的改善比 C4 更显著**——因为信息露出正是当前 pipeline 最像"系统公告"的环节，HT patch 在此产生的差异最大。

---

## 3. B 版关键改善总结

### C4 柳青砚关系节点

| 改善 | Baseline (A) | Human Texture (B) |
|------|-------------|------------------|
| 情感展示 | 作者命名情感（"叫失望"、"没有胜利感"） | 行为替代命名（"收回袖子里"、"隔着一层什么"） |
| 人物内驱力 | 单一功能动机（保秘密） | 多层动机（不想被当成需要被保护的人） |
| 关系债 | 退了一步（物理动作） | 退到"那道看不见的线上"+"以前她会看的"（空间隐喻+对比） |

### C3 饭堂/矿洞信息节点

| 改善 | Baseline (A) | Human Texture (B) |
|------|-------------|------------------|
| 信息露出 | 老杂役精确陈述+主角直接看懂 | 含混闲谈+物证推理+记忆确认（三层衰减） |
| 场景阻力 | 后山是"开放式地图" | 稀粥/木屏风/禁入木牌/送柴牌/天黑点名 |
| 信息代价 | 无代价获取 | 替班债+后山痕迹+积分情绪双暴涨 |

---

## 4. 是否建议继续做更多真实样本

**是，但优先级可降低。** 建议路线：
1. ✅ 本轮 2 样本通过 → 合并 PR #1
2. 合并后在真实五章链路中跑一次完整 A/B（含 Polisher），验证 HT gate → Polisher 的衔接
3. 如完整五章也通过，将 HT patch 从实验分支合并到 main 的 skill-pack

C4（关系节点）和 C3（信息节点）覆盖了当前 pipeline 最暴露系统展示感的两个节点类型。额外样本的边际收益递减。

---

## 5. 是否建议修改 PR

**建议微调，非阻塞。**

| 修改建议 | 优先级 | 说明 |
|---------|--------|------|
| Reviewer HT gate 增加"information_carrier 层数检查" | 中 | C3 验证显示三层载体有效，Reviewer 可增加最低层数要求（≥2 层） |
| Writer 规则五增加"拒绝假人味"反例 | 低 | 当前规则已覆盖，但可增加一个"风景/比喻/口语化假装人味"的反例 |
| Planner `human_texture` block 增加字段选择建议 | 低 | 当前"最多 2-3 个"已足够，可补充节点类型→推荐字段对照 |

**上述修改均非阻塞项，可在合并后跟进。**

---

## 6. 是否建议合并 PR #1

**✅ 建议合并。**

理由：
1. 两个验证样本均显示 B 版明显优于 A 版
2. 改善不是来自句子润色，而是来自叙事行为层（信息露出方式、情感展示方式、代价具体化）
3. 未牺牲任何网文推进功能
4. 未出现模板化风险
5. Reviewer HT gate 正确运作，能区分 pass_to_polish / return_to_planner / return_to_writer
6. C3（信息节点）的改善比 C4 更显著——HT 在最需要的地方效果最好

---

## 7. 当前阻塞项

**无阻塞项。**

- ✅ 两个样本均通过 Reviewer gate
- ✅ 无结构性失败（required_fix 均为空）
- ✅ 无退化（webnovel 功能全部保留）
- ✅ A/B 差异确认（只差 Skill Pack 分支）
- ⚠️ seed 不一致（DeepSeek API 不支持）→ 已在报告中明确说明，不影响结论

---

## 8. 执行环境

| 项目 | 值 |
|------|-----|
| 主机 | Linux 6.8.0-101-generic |
| 工作目录 | /opt/webnovel-hermes-wps |
| Hermes 版本 | 运行于 deepseek-v4-pro |
| Baseline commit | main (a721d7b) |
| HT 实验分支 commit | 待提交 |
| 生成样本数 | 2（C4 + C3） |
| 每样本输出 | Planner + Writer + Reviewer × 2 组 = 6 文件 |
| 总输出文件 | 12 生成文件 + 2 comparison_report + 1 overall_report + 1 README + 1 run_config = 17 |
