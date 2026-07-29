from decimal import Decimal
from uuid import uuid4

import pytest
from pydantic import ValidationError

from opticargo_shared.agent_state import RecommendationOutput
from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.agent_state.graph_analysis import BackhaulCandidate, GraphAnalysisInput
from opticargo_shared.enums import ConfidenceLevel, QueryIntent


def test_base_agent_state_accepts_legacy_request_id_and_isolates_defaults() -> None:
    request_id = uuid4()
    first = BaseAgentState(request_id=request_id)
    second = BaseAgentState(correlation_id=uuid4())
    first.trace.append("retrieval")
    assert first.request_id == request_id
    assert first.model_dump()["correlation_id"] == request_id
    assert second.trace == []


def test_graph_analysis_contracts() -> None:
    state = GraphAnalysisInput(request_id=uuid4(), origin_port_id=uuid4(), search_radius_days=14)
    candidate = BackhaulCandidate(
        supplier_id=uuid4(),
        commodity_id=uuid4(),
        volume_ton=Decimal("150.5"),
        match_score=Decimal("0.95"),
    )
    assert state.search_radius_days == 14
    assert candidate.match_score == Decimal("0.95")
    with pytest.raises(ValidationError):
        GraphAnalysisInput(request_id=uuid4())


def test_recommendation_abstention_rules() -> None:
    output = RecommendationOutput(
        correlation_id=uuid4(),
        intent=QueryIntent.unknown,
        summary="Insufficient evidence",
        confidence="0.1",
        confidence_level=ConfidenceLevel.low,
        abstained=True,
        abstention_reason="No citations retrieved",
    )
    assert output.recommendations == []
    with pytest.raises(ValidationError, match="abstention_reason"):
        RecommendationOutput(
            correlation_id=uuid4(),
            intent=QueryIntent.unknown,
            summary="Insufficient evidence",
            confidence="0.1",
            confidence_level=ConfidenceLevel.low,
            abstained=True,
        )
