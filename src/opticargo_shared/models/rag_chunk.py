from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class RagChunk(BaseModel):
    """Selaras dengan tabel `rag_chunks` di Bagian 14 dokumen desain."""
    id: UUID
    document_id: UUID
    chunk_index: int
    chunk_text: str
    qdrant_id: str
    token_count: int
    metadata: dict = {}
    embedded_at: datetime