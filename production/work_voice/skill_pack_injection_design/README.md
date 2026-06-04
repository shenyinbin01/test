# Work Voice Skill-Pack Injection Design v0

本包是 Work Voice MVP 到正式 `skill-pack` 注入之间的中间设计层。它把 MVP 中的 observation card、work_voice_map、voice_contract、reviewer gate 和 contamination checklist 翻译成未来 Planner / Writer / Reviewer / Polisher 可消费的接口设计。

## 本轮范围

- 不修改正式 `skill-pack`。
- 不生成正文。
- 不跑验证链路。
- 不调用 DeepSeek。
- 不读取、上传、保存 raw corpus。
- 不创建真实 voice_contract 成品。
- 不把 Work Voice 写成作者指纹、作者复刻或普通文风润色。

本轮目标是为未来 patch PR 降低不确定性：明确每个角色未来拿什么输入、产生什么输出、检查什么失败、失败后退回哪一层。

## 定位

Work Voice 是 Human Texture 之后的上层叙述合同。

- Human Texture 解决人物 / 信息 / 关系不像人。
- Work Voice 解决讲述者是否稳定存在。
- Work Voice 不等于作者指纹。
- Work Voice 不等于复刻作者。
- Work Voice 不等于普通文风润色。

## 设计原则

1. 上游 observation cards 和 aggregation 不进入生成链路。
2. 生成链路只接收 compact `work_voice_runtime_packet`。
3. Planner 将 runtime packet 压缩为章 / 场景级 `work_voice` block。
4. Writer 执行 compact brief，但不显性解释字段。
5. Reviewer 同时应用 Human Texture gate 和 Work Voice gate。
6. Polisher 只做结构已通过后的局部表达修正，不修复作者站位。
