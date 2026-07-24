from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.models.recommendation import Recommendation

class RecommendationAgentInput(BaseAgentState):
    optimization_result: dict
    retrieved_context: str | None = None

class RecommendationAgentOutput(BaseAgentState):
    final_recommendation: Recommendation
    draft_document_paths: list[str] = []