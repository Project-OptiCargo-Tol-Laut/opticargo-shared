from enum import StrEnum
from typing import Annotated

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class ValidationStatus(StrEnum):
    pending = "pending"
    valid = "valid"
    invalid = "invalid"


class RecordProvenance(ContractModel):
    source: Annotated[str, Field(min_length=1)]
    collected_or_generated_at: AwareDatetime
    transformation_version: Annotated[str, Field(min_length=1)]
    is_synthetic: bool
    generator_seed: int | None = None
    original_external_identifier: str | None = None
    validation_status: ValidationStatus
