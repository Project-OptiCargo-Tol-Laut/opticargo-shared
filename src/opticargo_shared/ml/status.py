from decimal import Decimal

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import ModelMode


class ModelStatus(ContractModel):
    model_name: str
    model_version: str | None = None
    model_mode: ModelMode
    trained_at: AwareDatetime | None = None
    dataset_version: str | None = None
    metrics: dict[str, Decimal] = Field(default_factory=dict)
    fallback_available: bool
    healthy: bool
