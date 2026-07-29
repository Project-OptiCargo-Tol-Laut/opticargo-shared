from typing import Annotated, Any
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class CommodityBase(ContractModel):
    name: Annotated[str, Field(min_length=1)]
    category: Annotated[str, Field(min_length=1)]
    hs_code: Annotated[str, Field(min_length=1)] | None = None
    special_requirements: dict[str, Any] = Field(default_factory=dict)
    is_perishable: bool = False
    max_stack_height: int | None = Field(default=None, ge=0)
    certifications_required: list[str] = Field(default_factory=list)


class CommodityCreate(CommodityBase):
    pass


class CommodityUpdate(ContractModel):
    name: Annotated[str, Field(min_length=1)] | None = None
    category: Annotated[str, Field(min_length=1)] | None = None
    hs_code: Annotated[str, Field(min_length=1)] | None = None
    special_requirements: dict[str, Any] | None = None
    is_perishable: bool | None = None
    max_stack_height: int | None = Field(default=None, ge=0)
    certifications_required: list[str] | None = None


class CommodityRead(CommodityBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Commodity = CommodityRead
