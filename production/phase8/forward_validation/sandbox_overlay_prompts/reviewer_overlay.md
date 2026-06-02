# Reviewer Overlay — Phase 8 Sandbox Injection

> **TEMPORARY**. Do not modify production `webnovel_reviewer` skill.

---

## Injected Patterns

### DCQG-C005: 短钩快兑，长钩慢兑 (Hook Payoff Pacing)
**Audit rule**: Check hook-payoff rhythm:
- Short hooks (chapter-level questions): pay off within 1-2 chapters
- Long hooks (arc-level mysteries): delay payoff, show progress markers
- Flag: if a short hook goes unpaid for 3+ chapters

### DCQG-C013: 情感锚点 (Emotional Anchor)
**Audit rule**: Each chapter must have at least ONE emotional anchor moment — a beat of warmth, protection, or human connection that grounds the reader.
- Flag: if the chapter is all action/intrigue with zero emotional grounding

### DCQG-C018: 喜剧调剂 (Comedy Relief)
**Audit rule**: Check tonal variety. Continuous tension without relief fatigues readers.
- Flag: if the chapter has zero moments of lightness, irony, or humor

### DCQG-C020: 终极代价与取舍 (Ultimate Cost)
**Audit rule**: Verify that the internal pressure/stakes established in the Planner phase are visible in the draft.
- Flag: if "precognition cost" is mentioned but never felt by the reader

---

## Review Dimensions (standard Phase 7 + overlay injections)

Evaluate across these dimensions:
1. **Cognitive advantage visibility**: Is the 10-second precognition SHOWN or just TOLD?
2. **Hook pacing**: Short/long hook distribution
3. **Emotional anchor**: Warmth/connection beat exists?
4. **Tonal variety**: Comedy/relief moment exists?
5. **Cost visibility**: Is the precognition cost FELT?

Output `validation_review.md` with rewrite_instructions.
