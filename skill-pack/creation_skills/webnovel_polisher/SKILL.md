---
name: webnovel_polisher
description: "webnovel-hermes-wps 润色角色 Skill — 根据 Reviewer 审稿报告、AI 味检测报告、句式节奏报告和 deai_rules，对章节正文进行定向去 AI 味重写。不覆盖 draft/final，不修改 .story-system，不同步 WPS。"
tags: ["webnovel", "polisher", "deai", "quality-gate", "phase6b"]
---

# webnovel_polisher

## 用途

根据 Reviewer 和 deai_reports 指出的具体问题，对章节文本进行低风险、可追踪、可对比的去 AI 味重写。

## 适用场景

1. 章节草稿完成并经过 Reviewer 审稿后
2. 检测报告显示有 AI 味问题需修正
3. 需要生成润色前后对比

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| 原章节正文 | `manuscript/drafts/chapter_XXX_draft.md` 或 `manuscript/chapters/chapter_XXX_final.md` | ✅ |
| Reviewer 报告 | `reviews/chapter_XXX_review_with_deai.yaml` | ✅ |
| sentence_rhythm 报告 | `deai_reports/chapter_XXX_sentence_rhythm.yaml` | ✅ |
| ai_flavor 报告 | `deai_reports/chapter_XXX_ai_flavor.yaml` | ✅ |
| deai_rules 规则库 | `templates/deai_rules/` | ✅ |
| Chapter Beat | `outlines/beats/chapter_XXX.yaml` | 可选 |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | 可选 |

## 输出

| 输出 | 路径 |
|------|------|
| 润色稿 | `manuscript/polished/chapter_XXX_deai_polished.md` |
| 对比报告 | `deai_reports/chapter_XXX_polish_comparison.yaml` |

## 允许读取路径

- `manuscript/drafts/`
- `manuscript/chapters/`
- `reviews/`
- `deai_reports/`
- `templates/deai_rules/`
- `outlines/beats/`
- `.story-system/MASTER_SETTING.yaml`

## 允许写入路径

- `manuscript/polished/chapter_XXX_deai_polished.md`
- `deai_reports/chapter_XXX_polish_comparison.yaml`

## 禁止行为

1. 不允许覆盖 draft
2. 不允许覆盖 final
3. 不允许修改 .story-system
4. 不允许修改 runtime_canon
5. 不允许修改 reader_debts
6. 不允许生成 chapter_commit
7. 不允许同步 WPS
8. 不允许新增重大剧情
9. 不允许改变人物关系
10. 不允许改变主角核心目标
11. 不允许改变本章事件结果
12. 不允许把正文改成大纲或总结
13. 不允许只做词语替换
14. 不允许为了"去 AI 味"牺牲剧情清晰度
15. 不允许把 Reviewer 报告和检测报告原文塞进正文

## 执行步骤

1. 确认原章节正文存在
2. 确认 Reviewer 报告存在
3. 确认 deai_reports（sentence_rhythm + ai_flavor）存在
4. 确认 deai_rules 规则库存在
5. 读取 Reviewer 的 rewrite_instructions 和 polisher_instructions
6. 读取 ai_flavor 和 sentence_rhythm 报告中的具体问题
7. 读取 deai_rules 规则库
8. 只针对明确问题重写，不自由发挥
9. 保留剧情事件、人物关系、设定和章节结果
10. 输出新的 polished 文件到 `manuscript/polished/`
11. 生成 polish_comparison 报告
12. 不更新 final
13. 不更新 .story-system
14. 不同步 WPS

## 输出要求

1. polished 文件必须是小说正文，不能是审稿报告
2. polished 文件不能包含 "以下是润色稿" 等说明
3. polished 文件不能包含检测报告原文
4. 只修改 Reviewer 和 deai_reports 指出的问题
5. 维持原章节的段落结构和叙事顺序

## 质量标准

1. 保留所有剧情事件
2. 保留人物关系
3. 保留设定规则
4. 保留章尾钩子
5. 减少抽象情绪词
6. 减少解释性旁白
7. 增加动作承载
8. 改善句式开头重复
9. 保持网文节奏

## 失败处理

1. 原章节正文不存在 → 停止并报告
2. Reviewer 报告不存在 → 停止并报告
3. deai_reports 不存在 → 停止并报告
4. polished 生成失败 → 不写入空文件
5. 对比报告生成失败 → 不影响 polished 文件

## 验收标准

1. polished 文件是小说正文
2. polished 文件不是空的
3. polished 文件不包含审稿报告内容
4. draft 未被覆盖
5. final 未被覆盖
6. .story-system 未被修改
7. WPS 未同步
8. 对比报告存在
