from opticargo_shared.base import ContractModel
from opticargo_shared.enums import QueryIntent


class IntentResult(ContractModel):
    intent: QueryIntent
    rationale: str | None = None


__all__ = ["IntentResult", "QueryIntent"]
