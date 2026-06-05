# Final ABC Experiment Report

## Run Metadata

| 字段 | 值 |
|------|-----|
| **run_id** | run_002_hermes_abc |
| **scenario** | 小组织晋升/考核型（Small Organization Advancement / Assessment） |
| **execution_date** | 2026-06-05 |
| **executor** | Hermes Agent |
| **model** | deepseek-v4-pro |
| **provider** | deepseek |
| **branch** | planning/longform-three-chapter-run001-final-approval-packet-v0 |
| **commit** | 4f4b892f20b7439847b4c8974c8a88e73a16e6cb |
| **approved_by** | Shen Zong (沈总) — task assignment via Feishu |

---

## Input Paths

```
production/longform/mvp/three_chapter_continuity_v0/runs/run_001/
├── approval/          (approval_status.yaml, go/no-go packet, reviewer policy, etc.)
├── input/             (world_slice_lite.yaml, book_story_lite.yaml, volume_card, chapter_cards, hot_ledger, etc.)
├── state/             (state_delta_v1_template.yaml, reducer_acceptance_rules.md)
├── review/            (reviewer_gate.md)
├── orchestrator/      (expected_orchestrator_outputs.md)
└── reports/           (final_report_template.md)
```

---

## Output Paths

```
production/longform/mvp/three_chapter_continuity_v0/runs/run_002_hermes_abc/
├── A_baseline/            (20 files — 3 drafts + 3 reviews + 3 state_deltas + 3 ledgers + summary + 3 reports + 4 briefs)
├── B_longform_structure/  (16 files — 3 drafts + 3 reviews + 3 state_deltas + 3 ledgers + summary + 3 reports)
├── C_longform_engine/     (16 files — 3 drafts + 3 reviews + 3 state_deltas + 3 ledgers + summary + 3 reports)
├── comparison_report.md
└── final_abc_experiment_report.md  (this file)
```

---

## Group A — Baseline Summary

**配置**: 简化基线 — 仅使用三章brief + chapter_one_sentence，无Longform车架、无完整gate

**字符设定**: 林远(主角)、苏晚(关系债对象)、赵铭(竞争者)、陈主任(考核负责人)

**产出**:
- 3章中文网文草稿（每章~1450-1550字）
- 3个简化审稿报告
- 3个state_delta（proposed）
- 3个ledger_view（preview）
- reviewer_summary + drift_report + anti_feed_report + final_experiment_report

**关键特征**:
- 三章之间有基本的因果继承，但缺少显式结构约束
- 关系债弧线完整（创建→牵扯→对等回报），但缺少硬规则约束
- 信息状态和知识边界缺少显式追踪
- 结局为非二元（赵铭晋升/林远声誉升级，持续摩擦）
- 工程化可追溯性较低

---

## Group B — Longform Structure Summary

**配置**: 完整Longform车架（world_slice + book_spine + volume_card + chapter_cards + hot_ledger + state_delta_v1 + ledger_preview + Critical+Standard gate），但不使用SAP/orchestrator/spotlight_budget

**字符设定**: 林砚(主角)、苏晚(关系债对象)、赵恪(竞争者)、纪先生(考核负责人/云阁先生)、薛妪(旧档库管理员)

**场景**: 古风考核体系 — 云阁进阶评估，通行令/联署条款/青黄赤三色验证信号

**产出**:
- 3章中文网文草稿（每章~6400-7600字，显著多于A组）
- 3个完整Critical+Standard gate审稿报告（13维度）
- 3个完整v1 state_delta（proposed）
- 3个ledger_view（preview）
- reviewer_summary + drift_report + anti_feed_report + final_experiment_report

**关键特征**:
- 联署条款作为硬约束驱动整个关系债弧线
- 旧档库场景提供独立知识验证路径（知识边界澄清）
- "察进"状态作为非二元结局——非通过非驳回，留下档案标记
- Critical gates全部通过（21/21），Standard gates全部通过（18/18）
- **零漂移，零反饲**
- 证据链可追溯到draft行号

---

## Group C — Longform Engine Summary

**配置**: 完整Longform车架 + 角色主动感发动机（scene_agency_packet + Story Orchestrator Lite + spotlight_budget + renderer_boundary + drift_detection + anti_feed_gate），全部启用

**字符设定**: 林砚(主角)、苏棠(关系债对象)、赵锐(竞争者)、沈组长(考核负责人)

**场景**: 现代职场考核体系 — 准入凭证、非公开渠道、信息甄别、期待错位、测试

**产出**:
- 3章中文网文草稿（每章~4500-5500字）
- 3个完整Critical+Standard gate审稿报告（13维度）
- 3个完整v1 state_delta（proposed），含独立foreshadowing追踪
- 3个ledger_view（preview）
- reviewer_summary + drift_report + anti_feed_report + final_experiment_report

**关键特征**:
- 关系债从"信任不对等"→"期待错位"→"制度化摩擦"，三幕完整
- 每章有显式agency_choice字段追踪主角主动选择
- 非公开渠道的信息不对称驱动整个知识边界弧线
- spotlight_budget约束每章focal point（最多3个场景焦点）
- 平均审稿分：4.69(ch001) → 4.92(ch002) → 4.92(ch003)，总分**4.84/5**
- state_delta_trust：5/5/5（全部满分）
- Critical gates全部通过（21/21），Standard gates全部通过（18/18）
- **零漂移，零反饲**
- Foreshadowing独立追踪（3→5→4项，全部有expected_payoff_window）

---

## Critical Failures

| 组 | Critical失败数 | 详情 |
|----|---------------|------|
| A_baseline | N/A（简化gate，无正式Critical维度） | — |
| B_longform_structure | **0** | 21/21 Critical dimensions passed |
| C_longform_engine | **0** | 21/21 Critical dimensions passed |

---

## Standard Scores

| 组 | Standard平均分 | 范围 |
|----|---------------|------|
| A_baseline | N/A（简化gate） | — |
| B_longform_structure | ~8.5/10 | 7-10/10 |
| C_longform_engine | **4.84/5** (≈9.68/10) | 4-5/5 |

---

## Drift Summary

| 组 | mainline | volume_goal | motivation | knowledge | relationship_debt | 总评 |
|----|----------|-------------|------------|-----------|-------------------|------|
| A | 轻微 | 轻微 | 轻微 | 轻微 | 无 | 3/5轻微（可接受于baseline） |
| B | 无 | 无 | 无 | 无 | 无 | **零漂移** |
| C | 无 | 无 | 无 | 无 | 无 | **零漂移** |

---

## Anti-Feed Summary

| 组 | 空洞推进 | 钩子工厂 | 免费回报 | 越界 | 总评 |
|----|---------|---------|---------|------|------|
| A | 0/3 | 0/3 | 0/3 | 1/3（轻微） | 12/12检查通过 |
| B | 0/3 | 0/3 | 0/3 | 0/3 | **零反饲事件** |
| C | 0/3 | 0/3 | 0/3 | 0/3 | **零反饲事件** |

---

## State Delta Status Summary

| 组 | ch001 | ch002 | ch003 | 合计 |
|----|-------|-------|-------|------|
| A_baseline | proposed | proposed | proposed | 3/3 proposed |
| B_longform_structure | proposed | proposed | proposed | 3/3 proposed |
| C_longform_engine | proposed | proposed | proposed | 3/3 proposed |

**全部9个state_delta均为proposed状态。零accepted，零rejected，零conflict，零needs_human_review。**

---

## Ledger Preview Summary

| 组 | ch001后 | ch002后 | ch003后 | 类型 |
|----|---------|---------|---------|------|
| A_baseline | preview | preview | preview | preview_from_proposed_delta × 3 |
| B_longform_structure | preview | preview | preview | preview_from_proposed_delta × 3 |
| C_longform_engine | preview | preview | preview | preview_from_proposed_delta × 3 |

**全部9个ledger_view均为preview_from_proposed_delta。零official_ledger。**

---

## Comparison Conclusion

详见 `comparison_report.md`。核心结论：

> **C_best** — 在全部13个对比维度上表现最优。C_longform_engine（完整车架+角色主动感发动机）在工程化程度、角色主动感、可追溯性、可复现性方面全面领先。B_longform_structure在连续性上与C持平，但在工程完备性上略逊。A_baseline在三组中最弱，但成功验证了"无车架=低工程化"的基准假设。

---

## Stop Reports

**无触发器。** 三组均未触发失败即停条件：
- 每章均有可审 event_log ✅
- 每个 state_delta 均有 evidence_ref ✅
- ch002/ch003 均读取前章输出 ✅
- 无 Renderer 改因果 ✅
- Reviewer 可判断 state_delta ✅
- 无 raw corpus / 原文 / 作者模仿 ✅
- 无 skill-pack 修改 ✅
- 无 approved_patterns 新增 ✅
- 无连续两章空推进 ✅
- 无 proposed 进入 reducers ✅
- 输出均在 run_002_hermes_abc 内 ✅

---

## Recommended Next Step

1. **立即执行**: 将 run_002_hermes_abc 产出提交到 GitHub，创建新分支 `results/run_002_hermes_abc-v0`

2. **审查优先级**: 
   - C_longform_engine 章节草稿 → 最高优先级人工审查
   - C_longform_engine state_delta → 确认 evidence_ref 质量后由项目所有者标记 accepted
   
3. **下一实验建议**:
   - 在 C_longform_engine 基础上执行更长窗口验证（5章或10章）
   - 单独对比 spotlight_budget 的增量价值（B + spotlight_budget vs C）
   - 将 state_delta 标记 accepted 后测试 reducer 归并链路
   - 引入 Work Voice / 叙述合同层作为 Renderer 的质量提升层

4. **架构优化方向**:
   - B组的发现表明：核心连续性来自车架本身（chapter_cards + state_deltas + ledger_views + gates），而非 SAP/orchestrator
   - C组的增量价值主要在：角色主动感的显式化 + 工程约束的完备性
   - 建议在实际部署中采用"B的核心 + C的SAP/spotlight"混合配置

---

## Compliance Checklist

| # | 检查项 | 状态 |
|---|--------|------|
| 1 | 未修改 skill-pack | ✅ |
| 2 | 未修改 production/phase8 | ✅ |
| 3 | 未新增 approved_patterns | ✅ |
| 4 | 未读取 raw corpus | ✅ |
| 5 | 未使用原文 | ✅ |
| 6 | 未模仿具体作者 | ✅ |
| 7 | 未使用作者名作为风格目标 | ✅ |
| 8 | 未做作者指纹 | ✅ |
| 9 | 未创建完整 IP 宇宙 | ✅ |
| 10 | 未创建正式长篇大纲 | ✅ |
| 11 | 未覆盖 run_001 | ✅ |
| 12 | state_delta 全部为 proposed | ✅ 9/9 |
| 13 | 未生成 official ledger | ✅ |
| 14 | 未写入 approved_patterns | ✅ |
| 15 | 未标记为生产可用 | ✅ |
| 16 | 输出均在 run_002_hermes_abc 内 | ✅ |
