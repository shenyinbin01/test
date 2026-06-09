# Renderer Boundary v2

## Renderer Receives

The Renderer may receive only:

1. `natural_language_scene_brief`
2. `narrative_stance_brief`
3. 1-3 rights-clear craft exemplars
4. safe continuity summary

## Renderer Must Not Receive

The Renderer is forbidden from receiving:

- raw state_delta full text
- full ledger
- raw scene_pressure_packet
- raw character_pressure_packet
- Orchestrator notes
- Reviewer scores
- proposed/official operational status terms
- acceptance-state management instructions
- private packet field names

## Renderer Output Forbids

Renderer output must not contain:

- event_log
- YAML
- Markdown engineering comments
- operational status fields
- meta terms such as “this chapter”
- “reader question”
- “relationship debt”
- “state delta”
- “agency choice”
- explanation of creative intent

## Boundary Principle

Renderer v2 renders lived pressure. It does not manage state, accept deltas, create ledgers, or explain the engine.
