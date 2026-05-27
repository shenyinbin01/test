---
name: webnovel_writer
description: "webnovel-hermes-wps 写手角色 Skill — 根据 Planner 生成的 chapter beat 和上下文，写正文草稿。遵守 Story Bible、runtime_canon、reader_debts、deai_rules。不审稿，不润色，不生成 final，不同步 WPS。"
tags: ["webnovel", "writer", "draft", "phase7"]
---

# webnovel_writer Skill

## 用途

根据 Planner 提供的 beat 和上下文，写出一章可读的网文正文草稿。Writer 不修改 final，不做质量判断。

## 适用场景

1. Planner 已完成 chapter beat 生成后
2. 需要对已有 beat 做草稿实现
3. 作为多角色链路的第一步正文生成

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| chapter beat | `outlines/beats/chapter_XXX.yaml` | ✅ |
| 章节上下文 | `.webnovel/context/chapter_XXX_context.yaml` | 可选 |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | ✅ |
| runtime_canon | `.story-system/runtime_canon.yaml` | ✅ |
| reader_debts | `.story-system/reader_debts.yaml` | ✅ |
| deai_rules | `templates/deai_rules/` | ✅ |
| Writer Prompt | `templates/prompts/chapter_writer.md` | ✅ |

## 输出

| 输出 | 路径 |
|------|------|
| 正文草稿 | `manuscript/drafts/chapter_XXX_draft.md` |

## 允许读取路径

- `outlines/beats/chapter_XXX.yaml`
- `.webnovel/context/`
- `.story-system/`
- `templates/deai_rules/`
- `templates/prompts/chapter_writer.md`

## 允许写入路径

- `manuscript/drafts/chapter_XXX_draft.md`

## 禁止行为

1. 不审稿
2. 不润色
3. 不生成 final
4. 不更新 runtime_canon
5. 不生成 chapter_commit
6. 不同步 WPS
7. 不跳过 Planner 直接自由发挥
8. 不改动 beat 中的场景事件
9. 不新增 beat 中未规划的剧情
10. 不修改已有 draft
11. 不覆盖已有 draft（除非 Hermes 明确要求重写）

## 执行步骤

1. 确认 chapter beat 存在
2. 读取 MASTER_SETTING、runtime_canon、reader_debts
3. 读取 deai_rules 规则库
4. 读取 Writer Prompt 模板
5. 调用 DeepSeek，传入 beat + context + 设定 + deai_rules
6. 接收 DeepSeek 输出的正文草稿
7. 检查是否完整（章节目标 2500-3000 中文字，最低 2200，超过 3500 建议拆章；场景数匹配 beat）
8. 写入 `manuscript/drafts/chapter_XXX_draft.md`
9. 向 Hermes 报告输出路径和基本信息（字数、场景数）

## 失败处理

1. chapter beat 不存在 → 停止并报告，要求先 Planner
2. DeepSeek 输出截断 → 分两段调用后合并
3. 字数低于 2200 或高于 3200 → 报告原因，由 Hermes 判断；超过 3500 建议拆章
4. 生成的内容明显偏离 beat → 停止并报告，不写入
5. 写入路径不存在 → 自动创建目录

## 验收标准

1. draft.md 是纯正文，不包含提示词或说明
2. 字数在 2500-3000 中文字范围（最低 2200 可接受，需说明原因；超过 3500 建议拆章）
3. 场景数与 beat 一致
4. 未出现禁止词列表中的词
5. 未修改 final / runtime_canon / .story-system
6. 未同步 WPS
7. 未出现 self-censor（如"我不能写"）

## 与其他 Skill 的关系

- **webnovel_planner**: Writer 依赖 Planner 的 beat；如果没有 beat，Writer 不应自行发挥
- **detect_webnovel_ai_flavor**: Writer 的 draft 是 Detector 的检测对象
- **webnovel_reviewer**: Writer 的 draft 是 Reviewer 的审稿对象
- **webnovel_polisher**: Writer 的 draft 不是 Polisher 的直接输入（Polisher 操作 polished 副本），但 Polisher 不覆盖 draft
- **webnovel_state_manager**: Writer 不处理状态更新
- **webnovel_wps_sync**: Writer 不同步 WPS
