from pydantic import BaseModel
from uuid import UUID

class BaseAgentState(BaseModel):
    request_id: UUID
    voyage_id: UUID | None = None
    trace: list[str] = []   # jejak agent mana saja yang sudah memproses, untuk debugging