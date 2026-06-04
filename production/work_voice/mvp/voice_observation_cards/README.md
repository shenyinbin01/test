# Voice Observation Cards

本目录定义单个受控样本的 Work Voice 观察卡。观察卡的目标是把“这段故事到底是谁在讲”拆成可观察字段。

## 文件

- `voice_observation_card_schema.yaml`：字段定义和禁用内容。
- `voice_observation_card_template.md`：人工填写用 Markdown 模板。
- `voice_observation_card_template.yaml`：机器可读 YAML 空模板。

## 填写原则

- 只记录抽象观察。
- 不复制原文。
- 不保存 raw corpus。
- 不写具体作者风格。
- 每张卡都必须同时写“可迁移规则”和“不可迁移原作专属元素”。
- `evidence_ref` 只能指向抽象位置，不得包含正文。

## 输出用途

观察卡会被汇总到：

- `work_voice_map`
- `transferable_voice_assets`
- `non_transferable_original_elements`
- `voice_contract`
