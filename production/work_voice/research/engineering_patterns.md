# Engineering Patterns

## 1. Voice profile extraction

- 解决问题：把“这本书听起来像谁在讲”从主观感受转成可讨论对象。
- 输入：受控样本、scene_type、人工观察。
- 输出：候选 voice features。
- 前人做法：商业工具的 style guide、NovelAI Author's Note、stylometry 特征。
- 迁移方式：不抽作者身份，只抽 narrator stance。
- 风险：误导成作者仿写。

## 2. Narrative stance tagging

- 解决问题：标记叙述者站在主角、世界、读者还是事件上方。
- 输入：样本片段摘要，不含原文摘录。
- 输出：`narrator_position`、`protagonist_distance`、`world_attitude`。
- 前人做法：叙事学 focalization / narrative distance。
- 迁移方式：做成 `voice_observation_card` 字段。
- 风险：标注主观，需要双人或复审。

## 3. Sample-based style observation cards

- 解决问题：避免凭感觉总结整本书。
- 输入：scene_type 分层样本。
- 输出：结构化观察卡。
- 前人做法：Fictionary scene metadata、编辑报告、人工 rubric。
- 迁移方式：每个样本只记录抽象观察和 evidence_ref，不记录原文。
- 风险：样本太少会过拟合。

## 4. Scene-type stratified sampling

- 解决问题：不同场景声音不同，不能只看开头或高潮。
- 输入：opening、conflict、revelation、payoff、relationship、transition、chapter ending 等样本。
- 输出：按场景分布的 voice map。
- 前人做法：创作工具的 scene card、长篇编辑器的 scene analysis。
- 迁移方式：MVP 每本先 30-60 个受控样本。
- 风险：抽样偏向单一爽点。

## 5. Feature aggregation

- 解决问题：把单张观察卡聚合成稳定规则。
- 输入：多张 `voice_observation_card`。
- 输出：`work_voice_map`。
- 前人做法：stylometry 的聚合统计、manual style guide。
- 迁移方式：按置信度、场景类型、可迁移性聚合。
- 风险：把偶发现象当稳定规则。

## 6. Generic-vs-work-specific feature separation

- 解决问题：区分类型通用套路、作品可迁移声音、原作专属表达。
- 输入：观察卡和对照作品。
- 输出：`transferable_voice_rule` 与 `non_transferable_original_element`。
- 前人做法：style transfer 的内容/风格分离，author attribution 的差异特征。
- 迁移方式：禁用角色名、设定、专有比喻、原文句式。
- 风险：边界不清时触发版权和仿写风险。

## 7. Voice contract generation

- 解决问题：把研究结论转成 Writer 可执行输入。
- 输入：`work_voice_map`。
- 输出：`voice_contract`。
- 前人做法：style guide、Author's Note、prompt control。
- 迁移方式：合同字段包括 voice_type、reader_relationship、intervention_rules、forbidden_original_elements。
- 风险：合同太抽象导致 Writer 不执行，太细则像仿写。

## 8. Writer conditioning

- 解决问题：让正文生成前就带着稳定叙述站位。
- 输入：beat、Human Texture packet、`voice_contract`。
- 输出：draft。
- 前人做法：NovelAI Memory / Lorebook / Author's Note、novel-bot context assembly。
- 迁移方式：Writer prompt 中新增外部 voice block，先实验不改 skill-pack。
- 风险：过多约束降低推进速度。

## 9. Reviewer gate

- 解决问题：发现站位漂移、AI 摄像头感、作者仿写风险。
- 输入：draft、beat、voice_contract。
- 输出：pass/fail、rewrite_instructions。
- 前人做法：GenerationGate、quality controller、creative writing rubric。
- 迁移方式：新增 Work Voice 检查维度。
- 风险：评价主观，需要样例校准。

## 10. A/B/C validation

- 解决问题：判断 Work Voice 是否真的优于 Human Texture v0。
- 输入：A old baseline、B Human Texture v0、C Human Texture v0 + Work Voice Contract。
- 输出：盲评结果和指标。
- 前人做法：LLM writing benchmark、产品 A/B。
- 迁移方式：同 beat、同约束、同字数窗口比较。
- 风险：一次样本不稳定，需要多场景复测。

## 11. Human review rubric

- 解决问题：把“像人写”“作者在哪里”转成可复审问题。
- 输入：候选文本。
- 输出：人工评分和审稿意见。
- 前人做法：AutoCrit、Fictionary、ProWritingAid 报告思路。
- 迁移方式：rubric 包括稳定讲述者、站位一致、读者关系、未复刻、网文推进。
- 风险：审稿人偏好会影响结论。
