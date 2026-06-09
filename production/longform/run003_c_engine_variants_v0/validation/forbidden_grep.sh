#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "FORBIDDEN_GREP_ROOT=$ROOT"

changed_forbidden="$(git -C "$ROOT/../../.." diff --name-only HEAD^ HEAD 2>/dev/null | grep -E '(^|/)skill-pack/|production/phase8|approved_patterns|(^|/)tmp/|deepcode_notify|runs/run_002_hermes_abc' || true)"
if [[ -n "$changed_forbidden" ]]; then
  echo "FORBIDDEN_CHANGED_PATHS"
  echo "$changed_forbidden"
  exit 1
fi

if grep -RIn --include='*.yaml' --include='*.yml' 'status:[[:space:]]*accepted' "$ROOT" >/tmp/run003_status_accepted_hits.txt; then
  echo "FORBIDDEN_STATUS_ACCEPTED"
  cat /tmp/run003_status_accepted_hits.txt
  exit 1
fi

if grep -RIn --include='*.yaml' --include='*.yml' 'official_ledger_created:[[:space:]]*true' "$ROOT" >/tmp/run003_official_ledger_hits.txt; then
  echo "FORBIDDEN_OFFICIAL_LEDGER"
  cat /tmp/run003_official_ledger_hits.txt
  exit 1
fi

RESULTS_DIR="$ROOT/results"
if [[ -d "$RESULTS_DIR" ]]; then
  prose_hits="$(grep -RIn --include='*_draft.md' -E 'Orchestrator|state_delta|ledger|agency_choice|scene_pressure_packet|character_pressure_packet|relationship_debt_change|reader_question_change|event_log|this chapter needs|the reader will|this is relationship debt|this is the third choice|this represents character agency' "$RESULTS_DIR" || true)"
  if [[ -n "$prose_hits" ]]; then
    echo "FORBIDDEN_PROSE_LEAKS"
    echo "$prose_hits"
    exit 1
  fi
else
  echo "NO_RESULTS_DIR_YET_STATIC_PACKAGE_ONLY"
fi

echo "FORBIDDEN_GREP_OK"
