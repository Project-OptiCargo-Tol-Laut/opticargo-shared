from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import RouteType

class Route(BaseModel):
    """Selaras dengan tabel `routes` di Bagian 14 dokumen desain."""
    id: UUID
    origin_port_id: UUID
    destination_port_id: UUID
    distance_nm: Decimal
    estimated_days: int
    route_type: RouteType
    is_active: bool = True
    created_at: datetime