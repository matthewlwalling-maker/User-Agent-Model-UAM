from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class ConfigError(ValueError):
    pass


@dataclass(frozen=True)
class RunConfig:
    raw: dict[str, Any]
    path: Path

    @property
    def run_series_id(self) -> str:
        return str(self.raw["run_series_id"])

    @property
    def base_dir(self) -> Path:
        return self.path.parent.resolve()

    def resolve(self, value: str | Path) -> Path:
        p = Path(value)
        return p.resolve() if p.is_absolute() else (self.base_dir / p).resolve()

    @property
    def authority_dir(self) -> Path:
        return self.resolve(self.raw["paths"]["authority_dir"])

    @property
    def fixture_view(self) -> Path:
        return self.resolve(self.raw["paths"]["fixture_view"])

    @property
    def run_root(self) -> Path:
        return self.resolve(self.raw["paths"]["output_root"]) / self.run_series_id

    @property
    def provider(self) -> dict[str, Any]:
        return self.raw["provider"]

    @property
    def execution(self) -> dict[str, Any]:
        return self.raw["execution"]

    @property
    def blinding(self) -> dict[str, Any]:
        return self.raw["blinding"]

    @property
    def capture(self) -> dict[str, Any]:
        return self.raw.get("capture", {})

    @property
    def status(self) -> str:
        return str(self.raw.get("status", "unknown"))


def load_config(path: str | Path) -> RunConfig:
    path = Path(path).resolve()
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ConfigError("Configuration root must be a mapping")
    required = ["run_series_id", "paths", "provider", "execution", "holdouts", "blinding"]
    missing = [k for k in required if k not in raw]
    if missing:
        raise ConfigError(f"Missing configuration keys: {missing}")
    if not raw["run_series_id"] or str(raw["run_series_id"]).startswith("SET-"):
        raise ConfigError("run_series_id must be populated")
    provider = raw["provider"]
    if provider.get("type") != "codex_cli":
        raise ConfigError("This package supports provider.type=codex_cli")
    if not provider.get("model"):
        raise ConfigError("provider.model is required")
    if provider.get("reasoning_effort", "high") not in {"minimal", "low", "medium", "high", "xhigh"}:
        raise ConfigError("provider.reasoning_effort must be minimal|low|medium|high|xhigh")
    if provider.get("model_verbosity", "low") not in {"low", "medium", "high"}:
        raise ConfigError("provider.model_verbosity must be low|medium|high")
    if provider.get("auth_mode", "auto") not in {"auto", "chatgpt", "api"}:
        raise ConfigError("provider.auth_mode must be auto|chatgpt|api")
    if int(raw["execution"].get("replicates_per_cell", 0)) < 1:
        raise ConfigError("execution.replicates_per_cell must be >= 1")
    if raw.get("status") == "authoritative":
        if not raw["holdouts"].get("required", True):
            raise ConfigError("Authoritative runs must require holdouts")
        for kind in ("material", "trivial"):
            h = raw["holdouts"].get(kind, {})
            for field in ("asset_file", "selection_record_file"):
                val = str(h.get(field, ""))
                if not val or val.startswith("SET-"):
                    raise ConfigError(f"Authoritative run requires holdouts.{kind}.{field}")
    return RunConfig(raw=raw, path=path)
