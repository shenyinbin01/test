# C Engine Architecture

The rebuilt C Engine has no more than eight modules.

| Module | Purpose | Inputs | Outputs | Private Or Public | Enters Prose Prompt | Failure Modes | Reviewer Checks |
|---|---|---|---|---|---|---|---|
| author_intent_compressor | Compress abstract intent into scene-level reader effect | volume card, chapter card, reader question | author_intent_card, intended reader feeling | Private | No raw card; compiled brief only | Theme explained directly; intent becomes slogan | Does prose show effect without naming intent? |
| character_pressure_modeler | Model why the focal character cannot choose cleanly | chapter objective, relation ledger, knowledge boundary | character_pressure_packet | Private | No raw packet | Desire as label; choice as task execution | Does choice contain want, fear, shame/misbelief, cost? |
| relationship_debt_modeler | Convert ledger debt into felt leverage | ledger preview, previous scene outcomes | debt pressure note, next friction | Private | Compiled brief only | Debt explained as accounting; no behavior change | Is debt visible through withholding, delay, concession, avoidance? |
| scene_heat_orchestrator | Build obstacle, counter-tactic, subtext, escalation | chapter beat, character pressure, opposition pressure | scene_heat_card | Private | Compiled brief only | Heat becomes shouting; no turn; conflict ornamental | Is there an irreversible mark after the scene? |
| reader_decompression_designer | Decide what readers infer and what remains unsaid | reader question ledger, knowledge gaps | reader_decompression_card | Private | Compiled brief only | Explains mystery; leaves no emotional room | Does reader know enough to worry but not enough to close? |
| narrative_stance_controller | Define focal distance, narrator judgment, detail bias | focal character, scene heat, intended feeling | narrative_stance_brief | Safe public brief | Yes, as natural terms | Style command too abstract; narrator moralizes | Does stance shape selection without explaining? |
| prose_renderer_v2 | Render prose from safe briefs | natural scene brief, stance brief, safe continuity, exemplars | draft prose | Public execution | Yes | Adds engineering notes; changes state; decorative prose | Does prose preserve function and avoid leak terms? |
| anti_technique_visibility_reviewer | Catch visible machinery before human review | draft prose, safe contracts, hidden packet checklist | pass/fail notes | Private review | No | Rewards compliance over readability | Does it flag process feel and field leakage? |
