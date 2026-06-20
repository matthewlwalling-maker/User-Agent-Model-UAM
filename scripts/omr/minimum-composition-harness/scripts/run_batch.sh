#!/usr/bin/env bash
set -euo pipefail
CONFIG="${1:-configs/run_series.yaml}"
CASES="${2:?Usage: scripts/run_batch.sh <config> <comma-separated-cases>}"
mch doctor --config "$CONFIG" --require-provider-auth
mch plan --config "$CONFIG"
set +e
mch run --config "$CONFIG" --cases "$CASES"
code=$?
set -e
mch usage-summary --config "$CONFIG"
if [[ $code -eq 4 ]]; then
  printf 'Codex usage window exhausted. Re-run the same batch after reset or credits.\n'
  exit 4
fi
if [[ $code -eq 3 ]]; then
  printf 'Batch completed; the full series remains incomplete. Continue with the next batch.\n'
  exit 0
fi
exit "$code"
