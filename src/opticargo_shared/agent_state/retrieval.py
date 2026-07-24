from opticargo_shared.agent_state.base import BaseAgentState

class RetrievalAgentInput(BaseAgentState):
    query: str
    top_k: int = 5

class RetrievalAgentOutput(BaseAgentState):
    retrieved_chunks: list[dict] = []
    knowledge_graph_context: str | None = None