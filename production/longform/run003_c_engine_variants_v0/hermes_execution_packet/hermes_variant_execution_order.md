# Hermes Variant Execution Order

Execute in this exact order:

1. C0_current_c_anchor
2. C1_private_deep_fields
3. C2_exemplar_distillation
4. C3_hybrid_harness

## Reason

C0 establishes the current-C anchor. C1 isolates private deep field effect. C2 isolates exemplar effect. C3 tests the combined harness.

## Isolation Rule

Do not use later variant outputs to improve earlier variants. Do not copy prose across variants. Do not change input contracts after a variant begins.
