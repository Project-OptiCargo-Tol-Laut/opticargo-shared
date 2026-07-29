from enum import StrEnum


class QueryIntent(StrEnum):
    regulation = "regulation"
    matching = "matching"
    route = "route"
    analytics = "analytics"
    unknown = "unknown"


class ModelMode(StrEnum):
    trained = "trained"
    heuristic = "heuristic"


class AgentNodeStatus(StrEnum):
    pending = "pending"
    running = "running"
    completed = "completed"
    skipped = "skipped"
    failed = "failed"
    fallback = "fallback"


class ConfidenceLevel(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"
