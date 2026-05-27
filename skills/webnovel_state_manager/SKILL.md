---
name: webnovel_state_manager
description: "webnovel-hermes-wps 状态管理角色 Skill — 读取 accepted chapter_commit，更新 runtime_canon、reader_debts、.webnovel/state.yaml、.webnovel/summaries/、.webnovel/projection/，写入 audit_log。支持 draft_commit 和 apply_commit 两种模式。不写正文，不润色，不同步 WPS。"
tags: ["webnovel", "state-manager", "canon", "projection", "phase7"]
---

# webnovel_state_manager Skill

## 用途

保证 .story-system 真源和 .webnovel 投影层的一致性。负责在章节通过验收后，将章节内容的影响写入状态文件。

## 两种模式

### mode: draft_commit
- 根据 polished / final 文本生成 chapter_commit.yaml 草案
- 不更新 runtime_canon
- 用于审稿前的状态初评

### mode: apply_commit
- 只接受 status: accepted 的 chapter_commit
- 更新 runtime_canon、reader_debts、.webnovel 投影
- 用于章节通过验收后的正式状态更新

## 适用场景

1. 章节经过 Polisher 处理后，生成 chapter_commit 草案（draft_commit）
2. 章节通过主控方验收后，正式应用 commit 到 story-system（apply_commit）
3. 需要更新 .webnovel 投影层时

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| 最终正文 | `manuscript/chapters/chapter_XXX_final.md` 或 `manuscript/polished/chapter_XXX_deai_polished.md` | ✅ |
| Reviewer 报告 | `reviews/chapter_XXX_review_with_deai.yaml` | 可选 |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | ✅ |
| runtime_canon | `.story-system/runtime_canon.yaml` | ✅ |
| reader_debts | `.story-system/reader_debts.yaml` | ✅ |
| canon_patterns | `.story-system/canon_patterns.yaml` | ✅ |
| 已有 chapter_commit | `.story-system/chapter_commits/chapter_XXX_commit.yaml` | 可选 |
| chapter_commit Prompt | `templates/prompts/chapter_commit.md` | ✅ |

## 输出

| 输出 | 路径 | 模式 |
|------|------|------|
| chapter_commit 草案 | `.story-system/chapter_commits/chapter_XXX_commit.yaml` | draft_commit |
| runtime_canon | `.story-system/runtime_canon.yaml` | apply_commit |
| reader_debts | `.story-system/reader_debts.yaml` | apply_commit |
| state.yaml | `.webnovel/state.yaml` | apply_commit |
| 章节摘要 | `.webnovel/summaries/chapter_XXX.yaml` | apply_commit |
| 投影文件 | `.webnovel/projection/*` | apply_commit |
| audit_log | `.story-system/audit_log.jsonl` | apply_commit |

## 允许读取路径

- `manuscript/chapters/`
- `manuscript/polished/`
- `reviews/`
- `.story-system/`
- `.webnovel/`（如存在）
- `templates/prompts/chapter_commit.md`
- `templates/prompts/projection.md`
- `scripts/validate_canon_consistency.py`

## 允许写入路径

- `.story-system/chapter_commits/`
- `.story-system/runtime_canon.yaml`
- `.story-system/reader_debts.yaml`
- `.story-system/audit_log.jsonl`
- `.webnovel/`
- `scripts/`（仅用于调用 validator）

## 禁止行为

1. 不写正文
2. 不润色正文
3. 不改 Story Bible 核心设定（MASTER_SETTING 中的角色设定 / 世界观规则）
4. 不同步 WPS
5. 不跳过 chapter_commit 直接改 runtime_canon
6. 不接受非 accepted 的 chapter_commit 更新正典（apply_commit 模式）
7. 不从 WPS 反推状态
8. 不删除已有 chapter_commit 记录
9. 不修改已有 draft / final
10. 不生成新正文

## 执行步骤

### draft_commit 模式

1. 确认 polished 或 final 正文存在
2. 读取 MASTER_SETTING、runtime_canon、reader_debts
3. 读取 chapter_commit Prompt 模板
4. 调用 DeepSeek，传入正文 + 当前状态，生成 chapter_commit 草案
5. 写入 `.story-system/chapter_commits/chapter_XXX_commit.yaml`
6. 报告 commit 草案路径和状态变化摘要

### apply_commit 模式

#### 安全顺序（必须严格按此顺序执行）

1. **校验准备**
   - 确认 `.story-system/chapter_commits/chapter_XXX_commit.yaml` 存在
   - 检查 commit 文件中 status 字段是否为 `accepted`
   - 如非 accepted → 停止并报告
   - 如为 accepted → 继续

2. **生成临时状态（不污染正式文件）**
   - 读取当前 runtime_canon.yaml、reader_debts.yaml、.webnovel/state.yaml
   - 基于 accepted chapter_commit，在内存中构建 `next_runtime_canon` / `next_reader_debts` / `next_webnovel_state`
   - 将临时状态写入临时文件（如 `_tmp_next_runtime_canon.yaml`），注意：临时文件必须位于同一目录，确保 validator 能读取

3. **运行 canon validator**
   - 调用 `scripts/validate_canon_consistency.py`，指向临时状态文件
   - 获取 validator 输出（pass / fail + 具体问题列表）

4. **根据验证结果决定写入**
   - **通过（pass）**：
     - 将 next_runtime_canon 写入正式 `runtime_canon.yaml`
     - 将 next_reader_debts 写入正式 `reader_debts.yaml`
     - 更新 `.webnovel/state.yaml`
     - 写入 `.webnovel/summaries/chapter_XXX.yaml`
     - 生成或刷新 `.webnovel/projection/` 下的投影文件
     - 写入 `.story-system/audit_log.jsonl`，记录 `validated: true, validation_result: pass`
   - **失败（fail）**：
     - 不写入任何正式文件
     - 不污染 runtime_canon、reader_debts、.webnovel 投影
     - 仅写入 `.story-system/audit_log.jsonl`，记录 `validated: true, validation_result: fail, issues: [...]`
     - 报告失败原因和具体问题列表，要求修改 chapter_commit 后重试

5. **清理临时文件**
   - 删除 `_tmp_next_*` 临时文件
   - 报告更新结果（通过或失败详情）

## 失败处理

1. polished/final 不存在 → draft_commit 停止并报告
2. chapter_commit 不存在 → apply_commit 停止并报告
3. chapter_commit status != accepted → apply_commit 停止并报告
4. canon validator 不一致 → 报告不一致项，阻止写入正式文件，仅记录 audit_log
5. 写入路径不存在 → 自动创建目录
6. DeepSeek 输出截断 → 重试最多 1 次

## 验收标准

1. chapter_commit.yaml 存在且字段完整
2. runtime_canon.yaml 已包含新章节事件
3. reader_debts.yaml 已更新
4. .webnovel/state.yaml 存在且反映最新状态
5. .webnovel/summaries/chapter_XXX.yaml 存在
6. .webnovel/projection/ 投影文件已更新
7. audit_log.jsonl 有新条目
8. canon validator 通过或无致命错误
9. 未修改任何 draft / final
10. 未同步 WPS

## 与其他 Skill 的关系

- **webnovel_planner**: StateManager 不规划剧情
- **webnovel_writer**: StateManager 不写正文
- **detect_webnovel_ai_flavor / webnovel_reviewer / webnovel_polisher**: StateManager 在质量闸门完成后执行，不在之前
- **webnovel_wps_sync**: StateManager 更新真源和投影，WpsSync 将投影同步到 WPS
