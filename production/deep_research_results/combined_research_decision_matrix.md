# Combined Research Decision Matrix

| recommendation | source_round | decision | reason | action | target_path | status |
|---|---|---|---|---|---|---|
| Character Agency 前移 | Round 1 | accept | 角色没有目标、误判、选择和代价回路时，后续 texture 与 voice 都会变成补丁。 | 建立 `scene_agency_packet` 并进入主线 P1。 | `production/character_agency/mvp_design/` | accepted_for_design |
| Consequence Ledger 前移 | Round 1 | accept | 代价不继承会让人物关系和情绪变成单章装饰。 | 与关系债账本、`state_delta` 一起进入 P2。 | `production/character_agency/mvp_design/` and `production/longform/schemas/` | accepted_for_design |
| 重组为四层框架 | Round 1 | accept | 原概念并列混杂了因果、质感、叙述和评价。 | 保留四层，并在 Round 2 后扩展为长篇热路径五层。 | `production/mainline_reframe/` | accepted_and_reframed |
| Reader Immersion 降为评价层 | Round 1 + Round 2 | accept | 读者代入更适合检查推断空间、读者问题和回收窗口，不宜变成 Writer 直写感觉。 | 收口到 `reader_question_ledger`、`chapter_card` 和 reviewer gate。 | `production/longform/schemas/reader_question_ledger.schema.yaml` | accepted_for_design |
| Live Leakage 降为微观技法 | Round 1 | accept | 它是 Human Texture 的低振幅表现，不是独立系统。 | 放入 Human Texture / Renderer 的局部执行规则，暂不单独立项。 | `production/mainline_reframe/do_not_do_now.md` | accepted_as_micro_rule |
| Agentic Narrative Engine 延后为 one-scene sandbox | Round 1 | accept | 完整 agentic runtime 成本高且难归因，容易让 coherence 和 agency 互相拖拽。 | 长线保留，当前主链不接入。 | `production/mainline_reframe/current_priority_order.md` | deferred |
| IP 宇宙降级为冷层资产 | Round 2 | accept | 完整宇宙会造成设定堆砌和资产幻觉，不能证明三章连续能力。 | 只做 `world_slice` 进入热路径。 | `production/longform/cold_asset_layer.md` | accepted_for_design |
| 单书故事作为热启动入口 | Round 2 | accept | 先确定一本书的承诺、对抗和终局方向，才能约束卷与章。 | 建立 `single_book_story` / Book Spine schema。 | `production/longform/schemas/single_book_story.schema.yaml` | accepted_for_design |
| 3 章连续 MVP 优先 | Round 2 | accept | 三章足够暴露章节边界问题，成本低于 10 章或完整卷。 | 创建 `three_chapter_continuity_v0` 设计包。 | `production/longform/mvp/three_chapter_continuity_v0/` | accepted_for_design |
| Delta First 状态回写 | Round 2 | accept | 账本直接手改会失真；所有账本视图必须追溯到写后增量事实。 | 建立 `state_delta` schema 与 reducers 说明。 | `production/longform/schemas/state_delta.schema.yaml` | accepted_for_design |
| Story Orchestrator Lite | Round 2 | accept | 长篇需要边界管理，但不需要隐藏作者。 | 定义职责边界、allowed divergence 和局部 replan。 | `production/longform/story_orchestrator_lite_spec.md` | accepted_for_design |
| Narrative Renderer 限权 | Round 2 | accept | Renderer 若修补因果会掩盖结构失败。 | 定义读 / 写 / 不能改，以及 render blocker。 | `production/longform/renderer_contract.md` | accepted_for_design |
| Work Voice 保留但不作为发动机 | Round 1 + Round 2 | partial_accept | Work Voice 解决叙述站位，不解决角色推动局面。 | 收口为 renderer contract 子模块，后续再接入。 | `production/longform/rendering_layer.md` | partial_accepted |
| 3 章连续能否显著改善长篇连续性 | Round 2 | pending | 目前仍是设计判断，没有真实链路样本。 | 先人工审，再 synthetic dry run，再 Hermes / DeepSeek 小样本。 | `production/longform/next_step_recommendation.md` | pending_validation |
| ledger 成本是否可控 | Round 2 | pending | 多账本可能带来 token、审核和归并成本。 | MVP 只测必要账本与 reducer 形态。 | `production/longform/risk_register.md` | pending_validation |
| Story Orchestrator 不会压死角色主动感 | Round 2 | pending | 边界管理过重会把角色变成执行件。 | 用 `allowed_divergence_band` 和 reviewer gate 检查。 | `production/longform/story_orchestrator_lite_spec.md` | pending_validation |
