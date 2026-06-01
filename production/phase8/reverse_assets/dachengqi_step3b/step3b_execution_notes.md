# Step 3B Execution Notes

> 生成时间: 2026-06-01T14:59:26.540223
> 执行耗时: 461s
> 模式: real (DeepSeek API)

## 1. 输入文件

1. `production/phase8/corpus/dachengqi/chapter_cards/`（774个YAML文件）
2. `production/phase8/audit/dachengqi/chapter_fact_audit_report.md`
3. `production/phase8/audit/dachengqi/chapter_card_quality_report.md`
4. `production/phase8/audit/dachengqi_step3_result_audit_package/volume_structure_report.md`（仅参考阶段划分思路）
5. `production/phase8/audit/dachengqi_step3_result_audit_package/book_architect_execution_notes.md`

## 2. 是否读取了全量 774 张 chapter_card

**是。** 脚本 `load_all_cards()` 读取了全部 774 张 chapter_card 的以下字段：
- chapter_number, title, one_sentence, chapter_function, main_events
- characters_present, protagonist_state_change
- hook_opened, hook_paid, reader_debts_opened, reader_debts_paid
- ending_pull, scene_vitality_notes, confidence

## 3. 哪些步骤是程序聚合

- Load all 774 chapter cards
- Generate full_chapter_spine.md (programmatic, zero LLM)
- Auto-detect stage boundaries (heuristic scoring)

## 4. 哪些步骤调用 LLM

共 15 次 LLM 调用：

- arc_mechanism_per_stage: chapters 1-95 (95 chapters), success=True
- arc_mechanism_per_stage: chapters 96-196 (101 chapters), success=True
- arc_mechanism_per_stage: chapters 197-289 (93 chapters), success=True
- arc_mechanism_per_stage: chapters 290-386 (97 chapters), success=True
- arc_mechanism_per_stage: chapters 387-452 (66 chapters), success=True
- arc_mechanism_per_stage: chapters 453-482 (30 chapters), success=True
- arc_mechanism_per_stage: chapters 483-577 (95 chapters), success=True
- arc_mechanism_per_stage: chapters 578-638 (61 chapters), success=True
- arc_mechanism_per_stage: chapters 639-675 (37 chapters), success=True
- arc_mechanism_per_stage: chapters 676-757 (82 chapters), success=True
- arc_mechanism_per_stage: chapters 758-774 (17 chapters), success=True
- refined_volume_structure: chapters 1-774 (774 chapters), success=True
- protagonist_engine: chapters 1-774 (774 chapters), success=True
- character_function_map: chapters 1-774 (774 chapters), success=True
- candidate_pool: chapters 1-774 (774 chapters), success=True

## 5. 每次 LLM 调用输入的章节范围

| 调用步骤 | 章节范围 | 章节数 |
|----------|----------|--------|
| arc_mechanism_per_stage | 1-95 | 95 |
| arc_mechanism_per_stage | 96-196 | 101 |
| arc_mechanism_per_stage | 197-289 | 93 |
| arc_mechanism_per_stage | 290-386 | 97 |
| arc_mechanism_per_stage | 387-452 | 66 |
| arc_mechanism_per_stage | 453-482 | 30 |
| arc_mechanism_per_stage | 483-577 | 95 |
| arc_mechanism_per_stage | 578-638 | 61 |
| arc_mechanism_per_stage | 639-675 | 37 |
| arc_mechanism_per_stage | 676-757 | 82 |
| arc_mechanism_per_stage | 758-774 | 17 |
| refined_volume_structure | 1-774 | 774 |
| protagonist_engine | 1-774 | 774 |
| character_function_map | 1-774 | 774 |
| candidate_pool | 1-774 | 774 |

## 6. 是否使用旧 Step 3 产物

**否。** 本 Step 3B 未读取以下旧产物：
- `production/phase8/reverse_assets/dachengqi/reverse_story_bible.md`
- `production/phase8/reverse_assets/dachengqi/character_cards/`
- `production/phase8/reverse_assets/dachengqi/reader_debt_lifecycle.md`
- `production/phase8/reverse_assets/dachengqi/hook_payoff_map.md`

仅参考了旧 volume_structure_report 的阶段划分思路（非内容）。

## 7. 是否生成 craft_assets

**否。** 本 Step 3B 生成的是 `dachengqi_step3b/` 下的分析产物，未写入 `craft_assets/` 目录。

## 8. 交付物清单

| 交付物 | 文件 | 状态 |
|--------|------|------|
| 1. full_chapter_spine | full_chapter_spine.md | ✅ |
| 2. refined_volume_structure | refined_volume_structure.md | ✅ |
| 3. arc_mechanism_index | arc_mechanism_index.md | ✅ |
| 4. protagonist_engine | protagonist_engine.md | ✅ |
| 5. character_function_map | character_function_map.md | ✅ |
| 6. candidate_pool | craft_distillation_candidate_pool.md | ✅ |

## 9. 统计数据

- 全量章节: 774
- 检测阶段数: 11
- 置信度分布: {'high': 768, 'low': 3, 'medium': 3}
- LLM 调用次数: 15
- LLM 调用成功率: 15/15 (100%)

## 10. 执行脚本

`tools/phase8/run_step3b_mechanism_index.py`
