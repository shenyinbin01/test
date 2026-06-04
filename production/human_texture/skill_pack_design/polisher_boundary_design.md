# Polisher Boundary Design

本文件设计 `webnovel_polisher` 在 Human Texture 接入后的边界。当前只写设计，不修改正式 `SKILL.md`。

## 基本原则

Polisher 不负责拯救结构性空心。Human Texture 的核心问题必须在 Planner / Writer / Reviewer 阶段解决：

- 私心和羞耻缺失，退回 Planner 或 Writer。
- 信息公告化，退回 Planner 或 Writer。
- 关系债没有变化，退回 Planner 或 Writer。
- 情绪没有后果，退回 Writer。
- 章尾钩子完全压过人物，退回 Planner。

Polisher 只在结构已经成立时，做轻量语言增强。

## Polisher 可以做什么

| 可做事项 | 边界 |
| --- | --- |
| 压缩显性说明 | 删除或弱化“他很羞愧”“信任裂开”等总结句，保留已有行为。 |
| 强化已有动作的清晰度 | 让已有动作更准，但不新增未规划行为。 |
| 调整句子节奏 | 让段落更顺、更紧，不改变事件顺序。 |
| 保留已有余味 | 对已经存在的人物承受点做 1-2 句收束。 |
| 减少公告感 | 在已有信息 carrier 成立时，压缩旁白解释。 |
| 修正模板动作 | 如果同段有多个“低头/苦笑/握拳”，可删减重复。 |

## Polisher 不可以做什么

| 禁止事项 | 原因 |
| --- | --- |
| 新增 private_want | 私心会改变人物选择，必须由 Planner / Writer 负责。 |
| 新增 relationship debt | 关系账会影响后续章节，必须进入 Planner ledger。 |
| 新增 information carrier | 信息载体会改变信息露出路径和因果。 |
| 新增 consequence_next_friction | 下一章摩擦属于结构设计。 |
| 把公告段改成完整场景 | 这会改变 beat 执行方式，应退回 Writer 或 Planner。 |
| 大幅增加生活细节 | 容易变成装饰性“人味”，且可能拖慢节奏。 |
| 改写完整段落结构 | 超出 Polisher 的轻润色边界。 |

## Polisher 接收条件

Reviewer 必须确认：

- `human_texture_review.gate = pass_to_polisher`
- 原剧情功能完整。
- focus fields 已经在正文中有可见落点。
- 关系债或后果账已明确。
- 剩余问题主要是语言显性、节奏略松、句子缺光泽。

如果 Reviewer 给出的 `required_fix` 涉及新增字段、改变信息来源、补关系债或改章尾结构，Polisher 应拒绝执行并返回 Reviewer。

## 推荐输入格式

```yaml
polisher_brief:
  human_texture_status: "structure_passed"
  allowed_actions:
    - "compress_explicit_emotion"
    - "sharpen_existing_aftertaste"
    - "reduce_announcement_tone"
  forbidden_actions:
    - "add_new_relationship_debt"
    - "add_new_information_carrier"
    - "change_beat_events"
  required_preserve:
    - "柳青砚不立刻原谅主角。"
    - "矿洞信息仍来自罚牌和老矿奴停顿。"
```

## 典型可润色问题

### 可交给 Polisher

原句：

> 他知道柳青砚已经不再相信他了，这让他心里很难受。

可改方向：

> 柳青砚没有接那枚玉简。他把手收回来，指腹在玉简边缘停了一下。

前提是正文前后已经建立关系债，Polisher 只压缩显性说明。

### 不可交给 Polisher

原段：

> 执事宣布了全部矿洞规则，众人震惊。主角立刻看出了规则漏洞。

问题不是语言粗糙，而是信息露出路径错误。应退回 Planner 或 Writer，补 `information_carrier` 和 `scene_resistance`。

## 篇幅边界

Polisher 仍遵守轻量增强原则：

- 整段字数变化建议控制在 ±10%。
- 不新增独立情节。
- 不新增角色和设定。
- 不改变 beat 事件顺序。
- 不把短钩子段扩写成情绪散文。

## 决策树

1. 问：Human Texture focus fields 是否已经在正文中有效出现？
2. 如果没有，退回 Planner / Writer。
3. 问：剩余问题是否只涉及语言显性、节奏和余味？
4. 如果是，允许 Polisher。
5. 问：修复是否需要新增关系债、信息载体或下一章摩擦？
6. 如果需要，停止 Polisher，退回 Reviewer 定层。

## 对正式 skill-pack 的后续建议

未来正式接入时，Polisher 的 `SKILL.md` 只需要增加一小段边界说明：

- Human Texture 结构未通过时不得执行。
- 不新增 6 个核心字段。
- 只压缩、保留和微调已存在的人味落点。

不建议给 Polisher 增加完整 Human Texture rubric，否则会诱导它越权做结构改写。
