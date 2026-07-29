from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel, NonNegativeDecimal


class SupplierBase(ContractModel):
    user_id: UUID
    business_name: Annotated[str, Field(min_length=1)]
    port_id: UUID
    commodity_ids: list[UUID] = Field(default_factory=list)
    avg_monthly_volume_ton: NonNegativeDecimal
    rating: Annotated[float, Field(ge=0, le=5, allow_inf_nan=False)] = 0
    verified: bool = False
    address: Annotated[str, Field(min_length=1)] | None = None


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(ContractModel):
    business_name: Annotated[str, Field(min_length=1)] | None = None
    port_id: UUID | None = None
    commodity_ids: list[UUID] | None = None
    avg_monthly_volume_ton: NonNegativeDecimal | None = None
    rating: Annotated[float, Field(ge=0, le=5, allow_inf_nan=False)] | None = None
    verified: bool | None = None
    address: Annotated[str, Field(min_length=1)] | None = None


class SupplierRead(SupplierBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Supplier = SupplierRead
