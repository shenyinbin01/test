# Commercial Tool Survey

本调查只评估商业写作工具是否提供可借鉴的 voice profile、style profile、long-form fiction、narrator stance 或 POV 控制能力。不把任何工具接入当前项目。

| 工具 | voice / style 能力 | 长篇 fiction | narrator stance / POV 控制 | 是否偏表层润色 | 中文网文适配 | 工程嵌入 | 值得试用 / 借鉴 |
|---|---|---|---|---|---|---|---|
| [Sudowrite](https://www.sudowrite.com/) / [Docs](https://docs.sudowrite.com/) | 有面向 fiction 的 rewrite、describe、brainstorm、Story Bible 类能力 | 支持 | 可在 prompt 中控制 POV，但未见成熟叙述站位合同 | 中等，不只是润色 | 中文可试，但核心体验偏英文 | 可借鉴 Story Bible 与 writer-facing controls | 值得试用，重点看长篇上下文和 rewrite 控件 |
| [Novelcrafter](https://www.novelcrafter.com/) / [Docs](https://docs.novelcrafter.com/) | Codex/series bible、scene drafting、AI chat | 支持 | 可通过 Codex 和 scene brief 控制视角 | 不只是表层 | 中文需验证 | 可借鉴 Codex 结构和 scene-level prompt 注入 | 值得试用，尤其是长篇知识管理 |
| [NovelAI](https://novelai.net/) / [Docs](https://docs.novelai.net/) | Memory、Lorebook、Author's Note 等生成控制 | 支持 | Author's Note 可影响语气和方向，但不是完整 stance map | 生成型，不是润色器 | 中文可试，稳定性需验证 | 可借鉴 Memory / Lorebook / Author's Note 分层 | 值得借鉴控制槽位 |
| [ProWritingAid](https://prowritingaid.com/) | Style、readability、grammar、repetition reports | 支持 manuscript 级检查 | 不控制叙述站位 | 偏表层和编辑诊断 | 中文支持有限 | 可作为英文同类编辑器参考，不适合直接嵌入 | 借鉴报告维度，不作为核心 |
| [AutoCrit](https://www.autocrit.com/) | fiction editing reports，genre comparison | 支持 | 不直接生成 narrator stance | 偏编辑诊断 | 中文不适配 | 可借鉴 genre-aware rubric | 值得看评价维度 |
| [Fictionary](https://fictionary.co/) | story structure、scene analysis、character/location tracking | 支持 | 更偏结构，不是声音抽取 | 非润色，偏结构编辑 | 中文需人工适配 | 可借鉴 scene metadata 和结构 gate | 值得借鉴场景级标注 |
| [Grammarly](https://www.grammarly.com/) / [Style Guide](https://www.grammarly.com/business/styleguide) | brand tone、style guide、写作建议 | 不专注 fiction | 不控制叙述者 | 偏表层到品牌语气 | 中文弱 | 可借鉴 style guide 管理，不适合小说核心 | 借鉴“可执行风格规则”形式 |
| [Squibler](https://www.squibler.io/) | AI story writing、outline、chapter drafting | 支持 | 多通过提示控制 | 偏生成工作流 | 中文需验证 | 可借鉴产品流程，不建议直接接入 | 可试用但优先级低 |

## 关键发现

1. 商业工具普遍有 story bible、style guide、memory、lorebook、author note、tone control 等容器。
2. 这些容器可以帮助控制输出，但多数没有把 narrator position、reader relationship、world attitude、intervention rules 明确拆成合同。
3. ProWritingAid、AutoCrit、Fictionary 更适合作为评价维度参考，不适合作为生成核心。
4. Sudowrite、Novelcrafter、NovelAI 更值得试用，因为它们面向长篇 fiction，能观察商业产品如何让用户给模型持续约束。
5. 对中文网文，商业工具只能提供产品结构借鉴，不能直接解决 Work Voice。

## 可借鉴点

- Story Bible / Codex：把稳定规则放在写作前。
- Memory / Lorebook：将长期设定和短期写作提示分层。
- Author's Note / Style Guide：把声音约束转成可执行 prompt 槽位。
- Editing reports：把主观评价拆成可勾选 gate。

## 结论

没有发现成熟商业工具能直接完成“作品声音蒸馏”。值得试用的不是它们的生成结果，而是它们如何把长篇上下文、语气约束、场景信息和编辑报告组织成产品流程。
