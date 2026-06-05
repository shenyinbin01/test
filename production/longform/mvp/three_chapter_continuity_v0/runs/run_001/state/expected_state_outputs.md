# Expected State Outputs

If actual run_001 execution is approved, expected files are:

- `state_delta_ch001.yaml`
- `state_delta_ch002.yaml`
- `state_delta_ch003.yaml`
- `ledger_view_after_ch003.yaml`

## Requirements

- Chapter 2 must read accepted `state_delta_ch001.yaml`.
- Chapter 3 must read accepted `state_delta_ch002.yaml`.
- `ledger_view_after_ch003.yaml` must be built only from accepted deltas.
- Conflict or needs-human-review deltas must remain outside reducers.
