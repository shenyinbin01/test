# Execution Artifact Flow

This task prepares the flow only. It does not execute the flow.

## Future Flow

```text
Input templates
-> Orchestrator Lite
-> chapter_card_lite x3
-> scene_agency_packet_tasks
-> event_log_standard
-> Renderer
-> draft
-> Reviewer
-> state_delta_v1
-> reducers
-> ledger views
-> drift / anti-feed checks
-> next chapter retrieval
```

## Review Points

- Orchestrator output is reviewed before Renderer reads it.
- Renderer output must include a render report and blocker if any.
- Reviewer output must decide pass, return, or state-delta review.
- State delta enters reducers only after accepted status.
- Ledger views expose only hot slices to Writer and Renderer.
- Drift and anti-feed checks decide whether to proceed to the next chapter.

## Stop Points

- Stop if Renderer reports structural blocker.
- Stop if Reviewer marks any Critical gate as failed.
- Stop if `state_delta.status` is `conflict` or `needs_human_review`.
- Stop if hot ledger slice omits required continuity evidence.
