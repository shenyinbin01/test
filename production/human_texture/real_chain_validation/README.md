# Human Texture Real Chain Validation

## 目的

在真实 DeepSeek 模型上验证 Human Texture Skill Pack patch 是否让生成正文更像人写。

## 结论

✅ **建议合并 PR #1。** 两个验证样本（C4 关系节点 + C3 信息节点）中，Human Texture 版本均明显优于 baseline。

## 目录结构

```
real_chain_validation/
├── README.md                    ← 本文件
├── run_config.md                ← 运行参数
├── c4_relationship_node/        ← 样本 1：柳青砚关系节点
│   ├── baseline_main/
│   │   ├── planner_output.yaml
│   │   ├── writer_output.md
│   │   └── reviewer_output.md
│   ├── human_texture_branch/
│   │   ├── planner_output.yaml
│   │   ├── writer_output.md
│   │   └── reviewer_output.md
│   └── comparison_report.md     ← C4 A/B 对照
├── c3_information_node/         ← 样本 2：饭堂/矿洞信息节点
│   ├── baseline_main/
│   │   ├── planner_output.yaml
│   │   ├── writer_output.md
│   │   └── reviewer_output.md
│   ├── human_texture_branch/
│   │   ├── planner_output.yaml
│   │   ├── writer_output.md
│   │   └── reviewer_output.md
│   └── comparison_report.md     ← C3 A/B 对照
└── overall_report.md            ← 总体报告
```

## 快速结论

| 问题 | C4 | C3 |
|------|----|----|
| B 版更像人写？ | ✅ | ✅（改善更大） |
| 减少系统展示感？ | ✅ | ✅（改善更大） |
| 人物不再是功能件？ | ✅ | ✅ |
| 有关系债/后果/阻力？ | ✅ | ✅ |
| 牺牲网文推进？ | ❌ 未牺牲 | ❌ 未牺牲 |
| 建议合并 PR？ | ✅ | ✅ |

## 关键改善

- **信息露出**：从"精确告知"变成"含混传播→物证推理→记忆确认"（C3 最显著）
- **情感展示**：从"作者命名"变成"行为替代命名"（C4 最显著）
- **代价具体化**：从"抽象感累"变成"替班债+后山痕迹+双重异常"

## 运行参数

详见 `run_config.md`。A/B 唯一差异：Skill Pack 分支。
