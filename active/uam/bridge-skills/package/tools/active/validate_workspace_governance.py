#!/usr/bin/env python3
"""QC the workspace hierarchy and future file-placement controls.

This performs static governance validation only. It does not delete files,
stage Git changes, publish, install, activate, or upgrade evidence claims.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
WORKSPACE_ROOT = PACKAGE_ROOT.parent

ACTIVE_PACKAGE_ROOT = PACKAGE_ROOT / "skills" / "active" / "uam-bridge-skills"
COMMANDS_ROOT = ACTIVE_PACKAGE_ROOT / "commands"

COMMAND_DIRS = {
    "align-work",
    "build-artifact",
    "compare-decide",
    "design-solution",
    "diagnose-problem",
    "handoff-state",
    "research-evidence",
    "review-work",
}

SOURCE_AUTHORITY_CHANGELOG = PACKAGE_ROOT / "docs" / "governance" / "source-authority-change-log.md"

GOVERNANCE_FILES = [
    WORKSPACE_ROOT / "AGENTS.md",
    PACKAGE_ROOT / "skills" / "active" / "uam-bridge-skills" / "MANIFEST.yaml",
    PACKAGE_ROOT / "SKILL_REGISTRY.yaml",
    PACKAGE_ROOT / "TEST_REGISTRY.yaml",
    SOURCE_AUTHORITY_CHANGELOG,
    PACKAGE_ROOT / "docs" / "cleanup" / "folder-organization-map.md",
    PACKAGE_ROOT / "docs" / "cleanup" / "workspace-taxonomy-v2.md",
    PACKAGE_ROOT / "docs" / "cleanup" / "workspace-taxonomy-v2-migration-ledger.md",
    PACKAGE_ROOT / "docs" / "cleanup" / "final-workspace-cleanup-record-2026-06-22.md",
    PACKAGE_ROOT / "docs" / "publication" / "bridge-skills-master-repo-publication-plan.md",
    PACKAGE_ROOT / "docs" / "publication" / "github-master-repo-automation.md",
    PACKAGE_ROOT / "docs" / "install" / "stage-2-codex-dogfood-install-packet.md",
    PACKAGE_ROOT / "adapters" / "codex" / "README.md",
    PACKAGE_ROOT / "adapters" / "generic" / "README.md",
]

EXPECTED_TOKENS = {
    "active package root": "skills/active/uam-bridge-skills",
    "active command root": "skills/active/uam-bridge-skills/commands",
    "docs cleanup": "docs/cleanup",
    "docs governance": "docs/governance",
    "source authority changelog": "source-authority-change-log.md",
    "docs install": "docs/install",
    "docs protocols": "docs/protocols",
    "docs publication": "docs/publication",
    "tools active": "tools/active",
    "lenses active": "lenses/active",
    "tests suites": "tests/suites",
    "tests runs": "tests/runs",
    "exports generated": "exports/generated",
    "packets": "packets/",
}

STALE_PATTERNS = [
    re.compile(r"(?<!skills/active/)uam-bridge-skills/(KERNEL|MANIFEST|CHAIN_ROUTER)\.md\b"),
    re.compile(r"skills/active/(align-work|build-artifact|compare-decide|design-solution|diagnose-problem|handoff-state|research-evidence|review-work)/SKILL\.md\b"),
    re.compile(r"skills/<command-skill>/SKILL\.md\b"),
    re.compile(r"skills/\*/SKILL\.md\b"),
    re.compile(r"docs/chain-router-reference\.md\b"),
    re.compile(r"docs/dogfood-install/"),
]


def load_yaml_module() -> Any:
    try:
        import yaml  # type: ignore[import-not-found]
    except ModuleNotFoundError:
        print("Missing dependency: PyYAML. Run validate_yaml.py from the project venv first.", file=sys.stderr)
        raise SystemExit(2)
    return yaml


def check_exists(path: Path, label: str, errors: list[str]) -> None:
    if not path.exists():
        errors.append(f"{label} missing: {path}")


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing governance file: {path}")
    except UnicodeDecodeError as exc:
        errors.append(f"cannot decode governance file as UTF-8: {path}: {exc}")
    return ""


def check_manifest(yaml_module: Any, errors: list[str]) -> None:
    manifest_path = ACTIVE_PACKAGE_ROOT / "MANIFEST.yaml"
    check_exists(manifest_path, "active manifest", errors)
    if not manifest_path.exists():
        return

    manifest = yaml_module.safe_load(manifest_path.read_text(encoding="utf-8"))
    source_authority = manifest.get("source_authority", {})

    expected_source_paths = {
        "manifest_file": "skills/active/uam-bridge-skills/MANIFEST.yaml",
        "kernel_file": "skills/active/uam-bridge-skills/KERNEL.md",
        "router_reference_file": "skills/active/uam-bridge-skills/CHAIN_ROUTER.md",
        "skills_root": "skills/active/uam-bridge-skills/commands",
        "lenses_root": "lenses/active",
        "tests_root": "tests",
        "tools_root": "tools/active",
        "exports_root": "exports/generated",
    }
    for key, expected in expected_source_paths.items():
        actual = source_authority.get(key)
        if actual != expected:
            errors.append(f"manifest source_authority.{key} expected {expected}, found {actual}")
        check_exists(PACKAGE_ROOT / expected, f"manifest source_authority.{key}", errors)

    change_log = source_authority.get("governance_change_log")
    if change_log != "docs/governance/source-authority-change-log.md":
        errors.append(
            "manifest source_authority.governance_change_log expected "
            "docs/governance/source-authority-change-log.md, found "
            f"{change_log}"
        )
    check_exists(SOURCE_AUTHORITY_CHANGELOG, "source authority changelog", errors)

    for command in manifest.get("commands", []):
        path = command.get("path")
        if not isinstance(path, str) or not path.startswith("skills/active/uam-bridge-skills/commands/"):
            errors.append(f"manifest command path not under active command root: {path}")
        elif not (PACKAGE_ROOT / path).exists():
            errors.append(f"manifest command path missing: {path}")

    for name, path in manifest.get("tools", {}).items():
        tool_path = path.get("path") if isinstance(path, dict) else None
        if not isinstance(tool_path, str) or not tool_path.startswith("tools/active/"):
            errors.append(f"manifest tool {name} not under tools/active: {tool_path}")
        elif not (PACKAGE_ROOT / tool_path).exists():
            errors.append(f"manifest tool path missing: {tool_path}")


def check_registries(yaml_module: Any, errors: list[str]) -> None:
    skill_registry = yaml_module.safe_load((PACKAGE_ROOT / "SKILL_REGISTRY.yaml").read_text(encoding="utf-8"))
    if skill_registry["authority"].get("current_skills_root") != "skills/active/uam-bridge-skills/commands":
        errors.append("SKILL_REGISTRY authority.current_skills_root does not point to active command root")
    for skill in skill_registry.get("skills", []):
        path = skill.get("current_path")
        if not isinstance(path, str) or not path.startswith("skills/active/uam-bridge-skills/commands/"):
            errors.append(f"SKILL_REGISTRY current_path not under active command root: {path}")
        elif not (PACKAGE_ROOT / path).exists():
            errors.append(f"SKILL_REGISTRY current_path missing: {path}")

    test_registry = yaml_module.safe_load((PACKAGE_ROOT / "TEST_REGISTRY.yaml").read_text(encoding="utf-8"))
    if test_registry["authority"].get("current_root") != "tests":
        errors.append("TEST_REGISTRY authority.current_root does not point to tests")
    if test_registry["authority"].get("current_manifest_path") != "skills/active/uam-bridge-skills/MANIFEST.yaml":
        errors.append("TEST_REGISTRY current_manifest_path does not point to active skill package manifest")
    for suite in test_registry.get("suites", []):
        path = suite.get("current_path")
        if not isinstance(path, str) or not path.startswith("tests/suites/"):
            errors.append(f"TEST_REGISTRY suite not under tests/suites: {path}")
        elif not (PACKAGE_ROOT / path).exists():
            errors.append(f"TEST_REGISTRY suite path missing: {path}")


def check_governance_text(errors: list[str]) -> None:
    combined = ""
    for path in GOVERNANCE_FILES:
        combined += "\n" + read_text(path, errors)

    for label, token in EXPECTED_TOKENS.items():
        if token not in combined:
            errors.append(f"governance text missing future-placement token for {label}: {token}")

    for path in GOVERNANCE_FILES:
        text = read_text(path, errors)
        for pattern in STALE_PATTERNS:
            for match in pattern.finditer(text):
                errors.append(f"stale path reference in {path}: {match.group(0)}")


def check_source_authority_changelog(errors: list[str]) -> None:
    text = read_text(SOURCE_AUTHORITY_CHANGELOG, errors)
    required_tokens = [
        "Required Entry Fields",
        "AGENTS.md",
        "UAM_Artifact_Index.yaml",
        "skills/active/uam-bridge-skills/MANIFEST.yaml",
        "skills/active/uam-bridge-skills/KERNEL.md",
        "skills/active/uam-bridge-skills/CHAIN_ROUTER.md",
        "skills/active/uam-bridge-skills/commands/*/SKILL.md",
        "SKILL_REGISTRY.yaml",
        "TEST_REGISTRY.yaml",
        "archive_ref",
        "validation",
        "evidence_ceiling",
        "2026-06-23-source-authority-change-log-created",
    ]
    for token in required_tokens:
        if token not in text:
            errors.append(f"source authority changelog missing required token: {token}")


def check_export_and_publish_tools(errors: list[str]) -> None:
    export_tool = PACKAGE_ROOT / "tools" / "active" / "export_relevant_files.ps1"
    publish_tool = PACKAGE_ROOT / "tools" / "active" / "publish_bridge_skills_to_master_repo.ps1"
    check_exists(export_tool, "export helper", errors)
    check_exists(publish_tool, "master repo publisher", errors)

    export_text = read_text(export_tool, errors)
    if 'exports\\generated' not in export_text and "exports/generated" not in export_text:
        errors.append("export helper default destination does not point to exports/generated")
    if "skills/active/uam-bridge-skills/commands" not in export_text:
        errors.append("export helper does not export active command package paths")

    publish_text = read_text(publish_tool, errors)
    if "https://github.com/matthewlwalling-maker/User-Agent-Model-UAM.git" not in publish_text:
        errors.append("publisher missing default master repo URL")
    if "PUSH UAM BRIDGE SKILLS TO MASTER" not in publish_text:
        errors.append("publisher missing explicit push confirmation guard")
    if "active/uam/bridge-skills" not in publish_text:
        errors.append("publisher missing active master repo root")
    if "validate_workspace_governance.py" not in publish_text or "validate_yaml.py" not in publish_text:
        errors.append("publisher does not run source validation before publication")
    if "workspace_agents_path" not in publish_text or "AGENTS.md" not in publish_text:
        errors.append("publisher missing Bridge-specific AGENTS.md publication")
    if "workspace_authority_root" not in publish_text or "authority" not in publish_text:
        errors.append("publisher missing workspace authority root publication")
    if "UAM_Artifact_Index.yaml" not in publish_text:
        errors.append("publisher missing UAM_Artifact_Index.yaml authority publication")
    if "UAM_Artifact_Naming_and_Archive_Convention.md" not in publish_text:
        errors.append("publisher missing naming/archive convention authority publication")


def check_filesystem_shape(errors: list[str], warnings: list[str]) -> None:
    check_exists(ACTIVE_PACKAGE_ROOT / "KERNEL.md", "active package KERNEL.md", errors)
    check_exists(ACTIVE_PACKAGE_ROOT / "MANIFEST.yaml", "active package MANIFEST.yaml", errors)
    check_exists(ACTIVE_PACKAGE_ROOT / "CHAIN_ROUTER.md", "active package CHAIN_ROUTER.md", errors)
    for command in COMMAND_DIRS:
        check_exists(COMMANDS_ROOT / command / "SKILL.md", f"active command {command}", errors)

    for old_anchor in ["KERNEL.md", "MANIFEST.yaml", "CHAIN_ROUTER.md"]:
        if (PACKAGE_ROOT / old_anchor).exists():
            errors.append(f"old package-root anchor still exists: {old_anchor}")

    evals_dir = PACKAGE_ROOT / "evals"
    if evals_dir.exists():
        entries = list(evals_dir.iterdir())
        if entries:
            errors.append("evals/ exists and is not empty; active eval/test material must live under tests/")
        else:
            warnings.append("evals/ exists as an empty delete-gated compatibility placeholder")


def main() -> int:
    yaml_module = load_yaml_module()
    errors: list[str] = []
    warnings: list[str] = []

    check_filesystem_shape(errors, warnings)
    check_manifest(yaml_module, errors)
    check_registries(yaml_module, errors)
    check_governance_text(errors)
    check_source_authority_changelog(errors)
    check_export_and_publish_tools(errors)

    if errors:
        print(f"WORKSPACE_GOVERNANCE_QC_FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        for error in errors:
            print(f"- ERROR: {error}")
        for warning in warnings:
            print(f"- WARNING: {warning}")
        return 1

    print(f"WORKSPACE_GOVERNANCE_QC_PASSED: 0 error(s), {len(warnings)} warning(s)")
    for warning in warnings:
        print(f"- WARNING: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
