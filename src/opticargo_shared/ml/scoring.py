from decimal import Decimal
from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel, DecimalScore, NonNegativeDecimal
from opticargo_shared.enums import ModelMode


class VoyageCapacitySummary(ContractModel):
    voyage_id: UUID
    remaining_weight_ton: NonNegativeDecimal
    remaining_volume_m3: NonNegativeDecimal


class CargoCandidateFeatures(ContractModel):
    cargo_listing_id: UUID
    cargo_weight_ton: NonNegativeDecimal
    cargo_volume_m3: NonNegativeDecimal | None = None
    features: dict[str, Decimal | str | bool | None] = Field(default_factory=dict)


class RouteScheduleFeatures(ContractModel):
    distance_nm: NonNegativeDecimal
    schedule_compatible: bool
    route_features: dict[str, Decimal | str | bool | None] = Field(default_factory=dict)


class SupplierRiskFeatures(ContractModel):
    supplier_id: UUID
    supplier_rating: Annotated[Decimal, Field(ge=0, le=5, allow_inf_nan=False)] | None = None
    risk_features: dict[str, Decimal | str | bool | None] = Field(default_factory=dict)


class CargoScoringRequest(ContractModel):
    correlation_id: UUID
    voyage: VoyageCapacitySummary
    candidate: CargoCandidateFeatures
    route_schedule: RouteScheduleFeatures
    supplier_risk: SupplierRiskFeatures


class FeatureExplanation(ContractModel):
    feature: str
    contribution: Decimal
    value: Any | None = None
    explanation: str | None = None


class CargoScoringResponse(ContractModel):
    correlation_id: UUID
    score: DecimalScore
    feature_explanations: list[FeatureExplanation] = Field(default_factory=list)
    model_mode: ModelMode
    model_version: str | None = None
    fallback_used: bool = False
    inference_timestamp: AwareDatetime
    warnings: list[str] = Field(default_factory=list)


ScoringRequest = CargoScoringRequest
ScoringResponse = CargoScoringResponse
