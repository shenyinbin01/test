# Human Texture Compact Packet Dry Run

日期：2026-06-04

## 目标

本轮 dry run 验证 `skill_pack_design/` 中的 6 字段精简版 Human Texture packet，是否仍能复现两轮 MVP 的效果。

本轮不是正式接入，不修改 `skill-pack`，不修改任何 `SKILL.md`，不重写完整五章，不启动 Polisher。

## 输入

- `production/human_texture/skill_pack_design/`
- `production/human_texture/experiment_mvp/`
- `production/human_texture/experiment_mvp_round2/`
- `production/phase8/skill_injection_minimal/validation_5ch/drafts/`

## 片段

1. C4 柳青砚关系节点
2. C3 饭堂 / 矿洞信息露出节点
3. C5 群体公告 / 规则公布节点
4. C4 情绪残留 / 情绪代价节点
5. C4 章尾钩子压过人味节点

## 方法

- 将两轮 MVP 的大 packet 压缩成 6 个核心字段。
- 每个片段只选择 2-3 个 `focus_fields`。
- 基于压缩 packet 写 B 版短改写，不替换正式正文。
- 用 `reviewer_gate_design.md` 判断 A 版失败应退回哪层、B 版是否可进入 Polisher。
- 用 `human_texture_evaluation_rubric.md` 的 10 个维度记录 A/B 分数。

## 通过标准

- 5 个片段中至少 4 个 B 版 Human Texture 平均分 >= 3.8。
- 5 个片段均保留原剧情功能。
- 没有明显篇幅膨胀。
- Reviewer 能明确定位失败层级。
- Human Texture 不退化成风景、比喻、口语化或装饰性细节。
- Polisher 不被要求救结构性空心。

## 输出文件

- `packets.yaml`：5 个压缩版 Human Texture packet。
- `writer_outputs.md`：baseline 问题摘要与 B 版短改写。
- `reviewer_gates.md`：A/B gate、退回层级和 Polisher 边界。
- `dry_run_scores.md`：10 维 A/B 评分。
- `result_report.md`：dry run 结论和下一步建议。

## 结论摘要

6 字段压缩版仍有效。5 个片段中 5 个 B 版平均分 >= 3.8，且全部保留原剧情功能。主要风险不是字段失效，而是情绪节点和章尾余味节点在正式接入时仍需控制篇幅与动作模板。
