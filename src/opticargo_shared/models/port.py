from decimal import Decimal
from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class PortBase(ContractModel):
    name: Annotated[str, Field(min_length=1)]
    city: Annotated[str, Field(min_length=1)]
    province: Annotated[str, Field(min_length=1)]
    latitude: Annotated[Decimal, Field(ge=-90, le=90, allow_inf_nan=False)]
    longitude: Annotated[Decimal, Field(ge=-180, le=180, allow_inf_nan=False)]
    facilities: dict[str, Any] = Field(default_factory=dict)
    max_vessel_tonnage: Annotated[int, Field(ge=0)] | None = None
    operating_hours: dict[str, Any] = Field(default_factory=dict)


class PortCreate(PortBase):
    pass


class PortUpdate(ContractModel):
    name: Annotated[str, Field(min_length=1)] | None = None
    city: Annotated[str, Field(min_length=1)] | None = None
    province: Annotated[str, Field(min_length=1)] | None = None
    latitude: Annotated[Decimal, Field(ge=-90, le=90, allow_inf_nan=False)] | None = None
    longitude: Annotated[Decimal, Field(ge=-180, le=180, allow_inf_nan=False)] | None = None
    facilities: dict[str, Any] | None = None
    max_vessel_tonnage: Annotated[int, Field(ge=0)] | None = None
    operating_hours: dict[str, Any] | None = None


class PortRead(PortBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Port = PortRead
