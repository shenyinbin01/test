# Work Voice / Narrative Stance Research

本目录是 `Work Voice / Narrative Stance / 作品声音 / 叙述站位` 的调研与立项包。

核心目标是调研“作者在哪里”这一问题是否已有可借鉴的理论、商业工具、开源项目和工程方法，并提出能嵌入当前网文自动创作链路的落地方案。

## 项目边界

- 不做作者仿写。
- 不复刻任何具体作者。
- 不使用原文训练。
- 不读取 raw corpus。
- 不读取 `corpus/dachengqi`。
- 不使用任何原文正文或摘录。
- 不修改 `skill-pack`、PR #1、Phase 8 `craft_assets`、`approved_patterns`。
- 不启动 DeepSeek 写作链路。

本项目只抽象“成功作品中可迁移的讲述策略”：叙述者站位、聚焦方式、读者关系、世界态度、插嘴规则、细节偏好、节奏偏好和稳定毛病。它不是“作者本人”的还原工程。

## 已读取仓库输入

- `AGENTS.md`
- `skill-pack/README.md`
- `skill-pack/AGENTS.md`
- `skill-pack/mapping.md`
- `skill-pack/creation/*/SKILL.md`
- `docs/phase7_multirole_creation_workflow.md`
- `docs/phase7_skill_audit_fix_result.md`
- `production/human_texture/`
- `production/project_status/CORPUS_ACCESS_POLICY.md`

输入缺口：当前 `main` 分支下未找到 `production/human_texture/real_chain_validation_rerun/` 与 `production/human_texture/skill_pack_patch_v0/`。本包按现有提交中的 Human Texture 文档、集成设计和审计报告完成调研，未读取任何 raw corpus。

## 输出文件

- `WORK_VOICE_RESEARCH_PLAN.md`
- `theory_survey.md`
- `academic_research_notes.md`
- `commercial_tool_survey.md`
- `github_project_survey.md`
- `engineering_patterns.md`
- `applicability_to_webnovel_pipeline.md`
- `proposed_work_voice_distillation_pipeline.md`
- `risks_and_open_questions.md`
- `summary.md`

## 一句话结论

叙事学和文体学已经能帮助我们描述 Work Voice，商业工具和开源项目提供了若干可借鉴的长篇状态、角色记忆、质量门禁和 style conditioning 结构，但没有发现可直接复用的成熟“作品声音蒸馏”方案。本项目建议自研一个小型 MVP：受控样本观察卡 -> work_voice_map -> voice_contract -> Writer 注入 -> Reviewer gate -> A/B/C 验证。
