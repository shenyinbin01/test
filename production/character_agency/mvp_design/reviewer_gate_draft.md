# Reviewer Gate Draft

```yaml
not_polisher_job: true
```

Reviewer 必须判断角色主动感是否通过，并定位失败层级。行动主权缺失是结构问题，不交给 Polisher。

## 检查问题

1. 人物是否有当前小目标。
2. 人物是否有自己的处理方式。
3. 人物是否做了取舍。
4. 人物注意力是否有选择。
5. 人物选择是否改变下一步局面。
6. 后果是否进入账本。
7. 关系债是否继承。
8. 作者是否替人物解释动机。
9. 人物是否只是标准反应器。

## Gate 输出草案

```yaml
character_agency_review:
  active_character: ""
  local_goal_present: false
  chosen_tactic_present: false
  tradeoff_present: false
  blindspot_or_wrong_model_present: false
  visible_action_seed_present: false
  consequence_written_to_ledger: false
  relationship_debt_written_to_ledger: false
  author_explains_for_character: false
  standard_reactor_risk: "low|medium|high"
  webnovel_function_preserved: true
  gate: "pass|return_to_planner|return_to_writer"
  not_polisher_job: true
  required_fix:
    - ""
```

## 退回规则

- 缺少 active_character 或 local_goal：退回 Planner。
- 缺少选择和取舍：退回 Planner。
- 有 packet 但正文只解释不行动：退回 Writer。
- 后果没有进入 ledger：退回 Planner。
- 关系债没有继承：退回 Planner。
- 语言粗糙但结构有效：才允许后续进入 Polisher。
