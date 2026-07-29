from datetime import date
from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import DocumentIngestionStatus, DocumentType


class DocumentBase(ContractModel):
    booking_id: UUID | None = None
    doc_type: DocumentType
    title: Annotated[str, Field(min_length=1)]
    object_key: Annotated[str, Field(min_length=1)]
    file_size: int = Field(gt=0)
    mime_type: Annotated[str, Field(min_length=1)]
    uploaded_by: UUID
    issuer: Annotated[str, Field(min_length=1)] | None = None
    document_version: Annotated[str, Field(min_length=1)] | None = None
    effective_date: date | None = None
    source_reference: Annotated[str, Field(min_length=1)] | None = None
    is_superseded: bool = False
    supersedes_document_id: UUID | None = None
    ingestion_status: DocumentIngestionStatus = DocumentIngestionStatus.queued
    ingestion_error: str | None = None

    @model_validator(mode="after")
    def validate_ingestion_and_supersession(self) -> Self:
        if self.ingestion_status == DocumentIngestionStatus.failed:
            if not self.ingestion_error:
                raise ValueError("ingestion_error is required when ingestion failed")
        elif self.ingestion_error is not None:
            raise ValueError("ingestion_error is only allowed when ingestion failed")
        return self


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(ContractModel):
    title: Annotated[str, Field(min_length=1)] | None = None
    issuer: Annotated[str, Field(min_length=1)] | None = None
    document_version: Annotated[str, Field(min_length=1)] | None = None
    effective_date: date | None = None
    source_reference: Annotated[str, Field(min_length=1)] | None = None
    is_superseded: bool | None = None
    supersedes_document_id: UUID | None = None
    ingestion_status: DocumentIngestionStatus | None = None
    ingestion_error: str | None = None


class DocumentRead(DocumentBase):
    id: UUID
    created_at: AwareDatetime
    updated_at: AwareDatetime


Document = DocumentRead
