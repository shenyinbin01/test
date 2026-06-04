# Writer Brief Design

本文件设计 `webnovel_writer` 后续如何接收并执行 Human Texture packet。当前只写设计，不修改正式 `SKILL.md`。

## Writer 的目标

Writer 不负责重新规划剧情，也不负责把 6 个字段逐项写进正文。Writer 的任务是：

- 保留 chapter beat 的原有剧情功能。
- 保留网文推进、爽点、规则破局、钩子和节奏。
- 将 `focus_fields` 转成具体选择、误读、场景阻力、关系变化和后果。
- 避免用风景、比喻、口语化或心理标签伪装“人味”。

## 输入形式

Writer 接收的 Human Texture brief 应尽量轻：

```yaml
human_texture_brief:
  focus_fields:
    - shame_or_avoidance
    - relationship_debt_change
  visible_requirements:
    - "主角不能立刻解释成功。"
    - "柳青砚必须保留失望后的行动边界。"
  avoid:
    - "不要写成两人当场和解。"
    - "不要用旁白总结信任破裂。"
  next_friction:
    - "下一章主角向柳青砚索取协助时，需要先偿还解释成本。"
```

完整 6 字段可以保留在 Planner 文件中，但 Writer brief 只突出本章要执行的 2-3 个字段和最小约束。

## 执行规则

### 1. 字段必须转成选择

错误做法：

> 他很羞愧，也知道两人的信任已经裂开。

正确方向：

> 他先把玉简推过去，说的是矿洞，不是自己为什么撒谎。柳青砚没有接，只让玉简停在桌沿。

判断标准：删掉解释句后，读者仍能从行为看出压力。

### 2. 每个主字段只要一个有效落点

Writer 不需要为每个字段连续写三遍。一个主字段有一个能改变场面走向的落点即可：

- `private_want`：一个回避、抢答、沉默或优先级选择。
- `shame_or_avoidance`：一个错误补偿或转移话题。
- `relationship_debt_change`：一个称呼、站位、信息保留或合作门槛变化。
- `scene_resistance`：一个阻碍目标的场景机制。
- `information_carrier`：一个承载信息的人、物、制度缝隙或误读。
- `consequence_next_friction`：一个进入下一章的未偿债、痕迹、资源损耗或被看见的动作。

### 3. 不牺牲原剧情功能

Human Texture 不能让正文变成慢速情绪戏。Writer 必须检查：

- 原 beat 的事件是否仍发生。
- 原规则破局是否仍清楚。
- 原信息点是否仍被读者获得。
- 原章尾钩子是否仍有效。
- 新增人味是否没有把主线推进挤掉。

如果 packet 要求会改变事件顺序、增加新角色、增加新线索或改变因果，应退回 Planner，而不是 Writer 自行补。

### 4. 不显性列字段

禁止写法：

- “他的私心是……”
- “这是他欠下的关系债。”
- “这个场景阻力让他……”
- “新的后果将在下一章体现。”

允许写法：

- 人物说少一句、说错一句、把话咽回去。
- 旁人不再帮他补台。
- 场景让他不得不绕路、等待、误听或付出额外成本。
- 信息只露出半截，且有人因此被看见。

## 与现有 Writer 规则的关系

| 现有 Writer 要求 | Human Texture 执行方式 |
| --- | --- |
| 200 字内事件驱动开场 | 开场仍从事件进入，但可让事件带出一个人的不完美选择。 |
| rule-breaking over power | 破局后追加一个继承后果，不把破局写成零成本胜利。 |
| cognitive advantage through action/dialogue/detail/reaction | Human Texture 可共用这一原则，通过误读、保留和反应表现人味。 |
| 不改 beat events | 如果 human texture 需要新增因果，退回 Planner。 |
| anti-template | 避免固定“沉默、苦笑、握拳、叹气”的情绪套件。 |

## 场景类型写法

### 关系节点

重点字段：`private_want`, `shame_or_avoidance`, `relationship_debt_change`

Writer 应让关系变化落在行为边界上：

- 不立刻和解。
- 不用旁白总结关系裂开。
- 一方继续完成必要合作，但减少额外信任。
- 下一次协作门槛变高。

### 信息露出节点

重点字段：`scene_resistance`, `information_carrier`, `consequence_next_friction`

Writer 应让信息从场景和人身上漏出来：

- 公告只能给表层规则，关键缝隙从例外处理、罚牌、扣食、沉默或误读中出现。
- 主角不应一次读懂底层源码。
- 读者能知道足够信息继续追，但仍看见信息代价。

### 情绪后果节点

重点字段：`shame_or_avoidance`, `relationship_debt_change`, `consequence_next_friction`

Writer 应避免“情绪被命名后消失”：

- 情绪导致一个选择变差。
- 情绪改变人物对人的态度、资源分配或风险承受。
- 情绪后果进入下一章，而不是本段被安抚清零。

### 章尾钩子节点

重点字段：`private_want`, `relationship_debt_change`, `consequence_next_friction`

Writer 应先完成网文钩子，再留下一个人的承受点：

- 大信息出现后，不要只写系统级震撼。
- 保留一个人物对这件事的具体损失、恐惧、误判或无法说出口的反应。
- 余味要短，不拖慢翻章。

## 篇幅控制

Human Texture 不应显著膨胀正文。建议：

- 单段片段改写增幅不超过 15%。
- 整章接入后增幅不超过 8-10%。
- 每个 focus field 只使用一个关键落点。
- 删除不能改变选择、信息、关系或后果的装饰细节。

## Writer 自检清单

提交草稿前，Writer 应自检：

- 我是否保留了原 beat 的剧情功能？
- `focus_fields` 是否至少各有一个可见落点？
- 人味是否来自选择、误读、关系、代价或场景阻力？
- 是否把字段写成了心理口号或说明文字？
- 是否因为人味降低了网文推进？
- 是否留下了下一章可继承的 friction？

如果这些问题无法在不改剧情的情况下解决，应退回 Planner。
