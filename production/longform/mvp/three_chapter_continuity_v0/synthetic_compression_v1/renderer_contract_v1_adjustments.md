# Renderer Contract v1 Adjustments

Renderer remains permission-limited. v1 adds explicit hot ledger slice and spotlight budget input.

## Renderer Inputs

- chapter_card Lite / Standard
- `scene_agency_packets`
- `event_log`
- `hot_ledger_slice`
- `human_texture_packet` placeholder
- `work_voice_contract` placeholder
- `spotlight_budget`

## Renderer Outputs

```yaml
renderer_output_shape:
  draft: placeholder_only
  render_report:
    source_chapter_card: ""
    source_event_logs: []
    hot_ledger_slice_used: []
    spotlight_budget_followed: true
    blockers: []
  blocker:
    blocker_type: ""
    severity: ""
    return_to: ""
```

## Renderer Forbidden

- 改角色行动结果。
- 改谁知道什么。
- 改关系债。
- 改资源状态。
- 改 accepted `state_delta`。
- 自己修复因果洞。
- 读取未整理的自由 agent chatter。
- 把 background_only spotlight 展开成主要场面负担。

## v1 Rule

If Renderer sees missing causality, missing evidence, or impossible knowledge state, it must return blocker. It must not repair structure in draft.
