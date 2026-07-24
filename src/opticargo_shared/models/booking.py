from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import BookingStatus

class Booking(BaseModel):
    """Selaras dengan tabel `bookings` di Bagian 14 dokumen desain."""
    id: UUID
    voyage_id: UUID
    cargo_listing_id: UUID
    booked_volume_ton: Decimal
    agreed_price_per_ton: Decimal
    status: BookingStatus
    booking_date: datetime
    confirmation_date: datetime | None = None
    booking_ref: str