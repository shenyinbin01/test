# Synthetic v1 Complexity Check

## Field Count Comparison

| area | v0 | v1 | result |
|---|---:|---:|---|
| chapter_card default fields | 18 | 12 | lighter |
| reviewer default gates | 12 | 7 Critical + 6 Standard | tiered |
| research reviewer gates | mixed into default risk | 4 Research only | lighter default |
| renderer ledger input | hot ledger slice but not capped | hot slice max 12 items | lighter |
| state_delta status | absent | proposed / accepted / rejected / conflict / needs_human_review | slightly heavier but safer |
| reducer conflict handling | noted but not shaped | explicit conflict types + provenance | safer |
| spotlight control | `spotlight_targets` only | explicit `spotlight_budget` | clearer |

## Renderer Input Scale

v0 risk: Renderer might receive all relevant ledgers.

v1 adjustment: Renderer receives:

- chapter_card Lite / Standard
- scene agency packets
- standardized event_log
- hot ledger slice
- placeholder Human Texture / Work Voice packet
- spotlight_budget

## Orchestrator Clarity

v1 improves clarity:

- Orchestrator owns hot slice and spotlight budget.
- Scene agency owns choices.
- Renderer owns rendering and blocker.
- Reducers own ledger views.

## Net Result

v1 is lighter than v0 for default use. The only added complexity is `state_delta` status / conflict / provenance, which is justified because it prevents false ledger merges.
