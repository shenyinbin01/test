# Human Texture Engine Research Package

日期：2026-06-03

本目录是 Human Texture Engine 的第一轮调研与立项包。它只基于当前仓库可用材料完成：Phase 8 报告、minimal skill injection 结果、approved craft assets、skill-pack、以及 5 章失败样本。未读取也未要求补充 `production/phase8/corpus/dachengqi/` 全量语料。

## 目标

Human Texture Engine 要解决的不是普通“去 AI 味”，而是让正文从“系统展示机制”转向“人物在关系、场景、私心和后果中经历故事”。本轮只做研究、诊断、评价框架和工程嵌入方案，不修改 skill-pack，不重写正文，不启动 Polisher。

## 文件索引

- `HUMAN_TEXTURE_PLAN.md`：项目立项方案与最小版本。
- `research/industry_research.md`：行业方案调研。
- `research/github_project_survey.md`：GitHub 开源项目筛选与代码深读。
- `research/paper_and_method_notes.md`：研究资料转化结论。
- `research/human_texture_evaluation_rubric.md`：Human Texture 评价框架。
- `audit/current_5ch_failure_diagnosis.md`：当前 5 章失败样本完整诊断。
- `candidates/reusable_projects_shortlist.md`：可复用项目短名单。
- `integration/integration_with_existing_skill_pack.md`：嵌入 Planner / Writer / Reviewer / Polisher 的方案。
- `summary.md`：执行摘要与下一步。

## 本轮边界

已做：

- 完整阅读 `validation_5ch/drafts/` 下 5 章正文。
- 阅读 Phase 8 minimal injection、cross-chapter validation、craft assets、polisher light 相关报告。
- 阅读 `skill-pack/` 主要创作技能。
- 调研行业工具、研究论文、GitHub 开源项目。
- 深读 `knowrite`、`NovelGenerator`、`novel-bot`，并补充阅读 `NovelClaw`、`Dramatron`、`pulpgen`、`kimi-writer` 等项目结构或关键代码。

未做：

- 未修改 `skill-pack/`。
- 未修改 Phase 8 craft assets。
- 未重写 5 章正文。
- 未生成新 approved patterns。
- 未读取全量原文 corpus。

## 关键判断

建议自研 Human Texture Engine。外部项目值得借鉴的是长篇状态管理、agent workflow、评价器、Codex/Lorebook 类上下文组织方式；但“人物私心、羞耻、关系摩擦、真实后果、非工具性细节”必须成为本项目自己的 Planner / Writer / Reviewer 合同，不能靠通用 humanizer 或后置润色完成。
