# Output Path Lock

All future run_001 artifacts may be written only under:

```text
production/longform/mvp/three_chapter_continuity_v0/runs/run_001/
```

## Allowed Areas

- `input/`
- `orchestrator/`
- `generation/`
- `review/`
- `state/`
- `reports/`
- `approval/`

## Forbidden Write Targets

- `skill-pack/`
- `production/phase8/`
- approved pattern stores
- repository root loose files
- any other run directory
- raw corpus directories
- original text material directories

## Enforcement

If a future execution attempts to write outside the allowed root, stop the run and report the attempted path.
