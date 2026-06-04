# Human Texture MVP Round 2

日期：2026-06-04

本目录是 Human Texture MVP 第二轮片段实验。它延续第一轮 `experiment_mvp/` 的方法，但补足三类未覆盖问题：群体公告节点、情绪后果节点、章尾钩子压过人味节点。

## 本轮边界

已做：

- 从现有 5 章失败样本中选择 3 个局部片段。
- 为每个片段生成 baseline excerpt、diagnosis、human texture packet、B 版改写和 A/B rubric score。
- 判断 B 版是否保留原剧情功能、是否更像人在经历故事、是否出现模板化或篇幅膨胀。

未做：

- 未修改 `skill-pack/`。
- 未修改 Phase 8 craft assets。
- 未读取 `production/phase8/corpus/dachengqi/`。
- 未接入外部项目。
- 未启动 Polisher。
- 未重写完整五章。
- 未生成新 approved patterns。

## 片段类型

1. 群体公告 / 规则公布：C5 元启古镜公布积分来源、古阵寿命、枯竭筛选。
2. 情绪残留 / 情绪代价：C4 苏衍燃烧积分压低复检读数。
3. 章尾钩子压过人味：C4 白签后柳青砚关系余波被天幕裂缝和元启降临盖过。

## 文件索引

- `selected_fragments.md`：选择理由和 baseline diagnosis。
- `human_texture_packets.yaml`：三个片段的 packet。
- `ab_versions/group_announcement_baseline.md`
- `ab_versions/group_announcement_human_texture.md`
- `ab_versions/emotion_consequence_baseline.md`
- `ab_versions/emotion_consequence_human_texture.md`
- `ab_versions/ending_hook_baseline.md`
- `ab_versions/ending_hook_human_texture.md`
- `rubric_scores.md`：三组 A/B 评分。
- `round2_result_report.md`：第二轮结论和是否进入 skill-pack 嵌入设计。

## 核心结论

第二轮显示 `human_texture_packet` 仍然有效，但不同场景收益不同。信息公告和章尾钩子最容易因 packet 获益；情绪代价节点有效但更容易篇幅膨胀，需要 Writer 压缩动作链。第一轮 + 第二轮共 5 个片段均保留剧情功能并提升人味，建议进入 Skill Pack 嵌入设计前，先把 packet 字段精简成稳定 schema。
