# Phase 8 Artifact Index — 《大乘期》 全量产物索引

## 1. 原始语料与章节目录
```
production/phase8/corpus/dachengqi/
├── chapters/                    # 774 章标准化章节 (chapter_0001.md ~ chapter_0774.md)
└── manifest.yaml                # 语料清单
```

## 2. Chapter Card 目录
```
production/phase8/corpus/dachengqi/
└── chapter_cards/               # 774 张 YAML 卡片 (chapter_0001.yaml ~ chapter_0774.yaml)
```

## 3. 审计目录
```
production/phase8/audit/dachengqi/
├── chapter_fact_audit_report.md
├── chapter_card_quality_report.md
└── step2_input_integrity_report.md
```

## 4. Step 3B 机制定位目录
```
production/phase8/reverse_assets/dachengqi_step3b/
├── full_chapter_spine.md        # 全 774 章 spine 聚合
├── refined_volume_structure.md  # 11 阶段划分
├── arc_mechanism_index.md       # 每阶段 arc_mechanism 分析
├── protagonist_engine.md        # 主角长篇续航机制
├── character_function_map.md    # 按功能位组织的人物分析
├── craft_distillation_candidate_pool.md  # 22 条候选技法
├── candidate_pool_curator_report.md
├── confidence_calibration_report.md
├── step3b_execution_notes.md
├── input_coverage_report.md + .json
└── step3b_quality_report.md + .json
```

## 5. Craft Assets 目录
```
production/phase8/craft_assets/
├── dachengqi_draft/             # Step 4 原始产物 (20 张 draft 技法卡)
│   ├── protagonist_engine_patterns/
│   ├── arc_structure_patterns/
│   ├── reader_pull_patterns/
│   ├── payoff_patterns/
│   ├── character_function_patterns/
│   ├── rejected_patterns/
│   └── craft_distiller_report.md + .json
├── approved_patterns/           # Step 5 最终: 20 张 status=approved
│   ├── DCQG-C001.md ~ DCQG-C020.md
│   └── manifest.yaml
├── revision_needed_patterns/    # 8 张备查副本 (带 curator 注释)
├── rejected_patterns/           # 2 张被拒绝 (DCQG-R001, R002)
└── craft_curator_report.md + .json
```

## 6. Forward Validation 目录 (Step 6)
```
production/phase8/forward_validation/
├── README.md
├── skill_injection_plan.md
├── sandbox_overlay_prompts/
│   ├── planner_overlay.md
│   ├── writer_overlay.md
│   ├── reviewer_overlay.md
│   └── polisher_overlay.md
├── validation_inputs/
├── validation_outputs/
│   ├── validation_story_bible.md
│   ├── validation_chapter_beat.yaml
│   ├── validation_draft.md
│   ├── validation_review.md
│   └── validation_polished.md
├── forward_validation_report.md
└── forward_validation_report.json
```

## 7. Skill Injection (Step 7-1)
```
production/phase8/skill_injection_minimal/
├── skill_injection_report.md
├── selected_patterns.yaml
├── modified_skills_summary.md
├── approved_patterns/           # 本批 6 张副本
├── task_templates/
│   └── step7_skill_pack_minimal_injection_task.md
└── validation/
    ├── validation_story_bible.md
    ├── validation_chapter_beat.yaml
    ├── validation_draft.md
    ├── validation_review.md
    └── validation_report.md
```

## 8. 五章连续验证 (Step 7-2)
```
production/phase8/skill_injection_minimal/validation_5ch/
├── outline_5ch.md
├── drafts/
│   ├── chapter_001_draft.md ~ chapter_005_draft.md
├── reviews/
│   └── chapter_002_review.md ~ chapter_005_review.md
└── cross_chapter_validation_report.md
```

## 9. Polisher 轻量注入 (Step 7-3)
```
production/phase8/polisher_light_injection/
├── task_templates/
│   └── step7_polisher_light_injection_task.md
└── validation/
    ├── polisher_injection_report.md
    ├── modified_skill_summary.md
    ├── before_after_samples.md
    ├── validation_polished_chapter_1.md
    ├── validation_polished_chapter_4.md
    └── polisher_light_validation_report.md
```

## 10. Skill Pack 修改位置
```
skill-pack/creation_skills/
├── webnovel_planner/SKILL.md    # 105→173 行
├── webnovel_writer/SKILL.md     # 100→168 行
├── webnovel_reviewer/SKILL.md   # 124→210 行
└── webnovel_polisher/SKILL.md   # 125→231 行
```

## 11. WPS 同步
```
WPS 云文档 / 小说 / 经络银行_Phase8五章验证/
├── Ch1_四十五点.docx
├── Ch2_杂役的夜晚.docx
├── Ch3_枯竭的阵眼.docx
├── Ch4_谎言的代价.docx
├── Ch5_选择.docx
├── Ch1_四十五点_Polished.docx
├── Ch4_谎言的代价_Polished.docx
├── 跨章验证报告.docx
├── Polisher轻量验证报告.docx
├── Polisher前后对比样本.docx
└── 五章大纲.docx
```

## 12. 关键 Commit 列表

| Commit | 内容 | 日期 |
|--------|------|------|
| `97e655a` | Step 5: status 字段 draft→approved 修复 | 2026-05 |
| `2c6bf3d` | Step 6: 沙盒注入与正向验证完整 | 2026-05 |
| `45e3c04` | Step 6: 报告口径小修 | 2026-05 |
| `fc105fc` | Step 7-1: Planner/Writer/Reviewer 第一批注入 | 2026-06-02 |
| `cf887a0` | Step 7-2: 五章连续验证 | 2026-06-02 |
| `403f9ad` | Step 7-3: Polisher 轻量注入 | 2026-06-02 |
| *(本次)* | Phase 8 completion report | 2026-06-02 |
