from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel, NonNegativeDecimal, PositiveDecimal
from opticargo_shared.enums import BookingStatus


class BookingBase(ContractModel):
    voyage_id: UUID
    cargo_listing_id: UUID
    booked_volume_ton: PositiveDecimal
    agreed_price_per_ton: NonNegativeDecimal
    status: BookingStatus = BookingStatus.pending
    booking_date: AwareDatetime
    confirmation_date: AwareDatetime | None = None
    booking_ref: Annotated[str, Field(min_length=1)]
    created_by: UUID | None = None

    @model_validator(mode="after")
    def validate_confirmation_date(self) -> Self:
        if self.confirmation_date is not None and self.confirmation_date < self.booking_date:
            raise ValueError("confirmation_date cannot be earlier than booking_date")
        return self


class BookingCreate(BookingBase):
    pass


class BookingUpdate(ContractModel):
    booked_volume_ton: PositiveDecimal | None = None
    agreed_price_per_ton: NonNegativeDecimal | None = None
    status: BookingStatus | None = None
    confirmation_date: AwareDatetime | None = None


class BookingRead(BookingBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Booking = BookingRead
