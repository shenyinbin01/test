# LLM Checklist Only Gate

The LLM reviewer cannot output the winning variant and cannot decide by total score. It may only flag checklist issues.

## Checklist Flags

- engineering term leaks
- manual/process feel
- visible technique
- character as task executor
- weak conflict
- missing misread
- missing shame or face cost
- missing subtext
- report-like ending
- no reader decompression room
- raw packet field names visible
- relationship change explained rather than felt
- scene heat replaced by shouting or summary

## Output

Use:

```yaml
llm_checklist:
  sample_id: ""
  flags:
    - ""
  severity: low|medium|high
  suggested_return_layer: c_engine|renderer_v2|human_eval
  cannot_choose_winner: true
```

The final preference remains human blind pairwise evaluation.
