from uuid import UUID

from pydantic import Field

from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.base import ContractModel, DecimalScore, NonNegativeDecimal


class GraphAnalysisInput(BaseAgentState):
    origin_port_id: UUID
    search_radius_days: int = Field(default=7, ge=0)


class BackhaulCandidate(ContractModel):
    supplier_id: UUID
    commodity_id: UUID
    volume_ton: NonNegativeDecimal
    match_score: DecimalScore


class GraphAnalysisOutput(BaseAgentState):
    candidates: list[BackhaulCandidate] = Field(default_factory=list)
