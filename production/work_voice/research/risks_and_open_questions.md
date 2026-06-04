# Risks And Open Questions

## 1. 仿写具体作者风险

- 风险描述：项目被误用为某作者风格模仿。
- 触发条件：使用作者名、保留标志性句法、生成“某作者风格 prompt”。
- 规避策略：统一使用 Work Voice；只抽象叙述关系；Reviewer gate 检查仿写倾向。
- 是否阻塞 MVP：不阻塞，但必须作为硬门禁。

## 2. 版权风险

- 风险描述：原文片段进入仓库、prompt、训练或输出。
- 触发条件：读取 raw corpus、保存原文、复刻桥段。
- 规避策略：遵守 `CORPUS_ACCESS_POLICY.md`；只记录 `evidence_ref`；不保存原文。
- 是否阻塞 MVP：若需要 raw corpus 且未获批准，则阻塞。

## 3. 把作品声音误判成作者本人风险

- 风险描述：把某本书的叙述策略误当作者身份特征。
- 触发条件：同作者多作品混合、使用 writeprint 语言。
- 规避策略：以单本作品的 work_voice_map 为对象，禁止作者身份目标。
- 是否阻塞 MVP：不阻塞。

## 4. 把类型套路误判成作品声音风险

- 风险描述：把“升级、打脸、反转”等类型结构误当声音。
- 触发条件：只看情节，不看叙述者关系。
- 规避策略：观察卡必须区分 sellpoint、genre convention、voice rule。
- 是否阻塞 MVP：不阻塞。

## 5. 把原作专属设定误迁移风险

- 风险描述：把原作角色、势力、术语、标志性桥段迁入原创项目。
- 触发条件：`non_transferable_original_element` 缺失。
- 规避策略：每张观察卡和 contract 都必须列 forbidden elements。
- 是否阻塞 MVP：可通过门禁控制。

## 6. 过拟合风险

- 风险描述：样本太少或太集中，导致 voice_contract 只适合局部场景。
- 触发条件：只抽开头、只抽高潮、只看高爽点。
- 规避策略：scene_type 分层，至少 30-60 个观察点。
- 是否阻塞 MVP：不阻塞，但会影响结论可信度。

## 7. 语感漂移风险

- 风险描述：长篇生成中前后叙述站位不一致。
- 触发条件：Writer 只看当前 beat，缺少 voice map 复用。
- 规避策略：每章注入同一 voice_contract；Reviewer gate 检查漂移。
- 是否阻塞 MVP：不阻塞。

## 8. 和 Human Texture v0 冲突风险

- 风险描述：Human Texture 要求贴人物，Work Voice 要求拉远到世界规则。
- 触发条件：场景目标未定义距离切换。
- 规避策略：contract 明确 scene_type 下的距离切换规则。
- 是否阻塞 MVP：不阻塞。

## 9. 评价主观风险

- 风险描述：人审对“稳定讲述者”的判断不一致。
- 触发条件：rubric 只写感受，不写判断问题。
- 规避策略：A/B/C 盲评、固定维度、保留审稿理由。
- 是否阻塞 MVP：不阻塞。

## 10. 长篇一致性风险

- 风险描述：短样本有效，但多章后声音坍塌。
- 触发条件：没有跨章 voice drift 检查。
- 规避策略：每 3-5 章做一次 work_voice drift review，与 `.story-system` 状态分离。
- 是否阻塞 MVP：不阻塞，但阻塞正式生产化。

## Open Questions

- 观察卡是否由 Hermes 人工填写，还是未来由 DeepSeek 生成后人工验收。
- Work Voice 是否最终成为独立 Skill，还是作为 Planner / Writer / Reviewer 的共享合同。
- 中文网文的 scene_type 分类是否需要按男频、女频、短剧化爽文分别扩展。
- A/B/C 人审是否需要外部审计方参与，还是先由项目负责人内部验收。
