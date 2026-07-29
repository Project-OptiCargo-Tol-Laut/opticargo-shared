from decimal import Decimal
from uuid import uuid4

from opticargo_shared.agent_state import RecommendationOutput
from opticargo_shared.enums import ConfidenceLevel, QueryIntent

recommendation = RecommendationOutput(
    correlation_id=uuid4(),
    intent=QueryIntent.unknown,
    summary="Evidence is insufficient to recommend cargo.",
    confidence=Decimal("0.2"),
    confidence_level=ConfidenceLevel.low,
    abstained=True,
    abstention_reason="No current regulation source was retrieved.",
)
print(recommendation.model_dump_json(indent=2))
