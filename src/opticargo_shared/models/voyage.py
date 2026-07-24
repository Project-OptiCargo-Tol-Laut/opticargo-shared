from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import VoyageStatus

class Voyage(BaseModel):
    id: UUID
    ship_id: UUID
    route_id: UUID
    departure_date: datetime
    arrival_date: datetime
    total_capacity_ton: Decimal
    used_capacity_ton: Decimal
    remaining_capacity_ton: Decimal
    status: VoyageStatus
    waypoints: list[dict] = []
    created_at: datetime

class CargoCapacity(BaseModel):
    id: UUID
    voyage_id: UUID
    available_weight_ton: Decimal
    available_volume_m3: Decimal
    cargo_type_allowed: list[str] = []
    temperature_range: dict | None = None
    updated_at: datetime