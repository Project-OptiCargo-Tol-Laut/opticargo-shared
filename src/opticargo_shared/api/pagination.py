from typing import Generic, TypeVar

from pydantic import Field

from opticargo_shared.base import ContractModel
from opticargo_shared.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

T = TypeVar("T")


class PageParams(ContractModel):
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE)


class PageMeta(ContractModel):
    page: int = Field(ge=1)
    page_size: int = Field(ge=1, le=MAX_PAGE_SIZE)
    total_items: int = Field(ge=0)
    total_pages: int = Field(ge=0)


class PageResponse(ContractModel, Generic[T]):
    items: list[T]
    meta: PageMeta


class CursorMeta(ContractModel):
    next_cursor: str | None = None
    has_more: bool


class CursorResponse(ContractModel, Generic[T]):
    items: list[T]
    meta: CursorMeta


class PaginatedResponse(ContractModel, Generic[T]):
    """Deprecated v0 compatibility contract; prefer :class:`PageResponse`."""

    items: list[T]
    total: int = Field(ge=0)
    page: int = Field(ge=1)
    page_size: int = Field(ge=1, le=MAX_PAGE_SIZE)
