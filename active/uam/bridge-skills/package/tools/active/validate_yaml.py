#!/usr/bin/env python3
"""Validate YAML syntax and lightweight test fixture structure.

This script performs static source validation only. It parses YAML files and
checks test fixture shape; it does not run prompts, score model outputs, update
release status, or create eval evidence beyond local syntax/schema inspection.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys
from typing import Any


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_DIR_NAMES = {"__pycache__"}
TEST_SUITE_REQUIRED_KEYS = ("suite_id", "version", "evidence_stage", "cases")


class ValidationError:
    def __init__(self, path: Path, message: str) -> None:
        self.path = path
        self.message = message


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def iter_yaml_files(root: Path, include_exports: bool) -> list[Path]:
    paths: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".yaml", ".yml"}:
            continue
        parts = set(path.relative_to(root).parts)
        if EXCLUDED_DIR_NAMES & parts:
            continue
        if not include_exports and "exports" in parts:
            continue
        paths.append(path)
    return sorted(paths)


def load_yaml_module() -> Any:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        print(
            "Missing dependency: PyYAML. Install dev dependencies with "
            "`python -m pip install -r uam-bridge-skills/requirements-dev.txt` "
            "from the workspace root.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return yaml


def load_documents(paths: list[Path], yaml_module: Any) -> tuple[dict[Path, Any], list[ValidationError]]:
    documents: dict[Path, Any] = {}
    errors: list[ValidationError] = []

    for path in paths:
        try:
            documents[path] = yaml_module.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:  # PyYAML exposes several parse exception types.
            errors.append(ValidationError(path, f"YAML parse error: {exc}"))

    return documents, errors


def validate_test_suite(path: Path, document: Any) -> tuple[int, list[ValidationError]]:
    errors: list[ValidationError] = []

    if not isinstance(document, dict) or "cases" not in document:
        return 0, errors

    for key in TEST_SUITE_REQUIRED_KEYS:
        if key not in document:
            errors.append(ValidationError(path, f"test suite missing top-level key: {key}"))

    cases = document.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append(ValidationError(path, "test suite `cases` must be a non-empty list"))
        return 0, errors

    case_ids: list[str] = []
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(ValidationError(path, f"case #{index} must be a mapping"))
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(ValidationError(path, f"case #{index} missing non-empty string `id`"))
            continue
        case_ids.append(case_id)

    duplicates = sorted(case_id for case_id, count in Counter(case_ids).items() if count > 1)
    for case_id in duplicates:
        errors.append(ValidationError(path, f"duplicate case id in suite: {case_id}"))

    return len(case_ids), errors


def validate_documents(root: Path, documents: dict[Path, Any]) -> tuple[int, int, list[ValidationError]]:
    suite_count = 0
    case_count = 0
    errors: list[ValidationError] = []

    for path, document in documents.items():
        if document is None:
            errors.append(ValidationError(path, "YAML document is empty"))
            continue
        if path.is_relative_to(root / "tests" / "suites"):
            parsed_cases, suite_errors = validate_test_suite(path, document)
            if isinstance(document, dict) and "cases" in document:
                suite_count += 1
                case_count += parsed_cases
            errors.extend(suite_errors)

    return suite_count, case_count, errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate UAM Bridge Skills YAML syntax and test fixture structure."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=PACKAGE_ROOT,
        help="Package root to validate. Defaults to the uam-bridge-skills package root.",
    )
    parser.add_argument(
        "--include-exports",
        action="store_true",
        help="Also validate generated export snapshots under the exports directory.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if not root.exists():
        print(f"Root does not exist: {root}", file=sys.stderr)
        return 2

    yaml_module = load_yaml_module()
    yaml_files = iter_yaml_files(root, include_exports=args.include_exports)
    documents, parse_errors = load_documents(yaml_files, yaml_module)
    suite_count, case_count, schema_errors = validate_documents(root, documents)
    errors = parse_errors + schema_errors

    if errors:
        print(
            f"YAML validation failed: {len(errors)} error(s), "
            f"{len(documents)}/{len(yaml_files)} file(s) parsed."
        )
        for error in errors:
            print(f"- {relative(error.path, root)}: {error.message}")
        return 1

    print(
        "YAML validation passed: "
        f"{len(yaml_files)} file(s) parsed, "
        f"{suite_count} test suite(s) checked, "
        f"{case_count} case id(s) checked."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
