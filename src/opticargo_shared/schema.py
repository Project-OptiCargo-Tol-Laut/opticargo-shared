"""Registry and deterministic JSON Schema generation for public contracts."""

from __future__ import annotations

import inspect
from collections.abc import Iterable
from typing import Any

from pydantic import BaseModel


def _classes_from_module(module: Any, exported_names: Iterable[str]) -> list[type[BaseModel]]:
    classes: list[type[BaseModel]] = []
    for name in exported_names:
        value = getattr(module, name, None)
        if (
            inspect.isclass(value)
            and issubclass(value, BaseModel)
            and value is not BaseModel
            and not name.endswith("Internal")
        ):
            classes.append(value)
    return classes


def public_contract_models() -> tuple[type[BaseModel], ...]:
    """Return every exported public model once, in stable qualified-name order."""

    from opticargo_shared import agent_state, api, dataset, ml, models
    from opticargo_shared.events import DomainEvent, payloads

    candidates: list[type[BaseModel]] = [DomainEvent]
    for module in (models, api, agent_state, ml, dataset, payloads):
        candidates.extend(_classes_from_module(module, getattr(module, "__all__", ())))

    unique = {qualified_model_name(model): model for model in candidates}
    return tuple(unique[name] for name in sorted(unique))


def qualified_model_name(model: type[BaseModel]) -> str:
    return f"{model.__module__}.{model.__name__}"


def generate_json_schemas() -> dict[str, dict[str, Any]]:
    """Generate a stable mapping of fully qualified model name to JSON Schema."""

    return {
        qualified_model_name(model): model.model_json_schema(mode="serialization")
        for model in public_contract_models()
    }
