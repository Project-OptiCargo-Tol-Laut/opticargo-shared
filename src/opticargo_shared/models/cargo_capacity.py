from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel, NonNegativeDecimal


class TemperatureRange(ContractModel):
    min_celsius: Annotated[float, Field(allow_inf_nan=False)]
    max_celsius: Annotated[float, Field(allow_inf_nan=False)]

    @model_validator(mode="after")
    def validate_range(self) -> Self:
        if self.min_celsius > self.max_celsius:
            raise ValueError("min_celsius cannot exceed max_celsius")
        return self


class CargoCapacityBase(ContractModel):
    voyage_id: UUID
    available_weight_ton: NonNegativeDecimal
    available_volume_m3: NonNegativeDecimal
    cargo_type_allowed: list[str] = Field(default_factory=list)
    temperature_range: TemperatureRange | None = None

    @model_validator(mode="after")
    def validate_unique_cargo_types(self) -> Self:
        normalized = [item.strip().casefold() for item in self.cargo_type_allowed]
        if len(normalized) != len(set(normalized)):
            raise ValueError("cargo_type_allowed cannot contain duplicates")
        return self


class CargoCapacityCreate(CargoCapacityBase):
    pass


class CargoCapacityUpdate(ContractModel):
    available_weight_ton: NonNegativeDecimal | None = None
    available_volume_m3: NonNegativeDecimal | None = None
    cargo_type_allowed: list[str] | None = None
    temperature_range: TemperatureRange | None = None


class CargoCapacityRead(CargoCapacityBase):
    id: UUID
    updated_at: AwareDatetime


CargoCapacity = CargoCapacityRead
