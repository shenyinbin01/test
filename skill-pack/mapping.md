# webnovel-hermes-wps Skill Pack — 文件映射

## 创作角色 Skill（7 个，全部已实现）

| Skill 名 | 实际路径 | 状态 |
|----------|----------|------|
| webnovel_planner | `skills/webnovel_planner/SKILL.md` | ✅ Phase 7 新增 |
| webnovel_writer | `skills/webnovel_writer/SKILL.md` | ✅ Phase 7 新增 |
| detect_webnovel_ai_flavor | `skills/detect_webnovel_ai_flavor/SKILL.md` | ✅ Phase 6B 已实现 |
| webnovel_reviewer | `skills/webnovel_reviewer/SKILL.md` | ✅ Phase 6B 已实现 |
| webnovel_polisher | `skills/webnovel_polisher/SKILL.md` | ✅ Phase 6B 已实现 |
| webnovel_state_manager | `skills/webnovel_state_manager/SKILL.md` | ✅ Phase 7 新增 |
| webnovel_wps_sync | `skills/webnovel_wps_sync/SKILL.md` | ✅ Phase 7 新增 |

> 注意：所有 Skill 名统一使用 underscore（`_`），实际 SKILL.md 文件中使用 YAML frontmatter 的 `name` 字段，已全部对齐为 underscore。

## 完整创作链路

```
webnovel_planner
  → webnovel_writer
  → detect_webnovel_ai_flavor
  → webnovel_reviewer
  → webnovel_polisher
  → webnovel_state_manager
  → webnovel_wps_sync
```

参见: `docs/phase7_multirole_creation_workflow.md`

## DeepCode 编程 Skill（5 个，全部已实现）

| Skill 名 | 实际路径 |
|----------|----------|
| deepcode_project_onboarding | `deepcode_skills/deepcode_project_onboarding/SKILL.md` |
| deepcode_repo_audit | `deepcode_skills/deepcode_repo_audit/SKILL.md` |
| deepcode_safe_refactor | `deepcode_skills/deepcode_safe_refactor/SKILL.md` |
| deepcode_regression_test | `deepcode_skills/deepcode_regression_test/SKILL.md` |
| deepcode_engineering_report | `deepcode_skills/deepcode_engineering_report/SKILL.md` |

## 支撑文档

| 文档 | 实际路径 | 用途 |
|------|----------|------|
| AGENTS.md | `AGENTS.md` | 最高原则、分工、Skill 边界定义 |
| DeepCode Onboarding | `docs/deepcode_onboarding.md` | DeepCode 入职规则 |
| 多角色创作工作流 | `docs/phase7_multirole_creation_workflow.md` | 完整 7 步链路说明 |
| 质量检测规则 | `templates/deai_rules/` | 7 个去 AI 味规则文件 |
| Planner Prompts | `templates/prompts/story_bible.md`, `chapter_outline.md`, `chapter_beat.md` | 规划类 Prompt 模板 |
| Writer Prompt | `templates/prompts/chapter_writer.md` | 写作 Prompt 模板 |
| Reviewer Prompt | `templates/prompts/chapter_review.md` | 审稿 Prompt 模板 |
| Polisher Prompt | `templates/prompts/chapter_polish.md` | 润色 Prompt 模板 |
| StateManager Prompts | `templates/prompts/chapter_commit.md`, `projection.md` | 状态管理 Prompt 模板 |
| Phase 7 审计修正 | `docs/phase7_skill_audit_fix_result.md` | 审计修正报告 |
