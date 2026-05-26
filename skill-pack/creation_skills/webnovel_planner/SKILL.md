---
name: webnovel_planner
description: "webnovel-hermes-wps 规划角色 Skill — 生成 Story Bible、前 N 章章节大纲、单章 chapter beat、维护读者期待债规划。不写正文，不审稿，不润色，不同步 WPS。"
tags: ["webnovel", "planner", "outline", "beat", "phase7"]
---

# webnovel_planner Skill

## 用途

为创作链路提供剧情规划输入。Planner 的输出是 Writer 的唯一写作依据。

## 适用场景

1. 新项目启动时生成 Story Bible
2. 连载过程中生成新的前 N 章大纲
3. 每章开始前生成该章 chapter beat
4. 用户有剧情讨论需求时参与规划讨论
5. 维护 reader_debts 的规划部分（不直接修改文件）

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| project.yaml | `project.yaml` | ✅ |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | 可选 |
| runtime_canon | `.story-system/runtime_canon.yaml` | 可选 |
| reader_debts | `.story-system/reader_debts.yaml` | 可选 |
| 已有 outline | `outlines/chapters_001_030.yaml` | 可选 |
| 已有 beats | `outlines/beats/` | 可选 |
| 用户任务说明 | Hermes 传入 | ✅ |

## 输出

| 输出 | 路径 |
|------|------|
| Story Bible | `.story-system/MASTER_SETTING.yaml` |
| 前 N 章大纲 | `outlines/chapters_001_030.yaml` |
| 单章 beat | `outlines/beats/chapter_XXX.yaml` |
| 章节上下文 | `.webnovel/context/chapter_XXX_context.yaml`（可选） |

## 允许读取路径

- `project.yaml`
- `.story-system/`
- `outlines/`
- `.webnovel/context/`（如存在）
- `templates/prompts/`（仅读取 Prompt 模板）

## 允许写入路径

- `.story-system/MASTER_SETTING.yaml`
- `outlines/`
- `.webnovel/context/`

## 禁止行为

1. 不写正文
2. 不审稿
3. 不润色
4. 不更新 runtime_canon
5. 不生成 chapter_commit
6. 不同步 WPS
7. 不跳过用户确认直接写入已有的 MASTER_SETTING
8. 不修改已有 chapter_commits
9. 不编辑已有 draft / final
10. 不决定章节是否通过验收

## 执行步骤

1. Hermes 传入任务说明（新项目 / 续写 / 剧情讨论）
2. 读取所有可选输入（如存在）
3. 如为新项目，生成 Story Bible → 写入 MASTER_SETTING.yaml
4. 如需要生成大纲，调用 DeepSeek 生成前 N 章 outline → 写入 `outlines/chapters_001_030.yaml`
5. 如需生成单章 beat，读取 outline + runtime_canon + reader_debts，调用 DeepSeek 生成 chapter beat → 写入 `outlines/beats/chapter_XXX.yaml`
6. 如需生成上下文，写入 `.webnovel/context/chapter_XXX_context.yaml`
7. 向 Hermes 报告输出文件路径

## 失败处理

1. project.yaml 不存在 → 停止并报告，要求创建
2. 生成 beat 但 outline 不存在 → 先建议生成 outline，不强制
3. DeepSeek 输出截断 → 重试最多 1 次
4. 写入路径不存在 → 自动创建目录

## 验收标准

1. MASTER_SETTING.yaml 包含可用设定
2. outline 有完整主线路线图
3. chapter beat 包含 4-6 个场景
4. 所有输出与已有 canon 无冲突
5. 未写入任何正文内容
6. 未修改任何已有正文文件

## 与其他 Skill 的关系

- **webnovel_writer**: Planner 的输出 beat 是 Writer 的唯一写作输入
- **webnovel_state_manager**: Planner 不替代 StateManager 的职责，不更新 runtime_canon
- **detect_webnovel_ai_flavor / webnovel_reviewer / webnovel_polisher**: Planner 的 beat 供 Reviewer 判断章节是否按规划执行
- **webnovel_wps_sync**: Planner 不同步 WPS
