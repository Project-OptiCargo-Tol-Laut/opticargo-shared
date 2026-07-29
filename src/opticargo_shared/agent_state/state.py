from uuid import UUID

from pydantic import Field

from opticargo_shared.agent_state.candidates import CargoCandidate, ScoreBreakdown
from opticargo_shared.agent_state.optimization import OptimizationResult
from opticargo_shared.agent_state.recommendation import RecommendationOutput
from opticargo_shared.base import ContractModel
from opticargo_shared.enums import AgentNodeStatus, QueryIntent


class RetrievedChunk(ContractModel):
    document_id: UUID
    chunk_id: UUID
    text: str
    score: float | None = None


class OrchestratorState(ContractModel):
    correlation_id: UUID
    user_id: UUID
    query: str
    query_intent: QueryIntent = QueryIntent.unknown
    retrieved_chunks: list[RetrievedChunk] = Field(default_factory=list)
    graph_candidates: list[CargoCandidate] = Field(default_factory=list)
    scoring_results: dict[UUID, ScoreBreakdown] = Field(default_factory=dict)
    optimization_result: OptimizationResult | None = None
    recommendation_output: RecommendationOutput | None = None
    route_taken: list[str] = Field(default_factory=list)
    node_statuses: dict[str, AgentNodeStatus] = Field(default_factory=dict)
    errors: list[str] = Field(default_factory=list)
    fallback_used: bool = False
