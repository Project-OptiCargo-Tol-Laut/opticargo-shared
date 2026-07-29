from uuid import UUID

from pydantic import Field

from opticargo_shared.base import ContractModel


class ReviewCreatedPayload(ContractModel):
    review_id: UUID
    booking_id: UUID
    reviewer_id: UUID
    reviewee_id: UUID
    rating: int = Field(ge=1, le=5)
