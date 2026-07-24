from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel
from opticargo_shared.agent_state.base import BaseAgentState

class GraphAnalysisInput(BaseAgentState):
    origin_port_id: UUID
    search_radius_days: int = 7

class BackhaulCandidate(BaseModel):
    supplier_id: UUID
    commodity_id: UUID
    volume_ton: Decimal
    match_score: float

class GraphAnalysisOutput(BaseAgentState):
    candidates: list[BackhaulCandidate]