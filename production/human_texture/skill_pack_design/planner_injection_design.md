# Planner Injection Design

本文件设计 `webnovel_planner` 后续如何接入 Human Texture。当前只写设计，不修改正式 `SKILL.md`。

## 接入位置

Planner 应在 chapter beat 阶段新增一个轻量 `human_texture` 输出块，位置建议放在原有 beat / hook / payoff / rule-breaking / cost 之后，Writer 输入之前。

它不是新增一套文学分析，而是给每章标出 2-3 个“人味压力点”：

- 谁有不愿承认的私心。
- 谁在回避羞耻或亏欠。
- 哪条关系账发生变化。
- 场景如何阻碍人物目标。
- 信息从哪个载体露出。
- 本章给下一章留下什么摩擦。

## 建议 YAML

```yaml
human_texture:
  focus_fields:
    - relationship_debt_change
    - information_carrier
  private_want: "主角想保住自己没有欺瞒柳青砚的形象，但事实已经相反。"
  shame_or_avoidance: "他回避直接解释，把话题推回任务。"
  relationship_debt_change: "柳青砚继续提供必要信息，但不再默认相信他的判断。"
  scene_resistance: ""
  information_carrier: "柳青砚只说她亲眼确认过的半段线索，保留另一半。"
  consequence_next_friction: "下一章主角需要在继续隐瞒和重新取得信任之间付代价。"
  carry_forward:
    relationship_debt:
      - "柳青砚知道主角撒过谎；合作可以继续，信任不可默认恢复。"
    consequence:
      - "主角若继续借用柳青砚的信息，必须面对解释成本。"
```

## 与原有 beat / hook / payoff 的结合

| 原有 Planner 功能 | Human Texture 接法 | 目的 |
| --- | --- | --- |
| beat | 给关键 beat 加 1 个可见的人物选择压力。 | 避免 beat 只是事件列表。 |
| hook | 钩子前后保留人物承受点。 | 避免章尾大信息吞掉人。 |
| payoff | payoff 后记录谁付出了关系、情绪或制度代价。 | 让爽点不清零。 |
| rule-breaking | 破局必须问“谁因此更难过下一关”。 | 保留网文爽感，同时继承后果。 |
| cost | cost 从抽象代价变成可继承摩擦。 | 避免“沉重代价”只是一句口号。 |
| revelation | 每个信息点指定 carrier 和 exposure cost。 | 避免公告化和主角直接读懂源码。 |

## 每章如何选 2-3 个核心字段

Planner 不应把 6 个字段全量塞入每章。选择顺序建议：

1. 先判断本章主功能：关系、信息、情绪后果、章尾钩子、战斗破局、转场。
2. 选 1 个与主功能强绑定的字段。
3. 再选 1 个能制造下一章摩擦的字段。
4. 如果本章有重要关系人，再选 1 个关系或羞耻字段。
5. 如果字段不能改变选择、信息露出或后果，就不选。

示例：

- 关系节点：`private_want` + `shame_or_avoidance` + `relationship_debt_change`
- 信息节点：`scene_resistance` + `information_carrier` + `consequence_next_friction`
- 章尾钩子：`relationship_debt_change` + `consequence_next_friction`
- 战斗破局：`private_want` + `scene_resistance` + `consequence_next_friction`

## Relationship Debt / Consequence Ledger

Planner 应维护轻量账本，供下一章 beat 读取。

```yaml
human_texture_ledger:
  relationship_debt:
    - id: "liu-qingyan-trust-01"
      characters: ["主角", "柳青砚"]
      change: "柳青砚知道主角撒谎；合作继续，信任下降。"
      evidence: "她不再追问，只把信息说完。"
      next_use: "下一章主角请求协助时，她先要求完整解释。"
  consequence:
    - id: "mine-info-cost-01"
      source_beat: "C3 饭堂信息露出"
      friction: "主角拿到线索，但暴露了他在打听矿洞。"
      next_use: "监工开始留意他和老矿奴的接触。"
```

账本只记录会在后续使用的债。没有后续使用计划的“关系变化”应删除。

## 信息揭示设计

Planner 默认不应使用公告或权威说明来完成信息揭示，除非这是本章刻意要写的制度压迫场景。每个重要信息点应至少回答：

- 信息由谁或什么承载？
- 承载者为什么会露出它？
- 主角是否误读、漏读或只拿到半截？
- 谁因此付出暴露、被扣资源、得罪人或欠债的代价？
- 这个代价是否进入下一章 friction？

可用载体包括：

- 人：旁人半句话、敌人试探、师长沉默、同伴保留。
- 物：罚牌、账册、伤口、破损器物、饭票、旧符。
- 制度缝隙：例外处理、扣发、排队顺序、禁令执行差异。
- 场景行为：谁能靠近、谁必须避开、谁被迫闭嘴。

## 避免抽象口号

Planner 输出不能写成：

- “增加人味”
- “表现信任破裂”
- “加入生活质感”
- “让情绪更真实”
- “加强余味”

每个字段必须能转成一个可写动作：

- 谁做了什么不完美选择？
- 谁少说了哪句话？
- 谁保留了哪段信息？
- 哪个场景阻力打断了目标？
- 哪个后果会让下一章更难？

## Planner 负责什么

Planner 负责：

- 选择本章 2-3 个 focus fields。
- 给关键 beat 绑定人味压力点。
- 决定信息 carrier 和 consequence。
- 维护 relationship debt / consequence ledger。
- 判断哪些后果必须在下一章继承。
- 避免将重要设定默认写成公告。

Planner 不负责：

- 写正文句子。
- 写心理独白和具体动作细节。
- 处理句子节奏、语言光泽和局部余味。
- 在 Writer 阶段临时新增未规划剧情。
- 用 Human Texture 替代原有 hook、payoff、rule-breaking 和 cost 设计。

## 输出失败时的退回规则

如果 Planner 输出出现以下问题，Reviewer 应退回 Planner：

- `focus_fields` 超过 3 个，导致 Writer 只能逐项模板化。
- 字段全是抽象口号，不能转成动作。
- 信息揭示没有 carrier，仍依赖旁白公告。
- 代价没有下一章摩擦。
- 关系债没有后续使用计划。
- Human Texture 与原 beat 冲突，削弱主线推进。
