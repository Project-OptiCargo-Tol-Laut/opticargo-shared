from typing import Annotated
from uuid import UUID

from pydantic import Field

from opticargo_shared.base import ContractModel


class IdempotencyContext(ContractModel):
    idempotency_key: Annotated[str, Field(min_length=1, max_length=255)]
    correlation_id: UUID
