from datetime import date
from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class RagChunkMetadata(ContractModel):
    document_version: str | None = None
    title: Annotated[str, Field(min_length=1)]
    issuer: str | None = None
    page: int | None = Field(default=None, ge=1)
    section: str | None = None
    effective_date: date | None = None
    source_reference: str | None = None
    is_superseded: bool = False
    checksum: Annotated[str, Field(min_length=1)]


class RagChunkBase(ContractModel):
    document_id: UUID
    chunk_index: int = Field(ge=0)
    chunk_text: Annotated[str, Field(min_length=1)]
    qdrant_id: Annotated[str, Field(min_length=1)]
    token_count: int = Field(ge=0)
    metadata: RagChunkMetadata
    embedded_at: AwareDatetime


class RagChunkCreate(RagChunkBase):
    pass


class RagChunkRead(RagChunkBase):
    id: UUID


RagChunk = RagChunkRead
