from uuid import UUID

from opticargo_shared.base import ContractModel, DecimalScore
from opticargo_shared.enums import RecommendationStatus


class RecommendationCreatedPayload(ContractModel):
    recommendation_id: UUID
    voyage_id: UUID
    score: DecimalScore
    status: RecommendationStatus
    recipient_user_ids: list[UUID]
    threshold_triggered: bool
