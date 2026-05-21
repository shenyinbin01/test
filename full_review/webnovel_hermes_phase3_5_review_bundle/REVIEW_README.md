# Webnovel Hermes Phase 3.5 — Review Bundle

## Purpose
Converge Phase 3 real DeepSeek outputs back to the fixed seed canon of 《人生价格标签》.

## Scope
- Add canon_constraints.yaml — formal constraint file for the novel's core setting
- Inject canon into 3 prompts (story_bible, chapter_beat, humanize)
- Modify run_demo.py to load, inject, and verify canon in real mode
- Add validate_canon_consistency.py — rules-based forbidden-word & anchor check
- Enhance validate_phase3.py to verify canon_consistency_report.json and prompt_inputs

## Results
| Measure | Status |
|---------|--------|
| Code changes (7 files) | ✅ Complete |
| Mock verification | ✅ Passed (exit 0) |
| Real DeepSeek calls | ✅ 3/3 successful |
| Canon consistency | ⚠️ **Partially passed** — story_bible ✅, chapter_beat ❌ (found "生命倒计时") |
| WPS dry-run safety | ✅ Passed |
| Security scan | ✅ No leaks found |

## Key Files
| File | Description |
|------|-------------|
| `canon_constraints.yaml` | Canon constraint file for 《人生价格标签》 |
| `validate_canon_consistency.py` | Rules-based canon consistency checker |
| `phase3_5_result.md` | Full execution report |

## Known Issues
1. chapter_beat_real.md still contains "生命倒计时" — prompt constraints need strengthening
2. canon_constraints.yaml content is stored in input snapshots but not yet inlined into the actual DeepSeek request payload by call_deepseek.py
3. Rule checks are keyword-level only; semantic drift may still occur
