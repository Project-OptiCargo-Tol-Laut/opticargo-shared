from uuid import UUID

from opticargo_shared.base import ContractModel, PositiveDecimal
from opticargo_shared.enums import BookingStatus


class BookingCreatedPayload(ContractModel):
    booking_id: UUID
    voyage_id: UUID
    cargo_listing_id: UUID
    booked_volume_ton: PositiveDecimal
    status: BookingStatus
    actor_id: UUID | None = None


class BookingStatusChangedPayload(ContractModel):
    booking_id: UUID
    previous_status: BookingStatus
    new_status: BookingStatus
    voyage_id: UUID
    cargo_listing_id: UUID
    actor_id: UUID | None = None
    reason: str | None = None
