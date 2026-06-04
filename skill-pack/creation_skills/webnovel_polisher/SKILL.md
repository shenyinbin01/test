---
name: webnovel_polisher
description: "webnovel-hermes-wps 润色角色 Skill — 根据 Reviewer 审稿报告、AI 味检测报告、句式节奏报告和 deai_rules，对章节正文进行定向去 AI 味重写和轻量表达增强。不覆盖 draft/final，不修改 .story-system，不同步 WPS。Phase 8 注入后定位升级：轻量增强而非救稿。"
tags: ["webnovel", "polisher", "deai", "quality-gate", "phase6b", "phase8"]
---

# webnovel_polisher

## 用途

根据 Reviewer 和 deai_reports 指出的具体问题，对章节文本进行低风险、可追踪、可对比的去 AI 味重写和轻量表达增强。

**Phase 8 核心定位变更：Polisher 是轻量增强角色，不是救稿角色。**
如果章节在结构、爽点、钩子、主角动机层面存在缺失，应退回 Reviewer → Writer 重新处理，不由 Polisher 硬补。

**Human Texture 实验 v0 边界：如果 Reviewer 的 `human_texture_review.gate` 不是 `pass_to_polisher`，不得进入 Polisher。**
Polisher 只能压缩显性说明、调整重复句式、增强已有章尾留白、让已有动作和对话更贴人物状态，并在结构通过后提升语言光泽。
Polisher 不得补人物私心、补关系债、重排信息露出、补代价后果、重写场景生活逻辑、用风景/比喻/口语化假装有人味，或把结构性失败润色成顺滑失败。

## 适用场景

1. 章节草稿完成并经过 Reviewer 审稿后
2. 检测报告显示有 AI 味问题需修正
3. 需要生成润色前后对比
4. 已有内容成立的前提下，做表达层面的轻量增强

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
16. **不允许补充缺失的结构、爽点、钩子或主角动机——这些应退回 Reviewer/Writer**
17. **不允许改变原 beat、原事件、原因果链**
18. **不允许补 Human Texture 的 private_want / relationship_debt_change / information_carrier / consequence_next_friction**
19. **不允许在 Human Texture gate 未通过时执行润色**

---

## Phase 8 轻量增强规则

以下四条规则是 Polisher 的表达增强方向。**每条规则只能在原文已有基础上增强，不可凭空新增内容。**

### 规则一：认知对比锐化（DCQG-C001）

**用途**：在原文已经存在"主角洞察 vs 他人误判"的场景中，强化对比的清晰度和情绪张力。

**允许的操作**：
- 将平淡的对比描写压实——减少中间解释性语句，让"对的"和"错的"直接碰撞
- 在他人的误判前增加一个微小的行为细节（一个表情、一个动作），让误判更可见
- 在主角洞察被验证的瞬间，增强验证方式的简洁度和冲击力

**禁止的操作**：
- 禁止新增原文没有的认知碾压桥段
- 禁止在原文没有对比的地方硬造对比
- 禁止把原本靠行动的展示改成旁白解释
- 禁止每章都机械强化同一模式

**判断标准**：如果原文已经被 Reviewer 判定为 `cognitive_advantage_triggered: true` 且执行良好——这条规则可以跳过。只在对比表达较平淡时介入。

---

### 规则二：价值观/理念冲突对话增强（DCQG-C015）

**用途**：在原文已经存在的关键对话场景中，压实立场差异、潜台词和人物态度。

**允许的操作**：
- 将"表明立场"的对话改为"透露立场"——减少直白声明，增加潜台词
- 在立场对立的对话中增加一个非语言的对抗细节（沉默、动作停顿、眼神偏移）
- 将两人连续替代表明立场的"A说B说A说B说"结构压缩，让关键句更有重量
- 在同一对话中，确保二人说话的节奏和长度不同（一人短而硬，一人长而绕）

**禁止的操作**：
- 禁止新增长篇价值观独白
- 禁止把人物写成"观点接口"——每句话都要像这个人在说话而非作者在借他说话
- 禁止在原本只是信息交换的对话中强行塞入价值观冲突
- 禁止为所有角色统一增加"深度思考"式内心活动

**判断标准**：如果原文对话 Reviewer 的 `character_voice` 评分 ≥7，且对话本身不是关键冲突场景——这条规则可以跳过。

---

### 规则三：规则利用清晰化（DCQG-C021）

**用途**：在原文已经存在 rule-based 破局的章节中，让规则破局的行动链条更可见。

**允许的操作**：
- 在破局前增加一个"主角注意到规则细节"的瞬间（一句话即可，不是新增发现，是强化原文中已有的观察）
- 将"他利用规则反败为胜"的模糊表述改为可感知的动作链条（观察到→试探→确认→反制）
- 在破局瞬间增加对手的微反应（一瞬的困惑→意识到来不及），强化"规则反转"的可感度

**禁止的操作**：
- 禁止改变原有破局逻辑——原文中主角利用了哪个规则漏洞，就是哪个，不得改
- 禁止新增设定或新增规则解释
- 禁止在原文没有 rule-based 破局的章节中制造规则破局
- 禁止在规则链中加入大段说明性文字

**判断标准**：检查 Reviewer 的 `conflict_resolution_type`。若为 `rule` 且 `cool_point` 评分 ≥8——链条已足够清晰，此规则可跳过。

---

### 规则四：章尾余味/回环增强（DCQG-C022）

**用途**：在原文已经有回环基础（章尾与开章/主线/情绪钩子有呼应）的章节，强化余味。

**允许的操作**：
- 在章尾最后 1-2 句增加一个与开章意象的隐性呼应（不是明说，是靠读者自己联想的细节——同一物件、同一光线、同一声音以变化后的状态再次出现）
- 将"总结式"章尾句改为"留白式"——删掉最后一句的总结性半句，让画面自己说话
- 在章尾钩子前增加 1 个感官细节（温度、声音、光线的变化），让情绪先于信息到达读者

**禁止的操作**：
- 禁止强行煽情（"他突然明白了生命的真谛"类句式）
- 禁止每章章尾都写"初心回归""想起最初的自己"等模板化表达
- 禁止在原文章尾已经很有力时再叠床架屋
- 禁止在章尾新增信息或新增钩子——回环是对已有意象的呼应，不是新内容

**判断标准**：检查 Reviewer 的 `ending_hook` 评分。若 ≥8 且章尾已有明显的意象呼应——这条规则可以跳过。评分 6-7 时适度介入。

---

### 四条规则的优先级和互斥

1. 不是每章都要用到全部四条规则——**根据 Reviewer 评分和原文实际情况选择 1-2 条即可**
2. 如果原文已被 Reviewer 判定为高质量（`overall_score ≥ 8.0`），四条规定全部可跳过
3. 永远不要让增强后的文本比原文更"像 AI 写的"——增强的目标是更像人写的
4. 如果拿不准某处是否该增强——不增强。Polisher 的第一原则是"不破坏已有的好东西"

---

## 执行步骤

1. 确认原章节正文存在
2. 确认 Reviewer 报告存在
3. 确认 deai_reports（sentence_rhythm + ai_flavor）存在
4. 确认 deai_rules 规则库存在
5. 读取 Reviewer 的 rewrite_instructions 和 polisher_instructions
6. 读取 ai_flavor 和 sentence_rhythm 报告中的具体问题
7. 读取 deai_rules 规则库
8. 如 Reviewer 报告包含 `human_texture_review`，确认其 `gate` 为 `pass_to_polisher`；否则停止并退回 Reviewer
9. **审查 Reviewer 的 template_risk 分数——若 ≥8，四条 Phase 8 增强规则全部跳过**
10. **根据 Reviewer 各项评分，选择适用的 Phase 8 增强规则（通常 1-2 条）**
11. 只针对明确问题 + 适用规则重写，不自由发挥
12. 保留剧情事件、人物关系、设定和章节结果
13. **保留原 beat、原事件、原因果链——不得修改**
14. 输出新的 polished 文件到 `manuscript/polished/`
15. 生成 polish_comparison 报告
16. 不更新 final
17. 不更新 .story-system
18. 不同步 WPS

## 输出要求

1. polished 文件必须是小说正文，不能是审稿报告
2. polished 文件不能包含 "以下是润色稿" 等说明
3. polished 文件不能包含检测报告原文
4. 只修改 Reviewer 和 deai_reports 指出的问题 + 选用的 Phase 8 增强规则
5. 维持原章节的段落结构和叙事顺序
6. **polished 文件的字数增减应控制在原文的 ±10% 以内**

## 质量标准

1. 保留所有剧情事件
2. 保留人物关系
3. 保留设定规则
4. 保留章尾钩子
5. 保留原 beat、原事件、原因果链
6. 减少抽象情绪词
7. 减少解释性旁白
8. 增加动作承载
9. 改善句式开头重复
10. 保持网文节奏
11. **不新增结构/爽点/钩子/主角动机**

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
9. **polished 文件的剧情结构和事件结果与原文一致**
10. **字数增减在原文 ±10% 以内**
11. 如存在 `human_texture_review`，必须已通过 gate，且未新增结构性 Human Texture 字段
