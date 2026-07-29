from enum import StrEnum
from typing import Annotated, Any
from uuid import UUID

from pydantic import Field

from opticargo_shared.base import ContractModel


class EntityChangeType(StrEnum):
    created = "created"
    updated = "updated"
    deleted = "deleted"


class EntityChangedPayload(ContractModel):
    entity_type: Annotated[str, Field(min_length=1)]
    entity_id: UUID
    change_type: EntityChangeType
    changed_fields: list[str] = Field(default_factory=list)
    entity_version: Annotated[str, Field(min_length=1)]
    snapshot: dict[str, Any] | None = None
    lookup_hint: dict[str, Any] | None = None
