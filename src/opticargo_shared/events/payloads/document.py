from typing import Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import DocumentIngestionStatus


class DocumentUploadedPayload(ContractModel):
    document_id: UUID
    object_key: str
    mime_type: str
    checksum: str
    document_version: str | None = None
    is_superseded: bool = False


class DocumentIngestionResultPayload(ContractModel):
    document_id: UUID
    status: DocumentIngestionStatus
    chunk_count: int = Field(ge=0)
    indexed_at: AwareDatetime | None = None
    error_code: str | None = None
    error_message: str | None = None

    @model_validator(mode="after")
    def validate_result(self) -> Self:
        if self.status == DocumentIngestionStatus.failed:
            if not self.error_code or not self.error_message:
                raise ValueError("failed ingestion requires error_code and error_message")
        elif self.status == DocumentIngestionStatus.indexed and self.indexed_at is None:
            raise ValueError("indexed_at is required for indexed ingestion")
        return self
