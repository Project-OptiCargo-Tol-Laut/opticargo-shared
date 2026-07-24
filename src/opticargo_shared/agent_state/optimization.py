from decimal import Decimal
from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.agent_state.graph_analysis import BackhaulCandidate

class OptimizationInput(BaseAgentState):
    candidates: list[BackhaulCandidate]
    remaining_capacity_ton: Decimal

class OptimizationOutput(BaseAgentState):
    selected_candidates: list[BackhaulCandidate] = []
    estimated_total_revenue: Decimal