# Critical + Standard Reviewer Gate

This gate excludes Research checks. It is the default future review mode for the three-chapter sample.

## Critical Gates

| gate | check_question | pass_signal | fail_signal | return_to | severity |
|---|---|---|---|---|---|
| chapter_contract_compliance | Does the output follow the chapter card contract? | Required conflict, payoff or debt, and next seed are traceable. | Output ignores required conflict or creates forbidden event. | Orchestrator | critical |
| state_delta_traceability | Can every accepted delta point to event evidence? | Accepted changes cite event log evidence. | Delta contains unsupported summary or missing evidence. | Reviewer / StateManager | critical |
| relationship_debt_continuity | Is active relationship debt inherited or explicitly changed? | Debt is manifested, delayed, paid, or worsened with evidence. | Debt vanishes or resets without delta. | Orchestrator | critical |
| knowledge_state_consistency | Does each character know only what evidence allows? | Knowledge changes cite visible event or accepted delta. | Character acts on unearned certainty. | Reviewer / Orchestrator | critical |
| renderer_overreach | Did Renderer stay inside contract? | Renderer reports blockers instead of repairing structure. | Renderer changes causality, knowledge, debt, or resources. | Renderer | critical |
| polisher_boundary | Is Polisher limited to surface-level work after gate pass? | Polisher is not asked to repair structure. | Polisher fills causality, debt, or knowledge holes. | Reviewer | critical |
| anti_feed_hard_fail | Does the chapter avoid empty advance and hook factory output? | State, debt, knowledge, resource, or reader question changes. | Only new hooks appear without cost, payoff, or delay. | Orchestrator | critical |

## Standard Gates

| gate | check_question | pass_signal | fail_signal | return_to | severity |
|---|---|---|---|---|---|
| volume_goal_progress | Does the chapter progress, delay, reverse, or price the volume goal? | Progress type is explicit and linked to volume card. | Chapter is busy but detached from volume goal. | Orchestrator | standard |
| reader_question_continuity | Are reader questions refreshed, delayed, or resolved cleanly? | Before and after questions are traceable. | Questions multiply without management. | Reviewer | standard |
| agency_clarity | Does the active character make a bounded choice? | Choice pressure, tactic, and cost are visible. | Character is only a reaction machine. | Scene Engine / Orchestrator | standard |
| foreshadow_payoff_tracking | Are seeds and payoffs tracked without free reward? | Payoff or delay has evidence and cost. | Reveal arrives without constraint or consequence. | Reviewer / StateManager | standard |
| narrator_overreach | Does narration avoid explaining outcomes before scene evidence? | Scene evidence carries the judgment. | Narrator certifies intent, emotion, or meaning too early. | Renderer | standard |
| hook_payoff_balance | Does hook pressure leave human or state consequence? | Hook is tied to debt, cost, or next friction. | Hook replaces character consequence. | Orchestrator / Renderer | standard |
