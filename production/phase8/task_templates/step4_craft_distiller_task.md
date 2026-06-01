# Phase 8 Step 4: Craft Distiller 技法蒸馏 — 任务模板

## 一、任务目标

把 Step 3B 清洗后的机制候选池（candidate_pool），蒸馏成可复用、去原作化、可审计的写作技法草案（draft craft_assets）。

目标不是继续分析《大乘期才有逆袭系统》，而是把其中可迁移的写作机制变成项目自己的 draft craft assets。

最终效果：
1. 从候选机制中提炼出 draft 技法卡。
2. 每张技法卡必须去原作化。
3. 每张技法卡必须说明解决什么写作问题。
4. 每张技法卡必须能被 Planner / Writer / Reviewer / Polisher 理解和使用。
5. 每张技法卡必须标注污染风险、适用边界、禁用内容。
6. 所有技法卡状态只能是 draft，不能 approved。

---

## 二、允许读取的输入

只允许读取以下文件：

```
production/phase8/reverse_assets/dachengqi_step3b/full_chapter_spine.md
production/phase8/reverse_assets/dachengqi_step3b/refined_volume_structure.md
production/phase8/reverse_assets/dachengqi_step3b/arc_mechanism_index.md
production/phase8/reverse_assets/dachengqi_step3b/protagonist_engine.md
production/phase8/reverse_assets/dachengqi_step3b/character_function_map.md
production/phase8/reverse_assets/dachengqi_step3b/craft_distillation_candidate_pool.md
production/phase8/reverse_assets/dachengqi_step3b/candidate_pool_curator_report.md
production/phase8/reverse_assets/dachengqi_step3b/confidence_calibration_report.md
```

---

## 三、禁止读取的输入

禁止读取以下文件：

```
production/phase8/reverse_assets/dachengqi/reverse_story_bible.md
production/phase8/reverse_assets/dachengqi/character_cards/
production/phase8/reverse_assets/dachengqi/reader_debt_lifecycle.md
production/phase8/reverse_assets/dachengqi/hook_payoff_map.md
原文全文
旧 Step 3 审计包里的 story_bible / character_cards / reader_debt_lifecycle / hook_payoff_map
未经 curator 标记的 candidate
```

原因：旧 Step 3 生成策略错误，不允许污染 Step 4。

---

## 四、Candidate Pool 处理规则

candidate_pool 共有 22 条候选：

| 标记 | 数量 | 处理方式 |
|------|------|----------|
| keep | 12 | 直接蒸馏为 draft 技法卡 |
| revise | 8 | 先去原作化改写，再蒸馏 |
| reject | 2 | 不进入 draft，放入 rejected_patterns |

### 4.1 Keep 条目（12条）

直接进入蒸馏，不需要去原作化。

### 4.2 Revise 条目（8条）— 必须先去原作化

各条目的去原作化要求：

**C002 规则解构式破局**
- 删除"辟谷丹""灵厨比赛"等具体例子
- 改成"非预期资源解决规则型竞赛"

**C003 镜像反派/黑暗可能**
- 不得依赖"平行世界""另一个我"
- 改成"主角某种选择的极端化投影"

**C005 短钩快兑，长钩慢兑**
- 删除原作 hook 名
- 改成通用 hook 类型

**C010 冲突螺旋升级**
- 不得写"九州→异世界→仙界"
- 改成"局部场域→外部系统→上层秩序→终极规则"

**C011 主角多重介入身份**
- 删除"人皇"
- 改成"高位身份持有者"

**C014 降维打击式世界观引入**
- 删除具体系统设定
- 改成"外部触发事件"

**C017 多线并行与交织**
- 删除具体人物线
- 改成"主线、支线、功能线、情绪线的织网模型"

**C021 系统/规则后门与例外**
- 不局限系统
- 扩展成"规则系统中的后门、例外、漏洞、未定义行为"

### 4.3 Reject 条目（2条）

以下条目不进入 draft 技法卡：

- **C016 终局清算与情感闭环**
- **C019 主角的非典型成长**

必须写入 `production/phase8/craft_assets/dachengqi_draft/rejected_patterns/`，每条说明：source_candidate_id、rejected_reason、why_not_actionable、是否可作为普通写作提醒保留。

---

## 五、技法卡格式

每张 draft 技法卡使用 Markdown，文件名建议：

```
PATTERN_001_cognitive_overmatch.md
PATTERN_002_task_trigger_engine.md
PATTERN_003_disguise_reveal_payoff.md
```

每张卡必须包含以下 9 节：

### 1. Metadata

```
pattern_id:
pattern_name:
source_candidate_id:
source_book_id: dachengqi
status: draft
suggested_target_skill:
applicable_genres:
pattern_type:
confidence:
contamination_risk:
```

### 2. Solves Writing Problem

说明这个技法解决什么写作问题。例如：
- 无敌流主角战斗无悬念
- 长篇中盘爽点重复
- 读者追读钩子断裂
- 人物功能位不清
- 阶段转场生硬
- 世界观揭秘缺少持续拉力

### 3. Mechanism

用抽象机制描述，不得复述原作桥段。必须写成可执行步骤。

建议格式：
1. 设置一个叙事环境或冲突场。
2. 让读者形成某种预期。
3. 让主角以某种机制进入冲突。
4. 延迟兑现或制造反差。
5. 在关键节点释放爽点。
6. 结尾打开下一层问题。

### 4. How To Use

说明 Planner / Writer / Reviewer / Polisher 如何使用。

必须至少包含：
- Planner 如何用它设计 story_bible / arc / beat
- Writer 如何用它写 scene / chapter
- Reviewer 如何检查它是否真正生效
- Polisher 如何增强它的表现力

### 5. Positive Abstract Example

写一个完全去原作化的抽象正例。禁止出现：
- 江离、人皇、大乘期、九州
- 域外天魔、天道、成仙天梯、神藏教
- 原作具体道具、原作具体桥段

### 6. Negative Example

说明错误使用方式。例如：
- 只让主角秒杀敌人，没有认知差
- 只设置系统任务，没有人物主动性
- 只堆世界观谜团，没有阶段兑现
- 只复制原作设定

### 7. Boundary

说明适用边界：
- 适合哪些题材
- 不适合哪些题材
- 主角类型要求
- 节奏要求
- 篇幅要求

### 8. Original Contamination Guard

必须包含：
- forbidden_original_elements
- contamination_notes
- de_originalization_method

### 9. Evidence Source

只写抽象证据来源，不复制原文。

格式：
```
source_arc:
source_chapters:
source_files:
supporting_mechanism:
evidence_confidence:
```

---

## 六、输出目录结构

```
production/phase8/craft_assets/dachengqi_draft/
  README.md
  manifest.yaml
  protagonist_engine_patterns/
  arc_structure_patterns/
  reader_pull_patterns/
  payoff_patterns/
  character_function_patterns/
  conflict_generator_patterns/
  pacing_patterns/
  comedy_contrast_patterns/
  rejected_patterns/
  craft_distiller_report.md
  craft_distiller_report.json
```

---

## 七、Manifest 要求

`manifest.yaml` 必须包含：

- book_id: dachengqi
- source_step: phase8_step3b_cleanup
- status: draft
- total_candidates: 22
- keep_candidates: 12
- revise_candidates: 8
- reject_candidates: 2
- draft_patterns_generated:
- rejected_patterns_generated:
- approved_patterns_generated: 0
- input_files:
- output_files:
- forbidden_sources_checked: true
- original_contamination_check: true
- generated_at:

---

## 八、报告要求

`craft_distiller_report.md` 和 `craft_distiller_report.json` 必须包含：

1. 输入文件列表
2. 处理 candidate 数量
3. keep / revise / reject 处理结果
4. draft pattern 数量
5. rejected pattern 数量
6. 每类 pattern 数量（按目录分类）
7. 是否生成 approved_patterns
8. 原作污染检查结果
9. 仍需人工复核的 pattern
10. 是否建议进入 Step 5 Craft Asset Curator

---

## 九、Validate 脚本要求

建议新增 `tools/phase8/validate_craft_assets.py`，至少检查：

1. `manifest.yaml` 可解析
2. draft pattern 数量
3. rejected pattern 数量
4. status 是否全部为 draft
5. `approved_patterns_generated` 是否为 0
6. 是否出现原作人名
7. 是否出现原作专属设定词
8. 是否缺少 How To Use
9. 是否缺少 Original Contamination Guard
10. 是否缺少 suggested_target_skill
11. 是否缺少 Boundary
12. 是否缺少 solves_writing_problem

---

## 十、禁止事项

1. 不要生成 approved_patterns。
2. 不要把 draft 技法卡直接注入 Skill。
3. 不要修改 Phase 7 Skill Pack。
4. 不要进入 Step 5。
5. 不要读取旧 Step 3 的错误产物。
6. 不要读取原文全文。
7. 不要照搬原作人物、设定、组织、桥段。
8. 不要把泛泛写作建议包装成技法卡。
9. 不要删除 reject 条目，必须记录 rejection reason。
10. 不要把 candidate_pool 原文原样复制成 pattern。

---

## 十一、质量门槛

完成后必须满足：
1. draft_patterns 数量应为 20 条左右。
2. rejected_patterns 数量应为 2 条。
3. 所有 draft pattern 都必须 status: draft。
4. approved_patterns_generated 必须为 0。
5. draft pattern 中不得出现原作人物名。
6. draft pattern 中不得出现原作专属组织名。
7. draft pattern 中不得复制具体桥段。
8. 每张卡必须有 How To Use。
9. 每张卡必须有 Original Contamination Guard。
10. 每张卡必须指定 suggested_target_skill。
11. 每张卡必须说明适用边界。
12. 每张卡必须说明解决的写作问题。
13. 每张卡必须能被后续 Step 5 审核。

---

## 十二、回传要求

完成后回传：
1. commit hash
2. 修改文件列表
3. draft pattern 数量
4. rejected pattern 数量
5. 各分类 pattern 数量
6. manifest.yaml 摘要
7. craft_distiller_report 摘要
8. validate_craft_assets.py 结果
9. 是否确认 approved_patterns_generated = 0
10. 是否确认未修改 Phase 7 Skill Pack
11. 是否确认未读取旧 Step 3 产物
12. 是否确认未读取原文全文
13. 当前风险
14. 是否建议进入 Step 5 Craft Asset Curator
