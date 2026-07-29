from typing import Annotated
from uuid import UUID

from pydantic import Field

from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.agent_state.graph_analysis import BackhaulCandidate
from opticargo_shared.base import ContractModel, Money, NonNegativeDecimal


class RejectedCandidate(ContractModel):
    cargo_listing_id: UUID
    reasons: list[str] = Field(min_length=1)


class OptimizationResult(ContractModel):
    selected_cargo_ids: list[UUID] = Field(default_factory=list)
    total_weight_ton: NonNegativeDecimal
    total_volume_m3: NonNegativeDecimal
    capacity_remaining_ton: NonNegativeDecimal
    estimated_revenue: NonNegativeDecimal
    estimated_cost: NonNegativeDecimal | None = None
    hard_constraints_valid: bool
    rejected_candidates: list[RejectedCandidate] = Field(default_factory=list)
    method: Annotated[str, Field(min_length=1)]
    duration_ms: Annotated[int, Field(ge=0)]


class OptimizationInput(BaseAgentState):
    candidates: list[BackhaulCandidate]
    remaining_capacity_ton: NonNegativeDecimal


class OptimizationOutput(BaseAgentState):
    selected_candidates: list[BackhaulCandidate] = Field(default_factory=list)
    estimated_total_revenue: Money
