from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel, NonNegativeDecimal
from opticargo_shared.enums import ModelMode


class HistoricalDemandPoint(ContractModel):
    timestamp: AwareDatetime
    volume_ton: NonNegativeDecimal


class ForecastRequest(ContractModel):
    correlation_id: UUID
    commodity_id: UUID
    port_id: UUID | None = None
    region: str | None = None
    horizon_days: Annotated[int, Field(gt=0)]
    historical_series_version: str
    history: list[HistoricalDemandPoint] = Field(default_factory=list)


class ForecastPoint(ContractModel):
    timestamp: AwareDatetime
    predicted_volume_ton: NonNegativeDecimal
    confidence_lower: NonNegativeDecimal
    confidence_upper: NonNegativeDecimal


class ForecastResponse(ContractModel):
    correlation_id: UUID
    commodity_id: UUID
    points: list[ForecastPoint]
    model_mode: ModelMode
    model_version: str | None = None
    warnings: list[str] = Field(default_factory=list)
