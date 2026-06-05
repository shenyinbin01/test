# Next Step Recommendation

## Options

### A. 人工审 v1 压缩结果

Review:

- Lite / Standard / Research 是否合理。
- `chapter_card_lite` 是否过轻。
- Critical + Standard gate 是否足够。
- `state_delta_v1` 的 status / conflict / provenance 是否可接受。
- hot ledger slice 是否足够控制上下文。

### B. v1.1 小修

只修 schema 命名和字段，不扩新模块。

Candidate fixes:

- Finalize `event_log` naming.
- Finalize `state_delta_v1` status and conflict shape.
- Finalize `spotlight_budget`.
- Decide hot slice max item count.

### C. Hermes / DeepSeek 三章连续小样本

获批后进入真实三章小样本。仍然不做：

- 10 章。
- 完整 IP 宇宙。
- 完整 multi-agent。
- 正式 skill-pack 修改。

## Recommendation

Recommended order:

```text
A -> B -> C
```

不建议再做第三轮纯文档扩展。不建议直接上 10 章。不建议现在做完整 IP 宇宙。不建议现在改正式 skill-pack。

## Execution Packet Needed Before C

If approved for Hermes / DeepSeek sample, prepare:

- `world_slice_lite.yaml`
- `single_book_story_lite.yaml`
- `volume_card_lite.yaml`
- `chapter_card_lite_x3.yaml`
- `scene_agency_packet_tasks.yaml`
- `event_log_standard_template.yaml`
- `state_delta_v1_template.yaml`
- `hot_ledger_slice_template.yaml`
- `critical_standard_reviewer_gate.md`
- `renderer_contract_v1_prompt_boundary.md`
