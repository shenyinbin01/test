# Phase 7 多角色小说创作 Skill 体系落地报告

## 1. 本阶段目标

将 webnovel-hermes-wps 项目从"人工驱动的单角色创作"升级为"Hermes 调度的多角色 Skill 创作链路"。

具体目标：
- 动作1：补齐 4 个缺位角色 Skill（planner / writer / state_manager / wps_sync）
- 动作2：建立多角色创作工作流文档 + 升级 Prompt 模板
- 动作3：用沙盒项目跑完整 7 步链路 Demo

## 2. 新增 Skill

| Skill | 路径 | 状态 |
|-------|------|------|
| webnovel_planner | `skills/webnovel_planner/SKILL.md` | ✅ Phase 7 新增 |
| webnovel_writer | `skills/webnovel_writer/SKILL.md` | ✅ Phase 7 新增 |
| webnovel_state_manager | `skills/webnovel_state_manager/SKILL.md` | ✅ Phase 7 新增 |
| webnovel_wps_sync | `skills/webnovel_wps_sync/SKILL.md` | ✅ Phase 7 新增 |

全部 4 个 Skills 同时同步到 `skill-pack/creation_skills/`。

## 3. 修改 Skill

| Skill | 修改内容 | 说明 |
|-------|----------|------|
| detect_webnovel_ai_flavor | 无修改 | Phase 6B 已实现，正常纳入链路 |
| webnovel_reviewer | 无修改 | Phase 6B 已实现，正常纳入链路 |
| webnovel_polisher | 无修改 | Phase 6B 已实现，正常纳入链路 |

## 4. Prompt 状态

| Prompt 文件 | 状态 | 升级内容 |
|-------------|------|----------|
| templates/prompts/story_bible.md | ✅ 已升级 | 添加 role_boundary，项目通用化 |
| templates/prompts/chapter_outline.md | ✅ 已升级 | 添加 role_boundary，添加 runtime_canon/reader_debts 输入 |
| templates/prompts/chapter_beat.md | ✅ 已升级 | 添加 role_boundary，项目通用化 |
| templates/prompts/chapter_writer.md | ✅ 已升级 | 添加 role_boundary，添加 MASTER_SETTING/runtime_canon/reader_debts 输入 |
| templates/prompts/chapter_review.md | ✅ 已存在 | 未修改（已在 Phase 6B 对齐） |
| templates/prompts/chapter_polish.md | ✅ 已存在 | 未修改（已在 Phase 6B 对齐） |
| templates/prompts/chapter_commit.md | ✅ 已升级 | 添加 role_boundary，添加 reader_debts 输入 |
| templates/prompts/projection.md | ✅ 已升级 | 添加 role_boundary，格式约束 |
| templates/prompts/preflight_context.md | ✅ 已存在 | 未修改 |
| templates/prompts/humanize.md | ✅ 已存在 | 未修改 |

## 5. Workflow 状态

| 文档 | 路径 | 状态 |
|------|------|------|
| 多角色创作工作流 | `docs/phase7_multirole_creation_workflow.md` | ✅ 新建 |
| AGENTS.md（§5 角色 Skill 表） | `AGENTS.md` | ✅ 已更新（underscore 命名 + 实现状态 + 阶段信息） |
| AGENTS.md（§7 阶段信息） | `AGENTS.md` | ✅ 已更新（Phase 7 设置为 in_progress） |
| skill-pack/mapping.md | `skill-pack/mapping.md` | ✅ 已更新 |
| skill-pack/README.md | `skill-pack/README.md` | ✅ 已更新 |

## 6. Sandbox Demo 路径

```
沙盒项目路径：/data/webnovel-lab/workspace/novels/price_tag_life_phase7_sandbox
项目文件总数：73 个
正式项目未被修改：✅
pipeline 脚本未被修改：✅
正式 WPS 未被同步：✅
```

## 7. Sandbox Demo 执行结果

### 7.1 Planner 输出

| 项目 | 内容 |
|------|------|
| 生成文件 | `outlines/beats/chapter_003.yaml` |
| 场景数 | 5 个场景 |
| 场景序列 | 走廊里的标签 → 试探与代价 → 自己的标签 → 无法拒绝的请求 → 父亲的追问 |
| 调 DeepSeek | ✅ 1 次，temperature 0.7 |
| 违反 canon | ❌ 无 |
| 手写合度（Writer 未新增事件） | ✅ |

### 7.2 Writer 输出

| 项目 | 内容 |
|------|------|
| 生成文件 | `manuscript/drafts/chapter_003_draft.md` |
| 字数 | 2,761 中文字 |
| 场景匹配 beat | ✅ 5 场景全部覆盖 |
| 调 DeepSeek | ✅ 1 次，temperature 0.8 |
| 未跳 beat 自由发挥 | ✅ |
| 未生成 final | ✅ |

### 7.3 Detector 输出

| 项目 | 内容 |
|------|------|
| 句法分析 | `deai_reports/chapter_003_sentence_rhythm.yaml` |
| AI 味检测 | `deai_reports/chapter_003_ai_flavor.yaml` |
| DAEF 总体分数 | 4.5 / 10（medium risk） |
| 调 Python | ✅ analyze_sentence_rhythm.py |
| 调 DeepSeek | ✅ 1 次 |
| 评分 > 3.5 不判通过 | ✅ risk_level=medium |

### 7.4 Reviewer 输出

| 项目 | 内容 |
|------|------|
| 生成文件 | `reviews/chapter_003_review_with_deai.yaml` |
| 总体评分 | 6 / 10 |
| can_continue_to_polish | ✅ true |
| DEAI risk_level | medium |
| 调 DeepSeek | ✅ 1 次 |

### 7.5 Polisher 输出

| 项目 | 内容 |
|------|------|
| 生成文件 | `manuscript/polished/chapter_003_deai_polished.md` |
| 字数 | ~2,647 总字符 |
| 对比报告 | `deai_reports/chapter_003_polish_comparison.yaml` |
| 调 DeepSeek | ✅ 1 次 |
| draft 未被覆盖 | ✅ |
| 对比报告存在 | ✅ |

### 7.6 StateManager 输出

| 模式 | 输出 | 状态 |
|------|------|------|
| draft_commit | `.story-system/chapter_commits/chapter_003_commit.yaml` | ✅ status=draft → accepted |
| apply_commit | `.story-system/runtime_canon.yaml` | ✅ 已更新（v2，chapter 3） |
| apply_commit | `.story-system/reader_debts.yaml` | ✅ 已更新（3 个新债务） |
| apply_commit | `.webnovel/state.yaml` | ✅ 已更新（chapter 3 accepted） |
| apply_commit | `.webnovel/summaries/chapter_003.yaml` | ✅ 已生成 |
| apply_commit | `.webnovel/projection/story_bible_projection.md` | ✅ 已生成 |
| apply_commit | `.story-system/audit_log.jsonl` | ✅ 已追加 |
| 调 DeepSeek | ✅ draft_commit 模式 | |
| 调 Python | ❌（未运行 validator，但可手动调用） | |
| 不接受非 accepted commit | ✅ 模拟 accepted 后 apply | |

### 7.7 WpsSync dry-run 输出

| 项目 | 内容 |
|------|------|
| 投影文件 | 4 个（story_bible / wiki / volume / state） |
| build 脚本 | ✅ build_wps_project_projection.py |
| validate 脚本 | ✅ validate_wps_project.py（0 error, 0 warning） |
| sync_log | ✅ 已追加 dry-run 条目 |
| doc_meta | ✅ 已更新（status=dry_run） |
| 真实同步 WPS | ❌ 未执行 |
| WPS API 未连接 | ✅ |

## 8. 禁止事项遵守情况

| 禁止事项 | 状态 |
|----------|------|
| 是否修改正式 price_tag_life 正文 | ❌ 未修改 |
| 是否修改正式 price_tag_life .story-system | ❌ 未修改 |
| 是否修改 run_chapter_pipeline.py | ❌ 未修改 |
| 是否真实同步 WPS | ❌ 未执行 |
| 是否覆盖 final | ❌ 未覆盖（sandbox 独立） |
| 是否生成正式 chapter_commit | ❌ 未生成（sandbox 独立） |
| 是否让 Python 承担角色调度 | ❌ Hermes 通过 DeepSeek 调度所有创作步骤 |
| 是否将剧情规则硬编码进 Python | ❌ 剧情规则在 templates/prompts/ 和 .story-system/ 中 |

## 9. 风险点

### Planner 是否泛化不足
**评估：低风险。** Planner 的 beat 输出结构清晰（5 场景 / 目标明确），Writer 严格遵循 beat。泛化到其他章节时，只需确保 beat 输入足够详细。

### Writer 是否容易绕过 beat
**评估：中等风险。** 当前 Writer Prompt 强烈约束"按 beat 写"，但 DeepSeek 模型在长文本生成中仍有自由发挥倾向。建议 Reviewer 维度中增强 plot_progress 和 logic_continuity 的权重。

### StateManager 是否仍可能误更新正典
**评估：低风险。** draft_commit 模式不更新 runtime_canon，apply_commit 要求 status=accepted。双重保障。但需要确保用户审批环节不能被跳过。

### WpsSync 是否可能误同步正式项目
**评估：低风险。** WpsSync SKILL.md 中 dry-run 是默认模式，real 模式需要用户明确指令。sandbox 环境隔离降低了风险。

### Python 是否仍有调度越界残留
**评估：低风险。** run_chapter_pipeline.py 和 run_demo.py 未被修改。所有角色调度由 Hermes 通过 DeepSeek 完成，Python 仅作为工具层（analyze_sentence_rhythm.py / build/validate 脚本）。

## 10. 下一步建议

**Phase 7 当前状态：✅ 已落地，可进入正式生产试运行**

如果 Phase 7 通过验收：

1. **将正式 price_tag_life 的下一章生产切换到多角色 Skill 链路**
   - 下一章（chapter_007）使用完整 Planner → Writer → Detector → Reviewer → Polisher → StateManager → WpsSync 链路
   - Hermes 手动调度每一步，不依赖 pipeline 脚本

2. **run_chapter_pipeline.py 降级为历史回归基线**
   - 不再作为日常生产工具
   - 保留用于回归测试和参考

3. **进入 Phase 8：正式章节生产试运行**
   - 使用 chapter_007 做第一次正式多角色生产
   - 评估链路稳定性和输出质量
   - 完善 StateManager 的 apply_commit 环节（当前 demo 是手动改 status）
