from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel, PositiveDecimal
from opticargo_shared.enums import PaymentMethod, PaymentStatus


class PaymentBase(ContractModel):
    booking_id: UUID
    amount: PositiveDecimal
    method: PaymentMethod
    status: PaymentStatus = PaymentStatus.pending
    external_reference: Annotated[str, Field(min_length=1)] | None = None
    paid_at: AwareDatetime | None = None

    @model_validator(mode="after")
    def validate_paid_at(self) -> Self:
        if self.status == PaymentStatus.paid and self.paid_at is None:
            raise ValueError("paid_at is required when payment status is paid")
        if self.status != PaymentStatus.paid and self.paid_at is not None:
            raise ValueError("paid_at is only allowed when payment status is paid")
        return self


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(ContractModel):
    status: PaymentStatus | None = None
    external_reference: Annotated[str, Field(min_length=1)] | None = None
    paid_at: AwareDatetime | None = None


class PaymentRead(PaymentBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Payment = PaymentRead
