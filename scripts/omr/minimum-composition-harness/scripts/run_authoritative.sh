#!/usr/bin/env bash
set -euo pipefail
CONFIG="${1:-configs/run_series.yaml}"
mch doctor --config "$CONFIG"
mch plan --config "$CONFIG"
mch run --config "$CONFIG"
mch validate-run --config "$CONFIG"
