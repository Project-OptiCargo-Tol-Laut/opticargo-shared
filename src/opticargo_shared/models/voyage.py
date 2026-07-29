from typing import Any, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel, NonNegativeDecimal
from opticargo_shared.enums import VoyageStatus


class VoyageBase(ContractModel):
    ship_id: UUID
    route_id: UUID
    departure_date: AwareDatetime
    arrival_date: AwareDatetime
    total_capacity_ton: NonNegativeDecimal
    used_capacity_ton: NonNegativeDecimal
    remaining_capacity_ton: NonNegativeDecimal
    status: VoyageStatus
    waypoints: list[dict[str, Any]] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_schedule_and_capacity(self) -> Self:
        if self.arrival_date <= self.departure_date:
            raise ValueError("arrival_date must be later than departure_date")
        if self.used_capacity_ton > self.total_capacity_ton:
            raise ValueError("used_capacity_ton cannot exceed total_capacity_ton")
        if self.remaining_capacity_ton != self.total_capacity_ton - self.used_capacity_ton:
            raise ValueError("remaining_capacity_ton must equal total minus used capacity")
        return self


class VoyageCreate(VoyageBase):
    pass


class VoyageUpdate(ContractModel):
    ship_id: UUID | None = None
    route_id: UUID | None = None
    departure_date: AwareDatetime | None = None
    arrival_date: AwareDatetime | None = None
    total_capacity_ton: NonNegativeDecimal | None = None
    used_capacity_ton: NonNegativeDecimal | None = None
    remaining_capacity_ton: NonNegativeDecimal | None = None
    status: VoyageStatus | None = None
    waypoints: list[dict[str, Any]] | None = None


class VoyageRead(VoyageBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Voyage = VoyageRead
