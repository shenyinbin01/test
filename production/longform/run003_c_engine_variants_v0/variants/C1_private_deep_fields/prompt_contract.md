# C1 Prompt Contract

Hermes must fill private engine templates for each chapter, then compile them into a short natural-language renderer brief.

## Renderer Receives

- natural-language scene brief
- narrative stance brief
- safe continuity summary
- forbidden terms

## Renderer Must Not Receive

- raw YAML packets
- field names such as desire, fear, shame, misbelief
- state_delta or ledger artifacts
- Orchestrator notes

## Failure Signal

C1 fails if it improves structure but still reads like a field checklist.
