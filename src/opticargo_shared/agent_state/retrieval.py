from typing import Any

from pydantic import Field

from opticargo_shared.agent_state.base import BaseAgentState


class RetrievalAgentInput(BaseAgentState):
    query: str
    top_k: int = 5


class RetrievalAgentOutput(BaseAgentState):
    retrieved_chunks: list[dict[str, Any]] = Field(default_factory=list)
    knowledge_graph_context: str | None = None
