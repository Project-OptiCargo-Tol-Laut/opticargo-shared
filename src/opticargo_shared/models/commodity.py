from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class Commodity(BaseModel):
    """Selaras dengan tabel `commodities` di Bagian 14 dokumen desain."""
    id: UUID
    name: str
    category: str
    hs_code: str
    special_requirements: dict = {}
    is_perishable: bool
    max_stack_height: int
    certifications_required: list[str] = []
    created_at: datetime