# Phase 8 Step 7 — Skill Pack 第一批最小正式注入报告

## 概述
- 日期: 2026-06-02
- 模式: minimal_formal_injection
- 注入 Skill: webnovel_planner, webnovel_writer, webnovel_reviewer
- 排除 Skill: webnovel_polisher, webnovel_state_manager, webnovel_wps_sync, detect_webnovel_ai_flavor
- Selected Patterns: 6/20 (DCQG-C001, C009, C012, C004, C002, C005)

---

## 一、修改了哪些 Skill

| Skill | 文件路径 | 原行数 | 新行数 |
|-------|---------|--------|--------|
| webnovel_planner | ~/.hermes/skills/webnovel/webnovel_planner/SKILL.md | 105 | 173 |
| webnovel_writer | ~/.hermes/skills/webnovel/webnovel_writer/SKILL.md | 100 | 168 |
| webnovel_reviewer | ~/.hermes/skills/webnovel/webnovel_reviewer/SKILL.md | 124 | 210 |

---

## 二、每个 Skill 注入了哪些 Pattern

### webnovel_planner (3 patterns)

| Pattern | 转化方式 | 注入位置 |
|---------|---------|---------|
| DCQG-C001 认知优势 | Bible 新增字段 `protagonist_cognitive_advantage`，要求定义 domain / advantage / revelation_plan | Story Bible 增强字段 §1 |
| DCQG-C009 内在代价 | Bible 新增字段 `internalized_pressure`，要求定义 source / manifestation / escalation | Story Bible 增强字段 §2 |
| DCQG-C012 世界观揭秘驱动 | Bible 新增字段 `revelation_phases`；大纲要求体现分阶段设计；beat 要求标注 `revelation_progress` | Story Bible 增强字段 §3 + 执行步骤 §4 + beat 标注 |

### webnovel_writer (2 patterns)

| Pattern | 转化方式 | 注入位置 |
|---------|---------|---------|
| DCQG-C004 事件驱动开场 | 写作约束：开章 200 字内必须进入压力/冲突/任务/异常场景，三种标准入口 | 写作约束 §规则一 |
| DCQG-C002 规则破局 | 写作约束：高潮优先规则利用（先理解规则→找漏洞→在框架内逆转），禁止连续 3 章力量碾压 | 写作约束 §规则二 |

额外注入：
- 认知优势展示规则（beat 标注 `cognitive_advantage_triggered: true` 时的行为约束）
- 反模板化规则（不允许机械使用"认知碾压三拍"，要求变异使用方式）

### webnovel_reviewer (1 pattern + 1 额外检查)

| Pattern | 转化方式 | 注入位置 |
|---------|---------|---------|
| DCQG-C005 短钩快兑/长钩慢兑 | 新增审稿维度 #12 `hook_pacing` + #13 `payoff_visibility`，含详细检查清单和评分标准 | 审稿维度 → Phase 8 注入三维度 |
| (template_risk) | 新增审稿维度 #14 `template_risk`，检查认知碾压重复/冲突解法单一/技法感>故事感 | 审稿维度 → Phase 8 注入三维度 |

---

## 三、每个 Pattern 被转化成了什么

### DCQG-C001 → Planner Bible 字段
```yaml
protagonist_cognitive_advantage:
  domain: ""           # 优势领域
  advantage: ""        # 具体优势描述
  revelation_plan: ""  # 逐步展示计划
```
规则：不写旁白解释，通过动作/决策/对话展示。每 2~3 章显性使用一次。

### DCQG-C009 → Planner Bible 字段
```yaml
internalized_pressure:
  source: ""          # 代价源（能力的副作用）
  manifestation: ""   # 代价如何具体体现
  escalation: ""      # 如何在剧情中渐进加深
```
规则：代价必须是能力同源产物，影响剧情选择。连续 3 章未体现需标出。

### DCQG-C012 → Planner Bible 字段 + 分卷规则
```yaml
revelation_phases:
  - phase: 1
    mystery: ""       # 本阶段核心谜面
    answer: ""        # 核心谜底
    trigger: ""       # 揭示触发条件
    deeper_mystery: "" # 揭示后更深谜面
```
规则：每卷至少 1 谜面+1 谜底，最长谜面不超过 2 卷。

### DCQG-C004 → Writer 写作约束（规则一）
开章 200 字内必须进入：冲突入口/任务入口/异常入口。
禁止：大段设定说明/纯环境描写/长篇穿越回忆。

### DCQG-C002 → Writer 写作约束（规则二）
高潮解法：先理解规则 → 找出漏洞/约束 → 在框架内逆转。
禁止连续 3 章力量碾压式解法。
每卷至少 2~3 个关键冲突使用规则破局。

### DCQG-C005 → Reviewer 双维度检查
- hook_pacing: 短钩/长钩/兑现状态/章尾拉力/overload 检查
- payoff_visibility: 兑现可见度/情绪冲击/信息说明检测

---

## 四、哪些 Pattern 未注入

| Pattern | 原因 |
|---------|------|
| DCQG-C006, C007, C008 | 不在本批 selected_patterns 中 |
| DCQG-C010, C011 | 不在本批 selected_patterns 中 |
| DCQG-C013 ~ C020 | 不在本批 selected_patterns 中 |
| DCQG-R001, R002 | 已被 curator 拒绝 |

本批为最小注入（6/20 approved patterns），第二批将覆盖剩余 patterns。

---

## 五、为什么暂缓 Polisher

1. **好稿应主要在 Planner / Writer / Reviewer 阶段成型** — 这是本批的核心原则
2. 验证结果（validation_report.md）显示：不经过 Polisher，正文已基本可读，有爽感，不需要救稿
3. 在 Planner+Writer+Reviewer 链路未稳定前，过早注入 Polisher 会导致 Polisher 承担"补漏"角色，而非"轻量增强"
4. 建议等多章验证（3~5 章）确认链路稳定后再决定 Polisher 注入时机

---

## 六、如何防止模板化

### Writer 层面
1. 规则四明确禁止"认知碾压三拍"（发现问题→心算真相→碾压解决）的机械重复
2. 提供变异方式：认知有时只提供线索、有时主角判断错误、有时用人性维度打破认知模式
3. 验收标准增加"未出现机械重复的认知碾压模板"

### Reviewer 层面
1. 新增 template_risk 维度（#14），逐章检查
2. 检查项：连续章是否同模式、所有冲突是否同解法、技法感是否强于故事感

---

## 七、如何防止原作污染

1. 本批所有 patterns 均为去原作化的抽象技法，bind 到通用叙事规则而非具体原作设定
2. 每张 approved pattern 的 Original Contamination Guard 中 forbidden_elements 均为空
3. Skill 修改中不出现《大乘期》书名、人物名、设定名、桥段名
4. 验证用 Story Bible 为全架空世界观（经络积分系统），与任何已知作品无关
5. 如果后续使用中出现疑似污染，Reviewer 的 template_risk 维度会标记

---

## 八、修改文件完整清单

### 修改的 Skill 文件
- `/home/agentuser/.hermes/skills/webnovel/webnovel_planner/SKILL.md` (105→173 行)
- `/home/agentuser/.hermes/skills/webnovel/webnovel_writer/SKILL.md` (100→168 行)
- `/home/agentuser/.hermes/skills/webnovel/webnovel_reviewer/SKILL.md` (124→210 行)

### 新增文件
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C001.md`
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C002.md`
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C004.md`
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C005.md`
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C009.md`
- `production/phase8/skill_injection_minimal/approved_patterns/DCQG-C012.md`
- `production/phase8/skill_injection_minimal/selected_patterns.yaml`
- `production/phase8/skill_injection_minimal/task_templates/step7_skill_pack_minimal_injection_task.md`
- `production/phase8/skill_injection_minimal/validation/validation_story_bible.md`
- `production/phase8/skill_injection_minimal/validation/validation_chapter_beat.yaml`
- `production/phase8/skill_injection_minimal/validation/validation_draft.md`
- `production/phase8/skill_injection_minimal/validation/validation_review.md`
- `production/phase8/skill_injection_minimal/validation/validation_report.md`

### 未修改的文件（确认）
- ❌ webnovel_polisher/SKILL.md — 未修改
- ❌ webnovel_state_manager/SKILL.md — 未修改
- ❌ webnovel_wps_sync/SKILL.md — 未修改
- ❌ detect_webnovel_ai_flavor/SKILL.md — 未修改
