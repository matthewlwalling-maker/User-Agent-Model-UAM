from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .blinding import load_or_create_key
from .config import ConfigError, load_config
from .exporter import build_evaluator_packets
from .fixtures import iter_cells, load_all_fixtures
from .orchestrator import doctor, plan, recover_attempt, run, usage_summary, validate_run


def _print(value) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mch", description="Minimum Composition authoritative comparison harness")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("doctor", "plan", "run", "validate-run"):
        p = sub.add_parser(name)
        p.add_argument("--config", required=True)
        if name == "doctor":
            p.add_argument("--require-provider-auth", action="store_true")
            p.add_argument("--require-api-key", action="store_true", help="Deprecated alias for --require-provider-auth")
        if name == "run":
            p.add_argument("--cases", help="Comma-separated case/cell IDs")
    rec = sub.add_parser("recover")
    rec.add_argument("--config", required=True)
    rec.add_argument("--attempt-id", required=True)
    rec.add_argument("--note", required=True)
    intervention = sub.add_parser("record-intervention")
    intervention.add_argument("--config", required=True)
    intervention.add_argument("--attempt-id", required=True)
    intervention.add_argument("--kind", required=True)
    intervention.add_argument("--note", required=True)
    intervention.add_argument("--tokens-added", type=int, default=0)
    intervention.add_argument("--latency-added-ms", type=int, default=0)
    sub.add_parser("usage-summary").add_argument("--config", required=True)
    exp = sub.add_parser("export-evaluator")
    exp.add_argument("--config", required=True)
    exp.add_argument("--full-fixtures", required=True)

    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        if args.command == "doctor":
            result = doctor(config, require_provider_auth=(args.require_provider_auth or args.require_api_key))
            _print(result)
            return 0 if result["ok"] else 2
        if args.command == "plan":
            _print(plan(config)); return 0
        if args.command == "run":
            cases = set(args.cases.split(",")) if args.cases else None
            result = run(config, cases=cases)
            payload = dict(result["completion"])
            payload["pause"] = result.get("pause")
            _print(payload)
            if result.get("pause"):
                return 4
            return 0 if result["completion"]["complete"] else 3
        if args.command == "validate-run":
            result = validate_run(config)
            _print(result)
            return 0 if result["complete"] else 3
        if args.command == "usage-summary":
            _print(usage_summary(config)); return 0
        if args.command == "recover":
            result = recover_attempt(config, args.attempt_id, note=args.note)
            _print(result); return 0 if result.get("status") == "completed" else 3
        if args.command == "record-intervention":
            from .storage import append_manual_intervention
            path = append_manual_intervention(config.run_root, {
                "attempt_id": args.attempt_id,
                "trigger": args.kind,
                "actor": "human",
                "change": "Custodian-recorded manual intervention; see reason.",
                "reason": args.note,
                "affected_attempt": args.attempt_id,
                "whether_behavioral_scoring_contaminated": True,
                "before_ref": args.attempt_id,
                "after_ref": None,
                "tokens_added": args.tokens_added,
                "latency_added_ms": args.latency_added_ms,
            })
            _print({"recorded": True, "path": str(path)}); return 0
        if args.command == "export-evaluator":
            fixtures = load_all_fixtures(config)
            cells = [(f.cell_id, c, r) for f, c, r in iter_cells(fixtures, config)]
            key = load_or_create_key(config.run_root / "private" / "system_key.json", cells, int(config.blinding.get("seed", 1)))
            paths = build_evaluator_packets(config, fixtures, key, Path(args.full_fixtures).resolve())
            _print({k: str(v) for k, v in paths.items()}); return 0
    except (ConfigError, FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
