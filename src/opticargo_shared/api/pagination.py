from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class PageParams(BaseModel):
    page: int = 1
    page_size: int = 20

class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    page_size: int