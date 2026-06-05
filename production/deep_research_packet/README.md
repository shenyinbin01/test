# Deep Research 资料包 v0

本目录是给 ChatGPT 深度研究（Deep Research）上传使用的压缩资料包。它来自当前仓库已有资料，只用于帮助 Deep Research 快速理解项目背景、概念边界、已完成资产、研究问题和禁止事项。

重要提醒：这是当前项目判断，不是外部研究结论。Deep Research 应基于本资料包继续做公开资料研究、理论对标、工程对标和批判性审计。

## 资料包目的

- 避免上传整个仓库，减少噪音和误读。
- 避免上传小说正文、raw corpus 或原作原文。
- 让 Deep Research 理解工程化网文创作系统的长期框架。
- 明确本项目不是普通 AI 写作、不是作者模仿、不是作者复刻、不是作者指纹工程。
- 给 Deep Research 一份可直接复制使用的研究 prompt。

## 使用方式

建议先上传整个 `production/deep_research_packet/` 目录，而不是整个仓库。若 Deep Research 要求补充背景，再按 `upload_manifest.md` 选择性补充。

## GitHub 入口模式

如果 Deep Research 可以读取 GitHub，优先使用 [DEEP_RESEARCH_ENTRYPOINT.md](DEEP_RESEARCH_ENTRYPOINT.md)。项目负责人只需要提供该入口页 URL，并复制 [deep_research_github_prompt.md](deep_research_github_prompt.md) 中的 prompt。

如果 Deep Research 无法读取 GitHub，再按 [upload_manifest.md](upload_manifest.md) 上传必传文件。不建议上传整个仓库。

## 文件清单

- `DEEP_RESEARCH_ENTRYPOINT.md`：Deep Research 读取 GitHub 时的唯一入口页。
- `deep_research_github_prompt.md`：只提供一个 GitHub URL 时使用的 prompt。
- `github_reading_order.md`：GitHub 读取顺序和每个文件用途。
- `packet_status.yaml`：资料包状态和输入路径检查。
- `upload_manifest.md`：建议上传、推荐上传和不建议上传的文件。
- `project_summary.md`：项目总摘要。
- `terminology_glossary.md`：中文主名优先术语表。
- `current_pipeline_summary.md`：当前多角色生成链路摘要。
- `completed_assets_summary.md`：已完成 / 进行中资产归位。
- `long_term_framework_summary.md`：长期两条主线框架。
- `content_philosophy_summary.md`：内容价值观和反低质投喂原则。
- `key_hypotheses.md`：需要 Deep Research 审计的关键假设。
- `research_questions.md`：研究问题清单。
- `forbidden_boundaries.md`：禁止事项和误读边界。
- `requested_outputs.md`：期望 Deep Research 输出。
- `deep_research_prompt.md`：可直接复制给 Deep Research 的 prompt。
- `source_file_index.md`：本资料包参考的仓库路径索引。

## 禁止事项摘要

不要生成小说正文，不要模仿具体作者，不要要求上传原文语料，不要把目标理解成作者指纹或作者复刻，不要把网文简单等同于低质套路内容，不要把工程化与真诚创作简单对立。

## 建议上传方式

第一批上传：`project_summary.md`、`terminology_glossary.md`、`long_term_framework_summary.md`、`content_philosophy_summary.md`、`key_hypotheses.md`、`research_questions.md`、`forbidden_boundaries.md`、`requested_outputs.md`、`deep_research_prompt.md`。

第二批按需上传：`current_pipeline_summary.md`、`completed_assets_summary.md`、`source_file_index.md`。
