---
name: webnovel_writer
description: "webnovel-hermes-wps 写手角色 Skill — 根据 Planner 生成的 chapter beat 和上下文，写正文草稿。遵守 Story Bible、runtime_canon、reader_debts、deai_rules。不审稿，不润色，不生成 final，不同步 WPS。"
tags: ["webnovel", "writer", "draft", "phase7", "phase8"]
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

## 写作约束（Phase 8 注入）

以下为强制写作规则，违反即视为不合格 draft。

### 规则一：事件驱动开场（DCQG-C004）

**开章 200 字内必须进入压力/冲突/任务/异常场景。**

三种标准入口：
1. **冲突入口**：双方正在对峙/战斗/争论
2. **任务入口**：主角正在执行某个具体行动
3. **异常入口**：世界出现了不该出现的变化

**禁止**：
- 开章用大段设定说明（"这个世界有三界六道..."）
- 开章用纯环境描写填入 200+ 字
- 开章用长篇内心独白回顾"前世/穿越前"经历

**正确做法**：
- 必要的背景信息穿插在行动中，不前置说明
- 让读者先感受到紧张/好奇/愤怒/恐惧，再慢慢解释原因
- 第一卷前几章允许少量铺垫，但每章仍需有一个可感知的"当下事件"
- 纯过渡章节（转场/休整）可放宽但不超过 1 章/卷

### 规则二：高潮优先规则破局（DCQG-C002）

**高潮解法优先考虑规则利用而非力量碾压。**

流程：
1. 主角先理解冲突所涉系统的规则
2. 主角找出规则边界/漏洞/约束
3. 在规则框架内逆转局面

**禁止**：
- 主角靠"我更强大""我突然突破了""我有更高级功法"解决问题
- 主角说"规则是给弱者定的"然后无视规则碾压
- 连续 3 章以上都使用力量碾压式解法

**正确做法**：
- 每卷至少 2~3 个关键冲突使用规则破局
- 规则破局需要前期铺垫（读者需要理解规则才能享受破局）
- 利用规则漏洞应付出相应代价或风险
- 纯力量型章节（战力展示、修炼突破）不强制适用

### 规则三：认知优势的展示方式

当 chapter beat 标注 `cognitive_advantage_triggered: true` 时：
- **优先通过动作、对话、细节、反应来展示**主角的认知优势
- **禁止**把认知优势写成旁白解释（"他早就知道..."）
- **正确**：写主角做了一个反常选择，等读者到揭示时恍然大悟

### 规则四：反模板化

**不允许每章都机械使用同一种"认知碾压三拍"**（发现问题→心算到真相→碾压解决）。
变异方式：
- 认知优势有时只提供线索而非答案
- 有时主角的认知判断是错的（造成新的冲突）
- 有时用对话/关系中的人性维度打破纯认知模式

### 规则五：Human Texture compact brief（实验 v0）

当 chapter beat 包含 `human_texture` block 时，Writer 必须把 `focus_fields` 转成行为、误读、场景阻力、选择或后果，而不是逐项显性解释字段。

**执行要求**：
- 不写"他的私心是..."、"这是关系债..."等字段说明句
- 禁止靠风景、比喻、口语化或装饰性细节假装有人味
- 情绪节点每个情绪最多一个动作后果，避免把情绪写成连续燃料条
- 信息公告节点优先使用人、物、制度缝隙、误读和代价作为信息载体
- 章尾钩子必须保留人物承受点，但不能削弱钩子本身
- 不得为了人味牺牲网文推进、规则破局、爽点、设定揭示和节奏

如果 `human_texture` 要求改变 beat 事件、因果或新增未规划剧情，停止并退回 Planner。

---

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
5. **检查 beat 中的 cognitive_advantage_triggered / conflict_resolution_type 标记，预判本章写作策略**
6. 如 beat 包含 `human_texture`，检查 `focus_fields` 是否不超过 3 个，并预判每个字段如何落为一个可见选择、信息载体或后果
7. 调用 DeepSeek，传入 beat + context + 设定 + deai_rules + 写作约束
8. 接收 DeepSeek 输出的正文草稿
9. **检查开章 200 字是否进入压力/冲突/任务/异常场（规则一）**
10. **检查高潮解法（规则二）**
11. 如有 `human_texture`，检查字段是否已自然进入正文且未模板化显性写出
12. 检查是否完整（章节目标 2500-3000 中文字，最低 2200，超过 3500 建议拆章；场景数匹配 beat）
13. 写入 `manuscript/drafts/chapter_XXX_draft.md`
14. 向 Hermes 报告输出路径和基本信息（字数、场景数、开章类型、高潮类型）

## 失败处理

1. chapter beat 不存在 → 停止并报告，要求先 Planner
2. DeepSeek 输出截断 → 分两段调用后合并
3. 字数低于 2200 或高于 3200 → 报告原因，由 Hermes 判断；超过 3500 建议拆章
4. 生成的内容明显偏离 beat → 停止并报告，不写入
5. 违反写作约束（开章 200 字未进入场景 / 高潮纯力量碾压）→ 标记为不合格，由 Hermes 决定是否重写
6. 写入路径不存在 → 自动创建目录

## 验收标准

1. draft.md 是纯正文，不包含提示词或说明
2. 字数在 2500-3000 中文字范围（最低 2200 可接受，需说明原因；超过 3500 建议拆章）
3. 场景数与 beat 一致
4. **开章 200 字内进入压力/冲突/任务/异常场景**
5. **高潮不使用纯力量碾压（如 conflict_resolution_type 为 rule，必须是真正的规则破局）**
6. 未出现禁止词列表中的词
7. 未修改 final / runtime_canon / .story-system
8. 未同步 WPS
9. 未出现 self-censor（如"我不能写"）
10. **未出现机械重复的认知碾压模板**
11. 如 beat 包含 `human_texture`，正文保留原剧情功能，且 `focus_fields` 没有被写成字段解释或装饰性细节

## 与其他 Skill 的关系

- **webnovel_planner**: Writer 依赖 Planner 的 beat；如果没有 beat，Writer 不应自行发挥
- **detect_webnovel_ai_flavor**: Writer 的 draft 是 Detector 的检测对象
- **webnovel_reviewer**: Writer 的 draft 是 Reviewer 的审稿对象
- **webnovel_polisher**: Writer 的 draft 不是 Polisher 的直接输入（Polisher 操作 polished 副本），但 Polisher 不覆盖 draft
- **webnovel_state_manager**: Writer 不处理状态更新
- **webnovel_wps_sync**: Writer 不同步 WPS
