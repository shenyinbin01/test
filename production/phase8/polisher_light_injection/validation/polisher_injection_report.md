# Phase 8 Step 7 第二批: Polisher 轻量注入报告

## 概述
- 日期: 2026-06-02
- 模式: polisher_light_injection
- 目标 Skill: webnovel_polisher (唯一修改目标)
- 不修改: webnovel_planner, webnovel_writer, webnovel_reviewer, webnovel_state_manager, webnovel_wps_sync, detect_webnovel_ai_flavor

## 注入规则 (4条)

### 规则一: 认知对比锐化 (DCQG-C001)
- 类型: 表达增强
- 触发条件: 原文已有"主角洞察 vs 他人误判"场景 + Reviewer `cognitive_advantage_triggered: true`
- 允许: 压实对比描写、增加误判者的行为细节、增强验证瞬间的冲击力
- 禁止: 新增认知碾压、在无对比处硬造对比、旁白解释
- 跳过条件: Reviewer `template_risk ≥ 8`

### 规则二: 价值观/理念冲突对话增强 (DCQG-C015)
- 类型: 对话增强
- 触发条件: 原文已有关键对话 + 立场差异场景
- 允许: "表明立场"→"透露立场"、增加非语言对抗细节、压缩"A说B说"结构
- 禁止: 新增长篇独白、人物变成观点接口、强行塞入价值观冲突
- 跳过条件: Reviewer `character_voice ≥ 7` 且非关键冲突场景

### 规则三: 规则利用清晰化 (DCQG-C021)
- 类型: 行动链增强
- 触发条件: Reviewer `conflict_resolution_type = rule`
- 允许: 强化"观察→试探→确认→反制"链条可见度、增加对手微反应
- 禁止: 改变原有破局逻辑、新增设定/规则解释、在非 rule 章节制造规则破局
- 跳过条件: Reviewer `cool_point ≥ 8`

### 规则四: 章尾余味/回环增强 (DCQG-C022)
- 类型: 章尾增强
- 触发条件: 原文已有回环基础（章尾与开章/主线/情绪钩子有呼应）
- 允许: 意象隐性呼应（同一物件/光线/声音变化后再次出现）、"总结式"改"留白式"、增加感官细节
- 禁止: 强行煽情、模板化"初心回归"、叠床架屋、新增钩子
- 跳过条件: Reviewer `ending_hook ≥ 8` 且已有明显意象呼应

## 核心约束
1. **定位变更**: Polisher 是轻量增强角色，不是救稿角色
2. **不硬补**: 结构/爽点/钩子/主角动机缺失→退回 Reviewer/Writer
3. **不修改**: 原 beat、原事件、原因果链
4. **字数控制**: ±10% 以内
5. **评分门控**: `overall_score ≥ 8.0` → 全部 Phase 8 规则跳过
6. **模板化门控**: `template_risk ≥ 8` → 全部跳过

## 修改范围
- 唯一修改文件: `skill-pack/webnovel_polisher/SKILL.md` (125→~250行)
- 新增: "Phase 8 轻量增强规则"整节（4条规则+优先级/互斥+判断标准+跳过条件）
- 新增禁止行为: 2条（#16 不补结构/#17 不改变beat/事件/因果链）
- 新增执行步骤: 2步（#8 审查template_risk门控/#9 根据评分选用规则）
- 新增质量标准: 1条（不新增结构/爽点/钩子/动机）
- 新增验收标准: 2条（结构与原文一致/字数±10%）
- tags 增加: "phase8"

## 未修改确认
- ❌ webnovel_planner/SKILL.md — 未修改
- ❌ webnovel_writer/SKILL.md — 未修改
- ❌ webnovel_reviewer/SKILL.md — 未修改
- ❌ webnovel_state_manager/SKILL.md — 未修改
- ❌ webnovel_wps_sync/SKILL.md — 未修改
- ❌ detect_webnovel_ai_flavor/SKILL.md — 未修改
