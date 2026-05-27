---
name: webnovel_reviewer
description: "webnovel-hermes-wps 审稿角色 Skill — 从十一维度评估章节正文质量，吸收 sentence_rhythm 报告和 ai_flavor 检测报告，输出结构化审稿报告和 Polisher 指令。不修改正文，不生成新章节，不同步 WPS。"
tags: ["webnovel", "reviewer", "quality-gate", "deai", "phase6b"]
---

# webnovel_reviewer Skill

## 适用场景

1. 章节草稿完成后，审稿人做十一维度质量评估
2. 审稿报告中必须吸收去 AI 味检测结果
3. 输出 rewrite_instructions 供 Writer 参考，输出 polisher_instructions 供 Polisher 使用
4. 决定该章节是否可以进入 Polisher 阶段

## 输入

| 输入 | 路径模式 | 必需 |
|------|----------|------|
| 章节草稿 | `manuscript/drafts/chapter_XXX_draft.md` 或 `manuscript/chapters/chapter_XXX_final.md` | ✅ |
| Chapter Beat | `outlines/beats/chapter_XXX.yaml` 或章节目录下的 `beat.md` | 可选 |
| MASTER_SETTING | `.story-system/MASTER_SETTING.yaml` | 可选 |
| 句式节奏报告 | `deai_reports/chapter_XXX_sentence_rhythm.yaml` | ✅ |
| AI 味检测报告 | `deai_reports/chapter_XXX_ai_flavor.yaml` | ✅ |
| deai_rules 规则库 | `templates/deai_rules/` | ✅ |

## 输出

`reviews/chapter_XXX_review_with_deai.yaml`

## 十一个审稿维度

| # | 维度 | 说明 | 分值方向 |
|---|------|------|----------|
| 1 | plot_progress | 剧情推进：是否有新信息/新冲突/不可逆变化 | 1-10 |
| 2 | character_consistency | 角色一致性：是否符合既定人设 | 1-10 |
| 3 | logic_continuity | 逻辑连续性：是否承接上章，不推翻 runtime_canon | 1-10 |
| 4 | pacing | 节奏：是否张弛有度，钩子密度合理 | 1-10 |
| 5 | ending_hook | 章尾钩子：是否制造了"必须读下一章"的缺口 | 1-10 |
| 6 | cool_point | 爽点：是否有兑现感，是否有外部反应支撑 | 1-10 |
| 7 | information_density | 信息密度：每千字推进的信息点数量 | 1-10 |
| 8 | character_voice | 人物声口：对话是否能区分角色 | 1-10 |
| 9 | sentence_rhythm | 句式节奏：基于 sentence_rhythm 报告 | 1-10 |
| 10 | ai_flavor | AI 味程度：基于 ai_flavor 报告 + 规则对照 | 1-10 |
| 11 | style_consistency | 风格一致性：是否保持网文质感 | 1-10 |

## 评分标准

- 1-3: 差（需要重写）
- 4-6: 中（有改善空间）
- 7-10: 好（可接受）

### 通过标准

- 十一个维度中没有 1-3 分项目
- ai_flavor 分数 <= 6
- deai_summary.risk_level 不为 high

## 输出 YAML 格式

```yaml
chapter: 1
source_file: ""
beat_file: ""
sentence_rhythm_report: ""
ai_flavor_report: ""

overall_score: 0
can_continue_to_polish: true | false

dimensions:
  plot_progress:
    score: 0
    issues: []
    suggestions: []
  # ... 其余 10 个维度

deai_summary:
  risk_level: low | medium | high
  main_ai_flavor_issues: []
  sentence_rhythm_issues: []
  must_fix_before_polish: []

rewrite_instructions: []
polisher_instructions: []
must_not_change: []
```

## Reviewer 职责

1. 读取章节草稿全文
2. 读取 chapter beat（如存在），判断是否按规划执行
3. 读取 MASTER_SETTING（如存在），判断世界观一致性
4. 读取 sentence_rhythm 报告，检查句式节奏问题
5. 读取 ai_flavor 报告，检查 AI 味问题
6. 读取 deai_rules 规则库，逐条对照
7. 输出结构化审稿报告
8. 给出 rewrite_instructions（给 Writer 的修改方向）
9. 给出 polisher_instructions（给 Polisher 的定向重写指令）

## Reviewer 禁止

1. 不生成正文
2. 不润色
3. 不改 final
4. 不改 runtime_canon
5. 不改 reader_debts
6. 不同步 WPS
7. 不生成 chapter_commit
8. 不把检测报告写回 WPS
9. 不新增剧情
10. 不改变 Story Bible
11. 不更新状态

## 执行步骤

1. 确认所有必需输入文件存在，缺少则停止并报告
2. 读取章节正文、beat、MASTER_SETTING
3. 读取 sentence_rhythm 报告和 ai_flavor 报告
4. 读取 deai_rules 规则库
5. 逐维度评估，产生 score + issues + suggestions
6. 综合 deai_summary
7. 生成 rewrite_instructions 和 polisher_instructions
8. 输出 YAML 到 reviews/chapter_XXX_review_with_deai.yaml
