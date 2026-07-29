"""Base models and canonical scalar types for OptiCargo contracts."""

from __future__ import annotations

from decimal import Decimal
from typing import Annotated, Any, TypeAlias
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ContractModel(BaseModel):
    """Strict, framework-independent base for every public wire contract."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        from_attributes=True,
        str_strip_whitespace=True,
        use_enum_values=False,
    )


EntityId: TypeAlias = UUID
Money: TypeAlias = Decimal
WeightTon: TypeAlias = Decimal
VolumeM3: TypeAlias = Decimal
DecimalScore: TypeAlias = Annotated[
    Decimal, Field(ge=Decimal("0"), le=Decimal("1"), allow_inf_nan=False)
]
NonNegativeDecimal: TypeAlias = Annotated[Decimal, Field(ge=Decimal("0"), allow_inf_nan=False)]
PositiveDecimal: TypeAlias = Annotated[Decimal, Field(gt=Decimal("0"), allow_inf_nan=False)]
Metadata: TypeAlias = dict[str, Any]
NonEmptyStr: TypeAlias = Annotated[str, Field(min_length=1)]
