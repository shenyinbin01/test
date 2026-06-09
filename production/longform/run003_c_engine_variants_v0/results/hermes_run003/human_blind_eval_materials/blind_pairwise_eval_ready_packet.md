# Human Blind Pairwise Evaluation — Ready Packet

## Status

Run003 prose generation is complete. Four variants (C0, C1, C2, C3) × three chapters each = 12 draft files. All outputs are ready for human blind pairwise evaluation.

## Important

- **LLM reviewer did not choose a winner.**
- **No variant is accepted by Hermes.**
- **No state_delta is accepted by Hermes.**
- **No official ledger is created by Hermes.**
- **Human blind pairwise evaluation is required.**

## Anonymized Sample Map

Each variant's three chapters have been placed in anonymized directories under `anonymized_samples/`:

| Anonymized ID | Actual Variant | Chapters |
|---------------|----------------|----------|
| V_A | C0_current_c_anchor | chapter_001, chapter_002, chapter_003 |
| V_B | C1_private_deep_fields | chapter_001, chapter_002, chapter_003 |
| V_C | C2_exemplar_distillation | chapter_001, chapter_002, chapter_003 |
| V_D | C3_hybrid_harness | chapter_001, chapter_002, chapter_003 |

## Pairwise Evaluation Matrix

Recommended head-to-head comparisons:

1. V_D vs V_A (C3 vs C0) — primary comparison
2. V_B vs V_A (C1 vs C0) — field contribution test
3. V_C vs V_A (C2 vs C0) — exemplar contribution test
4. V_D vs V_B (C3 vs C1) — exemplar additive value
5. V_D vs V_C (C3 vs C2) — field additive value

## Evaluation Criteria

For each pair, evaluator should answer:

1. **Reader pull**: Which chapter makes you more likely to continue reading?
2. **Anti-AI surface**: Which chapter reads less like machine-generated text?
3. **Character alive**: Which protagonist feels more like a person with desires, fears, and flaws?
4. **Scene heat**: Which scenes have more pressure, tension, and irreversible stakes?
5. **Overall preference**: Taking all factors into account, which variant do you prefer?

## Blind Protocol

- Evaluator must not know which variant ID maps to which actual variant.
- The mapping key is stored in `pair_map_private.yaml` (not to be shared with evaluator).
- Results should be recorded as preference counts per pair.
- After all comparisons, the map can be de-anonymized to compute C3 vs C0 preference ratio.

## Target Threshold

C3 must beat C0 in ≥60% of evaluator preferences to be considered a meaningful improvement.
