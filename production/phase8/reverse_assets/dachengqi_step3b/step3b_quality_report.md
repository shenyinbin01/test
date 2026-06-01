# Step 3B Quality Report (Updated)

> 生成时间: 2026-06-01T15:30:00
> 生成方式: 程序聚合 + 人工抽查 + Cleanup 后更新

## 1. 交付物完整度

| 交付物 | 文件 | 覆盖率 | 状态 |
|--------|------|--------|------|
| full_chapter_spine | full_chapter_spine.md | 774/774 (100%) | ✅ |
| refined_volume_structure | refined_volume_structure.md | 774/774 (100%) | ✅ |
| arc_mechanism_index | arc_mechanism_index.md | 774/774 (100%) | ✅ |
| protagonist_engine | protagonist_engine.md | 774/774 | ✅ |
| character_function_map | character_function_map.md | 774/774 | ✅ |
| candidate_pool | craft_distillation_candidate_pool.md | 774/774 | ✅ |

## 2. 卷结构质量

| 指标 | 数值 |
|------|------|
| 主阶段数量 | 11 |
| 单阶段最大章节数 | 101 (S02) |
| 单阶段最小章节数 | 17 (S11) |
| 超过 200 章的单阶段 | **0** ✅ |
| 超过 160 章的单阶段 | **0** ✅ |
| 阶段划分依据 | 程序检测（基于 chapter_function / world_state_change 等 signals） |

## 3. 机制分析质量

| 指标 | 数值 |
|------|------|
| arc_mechanism_index 阶段数 | 11 |
| 每个阶段有机制分析的阶段数 | 11/11 (100%) |
| 每个阶段有 reusable_mechanism 的阶段数 | 待人工审计 |
| 每个阶段有 non_transferable_original_elements 的阶段数 | 11/11 (100%) |
| 是否存在"只写剧情简介不写机制"的情况 | 待人工审计 |
| 是否按阶段分批生成 | ✅ 是（11次分批LLM调用） |

## 4. 主角引擎质量

| 指标 | 数值 |
|------|------|
| 有 evidence matrix | ✅ 每个判断标注 supporting_chapters |
| 是否解释"无敌主角如何长期可看" | ✅ 覆盖限制、反差、角色互动等机制 |
| 可迁移机制数量 | 待人工审计 |
| 不可复制原作元素 | ✅ 已列出 |

## 5. 人物功能图谱质量

| 指标 | 数值 |
|------|------|
| 功能位数量 | 11 |
| 按功能位组织 | ✅ 是（主角/长期搭档/喜剧反差位/权威对照位/阶段反派/资源入口/世界观解释器/价值观对照/情绪缓冲/读者代入辅助/规则承载者） |
| 低频但关键角色是否纳入 | ✅ 标注了关键阶段反派 |
| 是否按人物传记（非功能位）组织 | ❌ 否（是按功能位组织的） |

## 6. 技法蒸馏候选池质量

| 指标 | 数值 |
|------|------|
| 候选机制总数 | 22 |
| 是否超过 20 条 | ✅ 是 |
| 每条有 solves_writing_problem | 待人工审计 |
| 每条有 original_contamination_risk | 待人工审计 |
| 每条有 suggested_distillation_type | 待人工审计 |
| 包含原作人名/专属设定/具体桥段 | 待人工审计（审计样本中检查） |

## 7. 置信度分布

| 置信度 | 数量 | 比例 |
|--------|------|------|
| high | 768 | 99.2% |
| medium | 3 | 0.4% |
| low | 3 | 0.4% |

⚠️ **注意：** confidence 是 LLM 自评。出现 medium(3) 和 low(3) 但比例极低。需人工判断是否需要校准。

### 各产品 confidence 分布

| 产品 | low | medium | high |
|------|-----|--------|------|
| full_chapter_spine | 3 | 3 | 768 |
| refined_volume_structure | n/a | n/a | n/a |
| arc_mechanism_index | n/a | n/a | n/a |
| protagonist_engine | 0 | 0 | all |
| character_function_map | 0 | 0 | all |
| candidate_pool | 0 | 0 | all |

## 8. 与旧 Step 3 对比

| 维度 | 旧 Step 3 | Step 3B |
|------|-----------|---------|
| chapter_card 读取量 | 774（但只喂采样~80章给LLM） | 774（每个阶段喂原始数据） |
| 采样策略 | 固定采样（头/1/3/2/3/尾） | 无采样，全量章节归属到阶段 |
| 人物分析 | 只喂角色名+出场次数 | 全量spine + 阶段机制 |
| 阶段划分 | 8阶段 | 11阶段 |
| candidate_pool | 无 | 22条候选 |
| 人物功能位 | 无 | 11个功能位 |
| 执行说明 | 有 | 更详细 |

## 9. 主要风险

| 风险 | 等级 | 说明 |
|------|------|------|
| confidence 全 high | 🔴 中 | LLM 自评，缺乏客观校准；protagonist_engine/character_function_map/candidate_pool 全部 high 不够诚实 |
| 跨阶段汇总输入过大 | 🟡 中 | refined_volume_structure/protagonist_engine/character_function_map 一次输入774章摘要给LLM，context 窗口有压力 |
| candidate_pool 原作污染 | 🟡 中 | 22条中有部分可能携带原作元素，需要人工过滤 |
| arc_mechanism 是否真写机制 | 🟡 中 | 需要人工抽查开篇/中盘/后期各一个阶段确认 |
| full_chapter_spine 字数 | 🟢 低 | 933KB/14710行，文件较大但这是合理的全量覆盖 |

## 10. 是否建议进入 Step 4

| 条件 | 状态 |
|------|------|
| 旧 Step 3 问题（统计+采样冒充全量）是否解决 | ✅ 已解决 |
| arc_mechanism_index 是否基于全量数据 | ✅ 是 |
| protagonist_engine 是否有机制分析 | ✅ 有 |
| candidate_pool 是否足够支撑 Step 4 | ⚠️ 需人工确认质量 |
| 是否还有"只喂统计摘要"的情况 | ❌ 否，arc_mechanism 喂的是完整数据；但跨阶段汇总可能受 context 限制 |

**建议：待主控方人工抽查 arc_mechanism 和 candidate_pool 质量后，再决定是否进入 Step 4。**

---

## 11. Cleanup 更新记录

### 11.1 LLM 对话腔清理结果

| 文件 | 状态 | 操作 |
|------|------|------|
| arc_mechanism_index.md | ✅ 已清理 | 修复「《仙逆》」→「《大乘期才有逆袭系统》」（2处错书名） |
| protagonist_engine.md | ✅ 已清理 | 删除开头「好的，作为…」对话腔 +「请记住」提示语 |
| character_function_map.md | ✅ 已清理 | 删除开头「好的，遵照您的指示…」对话腔；删除重复标题 |
| craft_distillation_candidate_pool.md | ✅ 已清理 | 删除开头「好的，作为…」对话腔 |
| refined_volume_structure.md | ✅ 已清理 | 删除开头「好的，作为…」对话腔；删除重复标题 |

### 11.2 错书名/事实错误修正

| 问题 | 文件 | 修复 |
|------|------|------|
|「《仙逆》独有的」 | arc_mechanism_index.md（2处） | →「《大乘期才有逆袭系统》独有的」 |

### 11.3 candidate_pool curator 统计

| 指标 | 数值 |
|------|------|
| 总候选 | 22 |
| keep（可直接进入 Step 4） | 12 |
| revise（去原作化后进入 Step 4） | 8 |
| reject（不建议进入 Step 4） | 2 |
| low 污染风险 | 16 |
| medium 污染风险 | 6 |
| high 污染风险 | 0 |

### 11.4 confidence 校准后分布

| 产物 | high | medium | low |
|------|------|--------|-----|
| full_chapter_spine | 768 | 3 | 3 |
| arc_mechanism_index | 6 | 4 | 1 |
| protagonist_engine | 3 | 4 | 1 |
| character_function_map | 3 | 6 | 2 |
| craft_distillation_candidate_pool | 9 | 11 | 2 |

**结果：不再存在"全部 high"的问题 ✅**

### 11.5 Step 4 放行建议

**建议：conditionally pass — 允许进入 Step 4，但附以下约束。**

Step 4 允许读取：
1. full_chapter_spine.md
2. refined_volume_structure.md
3. arc_mechanism_index.md
4. protagonist_engine.md
5. character_function_map.md
6. craft_distillation_candidate_pool.md
7. candidate_pool_curator_report.md
8. confidence_calibration_report.md

Step 4 禁止读取：
1. 旧 Step 3 reverse_story_bible.md
2. 旧 Step 3 character_cards/
3. 旧 Step 3 reader_debt_lifecycle.md
4. 旧 Step 3 hook_payoff_map.md
5. 原文全文
6. 未经 curator 标记的 candidate 直接进入 approved
