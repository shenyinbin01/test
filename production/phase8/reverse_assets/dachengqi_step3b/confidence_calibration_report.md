# Confidence Calibration Report

> 生成时间: 2026-06-01T15:30:00
> 校准方式: Hermes 逐产物评估，基于 evidence 强度和污染风险

---

## 校准前分布

| 产物 | high | medium | low |
|------|------|--------|-----|
| full_chapter_spine（程序生成） | 768 | 3 | 3 |
| arc_mechanism_index | 11/11阶段 all high | 0 | 0 |
| protagonist_engine | all high | 0 | 0 |
| character_function_map | all high | 0 | 0 |
| craft_distillation_candidate_pool | 22/22 all high | 0 | 0 |

## 校准规则

- **high**：多阶段 evidence，机制稳定，污染风险低
- **medium**：有证据但解释空间较大；或机制可迁移但需人工改写；或依赖少量阶段证据
- **low**：证据不足；或污染风险高；或可能是模型推断；或只是泛化总结

---

## 逐产物校准

### 1. full_chapter_spine（程序生成）

无需校准。程序聚合基于774张 chapter_card 原始字段，置信度继承自 chapter_card 自身标注。

| 置信度 | 校准前 | 校准后 | 说明 |
|--------|--------|--------|------|
| high | 768 | 768 | 程序聚合，不调整 |
| medium | 3 | 3 | 继承 chapter_card 标注 |
| low | 3 | 3 | 继承 chapter_card 标注 |

### 2. arc_mechanism_index

每个阶段的机制分析基于该阶段全量 chapter_card 数据（30-101章），evidence 充分。

| 阶段 | 校准前 | 校准后 | 理由 |
|------|--------|--------|------|
| S01 (1-95) | high | high | 95章全量证据，阶段机制明确 |
| S02 (96-196) | high | high | 101章全量证据 |
| S03 (197-289) | high | high | 93章全量证据 |
| S04 (290-386) | high | high | 97章全量证据 |
| S05 (387-452) | high | medium | 66章证据，但部分机制提炼较泛 |
| S06 (453-482) | high | medium | 只有30章，证据偏少 |
| S07 (483-577) | high | high | 95章全量证据 |
| S08 (578-638) | high | medium | 61章，部分提炼需要更多支撑 |
| S09 (639-675) | high | medium | 37章，样本偏小 |
| S10 (676-757) | high | high | 82章全量证据 |
| S11 (758-774) | high | low | 只有17章，终局阶段判断需更谨慎 |

校准后分布：high=6, medium=4, low=1

### 3. protagonist_engine

基于全量774章 spine 摘要 + 11阶段机制分析，但 LLM 一次输入内容量大，部分判断可能压缩。

| 章节 | 校准前 | 校准后 | 理由 |
|------|--------|--------|------|
| 主角功能定义 | high | high | 有充分的多阶段 evidence |
| 爽点循环 | high | high | 3个循环均有各阶段例子支撑 |
| 冲突介入方式 | high | medium | 部分模式只有少量阶段佐证 |
| 限制与反差 | high | medium | 限制分析较强，但"反差"证据较分散 |
| 价值观锚点 | high | medium | 核心判断有证据，但佐证较泛 |
| 分阶段主角功能变化 | high | high | 逐阶段分析，证据充分 |
| 可迁移机制 | high | low | 跨全书的大判断，且涉及迁移性评估，LLM 自评不可靠 |
| 不可复制原作元素 | high | medium | 判断合理但偏主观 |

校准后分布：high=3, medium=4, low=1

### 4. character_function_map

基于全量 spine + 角色出场统计，按功能位组织。整体质量较好，但部分功能位证据单一。

| 功能位 | 校准前 | 校准后 | 理由 |
|--------|--------|--------|------|
| 主角 | high | high | 全书evidence充分 |
| 长期搭档 | high | high | 多阶段evidence |
| 喜剧反差位 | high | high | 全书贯穿 |
| 权威对照位 | high | medium | 出场频次低 |
| 阶段反派 | high | medium | 每个阶段反派证据分散 |
| 资源入口 | high | low | 功能定义偏泛，具体证据少 |
| 世界观解释器 | high | medium | 角色有限但功能明确 |
| 价值观对照 | high | medium | 依赖少数角色 |
| 情绪缓冲 | high | medium | 支撑证据较分散 |
| 读者代入辅助 | high | low | 概念合适但缺乏直接证据链 |
| 规则承载者 | high | medium | 出场不多但功能重要 |

校准后分布：high=3, medium=6, low=2

### 5. craft_distillation_candidate_pool

校准基于污染风险 + 是否去原作化。

| Candidate | 校准前 | 校准后 | 理由 |
|-----------|--------|--------|------|
| C001 认知碾压式爽点 | high | high | 完全去原作化 |
| C002 规则解构式破局 | high | medium | 举例有原作污染 |
| C003 镜像反派 | high | medium | 依赖本书核心设定 |
| C004 系统任务触发器 | high | high | 完全通用 |
| C005 短钩快兑长钩慢兑 | high | high | 通用钩子模型 |
| C006 伪装身份 | high | high | 完全通用 |
| C007 导师型主角 | high | medium | 部分依赖本书人皇设定 |
| C008 时间回溯 | high | high | 完全通用 |
| C009 压力源内化 | high | medium | 证据偏泛 |
| C010 冲突螺旋升级 | high | medium | 包含原作层级链 |
| C011 多重身份介入 | high | medium | 包含"人皇"引用 |
| C012 世界观揭秘 | high | high | 完全通用 |
| C013 情感锚点 | high | medium | 证据偏泛 |
| C014 降维打击式引入 | high | medium | 部分依赖系统设定 |
| C015 理念冲突 | high | high | 完全通用 |
| C016 终局清算 | high | low | 太泛，无具体操作 |
| C017 多线并行 | high | medium | 可能涉及具体人物线 |
| C018 喜剧调剂 | high | high | 完全通用 |
| C019 非典型成长 | high | low | 太泛，无具体操作 |
| C020 代价与取舍 | high | medium | 通用但证据泛 |
| C021 系统后门/例外 | high | medium | 过于依赖"系统"载体 |
| C022 番外初心回归 | high | medium | 通用但偏泛 |

校准后分布：high=9, medium=11, low=2

---

## 校准后总分布

| 产物 | high | medium | low |
|------|------|--------|-----|
| full_chapter_spine | 768 | 3 | 3 |
| arc_mechanism_index | 6 | 4 | 1 |
| protagonist_engine | 3 | 4 | 1 |
| character_function_map | 3 | 6 | 2 |
| craft_distillation_candidate_pool | 9 | 11 | 2 |

**结果：** 不再存在"全部 high"的问题 ✅。各产物均有 medium 和 low 标注。

---

## 校准说明

1. 校准基于 Hermes 对 evidence 强度的判断，不是 LLM 自评。
2. 部分 medium 和 low 标记的是整个产物层面，而非逐条标注（原产物中 confidence 为 LLM 自评，本报告不修改原产物标注，仅提供校准参考）。
3. Step 4 使用时，应以本校准报告为准，而非 LLM 自评。
