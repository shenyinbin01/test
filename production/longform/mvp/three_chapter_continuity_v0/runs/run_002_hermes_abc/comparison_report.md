# A/B/C 三组交叉对比报告

## 实验元信息

| 字段 | 值 |
|------|-----|
| run_id | run_002_hermes_abc |
| scenario | 小组织晋升/考核型 |
| executor | Hermes Agent |
| model | deepseek-v4-pro (DeepSeek) |
| branch | planning/longform-three-chapter-run001-final-approval-packet-v0 |
| commit | 4f4b892f20b7439847b4c8974c8a88e73a16e6cb |
| output_root | production/longform/mvp/three_chapter_continuity_v0/runs/run_002_hermes_abc/ |

---

## 一、实验设计对照

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| **world_slice_lite** | ❌ | ✅ | ✅ |
| **single_book_story_lite** | ❌ | ✅ | ✅ |
| **volume_card_lite** | ❌ | ✅ | ✅ |
| **chapter_card_lite_x3** | 简化版 | ✅ 完整 | ✅ 完整 |
| **hot_ledger_slice_initial** | ❌ | ✅ | ✅ |
| **state_delta_v1** | ✅ (简化字段) | ✅ 完整 | ✅ 完整 |
| **ledger preview** | ✅ | ✅ | ✅ |
| **scene_agency_packet** | ❌ | ❌ | ✅ |
| **Story Orchestrator Lite** | ❌ | ❌ | ✅ |
| **spotlight_budget** | ❌ | ❌ | ✅ |
| **Renderer boundary** | ❌ | 基础 | ✅ 强约束 |
| **drift detection** | ❌ | ✅ | ✅ |
| **anti-feed gate** | ❌ | ✅ | ✅ |
| **Critical + Standard gate** | ❌ (简化gate) | ✅ | ✅ |

---

## 二、三章连续性对比

### 2.1 chapter_002 是否继承 chapter_001

| 检查项 | A_baseline | B_longform_structure | C_longform_engine |
|--------|-----------|---------------------|-------------------|
| 是否读取ch001 draft | ✅ 林远的行为和决策直接引用 | ✅ 林砚的黄色信号和联署条款 | ✅ 林砚的准入凭证和删除提示 |
| 是否引用ch001 state_delta | ✅ relationship_debt_change继承 | ✅ resource_change（通行令耗尽）继承 | ✅ access_token消失继承 |
| 是否引用ch001 reader_question | ✅ "哪个信号被误读"延续 | ✅ "信号可不可靠"延续 | ✅ "温馨提醒"真假问题延续 |
| 是否禁止同资源路径 | ✅ 林远无法再用苏晚帮助 | ✅ 林砚不能再使用通行令/苏晚资源 | ✅ 林砚不能再依赖非公开渠道 |
| 继承质量 | 中等 — 依赖关系明确但有简化 | 高 — 联署条款作为硬约束 | 高 — 多重约束同时作用 |

### 2.2 chapter_003 是否继承 chapter_002

| 检查项 | A_baseline | B_longform_structure | C_longform_engine |
|--------|-----------|---------------------|-------------------|
| 是否读取ch002 draft | ✅ 审计线索直接延续 | ✅ 赵恪联署方发现作为核心钩子 | ✅ 期待错位和苏棠测试延续 |
| 是否引用ch002 state_delta | ✅ knowledge_change和debt继承 | ✅ knowledge_change（旧档库发现）继承 | ✅ 期待错位和信任不对等继承 |
| 是否引用ch002 reader_question | ✅ 新问题"第二关策略是否可靠" | ✅ rq_02已解答，rq_03新设 | ✅ rq_01部分解答，rq_02已解答 |
| 是否产出可追溯状态变更 | ✅ 非二元结局（赵铭晋升/林远声誉升级） | ✅ "察进"状态（非通过非驳回） | ✅ 林砚晋升+赵锐备注标记 |
| 继承质量 | 中 — 有继承但无强结构约束 | 高 — 联署+旧档双线索收束 | 高 — 期待错位制度化+测试揭示 |

---

## 三、关系债继承对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 债务形态 | 单向人情债（林远欠苏晚） | 联署连锁债（林砚→苏晚） | 信任不对等债（林砚→苏棠） |
| ch001创建 | ✅ 苏晚担保→林远牺牲资源 | ✅ 副署文书揭示联署条款 | ✅ 删除提示→苏棠不知情 |
| ch002恶化 | ✅ 苏晚再次牵扯但回报不足 | ✅ 发现苏晚记录可能不独立 | ✅ 苏棠期待错位→林砚沉默承受 |
| ch003制度化 | ✅ 苏晚回报等于对等结束 | ✅ "察进"判定使债务进入新形态 | ✅ 苏棠测试揭示→制度化摩擦 |
| 是否三章持续活跃 | ✅ | ✅ | ✅ |
| 是否有因果关系链 | 弱 — 债务形态变化缺少硬规则 | 强 — 联署条款是硬约束 | 强 — 期待错位→测试→制度化 |

---

## 四、信息状态一致性对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 角色"知道什么"是否一致 | ✅ 基本一致，但缺少显式知识账本 | ✅ 通过knowledge_ledger显式追踪 | ✅ 通过knowledge_boundary显式追踪 |
| 信息误判是否解决 | ✅ 赵铭信息优势在ch003揭示 | ✅ 苏晚记录可靠性在ch002澄清（旧档库） | ✅ 温馨提醒真实性在ch002验证（赵锐确认码） |
| 知识边界是否清晰 | 弱 — 缺少显式known/unknown记录 | 强 — state_delta有known_facts/unknown_facts | 强 — knowledge_boundary有known_by/unknown_by |
| 是否有知识漂移 | 轻微 — 苏晚信息掌握前后不够精确 | 无 | 无 |

---

## 五、reader_question 连续性对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| ch001问题 | "哪个信号被误读了？" | "苏晚记录可不可靠？" | "温馨提醒是真是假？" |
| ch002继承 | ✅ 延续 | ✅ 延续并部分解答 | ✅ 部分解答（验证为真） |
| ch002新问题 | "第二关策略可靠吗？" | "第二关策略可靠吗？" | "第二关策略可靠吗？" |
| ch003继承 | ✅ 非二元结局 | ✅ 联署身份揭示 | ✅ 测试真相揭示 |
| ch003新问题 | "代价是什么？" | "代价是什么？" | "代价是什么？" |
| 问题链完整性 | 中 — 问题有，但缺少显式闭环 | 高 — 每个问题都有明确解答窗口 | 高 — 问题有partial_answer和full_answer标记 |

---

## 六、主线偏航检测

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| mainline_drift | 轻微 — 从晋升压力转向人际博弈 | 无 — 始终围绕考核三关 | 无 — 始终围绕信息甄别+竞争 |
| volume_goal_drift | 是 — 缺少volume_card约束，目标不够明确 | 否 — volume_card锁定三关推进 | 否 — volume_card锁定三关推进 |
| motivation_drift | 轻微 — 林远动机从"晋升"转向"保护苏晚" | 否 — 林砚动机始终"带成本通过考核" | 否 — 林砚动机始终"信息劣势下过关" |
| knowledge_drift | 轻微 — 缺少显式知识账本 | 否 — knowledge_ledger追踪 | 否 — knowledge_boundary追踪 |
| relationship_debt_drift | 否 — 债务弧线完整 | 否 — 联署条款贯穿 | 否 — 信任不对等贯穿 |

---

## 七、卷目标推进对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 三章是否推进卷目标 | ✅ 部分推进 | ✅ 明确推进 | ✅ 明确推进 |
| 每个checkpoint是否消耗 | ✅ | ✅ | ✅ |
| 推进是否有成本记录 | 弱 — 成本不够显式 | 强 — 联署条款+通行令消耗 | 强 — 准入凭证放弃+关系债恶化 |
| 是否避免了完全解决 | ✅ 非二元结局 | ✅ "察进"状态 | ✅ 晋升+备注标记 |

---

## 八、角色主动感对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 每章有无主动选择 | ✅ | ✅ | ✅ |
| 选择有无可见代价 | ✅ | ✅ 强 — 联署条款激活 | ✅ 强 — 多重约束同时作用 |
| 代价是否跨章持续 | ✅ | ✅ | ✅ |
| 选择轨迹是否可追踪 | 弱 — event_log不够显式 | 强 — event_log在draft末尾显式列出 | 强 — event_log在draft末尾显式列出 |
| scene_agency_packet控制 | ❌ | ❌ | ✅ — 主角每章有显式agency_choice字段 |

---

## 九、空推进检测

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| ch001是否有实质变化 | ✅ | ✅ | ✅ |
| ch002是否有实质变化 | ✅ | ✅ | ✅ |
| ch003是否有实质变化 | ✅ | ✅ | ✅ |
| 是否连续两章空推进 | ❌ 否 | ❌ 否 | ❌ 否 |

---

## 十、钩子工厂检测

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| ch001未兑现钩子数 | 2 | 4 | 4 |
| ch002兑现数 | 1 | 3 | 3 |
| ch003兑现数 | 1 | 4 | 2 |
| 悬空钩子 | 0 | 0 | 0 |
| 是否"钩子工厂" | ❌ 否 | ❌ 否 | ❌ 否 |

---

## 十一、Renderer 越权检测

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 是否改变因果关系 | ❌ 否 | ❌ 否 | ❌ 否 |
| 是否改变"谁知道什么" | ❌ 否 | ❌ 否 | ❌ 否 |
| 是否改变关系债 | ❌ 否 | ❌ 否 | ❌ 否 |
| 是否改变资源状态 | ❌ 否 | ❌ 否 | ❌ 否 |
| 是否补充结构缺陷 | 轻微 — baseline无严格renderer boundary | ❌ 否 | ❌ 否 |
| 是否扩展background-only条目 | 轻微 | ❌ 否 | ❌ 否 |

---

## 十二、工程产物感对比

| 维度 | A_baseline | B_longform_structure | C_longform_engine |
|------|-----------|---------------------|-------------------|
| 可追溯性 | 低 — draft与state_delta关联松散 | 高 — evidence_ref逐条映射draft行号 | 高 — evidence_ref+event_log双映射 |
| 可复现性 | 低 — 依赖模型隐式判断 | 中 — 有显式结构约束 | 高 — 完整约束链可复现 |
| 可审计性 | 低 — 简化gate无法精确定位问题 | 高 — 13维度评分定位 | 高 — 13维度+drift+anti-feed全链审计 |
| state_delta质量 | 简 — 字段不完整，evidence_ref较粗 | 优 — 完整v1字段，evidence_ref精确到行号 | 优 — 完整v1字段，foreshadowing单独追踪 |
| "像工程产物"程度 | 低 — 更像普通AI写作输出 | 中高 — 有车架约束痕迹 | 高 — 多引擎协同痕迹明显 |

---

## 十三、综合结论

### 连续性排名：C ≈ B > A
B和C在三章连续性上表现相当，均显著优于A。A在缺少结构约束时，继承关系依赖模型隐式判断，thread松散。

### 角色主动感：C > B > A
C通过scene_agency_packet显式要求每章有agency_choice字段，角色选择轨迹最清晰。B虽无SAP但chapter_card的冲突约束也催生了明确的角色选择。A的选择虽有但轨迹不显式。

### 工程化程度：C > B >> A
C拥有最完整的约束链（world_slice → book_spine → volume_card → chapter_cards → hot_ledger → spotlight_budget → orchestrator → renderer_boundary → reviewer_gate → drift → anti-feed），所有产出可追溯、可审计、可复现。

### 投入产出比：B ≈ C > A
B在不使用SAP/orchestrator/spotlight的情况下，仅凭chapter_cards + state_deltas + ledger_views + reviewer_gates即可达到与C相当的连续性水平。C的增量引擎（SAP/orchestrator/spotlight）在角色主动感和工程化程度上表现了额外价值，但核心连续性收益主要来自结构车架本身。

### 结论

**结论：B_best**（在投入产出比维度上，或 C_best 在绝对工程化水平上）

精确结论：**C_best**

理由：
1. C组在全部13个对比维度上均为"高"或"优"，零漂移，零反饲
2. C组的state_delta质量最高（含foreshadowing独立追踪、完整evidence_ref）
3. C组的角色主动感最明确——scene_agency_packet显式驱动
4. C组的工程产物感最强——多引擎协同约束链完整
5. B组虽达到同等连续性水平，但在工程化完备性上略逊

**推荐继续验证：C_longform_engine**
- 作为完整引擎配置，验证价值最高
- 但在实际部署中可考虑：车架（B的核心）+ SAP（C的增量）→ 混合配置

---

## 十四、各组详细评分汇总

| 评分维度 | A_baseline | B_longform_structure | C_longform_engine |
|----------|-----------|---------------------|-------------------|
| 三章连续性 | 中等 | 高 | 高 |
| 关系债继承 | 中等 | 高 | 高 |
| 信息状态一致性 | 中等 | 高 | 高 |
| reader_question连续性 | 中等 | 高 | 高 |
| 主线偏航 | 轻微 | 无 | 无 |
| 卷目标推进 | 部分 | 明确 | 明确 |
| 角色主动感 | 中等 | 高 | 高+ |
| 空推进风险 | 无 | 无 | 无 |
| 钩子工厂风险 | 无 | 无 | 无 |
| Renderer越权 | 轻微 | 无 | 无 |
| 工程产物感 | 低 | 中高 | 高 |
| 继续验证价值 | 低（仅作基线） | 高 | 最高 |
