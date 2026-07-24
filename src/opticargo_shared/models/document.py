from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.enums import DocumentType

class Document(BaseModel):
    """Selaras dengan tabel `documents` di Bagian 14 dokumen desain."""
    id: UUID
    booking_id: UUID | None = None
    doc_type: DocumentType
    title: str
    file_path: str
    file_size: int
    uploaded_by: UUID
    created_at: datetime