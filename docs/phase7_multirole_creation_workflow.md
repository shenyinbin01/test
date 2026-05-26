# Phase 7 多角色创作工作流

## 完整链路

```
Planner
  → Writer
  → analyze_sentence_rhythm.py（Python 工具）
  → detect_webnovel_ai_flavor（Hermes + DeepSeek）
  → webnovel_reviewer（Hermes + DeepSeek）
  → webnovel_polisher（Hermes + DeepSeek）
  → webnovel_state_manager（Hermes + DeepSeek + Python）
  → webnovel_wps_sync（Hermes + Python 工具链）
```

## 每一步详情

### Step 1: Planner

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_planner` |
| 输入 | project.yaml, MASTER_SETTING（可选）, runtime_canon（可选）, reader_debts（可选）, 已有 outline/beats |
| 输出 | MASTER_SETTING.yaml, outlines/chapters_001_030.yaml, outlines/beats/chapter_XXX.yaml, .webnovel/context/chapter_XXX_context.yaml（可选） |
| 调 DeepSeek | ✅ 生成 Story Bible / outline / beat |
| 调 Python | ❌ |
| 改 .story-system | ✅ 写 MASTER_SETTING.yaml（新项目） |
| 改正文 | ❌ |
| 同步 WPS | ❌ |
| 失败停止点 | beat 未生成 → 不进入 Step 2 |
| Hermes 验收 | 检查 beat 场景数、剧情线、与 canon 的一致性 |

### Step 2: Writer

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_writer` |
| 输入 | outlines/beats/chapter_XXX.yaml, .webnovel/context/（可选）, MASTER_SETTING, runtime_canon, reader_debts, deai_rules, chapter_writer prompt |
| 输出 | manuscript/drafts/chapter_XXX_draft.md |
| 调 DeepSeek | ✅ 写正文草稿 |
| 调 Python | ❌ |
| 改 .story-system | ❌ |
| 改正文 | ✅ 写 draft（不覆盖已有 final） |
| 同步 WPS | ❌ |
| 失败停止点 | draft 字数不足或偏离 beat → 报告不自动推进 |
| Hermes 验收 | 字数 1500-3000、场景匹配 beat、无 canon 禁止词 |

### Step 3: analyze_sentence_rhythm（Python 工具层）

| 项目 | 内容 |
|------|------|
| 工具 | `scripts/analyze_sentence_rhythm.py` |
| 输入 | manuscript/drafts/chapter_XXX_draft.md |
| 输出 | deai_reports/chapter_XXX_sentence_rhythm.yaml |
| 调 Python | ✅ 量化分析句式节奏 |
| 改正文 | ❌ |
| 失败停止点 | 脚本报错 → 修复后重试 |
| Hermes 验收 | 输出文件存在且包含量化数据 |

### Step 4: detect_webnovel_ai_flavor

| 项目 | 内容 |
|------|------|
| Skill | `detect_webnovel_ai_flavor` |
| 输入 | chapter_XXX_draft.md, sentence_rhythm.yaml, deai_rules, Story Bible（可选）, Chapter Beat（可选） |
| 输出 | deai_reports/chapter_XXX_ai_flavor.yaml |
| 调 DeepSeek | ✅ 语义理解检测 |
| 调 Python | ❌（Hermes 直接分析） |
| 改 .story-system | ❌ |
| 改正文 | ❌ |
| 同步 WPS | ❌ |
| 失败停止点 | risk_level=high → 不进入 Step 5 |
| Hermes 验收 | 报告维度完整、score 方向正确 |

### Step 5: webnovel_reviewer

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_reviewer` |
| 输入 | chapter_XXX_draft.md, chapter beat（可选）, MASTER_SETTING（可选）, sentence_rhythm.yaml, ai_flavor.yaml, deai_rules |
| 输出 | reviews/chapter_XXX_review_with_deai.yaml |
| 调 DeepSeek | ✅ 十维度审稿 |
| 调 Python | ❌ |
| 改 .story-system | ❌ |
| 改正文 | ❌ |
| 同步 WPS | ❌ |
| 失败停止点 | 任一维度 score 1-3 或 ai_flavor > 6 → 建议重写 |
| Hermes 验收 | 报告包含 score、issues、rewrite_instructions、polisher_instructions |

### Step 6: webnovel_polisher

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_polisher` |
| 输入 | chapter_XXX_draft.md（或被 reviewer 修改后的版本）, review_with_deai.yaml, sentence_rhythm.yaml, ai_flavor.yaml, deai_rules, chapter beat（可选）, MASTER_SETTING（可选） |
| 输出 | manuscript/polished/chapter_XXX_deai_polished.md, deai_reports/chapter_XXX_polish_comparison.yaml |
| 调 DeepSeek | ✅ 去 AI 味润色 |
| 调 Python | ❌ |
| 改 .story-system | ❌ |
| 改正文 | ✅ 写 polished 副本（不覆盖 draft / final） |
| 同步 WPS | ❌ |
| 失败停止点 | polished 文件为空 → 不进入 Step 7 |
| Hermes 验收 | polished 为纯正文、draft 未被覆盖、对比报告存在 |

### Step 7: webnovel_state_manager

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_state_manager` |
| 输入 | polished 或 final 正文, review（可选）, MASTER_SETTING, runtime_canon, reader_debts, canon_patterns, 已有 commit（可选）, chapter_commit prompt |
| 输出 | chapter_XXX_commit.yaml（draft）, runtime_canon.yaml（apply）, reader_debts.yaml（apply）, .webnovel/state.yaml, .webnovel/summaries/, .webnovel/projection/, audit_log.jsonl |
| 调 DeepSeek | ✅ draft_commit 模式 |
| 调 Python | ✅ validate_canon_consistency.py |
| 改 .story-system | ✅ runtime_canon + reader_debts + audit_log（仅 apply 模式） |
| 改正文 | ❌ |
| 同步 WPS | ❌ |
| 失败停止点 | commit 非 accepted → 不更新 runtime_canon |
| Hermes 验收 | commit 字段完整、projection 文件存在、validator 通过或无致命错误 |

### Step 8: webnovel_wps_sync

| 项目 | 内容 |
|------|------|
| Skill | `webnovel_wps_sync` |
| 输入 | doc_meta.yaml, .story-system, .webnovel/projection/, build/sync/validate 脚本, .env |
| 输出 | wps_projection/, doc_meta.yaml（更新后）, sync_log.jsonl, validate 结果 |
| 调 Python | ✅ build/sync/validate 脚本 |
| 改 .story-system | ❌ |
| 改正文 | ❌ |
| 同步 WPS | dry-run（默认）/ real（用户要求） |
| 失败停止点 | build 失败 → 保留已有投影 |
| Hermes 验收 | projection 存在、validate 通过、sync_log 有条目 |

## 链路总览表

| Step | Skill / 工具 | 调 DeepSeek | 调 Python | 改 story-system | 改正文 | 同步 WPS | 失败停止点 |
|------|-------------|:-----------:|:---------:|:---------------:|:------:|:--------:|-----------|
| 1 | webnovel_planner | ✅ | ❌ | ✅(新项目) | ❌ | ❌ | beat 缺失 |
| 2 | webnovel_writer | ✅ | ❌ | ❌ | ✅(draft) | ❌ | 字数/偏离 beat |
| 3 | analyze_sentence_rhythm.py | ❌ | ✅ | ❌ | ❌ | ❌ | 脚本报错 |
| 4 | detect_webnovel_ai_flavor | ✅ | ❌ | ❌ | ❌ | ❌ | risk=high |
| 5 | webnovel_reviewer | ✅ | ❌ | ❌ | ❌ | ❌ | 任一维度 1-3 |
| 6 | webnovel_polisher | ✅ | ❌ | ❌ | ✅(polished) | ❌ | polished 为空 |
| 7 | webnovel_state_manager | ✅(draft) | ✅(validate) | ✅(apply) | ❌ | ❌ | commit 非 accepted |
| 8 | webnovel_wps_sync | ❌ | ✅ | ❌ | ❌ | ✅(dry/real) | build/validate 失败 |

## Hermes 调度原则

1. **不放权给 Python**: 角色 Skill 由 Hermes 调用 DeepSeek 执行，不通过 Python 脚本编排
2. **每步验收**: 每个 Step 后 Hermes 检查输出，决定是否继续
3. **允许跳过**: 如果某步输出质量透明，Hermes 可以跳过（如 AI 味检测后直接进 Polisher）
4. **允许回退**: 如果 Reviewer 不合格，回到 Writer / Planner
5. **不变更边界**: 已定义的 Skill 禁止行为在任何步骤中都不被覆盖

## Prompt 对应

| Prompt 文件 | 用于 | 对应 Skill |
|-------------|------|-----------|
| templates/prompts/story_bible.md | 生成 Story Bible | webnovel_planner |
| templates/prompts/chapter_outline.md | 生成前 N 章大纲 | webnovel_planner |
| templates/prompts/chapter_beat.md | 生成单章 beat | webnovel_planner |
| templates/prompts/chapter_writer.md | 写正文草稿 | webnovel_writer |
| templates/prompts/chapter_review.md | 十维度审稿 | webnovel_reviewer |
| templates/prompts/chapter_polish.md | 去 AI 味润色 | webnovel_polisher |
| templates/prompts/chapter_commit.md | 生成 chapter_commit | webnovel_state_manager |
| templates/prompts/projection.md | 生成状态投影 | webnovel_state_manager |
| templates/prompts/preflight_context.md | 上下文摘要（可选） | webnovel_planner / webnovel_writer |
| templates/prompts/humanize.md | 人性化润色（备用） | 可选 |
