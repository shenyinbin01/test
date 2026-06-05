# Anti-Feed Gate Lite

Anti-feed checks prevent the sample from looking active while failing to advance state, debt, knowledge, or reader expectation.

## Critical Hard Fail

| gate | trigger | why_it_matters | return_to | severity |
|---|---|---|---|---|
| empty_advancement | No plot, character, relationship, knowledge, resource, or reader-question change. | The chapter consumes space without state movement. | Orchestrator | critical |
| hook_factory | Only adds hooks without payoff, cost, or explicit delay. | Hooks replace continuity instead of serving it. | Reviewer / Orchestrator | critical |
| free_payoff | Reward or reveal has no cost, limit, or consequence. | Payoff feels unearned and breaks pressure. | Scene Engine / StateManager | critical |
| narrator_steals_play | Narrator explains decisions or reader emotion before scene evidence. | Scene agency collapses into assertion. | Renderer | critical |
| relationship_evaporation | Active debt disappears without delta. | Relationship continuity fails. | Orchestrator / StateManager | critical |
| fake_ledger | Ledger item lacks accepted state delta evidence. | Memory becomes decorative instead of trustworthy. | StateManager | critical |
| renderer_polisher_overreach | Late layer fills causality, debt, resource, or knowledge gaps. | Structural failure is hidden as surface smoothness. | Reviewer | critical |

## Standard

| gate | trigger | why_it_matters | return_to | severity |
|---|---|---|---|---|
| setting_bloat | World detail expands beyond current slice and choice pressure. | Context becomes exposition load. | Orchestrator | standard |
| spotlight_imbalance | Background item steals scene burden from primary focus. | Agency and debt become diluted. | Orchestrator | standard |
| repeated_skeleton | Chapter repeats the same conflict, payoff, and question shape. | Continuity becomes formula. | Reviewer | standard |
