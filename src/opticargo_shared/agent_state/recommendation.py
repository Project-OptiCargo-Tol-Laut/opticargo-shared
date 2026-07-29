from typing import Annotated, Self
from uuid import UUID

from pydantic import Field, model_validator

from opticargo_shared.agent_state.candidates import ScoreBreakdown
from opticargo_shared.agent_state.citation import Citation
from opticargo_shared.base import ContractModel, DecimalScore, Money
from opticargo_shared.enums import ConfidenceLevel, QueryIntent


class RankedRecommendation(ContractModel):
    rank: Annotated[int, Field(ge=1)]
    cargo_listing_ids: list[UUID] = Field(default_factory=list)
    score: DecimalScore
    score_breakdown: ScoreBreakdown
    estimated_revenue: Money | None = None
    estimated_cost: Money | None = None
    risks: list[str] = Field(default_factory=list)
    recommended_action: str


class RecommendationOutput(ContractModel):
    correlation_id: UUID
    voyage_id: UUID | None = None
    intent: QueryIntent
    summary: Annotated[str, Field(min_length=1)]
    recommendations: list[RankedRecommendation] = Field(default_factory=list)
    citations: list[Citation] = Field(default_factory=list)
    confidence: DecimalScore
    confidence_level: ConfidenceLevel
    fallback_used: bool = False
    abstained: bool = False
    abstention_reason: str | None = None
    warnings: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_abstention(self) -> Self:
        if self.abstained and not self.abstention_reason:
            raise ValueError("abstention_reason is required when abstained is true")
        if not self.abstained and self.abstention_reason is not None:
            raise ValueError("abstention_reason is only allowed when abstained is true")
        if self.abstained and self.recommendations:
            raise ValueError("recommendations must be empty when abstained is true")
        return self
