# Work Voice Research Plan

## 1. 为什么要做 Work Voice

Human Texture v0 解决的是“人物是否像人在经历故事”，但它不能稳定回答“是谁在讲这个故事”。当前问题不是描写不足，而是叙述者像无身体、无偏好、无稳定毛病的摄像头。Work Voice 的目标是把“讲故事的人站在哪里”工程化。

## 2. 和 Human Texture v0 的关系

Human Texture 是场景和人物层的真实感合同，关注私欲、羞耻、关系债、阻力、信息承载和后果摩擦。

Work Voice 是叙述层的站位合同，关注叙述者和主角、世界、读者、爽点、荒诞事件之间的关系。两者不冲突：Human Texture 让场景像人经历过，Work Voice 让整本书像同一个稳定讲述者讲出来。

## 3. 和 Author Fingerprint 的区别

本项目不以具体作者为对象，不抽取作者本人身份特征，不生成某作者风格模仿 prompt。相邻研究如 stylometry、writeprint、author attribution 可用于诊断文本特征，但只能作为“可迁移声音规则”的辅助观察，不作为复刻作者的目标。

## 4. 和普通文风、润色、humanizer 的区别

普通文风和润色多处理词句层：句长、重复、口语化、修辞、AI 味。Work Voice 处理叙述关系：什么时候贴主角，什么时候站在世界规则上方，什么时候把读者当同谋，什么时候冷眼旁观，什么时候暴露偏见或稳定毛病。

## 5. 和叙事学的关系

Work Voice 可借叙事学概念来建模，包括 narrator、focalization、narrative distance、point of view、implied author、free indirect discourse 和 reader relationship。参考入口：[The Living Handbook of Narratology](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 6. 和 stylometry / writeprint 的关系

Stylometry 和 writeprint 擅长识别作者差异，可提供特征候选：词长、句长、功能词、标点、搭配、节奏、段落密度。但这些特征多数是“作者识别”用途，不能直接转成生成策略。参考：Efstathios Stamatatos 的作者归属综述 [A Survey of Modern Authorship Attribution Methods](https://onlinelibrary.wiley.com/doi/10.1002/asi.21001)。

## 7. 是否能工程化

可以，但不是用“作者指纹”一键蒸馏。可工程化对象应限定为：

- narrative stance 标签。
- scene_type 分层样本。
- voice_observation_card。
- work_voice_map。
- voice_contract。
- Reviewer gate。
- A/B/C 人审和模型审双验证。

## 8. 如何进入 Planner / Writer / Reviewer

推荐路径：

1. Planner 前：选择目标原创作品的“可迁移声音方向”，不绑定具体作者。
2. Planner 中：把叙述站位纳入 Story Bible / chapter beat 的叙述策略字段。
3. Writer 前：生成 `voice_contract`，作为 Writer 的约束输入。
4. Reviewer 中：新增 Work Voice gate，检查站位稳定性、读者关系、过拟合风险和作者仿写风险。

本阶段不修改 `skill-pack`。MVP 阶段可先把 Work Voice 做成外部 research contract，再决定是否创建独立 Skill。

## 调研方法

- 理论：叙事学、文体学、计算叙事学。
- 学术技术：stylometry、writeprint、style transfer、controllable text generation、persona-conditioned generation、creative writing evaluation。
- 商业工具：AI fiction writing、style guide、voice profile、long-form novel 工具。
- 开源项目：fiction generation、长篇状态管理、planner/writer/reviewer/evaluator、style/persona/voice conditioning 项目。

中英文关键词均覆盖，英文关键词包括 `narrative voice`、`focalization`、`computational narratology`、`stylometry`、`writeprint`、`controllable story generation`、`AI fiction writing voice profile` 等。
