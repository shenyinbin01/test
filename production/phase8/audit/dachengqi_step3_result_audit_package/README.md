# Dachengqi Step 3 Result Audit Package

## 1. 本包目的

用于审计 Phase 8 Step 3 Book Architect 的实际结果质量。让主控方基于真实产物判断后续方向。

## 2. 当前状态

- **Step 2（Chapter Card 全量压缩）：** accepted ✅（Hermes 已抽查验收）
- **Step 3（Book Architect）：** 已生成，但 **尚未 accepted** ❌——主控方初步反馈人物卡和 story bible 质量不达标
- **Step 4（craft_distiller）：** 暂停，等待 Step 3 审计结果

## 3. 目录结构

```
production/phase8/audit/dachengqi_step3_result_audit_package/
│
├── README.md                                 # 本文件
├── book_architect_execution_notes.md          # 生成逻辑说明（核心阅读材料）
├── book_architect.prompt.md                   # 使用的 LLM prompt
│
├── reverse_story_bible.md                     # Step 3 产物：故事工程分析
├── volume_structure_report.md                 # Step 3 产物：卷结构报告
├── reader_debt_lifecycle.md                   # Step 3 产物：读者债务生命周期
├── hook_payoff_map.md                         # Step 3 产物：钩子兑现映射
├── book_architect_summary.md                  # Step 3 产物：生成摘要
│
├── chapter_fact_audit_report.md               # 上游证据：章节事实审计表（974行）
├── chapter_card_quality_report.md             # 上游证据：Chapter Card 质量报告
│
├── chapter_card_samples/                      # 上游证据抽样（9章YAML）
│   ├── chapter_0001.yaml
│   ├── chapter_0014.yaml
│   ├── chapter_0100.yaml
│   ├── chapter_0250.yaml
│   ├── chapter_0388.yaml
│   ├── chapter_0541.yaml
│   ├── chapter_0681.yaml
│   ├── chapter_0745.yaml
│   └── chapter_0774.yaml
│
├── character_card_samples/                    # 人物卡抽样
│   ├── character_card_sample_index.md         # 抽样说明
│   ├── 江离.md
│   ├── 白宏图.md
│   ├── 玉隐.md
│   ├── 初帝.md
│   ├── 袁五行.md
│   └── 如意葫芦.md
│
└── tools_snapshot/                            # 生成脚本
    └── run_book_architect.py
```

## 4. 已知问题

1. **reverse_story_bible 完成度疑似不足** — 三幕划分太粗（第二幕 751 章挤在一个阶段），核心卖点/爽点模型/主线矛盾的描述泛泛而谈，缺乏具体证据支撑

2. **character_cards 质量差** — 实现方式是按人物名从聚合数据中抽取出场记录（角色名+出场次数+首末章），单独调 LLM 生成。LLM 看不到该角色在各章的具体行为、对话、状态变化。结果就是人物卡只有泛泛的性格标签，没有完整的人物弧光

3. **reader_debt_lifecycle 压缩过度** — 只看到 20 条 debt 取样+采样章节（约 80 章的摘要），LLM 无法真实判断全书的债务结构，最终只收敛到 3 条债务线

4. **hook_payoff_map 覆盖不足** — 同样基于采样（20 条 hook 取样），最终只提炼了 11 条关键 hook，无法覆盖全书 410 条记录的钩子网络

5. **low confidence = 0 不合理** — confidence 全部来自 LLM 自评，无任何校准机制。对于 774 章的全书反推，全部 high 明显不符合实际

6. **volume_structure_report 相对可用** — 8 个阶段划分、每阶段的目标/压力源/爽点/高潮的结构合理，但部分阶段边界基于机械采样的信息量有限

7. **根本问题：LLM 没看到全量数据** — 所有交付物的输入都是聚合摘要（统计+采样），不是全量 774 张 chapter_card 的原始内容。LLM 无法基于完整信息做出判断

## 5. 请求审计的问题

请主控方（沈总）判断：

1. **哪些产物可用？**
   - volume_structure_report 是否直接可用？
   - hook_payoff_map 和 reader_debt_lifecycle 是否可降级为参考？

2. **哪些产物不可用，需要重做？**
   - character_cards 是否需要基于全量 chapter_cards + 完整上下文的方案重做？
   - reverse_story_bible 是否需要基于全量数据的方案重做？

3. **重做策略：**
   - 是修复现有脚本（喂更完整的 chapter_card 数据给 LLM），还是换方案？
   - 人物卡如果改为"每张卡独立生成 + 基于全量该角色章节的 chapter_card + one_sentence + main_events"是否能解决？
   - 是否允许在 Step 3 第 2 轮中加大每个 LLM 调用的 token 预算？

4. **后续路线：**
   - 修完 Step 3 后再进 Step 4？
   - 还是 Step 3 现有产物降级为参考，Step 4 换个策略（从"故事圣经中心"改为"长篇结构+机制蒸馏中心"）？

## 6. 禁止事项

⚠️ 审计包内的所有文件均为原始产物副本，未被修改。
⚠️ 审计期间不允许进行 Step 3 内容重写、Step 4 craft_distiller、craft_assets 生成。
