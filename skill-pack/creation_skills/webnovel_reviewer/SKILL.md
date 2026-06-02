---
name: webnovel_reviewer
description: "webnovel-hermes-wps 审稿角色 Skill — 从十四维度评估章节正文质量，吸收 sentence_rhythm 报告和 ai_flavor 检测报告，输出结构化审稿报告和 Polisher 指令。不修改正文，不生成新章节，不同步 WPS。"
tags: ["webnovel", "reviewer", "quality-gate", "deai", "phase6b", "phase8"]
---

# webnovel_reviewer Skill

## 适用场景

1. 章节草稿完成后，审稿人做多维度质量评估
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

## 审稿维度（十四维度）

### 基础十一维度

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

### Phase 8 注入三维度

| # | 维度 | 说明 | 分值方向 |
|---|------|------|----------|
| 12 | hook_pacing | 钩子节奏：短钩是否快兑/长钩是否有延续/章尾是否形成拉力 | 1-10 |
| 13 | payoff_visibility | 兑现可见度：兑现是否被读者看见/是否有情绪冲击/是否只是信息说明 | 1-10 |
| 14 | template_risk | 模板化风险：是否过度重复认知碾压/是否所有冲突同一种解法/技法感是否强于故事感 | 1-10 |

---

## 评分标准

- 1-3: 差（需要重写）
- 4-6: 中（有改善空间）
- 7-10: 好（可接受）

### 通过标准

- 十四个维度中没有 1-3 分项目
- ai_flavor 分数 <= 6
- template_risk 分数 >= 5（不能有明显的模板化痕迹）
- deai_summary.risk_level 不为 high

---

## Phase 8 注入维度详细说明

### 维度 12: hook_pacing（钩子节奏）

检查清单：
- 本章开了哪些短钩（1~3 章内兑现的小悬念）？
- 本章开了哪些长钩（跨卷大悬念）？
- 上一章开的短钩是否在本章兑现？如未兑现，是否有合理解释？
- 长钩在本章是否有延续（线索/障碍/新问题）？
- 同期进行中的长钩是否超过 3 个？（超过则标记 overload）
- 章尾是否形成了下一章的拉力？

评分标准：
- 1-3: 本章无钩子，或开钩太多但一个都没推进
- 4-6: 有钩子但兑现节奏拖沓（短钩超过 3 章未兑现）
- 7-10: 短钩及时兑现，长钩持续推进，章尾拉力明确

### 维度 13: payoff_visibility（兑现可见度）

检查清单：
- 兑现点是否在正文中被读者清楚看到？（不是隐含的推理结果）
- 兑现时是否有情绪冲击？（不是平淡的信息说明）
- 兑现是否是"作者说给读者听"而非"角色经历给读者看"？
- 长钩的微推进是否可感知？（读者能感觉到"离真相更近了"）
- 有没有开了钩但悄悄丢掉没兑现的？

评分标准：
- 1-3: 兑现被埋在信息堆里，或开了钩没兑现就忘了
- 4-6: 有兑现但冲击力弱，像信息说明
- 7-10: 兑现清晰、有情绪冲击、读者能明确感受到

### 维度 14: template_risk（模板化风险）

检查清单：
- 是否本章又用了"认知碾压三拍"（发现问题→心算真相→碾压解决）？
- 是否连续 2 章以上都在用同一模式解决冲突？
- 所有冲突是否都用了同一种解法（认知/力量/规则）？
- 技法感是否强于故事感？（读起来像"这是一次认知碾压的演示"而非"这是一个故事"）
- 认知优势是否被写成了旁白解释而非行为展示？

评分标准：
- 1-3: 明显的模板化——连续多章同模式，技法感碾压故事感
- 4-6: 有模板化倾向但尚可接受
- 7-10: 技法自然融入故事，无模板感

---

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
  # ... 其余 10 个基础维度
  hook_pacing:
    score: 0
    short_hooks_opened: []
    short_hooks_paid: []
    long_hooks_progressed: []
    overloaded: false
    issues: []
    suggestions: []
  payoff_visibility:
    score: 0
    payoff_events: []
    emotional_impact: ""  # weak / moderate / strong
    issues: []
    suggestions: []
  template_risk:
    score: 0
    repeated_patterns: []
    all_conflict_same_method: false
    technique_feels_stronger_than_story: false
    issues: []
    suggestions: []

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
7. **逐章检查钩子节奏（hook_pacing）：本章的短钩/长钩/兑现状态**
8. **检查兑现可见度（payoff_visibility）：兑现是否被读者看见、是否有情绪冲击**
9. **检查模板化风险（template_risk）：是否过度重复认知碾压、冲突解法单一、技法感 > 故事感**
10. 输出结构化审稿报告
11. 给出 rewrite_instructions（给 Writer 的修改方向）
12. 给出 polisher_instructions（给 Polisher 的定向重写指令）

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
5. 逐维度评估（含 Phase 8 注入的 hook_pacing / payoff_visibility / template_risk），产生 score + issues + suggestions
6. 综合 deai_summary
7. 生成 rewrite_instructions 和 polisher_instructions
8. 输出 YAML 到 reviews/chapter_XXX_review_with_deai.yaml
