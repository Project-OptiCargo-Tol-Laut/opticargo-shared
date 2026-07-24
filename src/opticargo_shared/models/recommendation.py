from datetime import datetime
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import RecommendationStatus

class Recommendation(BaseModel):
    """Selaras dengan tabel `recommendations` di Bagian 14 dokumen desain."""
    id: UUID
    voyage_id: UUID
    recommendation_type: str
    content: dict = {}
    score: Decimal
    status: RecommendationStatus
    generated_at: datetime
    responded_at: datetime | None = None