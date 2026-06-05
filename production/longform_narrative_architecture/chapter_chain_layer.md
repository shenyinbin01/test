# Chapter Chain Layer

章节链层负责把卷目标拆成连续导航点。

## chapter_card 草案

```yaml
chapter_card:
  chapter_id: ""
  chapter_one_sentence: ""
  volume_goal_link: ""
  plot_function: ""
  required_conflict: ""
  required_reveal: ""
  required_payoff_or_debt: ""
  character_state_before: ""
  character_state_after: ""
  next_chapter_seed: ""
```

## 字段说明

- `chapter_one_sentence`: 本章一句话，不等于完整大纲。
- `volume_goal_link`: 本章如何服务卷目标。
- `plot_function`: 本章承担的推进功能。
- `required_conflict`: 必须发生的冲突。
- `required_reveal`: 必须露出的信息。
- `required_payoff_or_debt`: 必须回收或新增的债。
- `character_state_before`: 角色进入本章前的状态。
- `character_state_after`: 本章后角色状态变化。
- `next_chapter_seed`: 下一章继续的种子。

## 审查问题

章节链必须检查本章是否既推进主线，又改变状态。只完成钩子但不改变状态的章节，不应通过。
