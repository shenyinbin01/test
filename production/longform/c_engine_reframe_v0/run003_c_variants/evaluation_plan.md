# Evaluation Plan

## Main Evaluation

The main evaluation is human blind pairwise preference.

The evaluator should not see variant names, architecture notes, scores, packets, or engineering labels.

## Pairwise Questions

Ask which version:

- is more like fiction and less like process,
- feels less AI-written,
- makes the character feel like they can only choose this flawed tactic,
- has stronger scene heat,
- makes the reader want the next chapter,
- has fewer technique traces,
- explains itself less,
- makes relationship change felt,
- leaves more room for reader decompression.

## LLM Role

LLM reviewer is checklist-only. It flags leaks and obvious failure modes. It cannot output the winner, cannot decide by total score, and cannot replace blind human preference.

## Required Comparisons

- C3 vs C0
- C3 vs C1
- C3 vs C2
- C1 vs C0
- C2 vs C0

C0 remains an anchor, not a final target.
