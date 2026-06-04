# Risk Register

| risk_id | 风险 | 触发条件 | 缓解方式 | MVP 阻塞 |
|---|---|---|---|---|
| WV-R001 | 作者模仿风险 | 使用作者名、口癖、专属句法作为目标 | 所有目标统一为 Work Voice；污染检查硬门禁 | 是，若触发 |
| WV-R002 | 原文污染风险 | 原文句子、段落、raw corpus 路径进入仓库 | evidence_ref 只允许抽象引用；提交前 grep 检查 | 是，若触发 |
| WV-R003 | 过度抽象导致不可执行 | contract 只有“冷”“热血”等形容词 | 每条规则必须绑定 scene_type、执行条件、Reviewer check | 否 |
| WV-R004 | 过度工程化导致写作僵硬 | Writer 被 checklist 压住，文本像报告 | contract 保持少量核心规则；验证网文推进和爽点 | 否 |
| WV-R005 | voice_contract 变成普通文风 checklist | 只写句长、词汇、标点，不写叙述关系 | 必须包含 narrator_position、reader_relationship、world_attitude | 否 |
| WV-R006 | C 组牺牲网文推进 | 声音稳定但节奏慢、爽点不清 | A/B/C scorecard 加入 momentum 和 payoff visibility | 否 |
| WV-R007 | Reviewer 无法区分“技巧化人味”和“稳定讲述者” | 只检查生活细节和情绪动作 | reviewer gate 增加 narrator_position_stability 和 reader_relationship_clarity | 否 |
| WV-R008 | Polisher 越权修复结构性站位问题 | 缺少作者站位却交给 Polisher 改句子 | gate 明确退回 Contract / Planner / Writer，不退给 Polisher | 是，流程阻塞 |
| WV-R009 | 把类型套路误判为作品声音 | 把升级、打脸、反转当 voice rule | aggregation 必须区分 genre convention 与 voice rule | 否 |
| WV-R010 | 原作专属元素误迁移 | 专有设定、人物关系模式、桥段进入 contract | non-transferable 清单必填，contract 禁用项必填 | 是，若触发 |
| WV-R011 | 长篇声音漂移 | 多章后叙述站位变成通用 AI 旁白 | 每 3-5 章做 drift review；MVP 先在短窗口验证 | 否 |
| WV-R012 | Human Texture 冲突 | Human Texture 要贴人物，Work Voice 要拉远 | scene_type_switching_rules 写明距离切换条件 | 否 |
