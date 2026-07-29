from decimal import Decimal
from uuid import UUID

from pydantic import Field

from opticargo_shared.base import ContractModel, DecimalScore
from opticargo_shared.enums import ModelMode


class AnomalyRequest(ContractModel):
    correlation_id: UUID
    entity_type: str
    entity_id: UUID
    features: dict[str, Decimal | str | bool | None]


class AnomalyResponse(ContractModel):
    correlation_id: UUID
    entity_type: str
    entity_id: UUID
    is_anomaly: bool
    anomaly_score: DecimalScore
    reasons: list[str] = Field(default_factory=list)
    model_mode: ModelMode
    model_version: str | None = None
