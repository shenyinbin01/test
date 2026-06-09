# Validation Plan

## Before Commit

Run from `production/longform/run003_c_engine_variants_v0/`:

```bash
python validation/yaml_check.py
bash validation/forbidden_grep.sh
```

Run from repo root:

```bash
git diff --check HEAD^ HEAD
git status --short
```

## Static Package Checks

- YAML files parse.
- No protected paths changed.
- No state_delta accepted status.
- No official ledger creation.
- No run002 modification.
- No skill-pack modification.
- No phase8 modification.

## After Hermes Generation

- Re-run YAML check.
- Re-run forbidden grep.
- Confirm generated prose contains no engineering leak terms.
- Confirm LLM reviewer did not choose winner.
- Confirm human blind materials are anonymized.
