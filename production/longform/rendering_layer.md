# Rendering Layer

Narrative Renderer（正文渲染器）是限权渲染层，不是隐藏 Writer，也不是 Polisher。

## Renderer 读什么

- `chapter_card`：章节状态变化合同。
- `scene_agency_packets`：场景行动包。
- `event_log`：已发生事件和证据。
- `human_texture_packet`：人物质感约束。
- `work_voice_contract`：作品声音 / 叙述站位合同。
- 当前热账本切片：角色、关系债、信息、资源、读者问题和伏笔状态。

## Renderer 写什么

- `draft`：正文草稿。
- `render_report`：说明哪些合同被执行，哪些风险出现。
- `blocker`：如果结构不足以渲染，返回阻塞类型。

## Renderer 不能改什么

- 角色行动结果。
- 谁知道什么、谁误会什么、谁被瞒着什么。
- 资源、关系和状态账本事实。
- 已 accepted 的卷目标与章节合同。
- 因果决定。

## blocker 类型

| blocker | 定义 | 应退回 |
|---|---|---|
| `causal_thinness` | 因果太薄，事件不足以支撑状态变化。 | Orchestrator / Scene Engine |
| `embodied_consequence_missing` | 后果缺少可见行为或状态承载。 | Scene Engine / Writer brief |
| `focalization_breach` | 聚焦越界，叙述知道了人物不该知道的内容。 | Renderer contract / Reviewer |
| `exposition_clump` | 信息堆成公告或旁白说明。 | Chapter Card / Renderer |
| `spotlight_imbalance` | 聚光预算失衡，配角、设定或钩子吞掉人物承受点。 | Orchestrator / Chapter Card |
