# Webnovel Hermes Phase 3.5 Fix — Review Bundle

## Purpose
Force canon constraints into the actual DeepSeek request messages (system + user), not just input snapshots. Re-converge chapter_beat output.

## Changes
1. `call_deepseek.py` — Added `--canon-text` and `--hard-rules` args; injects canon into system message tail and user message head
2. `run_demo.py` — `render_canon_text_block()`, `render_chapter_beat_hard_rules()`, retry mechanism
3. `chapter_beat.md` — Added forbidden examples, correct examples, strict self-check sections
4. `validate_canon_consistency.py` — Forbidden hits now go to `errors` as structured objects
5. `validate_phase3.py` — Checks `canon_injected`, `hard_rules_injected`, rendered preview markers

## Results
| Measure | Status |
|---------|--------|
| canon injected into system+user messages | ✅ |
| chapter_beat actual content clean (no "生命倒计时") | ✅ |
| All 3 DeepSeek real calls successful | ✅ |
| Canon consistency — automated check | ⚠️ 2 false positives ("not 倒计时", "请充值" in hospital billing) |
| validate_phase3 real | 🔴 Blocked by canon check |
| Security scan | ✅ No leaks |

## Key Files
| File | Description |
|------|-------------|
| `phase3_5_fix_result.md` | Full fix execution report |
| `chapter_beat_real.md` | Converged chapter beat (no "生命倒计时") |
| `chapter_beat_input.json` | Shows canon_injected=true, hard_rules_injected=true, rendered previews |
| `canon_consistency_report.json` | 2 false positive errors |
