# Phase 8 — Lessons Learned

## 踩过的坑与最终规则

### 1. 不能用采样冒充全书反推
**旧 Step 3 的致命问题**: 774 章中只喂给 LLM 约 80 章采样 + 统计聚合数据。
- LLM 看到的是"角色名+出场次数+首末章"，看不到角色在各章的具体行为
- Story Bible 只有三幕概括（第二幕 751 章挤在一起）
- 人物卡只有泛泛的性格标签

**最终规则**: Step 3B 按阶段分批，每阶段喂全量 chapter_card 数据。不采样。

---

### 2. Story Bible 不能从局部章节硬猜
**问题**: 用统计+采样拼凑出来的 Story Bible 是"统计的影子"而非"故事的结构"。

**最终规则**: 先程序聚合生成 full_chapter_spine，再按阶段让 LLM 分析 arc_mechanism，最后跨阶段汇总。三层逐级递进。

---

### 3. 人物卡不能只按出场章节拼接
**问题**: 旧版人物卡给 LLM 的输入只有"角色名 + 出场次数 + 首末章"，LLM 只能输出泛泛的性格标签。

**最终规则**: character_function_map 按**功能位**组织（推动剧情者/障碍者/信息源/情感锚点），不是人物传记。功能位 > 性格标签。

---

### 4. 先做机制定位，再做技法蒸馏
**问题**: 如果直接从章节跳技法，会产出碎片化的"技巧列表"而非系统性的"技法资产"。

**最终规则**: Step 3B 机制定位 → Step 4 技法蒸馏。arc_mechanism_index 是 craft_distiller 的必要输入。

---

### 5. candidate_pool 不是 approved_patterns
**问题**: Step 3B 产出的 candidate_pool（22条）被误认为是可直接使用的技法。

**最终规则**: candidate_pool → Craft Distiller 蒸馏 → draft patterns → Curator 审核 → approved_patterns。四个阶段缺一不可。

---

### 6. draft patterns 必须经过 curator
**问题**: draft 技法卡中存在: contamination_risk 枚举值错误（`medium`→应为`low`）、forbidden_original_elements 含原作专属词、status 字段仍为 `draft`。跳过 curator 直接注入会引入污染。

**最终规则**: Step 5 Curator 必做步骤包括:
1. contamination_risk 枚举值校准
2. forbidden_original_elements 去原作化
3. status 字段 `draft`→`approved` 更新（极易遗漏）
4. grep 校验 `status=draft`=0 / `status=approved`=20

---

### 7. Skill Pack 注入不能全量塞 20 张卡
**问题**: 如果把 20 张技法卡全文复制进 Skill，Skill 会变成"技法大全"而非"角色操作手册"。

**最终规则**: 第一批只注入 6 张（最小注入）。每张技法卡转化为对应 Skill 的**可执行字段/规则/检查项**，不复制原文。

---

### 8. Planner / Writer / Reviewer 是主链路，Polisher 不是救稿角色
**问题**: 旧链路中 Polisher 承担了隐性的"审美修正"和"结构性救稿"。

**最终规则**: 五章验证确认 Planner→Writer→Reviewer 可独立产出合格章节。Polisher 定位升级为"轻量增强"，明确禁止补结构/爽点/钩子/动机。缺失 → 退回 Reviewer/Writer。

---

### 9. Polisher 必须有门控
**问题**: 没有门控的 Polisher 会对所有章节做同质化增强，导致高质量章节被过度润色。

**最终规则**: 四条 Phase 8 增强规则各有门控:
- `overall_score ≥ 8.0` → 全部规则跳过
- `template_risk ≥ 8` → 认知对比跳过
- `character_voice ≥ 7` → 对话增强跳过（非关键冲突）
- `cool_point ≥ 8` → 规则链跳过
- `ending_hook ≥ 8` → 章尾余味跳过
- 字数约束: ±10%

---

### 10. 多书技法库必须分层
**问题**: 如果每拆一本书就直接修改 Skill Pack，Skill Pack 会无限膨胀且技法间缺乏层次。

**最终规则**: 建立五层技法库:
- **book_patterns**: 绑定具体作品的技法（可能跨书验证后升级）
- **genre_patterns**: 经 2+ 本书验证的类型通用技法
- **universal_patterns**: 经 3+ 本书/跨类型验证的普适技法
- **style_profiles**: 特定风格/语调/节奏配置
- **project_patterns**: 当前创作项目的专用技法集

拆书 → 入库 → 跨书验证 → 决定是否注入 Skill Pack。不直接注入。
