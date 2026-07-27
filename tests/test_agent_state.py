import pytest
from uuid import uuid4
from decimal import Decimal
from pydantic import ValidationError
from opticargo_shared.agent_state.base import BaseAgentState
from opticargo_shared.agent_state.graph_analysis import (
    GraphAnalysisInput, 
    BackhaulCandidate, 
    GraphAnalysisOutput
)

def test_base_agent_state_valid():
    """Test instansiasi base state dengan request_id."""
    req_id = uuid4()
    state = BaseAgentState(request_id=req_id)
    assert state.request_id == req_id
    assert state.voyage_id is None
    assert state.trace == []

def test_graph_analysis_input_valid():
    """Test instansiasi state untuk Graph Analysis."""
    req_id = uuid4()
    port_id = uuid4()
    state = GraphAnalysisInput(
        request_id=req_id,
        origin_port_id=port_id,
        search_radius_days=14,
        trace=["IngestionAgent"]
    )
    assert state.search_radius_days == 14
    assert "IngestionAgent" in state.trace

def test_graph_analysis_input_invalid():
    """Test validasi gagal jika origin_port_id tidak disuplai (wajib)."""
    with pytest.raises(ValidationError):
        GraphAnalysisInput(  # type: ignore
            request_id=uuid4(),
            # origin_port_id hilang
        )

def test_backhaul_candidate_valid():
    """Test instansiasi DTO kandidat backhaul."""
    candidate = BackhaulCandidate(
        supplier_id=uuid4(),
        commodity_id=uuid4(),
        volume_ton=Decimal("150.5"),
        match_score=0.95
    )
    assert candidate.match_score == 0.95