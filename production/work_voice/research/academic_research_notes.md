# Academic And Technical Research Notes

## 1. Computational Narratology

计算叙事学把事件、角色、情节结构、叙述视角和叙事语义转成可分析对象。它能帮助 Work Voice 定义“谁知道什么”“谁在看”“事件如何被讲述”，但不直接给出网文生成合同。参考：[Computational Narratology - LHN](https://www-archiv.fdm.uni-hamburg.de/lhn/node/43.html)。

可转工程特征：叙事层级、角色知识边界、事件可见性、叙述者干预点。

## 2. Stylometry

Stylometry 用词频、功能词、句长、标点、n-gram 等统计特征识别文体差异。它适合辅助发现文本节奏和表层稳定性，不适合直接生成 Work Voice。参考：[Stamatatos 2009](https://onlinelibrary.wiley.com/doi/10.1002/asi.21001)。

可转工程特征：句长分布、段落密度、标点节奏、功能词倾向。风险是把作者身份特征误当可迁移作品声音。

## 3. Writeprint / Authorial Fingerprint

Writeprint 研究作者识别和身份归因，常用于安全、取证、匿名文本识别。它能提醒我们哪些特征很容易变成“作者本人”的不可迁移指纹。参考：[Abbasi and Chen writeprints research](https://dl.acm.org/doi/10.1145/1458082.1458101)。

本项目只把 writeprint 当风险边界和诊断工具，不把它作为主目标。

## 4. Author Attribution

作者归属研究能判断两段文本是否像同一作者，但它回答的是分类问题，不是“如何讲一个原创故事”。参考：[Koppel, Schler, Argamon 2009](https://doi.org/10.1561/1500000005)。

可用于评价：避免 C 组输出过度靠近某个来源作品或具体作者。

## 5. Style Transfer

文本风格迁移研究把内容和风格解耦，常用于情感、正式度、个性化表达等任务。参考：[Style Transfer in Text](https://arxiv.org/abs/1711.06861)。

对 Work Voice 的帮助：提供“内容不变、表达约束变化”的实验框架。限制：多数任务处理短文本或表层属性，不足以覆盖长篇叙述站位。

## 6. Controllable Text Generation

可控生成研究关注让模型按属性、计划、关键词、结构或控制码输出。参考：[A Survey of Controllable Text Generation using Transformer-based Pre-trained Language Models](https://arxiv.org/abs/2201.05337)。

可转工程特征：控制字段、解码前条件、后验评价、属性分类器。用于本项目时应以 `voice_contract` 做前置条件，以 Reviewer gate 做后验检查。

## 7. Persona-conditioned Generation

Persona-conditioned generation 将对话者人格或长期偏好注入生成。参考：[PersonaChat](https://arxiv.org/abs/1801.07243)。

可借鉴点：稳定偏好、说话边界、关系姿态。限制：对话 persona 不等于长篇 narrator stance，不能把角色人格误当叙述者人格。

## 8. Narrative Style Modeling

长篇故事生成研究常采用计划生成、层级结构、角色表和事件线。参考：[Plan-and-Write](https://arxiv.org/abs/1811.05701) 与 [Dramatron](https://arxiv.org/abs/2209.14958)。

可借鉴点：先规划再写作、结构层级、co-writing 而非全自动。缺口是多数项目更关注情节一致性，不细分叙述者与读者关系。

## 9. LLM Creative Writing Evaluation

创意写作评价常比较 coherence、engagement、style、originality、human-likeness。参考开源 benchmark：[lechmazur/writing](https://github.com/lechmazur/writing)。

可用于评价：A/B/C 盲评，加入“稳定讲述者”“作者位置可感”“未复刻来源”三个维度。

## 10. AI-generated Writing Homogenization

AI 写作同质化通常表现为解释过直、情绪标签化、功能性人物、句式平滑、缺少稳定偏见和具体身体位置。学术上可借 creative writing evaluation 和 stylometry 方法评估，但中文网文需要本项目自建 rubric。

## 综合判断

- 能帮助识别 Work Voice：叙事学、计算叙事学、stylometry、creative writing evaluation。
- 只能做作者识别：writeprint、author attribution。
- 能转工程特征：聚焦、叙述距离、读者关系、句式节奏、信息边界、插嘴规则。
- 可用于评价：stylometry 距离、A/B/C 盲评、Reviewer gate、人工 rubric。
- 不适合直接用于中文网文：短文本 style transfer、英文作者归属模型、对话 persona 模型、只看表层润色的 humanizer。
