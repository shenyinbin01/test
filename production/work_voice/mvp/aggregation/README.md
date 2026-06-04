# Aggregation

本目录定义如何把多张 `voice_observation_card` 汇总成可执行的 Work Voice 资产。

## 文件

- `work_voice_map_template.md`：声音地图汇总模板。
- `transferable_voice_assets_template.md`：可迁移声音资产模板。
- `non_transferable_original_elements_template.md`：不可迁移元素清单模板。

## 汇总原则

- 先区分 scene_type，再聚合规则。
- 只迁移叙述关系和讲述策略。
- 不迁移原作设定、名词、口癖、句式、桥段。
- 如果某项观察无法判断是否可迁移，先放入风险项，不进入 `voice_contract`。
