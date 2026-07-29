from typing import Annotated, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.agent_state.candidates import ScoreBreakdown
from opticargo_shared.agent_state.citation import Citation
from opticargo_shared.base import ContractModel, DecimalScore, Money
from opticargo_shared.enums import ModelMode, RecommendationStatus


class RankedCargoCombination(ContractModel):
    rank: Annotated[int, Field(ge=1)]
    cargo_listing_ids: list[UUID] = Field(min_length=1)
    score: DecimalScore


class RecommendationContent(ContractModel):
    summary: Annotated[str, Field(min_length=1)]
    ranked_cargo_combination: list[RankedCargoCombination] = Field(default_factory=list)
    score_breakdown: ScoreBreakdown
    estimated_revenue: Money | None = None
    estimated_cost: Money | None = None
    hard_constraints_checked: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    alternatives: list[str] = Field(default_factory=list)
    citations: list[Citation] = Field(default_factory=list)
    confidence: DecimalScore
    fallback_used: bool = False
    recommended_human_action: Annotated[str, Field(min_length=1)]


class RecommendationBase(ContractModel):
    voyage_id: UUID
    recommendation_type: Annotated[str, Field(min_length=1)]
    content: RecommendationContent
    score: DecimalScore
    status: RecommendationStatus = RecommendationStatus.pending
    generated_at: AwareDatetime
    responded_at: AwareDatetime | None = None
    model_mode: ModelMode | None = None
    trace_id: UUID

    @model_validator(mode="after")
    def validate_response_time(self) -> Self:
        has_response = self.responded_at is not None
        is_responded = self.status in {
            RecommendationStatus.accepted,
            RecommendationStatus.rejected,
        }
        if has_response != is_responded:
            raise ValueError("responded_at must be present exactly for accepted/rejected status")
        if self.responded_at is not None and self.responded_at < self.generated_at:
            raise ValueError("responded_at cannot be earlier than generated_at")
        return self


class RecommendationCreate(RecommendationBase):
    pass


class RecommendationUpdate(ContractModel):
    status: RecommendationStatus
    responded_at: AwareDatetime


class RecommendationRead(RecommendationBase):
    id: UUID


Recommendation = RecommendationRead
