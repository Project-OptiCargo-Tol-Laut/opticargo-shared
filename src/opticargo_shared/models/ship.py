from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import ShipStatus

class Ship(BaseModel):
    id: UUID
    name: str
    imo_number: str
    ship_type: str
    gross_tonnage: Decimal
    deadweight_tonnage: Decimal
    cargo_capacity_m3: Decimal
    operator_id: UUID  # FK -> User
    flag: str
    certifications: dict = {}
    status: ShipStatus
    created_at: datetime