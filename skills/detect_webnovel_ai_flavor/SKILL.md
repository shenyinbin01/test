---
name: detect_webnovel_ai_flavor
description: "中文网文 AI 味检测 Skill — 读取章节正文、deai_rules 规则库、句式节奏分析报告，生成 12 维度 AI 味检测报告。Hermes 读取此 Skill 后调用 analyze_sentence_rhythm.py 再进行语义检测，不直接改正文。"
tags: ["webnovel", "deai", "quality-gate", "detection", "phase6b"]
---

# detect-webnovel-ai-flavor Skill

## 适用场景

1. 章节生产完成后，运行 AI 味检测
2. 对现有正文做质量评估
3. 为 Reviewer / Polisher 提供定向重写依据
4. 生成 deai_reports/ 下的检测报告

## 输入

1. **章节正文文件** — final.md / humanized.md / draft.md
2. **句式节奏分析报告** — deai_reports/chapter_XXX_sentence_rhythm.yaml（由 analyze_sentence_rhythm.py 生成）
3. **deai_rules 规则库** — templates/deai_rules/（7 个规则文件）
4. **Story Bible / MASTER_SETTING.yaml** — 如存在，用于剧情上下文判断
5. **Chapter Beat** — 如存在，用于判断是否偏离目标

## 输出

deai_reports/chapter_XXX_ai_flavor.yaml

## 检测维度

| # | 维度 | 分值范围 | 说明 |
|---|------|----------|------|
| 1 | sentence_mechanicalness | 0-10 | 句式机械感高 = AI 腔 |
| 2 | paragraph_rhythm | 0-10 | 段落节奏太平均 = AI 腔 |
| 3 | character_voice | 0-10 | 人物声口差异不足 = AI 腔 |
| 4 | emotion_labeling | 0-10 | 情绪靠标签表达 = AI 腔 |
| 5 | explanatory_narration | 0-10 | 解释性旁白过多 = AI 腔 |
| 6 | action_grounding | 0-10 | 信息靠叙述而非动作承载 |
| 7 | information_density | 0-10 | 信息密度不足 = AI 腔 |
| 8 | conflict_grounding | 0-10 | 冲突不落地 |
| 9 | cool_point_payoff | 0-10 | 爽点兑现感不足 |
| 10 | ending_hook | 0-10 | 章尾钩子弱 |
| 11 | webnovel_texture | 0-10 | 网文质感 |
| 12 | overall_ai_flavor_score | 0-10 | 综合 AI 味分数 |

评分标准：
- 0-3: 好（网文化程度高，可接受）
- 4-6: 中（有改善空间，建议润色）
- 7-10: 差（需要重写）

风险等级：
- low: overall_ai_flavor_score <= 3
- medium: 4 <= overall_ai_flavor_score <= 6
- high: overall_ai_flavor_score >= 7

## 输出格式模板

```yaml
chapter: 1
source_file: "/path/to/chapter_001_draft.md"
sentence_rhythm_report: "/path/to/chapter_001_sentence_rhythm.yaml"

overall_ai_flavor_score: 5
risk_level: medium

dimensions:
  sentence_mechanicalness:
    score: 5
    issues:
      - "句长过于平均，缺少短长交替"
    evidence:
      - "avg_sentence_length: 16.2, variance: low"
    suggestions:
      - "插入短句（3-8字）打破平均节奏"

  paragraph_rhythm:
    score: 4
    issues: []
    evidence: []
    suggestions: []

  character_voice:
    score: 3
    issues: []
    evidence: []
    suggestions: []

  emotion_labeling:
    score: 6
    issues: []
    evidence: []
    suggestions: []

  explanatory_narration:
    score: 5
    issues: []
    evidence: []
    suggestions: []

  action_grounding:
    score: 4
    issues: []
    evidence: []
    suggestions: []

  information_density:
    score: 3
    issues: []
    evidence: []
    suggestions: []

  conflict_grounding:
    score: 4
    issues: []
    evidence: []
    suggestions: []

  cool_point_payoff:
    score: 5
    issues: []
    evidence: []
    suggestions: []

  ending_hook:
    score: 3
    issues: []
    evidence: []
    suggestions: []

rewrite_priorities:
  - "first_pass: sentence_mechanicalness + emotion_labeling"
  - "second_pass: explanatory_narration + action_grounding"

must_not_change:
  - "主线剧情"
  - "角色关系"
  - "能力设定"

polisher_instructions:
  - "减少他/她开句"
  - "心理描写改为动作承载"
  - "删除解释性旁白"
  - "增强对话声口区分"
```

## 使用方式

### Hermes 调用流程

```bash
# 1. 运行句式节奏分析
python scripts/analyze_sentence_rhythm.py \
  --input /path/to/chapter_001_draft.md \
  --output deai_reports/chapter_001_sentence_rhythm.yaml

# 2. Hermes 读取：
#    - analyze_sentence_rhythm 输出报告
#    - templates/deai_rules/ 下规则文件
#    - 章节正文文件
# 然后结合剧情上下文，按 12 维度逐项评估
# 输出 ai_flavor.yaml 报告

# 3. 检查报告
cat deai_reports/chapter_001_ai_flavor.yaml
```

### Hermes 检测流程

1. 读取 **句式节奏分析报告** — 获取量化指标
2. 读取 **deai_rules 规则库** — 逐条对照
3. 阅读 **正文** — 凭文本理解做 12 维度评测
4. 跨参考 **Story Bible / Chapter Beat** — 判断是否偏离
5. 输出 **YAML 检测报告** — 写入 deai_reports/

## 检测标准细则

### 1. sentence_mechanicalness（句式机械感）

高指标：
- avg_sentence_length 在 12-20 之间且方差 low
- 大量"他/她"开句
- 缺少残句/短句单段

### 2. paragraph_rhythm（段落节奏）

高指标：
- 段落句数标准差 < 0.8
- 大部分段落 3-5 句

### 3. character_voice（人物声口）

高指标：
- 对话摘掉角色名后无法区分
- 所有角色语气一致
- 缺少潜台词

### 4. emotion_labeling（情绪标签化）

高指标：
- abstract_emotion_density > 5/千字
- 大量"感到""觉得""愤怒""震惊"等词
- 情绪缺少身体反应和动作支撑

### 5. explanatory_narration（解释性旁白）

高指标：
- "因为""所以""这意味着""换句话说"等连接词密集
- inner_monologue_ratio > 0.3
- 解释角色行为动机

### 6. action_grounding（动作承载）

低指标：
- action_sentence_ratio < 0.15
- 信息通过心理活动或叙述传递

### 7. information_density（信息密度）

中指标：
- 每千字推进的剧情点数量
- dialogue_ratio 极端高或低

### 8. conflict_grounding（冲突落地）

高指标：
- 冲突停留在内心活动
- 冲突通过对话讨论而非行动

### 9. cool_point_payoff（爽点兑现）

高指标：
- 爽点用对话总结代替外部反应
- 缺少对手/旁观者的反馈

### 10. ending_hook（章尾钩子）

测试方法：
- 最后三句话是否制造了"必须读下一章"的缺口
- 章尾是否有总结性语言

### 11. webnovel_texture（网文质感）

检查：
- 场景切换是否自然
- 章内是否有节奏起伏
- 信息是否分层释放
- 有没有"读着像翻译文学"的感觉

## 禁止行为

1. 不直接改正文
2. 不输出润色稿
3. 不改变剧情
4. 不新增设定
5. 不更新 runtime_canon
6. 不同步 WPS
7. 不把检测报告写进 WPS
8. 不调用 DeepCode 改代码
9. 不新增章节
10. 不生成小说内容
