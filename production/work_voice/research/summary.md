# Summary

## 1. 是否已有成熟方案

没有发现可直接复用的成熟“Work Voice / Narrative Stance 蒸馏”方案。成熟的是相邻领域：叙事学能描述叙述站位，stylometry 能识别表层文体，商业工具能提供长篇上下文容器，开源项目能提供状态管理和门禁结构。

## 2. 哪些理论可以借

可借理论包括 narrator、focalization、narrative voice、narrative distance、point of view、implied author、free indirect discourse、reader relationship、authorial stance。核心参考入口：[The Living Handbook of Narratology](https://www-archiv.fdm.uni-hamburg.de/lhn/contents.html)。

## 3. 哪些开源项目可以借

重点借鉴：

- [KazKozDev/NovelGenerator](https://github.com/KazKozDev/NovelGenerator)：reader/character knowledge、quality controller、agent coordinator。
- [knoai/knowrite](https://github.com/knoai/knowrite)：多层记忆、输入输出治理、角色分工。
- [xiaoxiaoxiaotao/novel-bot](https://github.com/xiaoxiaoxiaotao/novel-bot)：轻量上下文装配。
- [iLearn-Lab/NovelClaw](https://github.com/iLearn-Lab/NovelClaw)：memory/retriever/evaluator/executor。
- [zy-zmc/tianming-novel-ai-writer](https://github.com/zy-zmc/tianming-novel-ai-writer)：GenerationGate、fact snapshot。
- [google-deepmind/dramatron](https://github.com/google-deepmind/dramatron)：层级 co-writing。
- [muckelverk/pulpgen](https://github.com/muckelverk/pulpgen)：小型 CLI 实验 harness。

## 4. 哪些商业工具值得试

优先试用或观察：

- [Sudowrite](https://www.sudowrite.com/)
- [Novelcrafter](https://www.novelcrafter.com/)
- [NovelAI](https://novelai.net/)
- [Fictionary](https://fictionary.co/)
- [AutoCrit](https://www.autocrit.com/)
- [ProWritingAid](https://prowritingaid.com/)
- [Grammarly Style Guide](https://www.grammarly.com/business/styleguide)

它们值得借鉴的是 story bible、memory、lorebook、author note、style guide、scene metadata 和 editing reports，不是直接复用生成结果。

## 5. 是否需要自研

需要自研。原因是现有方案要么偏作者识别，要么偏英文短文本风格迁移，要么偏商业产品容器，要么偏长篇状态管理，没有把“叙述者站在哪里”做成中文网文可执行 writing contract。

## 6. 最小可行版本

MVP 为：

1. 受控样本规划。
2. `voice_observation_card`。
3. `work_voice_map`。
4. `voice_contract`。
5. Writer 注入。
6. Reviewer gate。
7. A/B/C 验证。

## 7. 是否建议进入 Work Voice MVP

建议进入，但应作为独立研究 MVP，不修改 `skill-pack`，不启动生产链路，不读取 raw corpus。

## 8. MVP 应该怎么做

先选 1 本成功作品做 30-60 个受控观察点，按 scene_type 分层，只保存抽象卡片和 evidence_ref。生成一份 `voice_contract` 后，对同一 chapter beat 进行 A/B/C：A old baseline，B Human Texture v0，C Human Texture v0 + Work Voice Contract。

## 9. 是否建议合并 PR #1 后再做

建议等 PR #1 合并并验收后再做工程化 MVP。原因是 Work Voice 需要注入 Planner / Writer / Reviewer，若底层 skill-pack 仍在移动，会增加验证噪音。研究包本身可以先提交。

## 10. 当前最重要的判断

最重要的判断是：必须区分“可迁移的叙述策略”和“不可迁移的原作表达 / 作者身份”。Work Voice 只迁移前者。凡是角色名、设定名、专属桥段、标志性比喻、原文句法、具体作者口吻，都必须进入禁用项。

## 摘要

Work Voice 是 Human Texture 之后的上层叙述合同。它不解决“人物有没有人味”，而解决“讲故事的人是否稳定存在”。现有理论和工具足以支撑一个小型 MVP，但没有成熟方案可直接复用。本项目应自研 `voice_observation_card -> work_voice_map -> voice_contract -> Writer conditioning -> Reviewer gate -> A/B/C validation` 流程，并在全过程保持不读 raw corpus、不保存原文、不复刻作者的边界。
