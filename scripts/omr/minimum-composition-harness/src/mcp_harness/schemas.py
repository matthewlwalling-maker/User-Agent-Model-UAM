from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


OPERATOR_TO_KIND = {"O1": "GoalContract", "O2": "CapabilityModel", "O3": "CoverageMap", "O4": "ChangeDecision"}


class SchemaRegistry:
    def __init__(self, p2_path: Path):
        self.path = p2_path
        self.registry = json.loads(p2_path.read_text(encoding="utf-8"))
        self.defs = self.registry["$defs"]

    def validate_state(self, obj: dict[str, Any], kind: str) -> list[str]:
        schema = {"$schema": self.registry["$schema"], "$ref": f"#/$defs/{kind}", "$defs": self.defs}
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(obj), key=lambda e: list(e.absolute_path))
        return [f"{'/'.join(map(str, e.absolute_path)) or '$'}: {e.message}" for e in errors]

    def validate_evidence_entries(self, entries: list[dict[str, Any]]) -> list[str]:
        item = self.defs["EvidenceLedger"]["properties"]["entries"]["items"]
        validator = Draft202012Validator(item, format_checker=FormatChecker())
        out: list[str] = []
        for i, entry in enumerate(entries):
            for e in validator.iter_errors(entry):
                out.append(f"ledger_append_delta/{i}/{'/'.join(map(str, e.absolute_path))}: {e.message}")
        return out

    def operator_output_schema(self, operator: str, expected: dict[str, Any]) -> dict[str, Any]:
        """Return a stable constrained-output transport schema, not the canonical P2 schema.

        P2 remains the local source of truth and is applied after the response. The transport
        schema deliberately includes only P2-required substantive fields. The deterministic
        harness injects the common metadata envelope and O2 packet-boundary facts. This keeps
        constrained decoding within practical optional-field/union complexity limits and makes
        the grammar stable across attempts, while preserving full local validation.
        """
        del expected  # exact identity/ancestry is injected by the deterministic harness
        kind = OPERATOR_TO_KIND[operator]
        state_schema = _required_transport_schema(self.defs[kind], self.defs)

        # Metadata is not model-owned. Keep an explicit empty placeholder so the response still
        # has the same logical state-object shape; _apply_envelope supplies every canonical field.
        state_schema["properties"]["meta"] = {
            "type": "object",
            "additionalProperties": False,
            "properties": {},
            "required": [],
        }

        # O2 reports only possible asset-term contamination. Exact condition, packet hash,
        # allowed/forbidden inputs, and prior-exposure fact are computed from the request trace.
        if operator == "O2":
            state_schema["properties"]["derivation_boundary"] = {
                "type": "object",
                "additionalProperties": False,
                "required": ["asset_component_terms_used"],
                "properties": {
                    "asset_component_terms_used": {
                        "type": "array",
                        "items": {"type": "string"},
                    }
                },
            }

        entry_schema = _required_transport_schema(
            self.defs["EvidenceLedger"]["properties"]["entries"]["items"], self.defs
        )
        wrapper = {
            "type": "object",
            "additionalProperties": False,
            "required": ["validation", "state_object", "ledger_append_delta", "stop", "visible_answer"],
            "properties": {
                "validation": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["status", "errors"],
                    "properties": {
                        "status": {"enum": ["valid", "invalid", "blocked", "contested"]},
                        "errors": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": ["code", "message"],
                                "properties": {
                                    "code": {"type": "string"},
                                    "message": {"type": "string"},
                                },
                            },
                        },
                    },
                },
                "state_object": state_schema,
                "ledger_append_delta": {"type": "array", "items": entry_schema},
                "stop": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["scope", "code", "reason"],
                    "properties": {
                        "scope": {"enum": ["local", "global"]},
                        "code": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                },
                "visible_answer": {"type": "string"},
            },
        }
        return sanitize_for_structured_output(wrapper)


def _resolve_ref(schema: dict[str, Any], defs: dict[str, Any]) -> dict[str, Any]:
    if "$ref" not in schema:
        return copy.deepcopy(schema)
    ref = str(schema["$ref"])
    prefix = "#/$defs/"
    if not ref.startswith(prefix):
        raise ValueError(f"Unsupported non-local schema reference: {ref}")
    name = ref[len(prefix):]
    resolved = copy.deepcopy(defs[name])
    siblings = {k: copy.deepcopy(v) for k, v in schema.items() if k != "$ref"}
    return _merge_schema_objects(resolved, siblings)


def _merge_schema_objects(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    """Merge non-conflicting JSON-schema object fragments used by P2 allOf clauses."""
    out = copy.deepcopy(left)
    for key, value in right.items():
        if key == "properties":
            out.setdefault("properties", {}).update(copy.deepcopy(value))
        elif key == "required":
            out["required"] = list(dict.fromkeys([*out.get("required", []), *value]))
        elif key == "allOf":
            out.setdefault("allOf", []).extend(copy.deepcopy(value))
        else:
            out[key] = copy.deepcopy(value)
    return out


def _flatten_all_of(schema: dict[str, Any], defs: dict[str, Any]) -> dict[str, Any]:
    current = _resolve_ref(schema, defs)
    clauses = current.pop("allOf", [])
    for clause in clauses:
        # P2 conditional clauses are enforced by local validation, not constrained decoding.
        if any(k in clause for k in ("if", "then", "else")):
            continue
        resolved = _flatten_all_of(clause, defs)
        current = _merge_schema_objects(current, resolved)
    current.pop("if", None)
    current.pop("then", None)
    current.pop("else", None)
    current.pop("not", None)
    return current


def _required_transport_schema(schema: dict[str, Any], defs: dict[str, Any]) -> dict[str, Any]:
    """Dereference P2 and retain only required fields at every object boundary.

    Structured-output decoding supports a constrained subset of JSON Schema and may impose practical
    complexity limits on optional properties/unions. Omitting P2-optional fields here does not alter
    P2: the fully assembled object is still validated against the original Draft 2020-12 schema.
    """
    node = _flatten_all_of(schema, defs)
    out: dict[str, Any] = {}

    if "const" in node:
        out["enum"] = [copy.deepcopy(node["const"])]
    elif "enum" in node:
        out["enum"] = copy.deepcopy(node["enum"])
    if "type" in node:
        out["type"] = copy.deepcopy(node["type"])

    node_type = node.get("type")
    if node_type == "object" or "properties" in node:
        required = list(node.get("required", []))
        properties = node.get("properties", {})
        selected: dict[str, Any] = {}
        for name in required:
            if name not in properties:
                raise ValueError(f"Required property {name!r} missing from schema")
            selected[name] = _required_transport_schema(properties[name], defs)
        out.update({
            "type": "object",
            "additionalProperties": False,
            "required": required,
            "properties": selected,
        })
    elif node_type == "array":
        out["type"] = "array"
        out["items"] = _required_transport_schema(node.get("items", {}), defs)

    # Primitive schemas without an explicit type can legally be enum-only.
    return out


def sanitize_for_structured_output(schema: Any) -> Any:
    """Remove constraints unsupported by constrained decoding; local validation retains them."""
    unsupported = {
        "minimum", "maximum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf",
        "minLength", "maxLength", "pattern", "format", "minItems", "maxItems",
        "uniqueItems", "contains", "minContains", "maxContains", "minProperties", "maxProperties",
        "if", "then", "else", "not", "dependentRequired", "dependentSchemas",
    }
    if isinstance(schema, list):
        return [sanitize_for_structured_output(v) for v in schema]
    if not isinstance(schema, dict):
        return schema
    out: dict[str, Any] = {}
    for key, value in schema.items():
        if key in unsupported:
            continue
        if key == "const":
            out["enum"] = [value]
        else:
            out[key] = sanitize_for_structured_output(value)
    return out


def count_optional_properties(schema: Any) -> int:
    """Count object properties not present in their containing object's required list."""
    if isinstance(schema, list):
        return sum(count_optional_properties(v) for v in schema)
    if not isinstance(schema, dict):
        return 0
    total = 0
    props = schema.get("properties")
    if isinstance(props, dict):
        required = set(schema.get("required", []))
        total += sum(1 for name in props if name not in required)
        total += sum(count_optional_properties(v) for v in props.values())
    if "items" in schema:
        total += count_optional_properties(schema["items"])
    for key in ("anyOf", "oneOf", "allOf"):
        if key in schema:
            total += count_optional_properties(schema[key])
    return total
