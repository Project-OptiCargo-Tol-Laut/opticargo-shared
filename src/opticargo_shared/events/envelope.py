from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel
from opticargo_shared.events.types import EVENT_VERSION


class DomainEvent(ContractModel):
    event_id: UUID
    event_type: Annotated[str, Field(min_length=1)]
    event_version: Annotated[str, Field(min_length=1)] = EVENT_VERSION
    occurred_at: AwareDatetime
    producer: Annotated[str, Field(min_length=1)]
    entity_type: Annotated[str, Field(min_length=1)]
    entity_id: UUID
    actor_id: UUID | None = None
    correlation_id: UUID
    idempotency_key: Annotated[str, Field(min_length=1, max_length=255)]
    payload: dict[str, Any]
