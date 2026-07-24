from datetime import datetime, date
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import CargoListingStatus

class CargoListing(BaseModel):
    """Selaras dengan tabel `cargo_listings` di Bagian 14 dokumen desain."""
    id: UUID
    supplier_id: UUID
    commodity_id: UUID
    volume_ton: Decimal
    available_from: date
    available_until: date
    origin_port_id: UUID
    destination_port_id: UUID
    asking_price_per_ton: Decimal
    status: CargoListingStatus
    created_at: datetime