# Voice Contract

本目录定义 Work Voice Contract 的 schema 和空模板。

`voice_contract` 是 Writer 前置输入，但本轮不接入正式 Writer Skill。它的职责是把 `work_voice_map` 中的可迁移叙述策略转成可执行写作约束。

## 文件

- `voice_contract_schema.yaml`
- `voice_contract_v0_template.yaml`
- `voice_contract_v0_template.md`

## 合同边界

- 合同不写真实作品内容。
- 合同不写具体作者目标。
- 合同不保存 raw corpus。
- 合同不迁移原作专属元素。
- 合同不是 tone/style guide；必须包含叙述者位置、读者关系、主角距离、世界态度和 scene_type 切换。
