# Phase 8 Step 5: Craft Asset Curator — 任务模板

## 一、任务目标

审核 Step 4 Craft Distiller 生成的 draft 技法卡，逐卡判断是否可进入下一步。

目标不是重新蒸馏，而是审计。

---

## 二、允许读取的输入

```
production/phase8/craft_assets/dachengqi_draft/
```

包括：
- 20 张 draft 技法卡（各分类目录下）
- 2 条 rejected pattern
- manifest.yaml
- craft_distiller_report.md / .json
- validate_craft_assets.py

---

## 三、禁止读取的输入

```
production/phase8/reverse_assets/dachengqi/（旧 Step 3）
原文全文
Phase 7 Skill Pack
```

---

## 四、审核规则

### 4.1 逐卡判断

每张 draft 技法卡必须单独审核，判断结果只能是：

| 状态 | 含义 | 输出目录 |
|------|------|----------|
| approved | 卡无问题，可直接用于写作 | `approved_patterns/` |
| revision_needed | 卡有问题但可修复，标注修改点 | `revision_needed_patterns/` |
| rejected | 卡不可修复或含污染，不进入正库 | `rejected_patterns/` |

### 4.2 审核维度

每张卡检查以下维度：

1. **解决写作问题是否真实** — 不是伪问题
2. **Mechanism 是否可执行** — 不是泛泛建议
3. **How To Use 是否完整** — Planner/Writer/Reviewer/Polisher 四角色都有
4. **Positive Abstract Example** — 去原作化，无原作人物/组织/核心设定/具体桥段
5. **Boundary 是否准确** — 不是万能卡
6. **Original Contamination Guard** — forbidden_original_elements 不能过宽或过窄
7. **contamination_risk** — 枚举值必须为 low / medium / high
8. **证据来源** — evidence 不能为空

### 4.3 重点抽查

- C001 的 forbidden_original_elements 里"修仙体系"是否过宽（需区分通用题材表达和原作专属设定）
- C003 的 contamination_risk 不应写成 "medium → low"，应规范为枚举值并将说明放入 contamination_notes
- 所有卡的 Positive Abstract Example 不能带原作人物、组织、核心设定或具体桥段
- 泛化过度、不可操作的卡不得 approved

### 4.4 不允许的行为

- 不允许直接全部 approved
- 不允许修改 Phase 7 Skill Pack

---

## 五、输出目录结构

```
production/phase8/craft_assets/
  dachengqi_draft/            ← 已有，Step 4 产物
  approved_patterns/          ← 本次新建，通过审核的卡
  revision_needed_patterns/   ← 本次新建，需修改的卡
  rejected_patterns/          ← 本次新建，被拒绝的卡
  craft_curator_report.md
  craft_curator_report.json
```

---

## 六、每张卡的处理方式

### approved 卡

原样复制到 `approved_patterns/`。

### revision_needed 卡

复制到 `revision_needed_patterns/`，并在卡内新增 `revision_notes` 节，写明：

- 需要改什么
- 怎么改
- 改完后重新进入 curator

### rejected 卡

放在 `rejected_patterns/`，注明：

- source_pattern_id
- rejected_reason
- 是否可通过大改恢复

---

## 七、报告要求

新增：

```
production/phase8/craft_assets/craft_curator_report.md
production/phase8/craft_assets/craft_curator_report.json
```

报告必须包含：

1. 审核总数
2. approved 数量
3. revision_needed 数量
4. rejected 数量
5. 每张卡的审核状态表（含简要理由）
6. 主要修改点
7. 是否创建 approved_patterns/
8. 是否创建 revision_needed_patterns/
9. 是否创建 rejected_patterns/
10. 是否确认未修改 Phase 7 Skill Pack
11. 是否建议进入 Step 6 Skill Injection 与正向验证

---

## 八、质量门槛

1. 总审核数量 = 20
2. 每张卡都有独立审核结论
3. 不允许直接全部 approved
4. revision_needed 卡必须有具体修改说明
5. contamination_risk 字段必须为标准枚举值

---

## 九、禁止事项

1. 不重新蒸馏
2. 不修改 Phase 7 Skill Pack
3. 不读取旧 Step 3
4. 不读取原文全文
5. 不做 Skill Injection（那是 Step 6）
6. 不把通用题材词（如"修仙"）误判为原作专属污染
