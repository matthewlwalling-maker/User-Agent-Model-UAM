from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import yaml

from .config import RunConfig
from .util import sha256_file


@dataclass(frozen=True)
class Fixture:
    cell_id: str
    case_id: str
    title: str
    public: dict[str, Any]

    @property
    def asset(self) -> str | None:
        val = self.public.get("asset")
        return str(val) if val is not None else None

    @property
    def asset_version(self) -> str | None:
        val = self.public.get("asset_version")
        return str(val) if val is not None else None

    @property
    def evidence_stage(self) -> str:
        return str(self.public.get("evidence_stage", "design-time"))


def load_executor_fixtures(path: Path) -> list[Fixture]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    fixtures: list[Fixture] = []
    for case in raw.get("fixtures", []):
        base = dict(case.get("executor_view", {}))
        variants = case.get("variants") or []
        if variants:
            for variant in variants:
                merged = dict(base)
                merged.update(variant.get("executor_view", {}))
                fixtures.append(
                    Fixture(
                        cell_id=str(variant["id"]),
                        case_id=str(case["id"]),
                        title=f"{case['title']} — {variant.get('name', variant['id'])}",
                        public=merged,
                    )
                )
        else:
            fixtures.append(Fixture(str(case["id"]), str(case["id"]), str(case["title"]), base))
    return fixtures


def _load_holdout(kind: str, asset_path: Path, selection_path: Path) -> Fixture:
    if not asset_path.exists():
        raise FileNotFoundError(f"Missing {kind} holdout asset: {asset_path}")
    if not selection_path.exists():
        raise FileNotFoundError(f"Missing {kind} holdout selection record: {selection_path}")
    asset_text = asset_path.read_text(encoding="utf-8")
    selection = yaml.safe_load(selection_path.read_text(encoding="utf-8")) or {}
    required = ["user_request", "goal_constraints", "evidence_stage", "asset_version"]
    missing = [k for k in required if k not in selection]
    if missing:
        raise ValueError(f"{kind} holdout selection record missing {missing}")
    public = {
        "user_request": selection["user_request"],
        "goal_constraints": selection["goal_constraints"],
        "evidence_stage": selection["evidence_stage"],
        "asset_version": selection["asset_version"],
        "asset": asset_text,
        "holdout_selection_record": selection,
        "holdout_asset_sha256": sha256_file(asset_path),
        "holdout_selection_sha256": sha256_file(selection_path),
    }
    cell = "HOLDOUT-MATERIAL-01" if kind == "material" else "HOLDOUT-TRIVIAL-01"
    return Fixture(cell, cell, f"Unseen {kind.title()} holdout", public)


def load_all_fixtures(config: RunConfig) -> list[Fixture]:
    fixtures = load_executor_fixtures(config.fixture_view)
    holdouts = config.raw.get("holdouts", {})
    if holdouts.get("required", False):
        for kind in ("material", "trivial"):
            data = holdouts[kind]
            fixtures.append(_load_holdout(kind, config.resolve(data["asset_file"]), config.resolve(data["selection_record_file"])))
    requested = config.execution.get("cases", "all")
    if requested != "all":
        wanted = set(requested)
        fixtures = [f for f in fixtures if f.cell_id in wanted or f.case_id in wanted]
    return fixtures


def conditions_for(fixture: Fixture, config: RunConfig) -> list[str]:
    dual = set(config.execution.get("dual_condition_cells", []))
    enabled = config.execution.get("conditions", {})
    if fixture.cell_id in dual or fixture.case_id in dual:
        out = []
        if enabled.get("packet_boundary", True):
            out.append("PB")
        if enabled.get("separate_context", True):
            out.append("SC")
        return out
    return ["standard"] if enabled.get("standard", True) else ["PB"]


def iter_cells(fixtures: Iterable[Fixture], config: RunConfig):
    reps = int(config.execution.get("replicates_per_cell", 1))
    for fixture in fixtures:
        for condition in conditions_for(fixture, config):
            for replicate in range(1, reps + 1):
                yield fixture, condition, replicate
