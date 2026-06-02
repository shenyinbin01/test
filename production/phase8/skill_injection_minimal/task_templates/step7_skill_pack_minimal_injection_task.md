# Phase 8 Step 7: Skill Pack 第一批最小正式注入

## 任务目标
将 Phase 8 approved patterns 中经过正向验证的技法正式注入 Skill-Pack。

## 模式
mode=minimal_formal_injection

## 目标 Skill
- webnovel_planner（注入 C001, C009, C012）
- webnovel_writer（注入 C004, C002）
- webnovel_reviewer（注入 C005）

## 排除 Skill
- webnovel_polisher（暂缓）
- webnovel_state_manager（不涉及）
- webnovel_wps_sync（不涉及）
- detect_webnovel_ai_flavor（不涉及）

## Selected Patterns
| Pattern | 注入目标 | 核心规则 |
|---------|---------|---------|
| DCQG-C001 认知优势 | Planner | Bible增加protagonist_cognitive_advantage字段 |
| DCQG-C009 内在代价 | Planner | Bible增加internalized_pressure字段 |
| DCQG-C012 世界观揭秘驱动 | Planner | 分卷设计增加revelation_phases |
| DCQG-C004 事件驱动开场 | Writer | 开章200字内进入压力/冲突/任务场 |
| DCQG-C002 规则破局 | Writer | 高潮优先规则利用而非力量碾压 |
| DCQG-C005 短钩快兑/长钩慢兑 | Reviewer | 增加hook_pacing/payoff_visibility检查项 |

## 关键约束
- 不把技法卡全文复制进SKILL.md
- 只提炼为可执行字段/规则/检查项
- 不修改Polisher
- 不做全量注入
- 不生成新approved_patterns

## 输出目录
production/phase8/skill_injection_minimal/
├── skill_injection_report.md
├── selected_patterns.yaml
├── modified_skills_summary.md
└── validation/
    ├── validation_story_bible.md
    ├── validation_chapter_beat.yaml
    ├── validation_draft.md
    ├── validation_review.md
    └── validation_report.md

## 回传清单
1. commit hash
2. 修改文件列表
3. 修改了哪些SKILL.md
4. selected_patterns数量
5. Planner/Writer/Reviewer注入摘要
6. 是否确认未修改Polisher
7. validation_draft字数
8. validation_review摘要
9. validation_report摘要
10. 是否确认不经Polisher正文已基本可读
11. 是否出现原作污染
12. 是否建议进入第二批Polisher轻量注入
