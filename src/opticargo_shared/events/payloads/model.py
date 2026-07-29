from decimal import Decimal

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import ModelMode


class ModelStatusPayload(ContractModel):
    model_name: str
    model_version: str | None = None
    model_mode: ModelMode
    metrics: dict[str, Decimal] = Field(default_factory=dict)
    dataset_version: str | None = None
    promoted_at: AwareDatetime | None = None
    drift_detected_at: AwareDatetime | None = None
