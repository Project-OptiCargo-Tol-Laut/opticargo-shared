from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel

class Supplier(BaseModel):
    """Selaras dengan tabel `suppliers` di Bagian 14 dokumen desain."""
    id: UUID
    user_id: UUID
    business_name: str
    port_id: UUID
    commodity_ids: list[UUID] = []
    avg_monthly_volume_ton: Decimal
    rating: Decimal
    verified: bool = False
    address: str
    created_at: datetime