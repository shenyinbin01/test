# Dachengqi Draft Craft Assets — README

## 概述

本目录包含 Phase 8 Step 4（Craft Distiller）的产出：基于《大乘期才有逆袭系统》的 Step 3B 清洗后的 22 条机制候选池，蒸馏生成的 **20 张 draft 技法卡** 和 **2 条 rejected patterns**。

## 目录结构

```
dachengqi_draft/
├── README.md                    ← 本文件
├── manifest.yaml                ← 产物清单（含统计和文件列表）
├── craft_distiller_report.md    ← 蒸馏过程报告
├── craft_distiller_report.json  ← 蒸馏过程报告（JSON）
├── protagonist_engine_patterns/ ← 4 张主角引擎类技法
├── arc_structure_patterns/      ← 3 张弧线结构类技法
├── reader_pull_patterns/        ← 3 张读者拉力类技法
├── payoff_patterns/             ← 3 张兑现模式类技法
├── character_function_patterns/ ← 2 张角色功能类技法
├── conflict_generator_patterns/ ← 3 张冲突生成类技法
├── pacing_patterns/             ← 1 张节奏控制类技法
├── comedy_contrast_patterns/    ← 1 张喜剧调剂类技法
└── rejected_patterns/           ← 2 条 rejected patterns
```

## 统计

| 指标 | 值 |
|------|-----|
| 候选总数 | 22 |
| Keep（直接蒸馏） | 12 |
| Revise（去原作化后蒸馏） | 8 |
| Reject（不蒸馏） | 2 |
| Draft 技法卡生成 | 20 |
| Approved 技法卡 | 0（待 Step 5 审批） |
| 分类数 | 8 |
| Rejected patterns | 2 |

## 各分类详情

| 分类 | 数量 | 包含 |
|------|------|------|
| protagonist_engine | 4 | C001 认知碾压, C006 伪装身份, C009 压力源内化, C011 多重介入身份 |
| arc_structure | 3 | C010 冲突螺旋升级, C012 世界观揭秘驱动, C017 多线并行织网 |
| reader_pull | 3 | C004 外部任务触发器, C008 历史沉浸揭秘, C014 降维打击引入 |
| payoff | 3 | C005 短钩快兑长钩慢兑, C020 代价与取舍, C022 初心回归 |
| character_function | 2 | C003 镜像反派, C007 导师型主角 |
| conflict_generator | 3 | C002 规则解构破局, C015 理念冲突, C021 规则漏洞利用 |
| pacing | 1 | C013 情感锚点 |
| comedy_contrast | 1 | C018 喜剧调剂 |
| rejected | 2 | C016 终局清算, C019 非典型成长 |

## 每张技法卡的结构

每张 draft 技法卡包含 9 个标准节：
1. Metadata（pattern_id, name, source_candidate_id, status=draft, suggested_target_skill, applicable_genres, confidence, contamination_risk）
2. Solves Writing Problem
3. Mechanism（抽象机制 + 可执行步骤）
4. How To Use（Planner/Writer/Reviewer/Polisher 各角色使用指南）
5. Positive Abstract Example（完全去原作化的正例）
6. Negative Example（错误使用方式）
7. Boundary（适用/不适用边界）
8. Original Contamination Guard（forbidden_original_elements, contamination_notes, de_originalization_method）
9. Evidence Source（source_arc, source_chapters, source_files, supporting_mechanism, evidence_confidence）

## 去原作化确认

所有 20 张技法卡已完成去原作化检查：
- 不包含原作的任何专属设定词（如"人皇""九州""域外天魔""天道""大乘期""系统""逆袭系统"等）
- Revise 卡（8张）在 curator 的去原作化规则基础上进行了深度蒸馏
- 正例全部使用完全虚构的通用设定

## 下一步

Step 5：Hermes 审批 → approved patterns → 注入 Skill Pack
