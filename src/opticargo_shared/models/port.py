from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

class Port(BaseModel):
    """Selaras dengan tabel `ports` di Bagian 14 dokumen desain."""
    id: UUID
    name: str
    city: str
    province: str
    latitude: Decimal
    longitude: Decimal
    facilities: dict = {}
    max_vessel_tonnage: int
    operating_hours: dict = {}
    created_at: datetime