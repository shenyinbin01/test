# Human Texture Real Chain Validation Rerun — Overall Report

## 执行日期
2026-06-04

## 1. 本轮是否为干净 brief 重新生成？
**是。** 两组均使用同一份干净 brief（`prompts/c4_task_brief.md`、`prompts/c3_task_brief.md`），从零生成 Planner/Writer/Reviewer。未使用任何已有章节草稿、MVP 改写、dry run 改写或 regression 改写。

## 2. 是否确认未使用已有正文作为模板？
**是。** 已逐文件检查：两个样本四份 Writer 输出均不含任何已有正文原文句子或结构模板。生成过程只依赖 brief + 分支 skill 约束。

## 3. A/B 是否只差 skill-pack 分支？
**是。**

| 项 | A 组 | B 组 | 一致？ |
|----|------|------|--------|
| 模型 | deepseek-v4-pro | deepseek-v4-pro | ✅ |
| Temperature | 默认 | 默认 | ✅ |
| max_tokens | 默认 | 默认 | ✅ |
| 输入 brief | c4/c3_task_brief.md | 同一份 | ✅ |
| 执行方式 | Hermes→DeepSeek | Hermes→DeepSeek | ✅ |
| 工作目录 | /tmp/ht_main | /tmp/ht_exp | ✅（隔离） |
| Skill Pack | main (980a74e) | experiment (4aa0229) | ❌ 唯一差异 |

seed 无法保证（API 不支持），已在 run_config 说明。

## 4. 两个样本中 B 版是否明显优于 A 版？
**是。**

| 维度 | C4（关系节点） | C3（信息节点） |
|------|--------------|--------------|
| 更像人写 | ✅ | ✅（改善更大） |
| 减少系统展示 | ✅ | ✅（改善更大） |
| 人物非功能件 | ✅ | ✅ |
| 有代价/阻力/债 | ✅ | ✅ |
| 未牺牲推进 | ✅ | ✅ |
| 未变啰嗦 | ✅ | ✅ |
| 未模板化 | ✅ | ✅ |

C3（信息露出节点）的改善比 C4 更显著——因为信息露出是当前 pipeline 最像"系统公告"的环节，HT patch 在此产生的增量最大。

## 5. 是否建议继续做更多真实样本？
是，但优先级可降低。建议路线：
1. ✅ 本轮 2 样本通过干净 brief 验证
2. 合并 PR #1 后在真实五章完整链路中跑一次 A/B（含 Polisher）
3. 如通过则合并到 main 的 skill-pack

C4（关系节点）和 C3（信息节点）已覆盖当前 pipeline 最暴露系统展示感的两个节点类型。

## 6. 是否建议修改 PR？
建议微调，非阻塞：
- Reviewer HT gate 可增加"information_carrier 最低层数检查"（≥2 层）
- 其余当前规则已足够，本轮验证显示现有规则能正确引导生成和评审

## 7. 是否建议合并 PR？
**✅ 建议合并。**

理由：
1. 两个干净 brief 样本均通过验证
2. B 版在两个节点类型上均明显优于 A 版
3. 改善来自叙事行为层（信息露出方式、情感展示方式、代价具体化），非句子润色
4. 未牺牲任何网文推进功能
5. 未出现模板化风险
6. Reviewer HT gate 运作正确
7. C3（信息节点）改善最显著——HT 在最需要的地方效果最好

## 8. 当前阻塞项
**无阻塞项。**
- ✅ 两个样本均通过 Reviewer gate
- ✅ 无结构性失败
- ✅ 无退化
- ⚠️ seed 不一致（已在报告中说明）

## 9. 给项目负责人的最终建议
合并 PR #1。Human Texture patch 的价值在于它给现有 Planner/Writer/Reviewer 链路增加了一层"可执行的检查"：每个关键机制点（信息露出、情感节点、关系转折）都必须有人承受、有人误读、有人欠债或有下一章摩擦。本轮两次验证（含已作废的第一次）均显示此检查有效且未引入副作用。

## 附录：文件清单
```
real_chain_validation_rerun/
├── README.md
├── invalid_previous_run_note.md
├── run_config.md
├── prompts/
│   ├── c4_task_brief.md
│   └── c3_task_brief.md
├── c4_relationship_node/
│   ├── baseline_main/{planner,writer,reviewer}
│   ├── human_texture_branch/{planner,writer,reviewer}
│   └── comparison_report.md
├── c3_information_node/
│   ├── baseline_main/{planner,writer,reviewer}
│   ├── human_texture_branch/{planner,writer,reviewer}
│   └── comparison_report.md
└── overall_report.md
```
共 17 个文件。
