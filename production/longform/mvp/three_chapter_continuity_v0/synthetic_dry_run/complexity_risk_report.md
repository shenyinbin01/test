# Complexity Risk Report

## Risk 1: schema 过重

`chapter_card`、`state_delta` 和 ledger views together are useful, but too much for every ordinary chapter.

Mitigation: define Lite / Standard / Research modes.

## Risk 2: Orchestrator 压死角色主动感

If Orchestrator specifies tactics, it becomes hidden author.

Mitigation: Orchestrator may set boundaries, windows, and replan triggers; `scene_agency_packet` owns choices.

## Risk 3: ledger 维护成本过高

Nine ledgers are useful for diagnosis but costly for production.

Mitigation: MVP hot slice should prioritize plot, character state, relationship debt, knowledge, reader question, and volume progress. Resource and reputation can be conditional.

## Risk 4: Reviewer gate 过重

Twelve dimensions can slow every chapter.

Mitigation: use Lite gate for every chapter and full gate for milestone chapters or failed samples.

## Risk 5: 三章实验成本

Synthetic cost is low. Real generation cost may rise because each chapter creates cards, packets, logs, deltas, reducers, and reviews.

Mitigation: keep three chapters; do not jump to one volume / ten chapters.

## Suggested Modes

| mode | use | included |
|---|---|---|
| Lite | ordinary chapter continuity | chapter_card, one scene packet, state_delta, hot ledger slice |
| Standard | important chapter | full chapter_card, multiple scene packets, event logs, reducer views |
| Research | diagnostic run | all ledgers, drift reports, blocker reports, full reviewer gate |

## Bottom Line

The flow is viable, but production should not start with Research mode for every chapter.
