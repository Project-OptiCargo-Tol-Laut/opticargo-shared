from uuid import UUID

from opticargo_shared.base import ContractModel, PositiveDecimal
from opticargo_shared.enums import PaymentStatus


class PaymentCreatedPayload(ContractModel):
    payment_id: UUID
    booking_id: UUID
    amount: PositiveDecimal
    status: PaymentStatus
    external_reference: str | None = None


class PaymentStatusChangedPayload(ContractModel):
    payment_id: UUID
    booking_id: UUID
    previous_status: PaymentStatus
    new_status: PaymentStatus
    external_reference: str | None = None
    provider_event_id: str | None = None
    amount: PositiveDecimal
