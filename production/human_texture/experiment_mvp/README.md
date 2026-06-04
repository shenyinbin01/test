# Human Texture MVP A/B Experiment

日期：2026-06-04

本目录是 Human Texture Engine 的最小 A/B 实验。实验只使用现有 5 章失败样本中的两个局部片段，不重写完整章节，不修改 `skill-pack/`，不启动 Polisher，不接入 NovelClaw，不读取 `production/phase8/corpus/dachengqi/`。

## 实验目标

验证 `human_texture_packet` 是否能把原本“机制有效但不像人”的片段，改造成更像“人在经历故事”的正文，同时不损失中文网文推进。

## 实验片段

1. C4 柳青砚关系节点
   测试主角撒谎、柳青砚失望、信任破裂、关系债、人物不立刻和解。

2. C3 饭堂 / 矿洞信息露出节点
   测试场景生活质感、信息自然露出、制度缝隙、传闻误读、避免系统公告和主角直接读懂底层源码。

## 文件说明

- `selected_fragments.md`：两个片段的选择理由、baseline 摘要、原文问题诊断。
- `human_texture_packets.yaml`：两个片段的 `human_texture_packet`。
- `ab_versions/c4_baseline_excerpt.md`：C4 原始失败片段摘录。
- `ab_versions/c4_human_texture_version.md`：C4 Human Texture 改写片段。
- `ab_versions/c3_baseline_excerpt.md`：C3 原始失败片段摘录。
- `ab_versions/c3_human_texture_version.md`：C3 Human Texture 改写片段。
- `rubric_scores.md`：按 Human Texture rubric 对 A/B 分别评分。
- `mvp_result_report.md`：实验结论与下一步建议。

## 实验边界

已做：

- 针对两个局部片段生成 A/B 对照。
- 为每个片段生成 packet。
- 使用 10 维 rubric 评分。
- 判断是否保留原有剧情功能。

未做：

- 未修改任何正式正文。
- 未改 `skill-pack/`。
- 未改 Phase 8 craft assets。
- 未生成 approved patterns。
- 未启动 Polisher。
- 未继续外部项目调研或试跑。

## 初步结论

B 版在“人物私心、关系债、生活阻力、信息代价、真实后果”上明显优于 A 版，且没有牺牲原有剧情功能。风险是：如果 packet 写得太满，Writer 可能把所有字段都显性写出，导致新的模板化。因此下一步应继续做 2-3 轮片段实验，再决定是否设计 skill-pack 嵌入。
