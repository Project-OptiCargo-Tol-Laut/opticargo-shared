from typing import Annotated, Any
from uuid import UUID

from pydantic import AliasChoices, AwareDatetime, Field

from opticargo_shared.base import ContractModel


class AuditLogRead(ContractModel):
    id: UUID
    actor_id: UUID | None = Field(
        default=None, validation_alias=AliasChoices("actor_id", "user_id")
    )
    action: Annotated[str, Field(min_length=1)]
    entity_type: Annotated[str, Field(min_length=1)]
    entity_id: UUID
    before: dict[str, Any] | None = None
    after: dict[str, Any] | None = None
    correlation_id: UUID
    source_ip: str | None = None
    created_at: AwareDatetime


AuditLog = AuditLogRead
