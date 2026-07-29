from typing import Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel, PositiveDecimal
from opticargo_shared.enums import RouteType


class RouteBase(ContractModel):
    origin_port_id: UUID
    destination_port_id: UUID
    distance_nm: PositiveDecimal
    estimated_days: int = Field(gt=0)
    route_type: RouteType
    is_active: bool = True

    @model_validator(mode="after")
    def ports_must_differ(self) -> Self:
        if self.origin_port_id == self.destination_port_id:
            raise ValueError("origin_port_id and destination_port_id must differ")
        return self


class RouteCreate(RouteBase):
    pass


class RouteUpdate(ContractModel):
    origin_port_id: UUID | None = None
    destination_port_id: UUID | None = None
    distance_nm: PositiveDecimal | None = None
    estimated_days: int | None = Field(default=None, gt=0)
    route_type: RouteType | None = None
    is_active: bool | None = None


class RouteRead(RouteBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Route = RouteRead
