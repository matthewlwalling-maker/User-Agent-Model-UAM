#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.lock
pip install -e . --no-deps
printf 'Setup complete. Activate with: source .venv/bin/activate\n'
