from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel, NonNegativeDecimal
from opticargo_shared.enums import ShipStatus


class ShipBase(ContractModel):
    name: Annotated[str, Field(min_length=1)]
    imo_number: Annotated[str, Field(min_length=1)]
    ship_type: Annotated[str, Field(min_length=1)]
    gross_tonnage: NonNegativeDecimal
    deadweight_tonnage: NonNegativeDecimal
    cargo_capacity_m3: NonNegativeDecimal
    operator_id: UUID
    flag: Annotated[str, Field(min_length=1)] | None = None
    certifications: dict[str, Any] = Field(default_factory=dict)
    status: ShipStatus


class ShipCreate(ShipBase):
    pass


class ShipUpdate(ContractModel):
    name: Annotated[str, Field(min_length=1)] | None = None
    imo_number: Annotated[str, Field(min_length=1)] | None = None
    ship_type: Annotated[str, Field(min_length=1)] | None = None
    gross_tonnage: NonNegativeDecimal | None = None
    deadweight_tonnage: NonNegativeDecimal | None = None
    cargo_capacity_m3: NonNegativeDecimal | None = None
    operator_id: UUID | None = None
    flag: Annotated[str, Field(min_length=1)] | None = None
    certifications: dict[str, Any] | None = None
    status: ShipStatus | None = None


class ShipRead(ShipBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Ship = ShipRead
