from typing import Annotated
from uuid import UUID

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class ReviewBase(ContractModel):
    booking_id: UUID
    reviewer_id: UUID
    reviewee_id: UUID
    rating: Annotated[int, Field(ge=1, le=5)]
    comment: str | None = None


class ReviewCreate(ReviewBase):
    pass


class ReviewRead(ReviewBase):
    id: UUID
    created_at: AwareDatetime


Review = ReviewRead
