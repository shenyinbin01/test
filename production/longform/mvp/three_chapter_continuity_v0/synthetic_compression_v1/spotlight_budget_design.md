# Spotlight Budget Design

Spotlight budget is managed by Story Orchestrator Lite.

Spotlight is not word count. It is narrative burden: who or what carries the scene's decision, cost, reveal, or emotional pressure.

## Shape

```yaml
spotlight_budget:
  chapter_id: ""
  primary_focus:
    - protagonist_decision
  secondary_focus:
    - relationship_debt_01
    - hidden_fact_A
  background_only:
    - institution_A_setting
    - rival_circle_A_context
  forbidden_to_steal_scene:
    - full_world_exposition
    - rival_backstory_dump
  max_scene_focus_count: 3
  must_manifest_relationship_debt:
    - relationship_debt_01
  notes:
    - "Renderer must not expand background_only into main burden."
```

## Rules

- Orchestrator sets spotlight budget before Renderer.
- Renderer must obey spotlight budget.
- Budget prevents side characters from stealing the scene.
- Budget also prevents side characters from becoming pure tools by requiring specific relationship debt manifestation.
- If spotlight imbalance appears, return to Orchestrator, not Polisher.
