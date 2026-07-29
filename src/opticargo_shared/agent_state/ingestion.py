from opticargo_shared.agent_state.base import BaseAgentState


class IngestionAgentInput(BaseAgentState):
    raw_data_source: str
    data_type: str  # misal: "document", "spreadsheet", "api"


class IngestionAgentOutput(BaseAgentState):
    processed_records: int
    failed_records: int
    status: str
