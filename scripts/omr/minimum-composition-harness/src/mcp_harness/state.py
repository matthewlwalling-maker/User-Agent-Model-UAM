from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Any

from .schemas import SchemaRegistry
from .util import deep_remove_key, sha256_object, utc_now


KINDS = ["GoalContract", "CapabilityModel", "EvidenceLedger", "CoverageMap", "ChangeDecision"]


def object_ref(obj: dict[str, Any]) -> dict[str, Any]:
    m = obj["meta"]
    return {
        "object_id": m["object_id"],
        "object_kind": m["object_kind"],
        "revision": m["revision"],
        "branch_id": m["branch_id"],
        "content_hash": m["content_hash"],
    }


def compute_object_hash(obj: dict[str, Any]) -> str:
    cloned = copy.deepcopy(obj)
    if "meta" in cloned:
        cloned["meta"]["content_hash"] = ""
    return sha256_object(cloned)


def finalize_hash(obj: dict[str, Any]) -> dict[str, Any]:
    obj = copy.deepcopy(obj)
    obj["meta"]["content_hash"] = compute_object_hash(obj)
    return obj


def metadata(
    *, object_id: str, kind: str, revision: int, branch: str, producer: str,
    projection: str, parent_refs: list[dict[str, Any]] | None = None,
    evidence_refs: list[str] | None = None, status: str = "committed", freshness: str = "current",
) -> dict[str, Any]:
    return {
        "object_id": object_id,
        "object_kind": kind,
        "schema_version": "mcp-0.1",
        "revision": revision,
        "status": status,
        "freshness": freshness,
        "branch_id": branch,
        "parent_refs": parent_refs or [],
        "producer": producer,
        "evidence_refs": evidence_refs or [],
        "conflict_refs": [],
        "projection": projection,
        "created_at": utc_now(),
        "content_hash": "0" * 64,
    }


@dataclass
class StateStore:
    schema: SchemaRegistry
    attempt_id: str
    projection: str = "material"
    objects: dict[str, list[dict[str, Any]]] = field(default_factory=lambda: {k: [] for k in KINDS})
    incoming_invalid: list[dict[str, Any]] = field(default_factory=list)

    def current(self, kind: str, branch: str = "main") -> dict[str, Any] | None:
        candidates = [o for o in self.objects[kind] if o["meta"]["branch_id"] == branch and o["meta"]["freshness"] == "current"]
        return max(candidates, key=lambda o: o["meta"]["revision"], default=None)

    def currents(self, kind: str) -> list[dict[str, Any]]:
        by_branch: dict[str, dict[str, Any]] = {}
        for obj in self.objects[kind]:
            if obj["meta"]["freshness"] != "current":
                continue
            branch = obj["meta"]["branch_id"]
            if branch not in by_branch or obj["meta"]["revision"] > by_branch[branch]["meta"]["revision"]:
                by_branch[branch] = obj
        return list(by_branch.values())

    def add(self, obj: dict[str, Any], validate: bool = True) -> None:
        kind = obj["meta"]["object_kind"]
        if validate:
            errors = self.schema.validate_state(obj, kind)
            if errors:
                raise ValueError(f"Invalid {kind}: {errors}")
        self.objects[kind].append(copy.deepcopy(obj))

    def next_revision(self, kind: str, branch: str) -> int:
        vals = [o["meta"]["revision"] for o in self.objects[kind] if o["meta"]["branch_id"] == branch]
        return max(vals, default=0) + 1

    def invalidate_downstream(self, kind: str) -> None:
        mapping = {
            "GoalContract": ["CapabilityModel", "CoverageMap", "ChangeDecision"],
            "CapabilityModel": ["CoverageMap", "ChangeDecision"],
            "CoverageMap": ["ChangeDecision"],
            "EvidenceLedger": [],
            "ChangeDecision": [],
        }
        for target in mapping[kind]:
            for obj in self.objects[target]:
                if obj["meta"]["freshness"] == "current":
                    obj["meta"]["freshness"] = "stale"

    def ledger(self) -> dict[str, Any]:
        obj = self.current("EvidenceLedger")
        if obj is None:
            raise RuntimeError("EvidenceLedger not initialized")
        return obj

    def append_evidence(self, entries: list[dict[str, Any]], producer: str) -> dict[str, Any]:
        if not entries:
            return self.ledger()
        errors = self.schema.validate_evidence_entries(entries)
        if errors:
            raise ValueError(f"Invalid ledger append: {errors}")
        prior = self.ledger()
        seen = {e["evidence_id"] for e in prior["entries"]}
        dup = [e["evidence_id"] for e in entries if e["evidence_id"] in seen]
        if dup:
            raise ValueError(f"Evidence IDs already exist: {dup}")
        new = copy.deepcopy(prior)
        new["meta"] = metadata(
            object_id=prior["meta"]["object_id"], kind="EvidenceLedger",
            revision=prior["meta"]["revision"] + 1, branch=prior["meta"]["branch_id"],
            producer=producer, projection=prior["meta"]["projection"], parent_refs=[object_ref(prior)],
            evidence_refs=[e["evidence_id"] for e in entries],
        )
        new["entries"].extend(copy.deepcopy(entries))
        new["append_only_from_revision"] = prior["meta"]["revision"]
        new = finalize_hash(new)
        self.objects["EvidenceLedger"].append(new)
        return new

    def snapshots(self) -> dict[str, Any]:
        return copy.deepcopy(self.objects)


def seed_ledger(attempt_id: str, fixture: dict[str, Any], projection: str) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    target = fixture.get("asset_version") or attempt_id

    def add(eid: str, source_ref: str, source_type: str, statement: str, polarity: str = "supports", asset_version: str | None = None):
        scope = {"asset_or_target_ref": str(target), "branch_id": "main"}
        if asset_version:
            scope["asset_version"] = asset_version
        entries.append({
            "evidence_id": eid,
            "source_ref": source_ref,
            "source_type": source_type,
            "stage": str(fixture.get("evidence_stage", "design-time")),
            "statement": statement,
            "claim_refs": [],
            "polarity": polarity,
            "scope": scope,
            "limitations": ["Executor fixture evidence only; no higher-stage observation implied."],
            "recorded_by": "external-intake",
        })

    add("EV-REQUEST", "fixture.user_request", "user-request", str(fixture.get("user_request", "Assessment requested.")))
    for i, constraint in enumerate(fixture.get("goal_constraints", []) or [], 1):
        add(f"EV-CONSTRAINT-{i}", f"fixture.goal_constraints[{i-1}]", "user-request", str(constraint))
    if fixture.get("asset") is not None:
        add("EV-ASSET", "fixture.asset", "asset-text", str(fixture["asset"]), asset_version=str(fixture.get("asset_version", "unknown")))
    if fixture.get("dependency_map") is not None:
        add("EV-DEPENDENCY", "fixture.dependency_map", "dependency-map", str(fixture["dependency_map"]), asset_version=str(fixture.get("asset_version", "unknown")))
    if fixture.get("initial_state") is not None:
        add("EV-INITIAL-STATE", "fixture.initial_state", "governing-source", str(fixture["initial_state"]), polarity="context-only")
    meta = metadata(
        object_id=f"EL-{attempt_id}", kind="EvidenceLedger", revision=1, branch="main",
        producer="external-intake", projection=projection,
        evidence_refs=[e["evidence_id"] for e in entries],
    )
    obj = {
        "meta": meta,
        "ledger_id": f"EL-{attempt_id}",
        "entries": entries,
        "stage_vocabulary": ["design-time", "simulated", "live-runtime", "post-implementation", "production-observed"],
        "append_only_from_revision": None,
    }
    return finalize_hash(obj)
