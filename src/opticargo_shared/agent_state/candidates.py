from uuid import UUID

from opticargo_shared.base import ContractModel, DecimalScore, NonNegativeDecimal
from opticargo_shared.enums import ModelMode


class CargoCandidate(ContractModel):
    cargo_listing_id: UUID
    supplier_id: UUID
    commodity_id: UUID
    origin_port_id: UUID
    destination_port_id: UUID
    available_volume_ton: NonNegativeDecimal
    distance_to_port: NonNegativeDecimal | None = None
    schedule_compatible: bool
    capacity_compatible: bool
    certification_compatible: bool


class ScoreBreakdown(ContractModel):
    total_score: DecimalScore
    economic_value: DecimalScore
    schedule_fit: DecimalScore
    capacity_fit: DecimalScore
    distance_fit: DecimalScore
    risk_score: DecimalScore
    supplier_rating: DecimalScore | None = None
    model_mode: ModelMode
    model_version: str | None = None
    fallback_used: bool = False
