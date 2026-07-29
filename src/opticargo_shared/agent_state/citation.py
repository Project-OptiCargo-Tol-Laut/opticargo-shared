from typing import Annotated
from uuid import UUID

from pydantic import Field

from opticargo_shared.base import ContractModel


class Citation(ContractModel):
    document_id: UUID
    title: Annotated[str, Field(min_length=1)]
    issuer: str | None = None
    document_version: str | None = None
    page: int | None = Field(default=None, ge=1)
    section: str | None = None
    source_reference: str | None = None
    excerpt: str | None = None
