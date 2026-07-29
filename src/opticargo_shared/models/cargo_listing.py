from datetime import date
from typing import Self
from uuid import UUID

from pydantic import AwareDatetime, model_validator

from opticargo_shared.base import ContractModel, NonNegativeDecimal, PositiveDecimal
from opticargo_shared.enums import CargoListingStatus


class CargoListingBase(ContractModel):
    supplier_id: UUID
    commodity_id: UUID
    volume_ton: PositiveDecimal
    available_from: date
    available_until: date
    origin_port_id: UUID
    destination_port_id: UUID
    asking_price_per_ton: NonNegativeDecimal
    status: CargoListingStatus = CargoListingStatus.open

    @model_validator(mode="after")
    def validate_dates(self) -> Self:
        if self.available_until < self.available_from:
            raise ValueError("available_until cannot be earlier than available_from")
        return self


class CargoListingCreate(CargoListingBase):
    pass


class CargoListingUpdate(ContractModel):
    volume_ton: PositiveDecimal | None = None
    available_from: date | None = None
    available_until: date | None = None
    origin_port_id: UUID | None = None
    destination_port_id: UUID | None = None
    asking_price_per_ton: NonNegativeDecimal | None = None
    status: CargoListingStatus | None = None


class CargoListingRead(CargoListingBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


CargoListing = CargoListingRead
