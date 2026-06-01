# Craft Distiller Report: 大乘期才有逆袭系统

## 蒸馏概况

| 指标 | 值 |
|------|-----|
| 蒸馏日期 | 2026-06-01 |
| 输入来源 | Step 3B 产物（22条候选） |
| 输入 curator 决策 | keep=12, revise=8, reject=2 |
| 输出 draft 技法卡 | 20 |
| 输出 rejected patterns | 2 |
| Status | draft（待 Step 5 审批） |

## 蒸馏流程

1. **读取输入**：仅读取 8 个 Step 3B 允许的输入文件，未读取旧 Step 3 产物和原文全文。
2. **分类处理**：
   - Keep（12条）：直接蒸馏为技法卡，原机制已高度抽象。
   - Revise（8条）：按 curator 指定的去原作化规则改写后再蒸馏。
   - Reject（2条）：不生成技法卡，写入 rejected_patterns 并说明原因。
3. **去原作化检查**：所有 20 张技法卡逐一检查是否出现原作专有名词、设定词。
4. **格式标准化**：每张卡按 9 节格式生成（Metadata, Solves, Mechanism, HowToUse, PositiveExample, NegativeExample, Boundary, ContaminationGuard, EvidenceSource）。

## 各分类分布

| 分类 | 数量 | Pattern IDs |
|------|------|-------------|
| protagonist_engine_patterns | 4 | C001, C006, C009, C011 |
| arc_structure_patterns | 3 | C010, C012, C017 |
| reader_pull_patterns | 3 | C004, C008, C014 |
| payoff_patterns | 3 | C005, C020, C022 |
| character_function_patterns | 2 | C003, C007 |
| conflict_generator_patterns | 3 | C002, C015, C021 |
| pacing_patterns | 1 | C013 |
| comedy_contrast_patterns | 1 | C018 |
| rejected_patterns | 2 | C016, C019 |

## Revise 卡去原作化详情

| ID | 去原作化动作 | 结果 |
|----|------------|------|
| C002 | "辟谷丹""灵厨比赛"→"非预期资源解决规则型竞赛" | ✅ 通用化 |
| C003 | "平行世界""另一个我"→"主角选择极端化投影" | ✅ 通用化 |
| C005 | 原作 hook 名→通用钩子类型矩阵 | ✅ 通用化 |
| C010 | "九州→异世界→仙界"→六级螺旋升级模型 | ✅ 通用化 |
| C011 | "人皇"→"高维身份持有者" | ✅ 通用化 |
| C014 | "系统检测"→"外部触发事件" | ✅ 通用化 |
| C017 | 具体人物线→四线织网模型 | ✅ 通用化 |
| C021 | "系统"局限→"规则系统后门/例外/漏洞/未定义行为" | ✅ 扩展化 |

## 去原作化检查结果

- 原作人名出现次数：0
- 原作专属设定词出现次数：0
- 全部 20 张卡均含 Original Contamination Guard 节
- 全部 20 张卡均含去原作化的 Positive Abstract Example

## 已知限制

1. 部分 medium confidence 技法（C007, C009, C013, C020, C022）证据较泛，需在 Step 5 审批时重点评估。
2. 所有技法均源自单书反向工程，未经过多书交叉验证。
3. 技法卡中的"正例"为虚构创作，未在真实小说中验证。
4. 技法卡尚未注入 Skill Pack，不能直接用于生产创作。

## 建议

- Step 5 审批时应由 Hermes 逐卡评审，特别是 medium confidence 的 5 张卡。
- 建议在审批通过后进行至少一次沙盒 Demo 验证。
- Rejected patterns 中的 C019 的部分内容（认知/责任/道路/情感成长）已被其他技法吸收，不建议复活。
