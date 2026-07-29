from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from opticargo_shared.api import (
    CursorMeta,
    ErrorResponse,
    ExportJob,
    PageMeta,
    PageParams,
    PageResponse,
)
from opticargo_shared.enums import ExportFormat, ReportStatus


def test_page_and_cursor_contracts() -> None:
    assert PageParams().page_size == 20
    response = PageResponse[str](
        items=["one"],
        meta=PageMeta(page=1, page_size=20, total_items=1, total_pages=1),
    )
    assert response.meta.total_items == 1
    assert CursorMeta(next_cursor=None, has_more=False).has_more is False
    with pytest.raises(ValidationError):
        PageParams(page_size=101)


def test_error_uses_canonical_code_and_required_trace() -> None:
    trace_id = uuid4()
    error = ErrorResponse(
        error_code="VALIDATION_ERROR",
        message="Invalid input",
        details={"field": "email"},
        trace_id=trace_id,
    )
    assert error.code == "VALIDATION_ERROR"
    assert error.error_code == error.code
    assert "error_code" not in error.model_dump()
    with pytest.raises(ValidationError):
        ErrorResponse(code="INTERNAL_ERROR", message="Failure")


def test_export_completed_requires_result_metadata() -> None:
    now = datetime.now(UTC)
    completed = ExportJob(
        id=uuid4(),
        report_type="utilization",
        format=ExportFormat.xlsx,
        status=ReportStatus.completed,
        requested_by=uuid4(),
        created_at=now,
        completed_at=now,
        download_url="https://signed.example/report",
        expires_at=now,
    )
    assert completed.status == ReportStatus.completed
    with pytest.raises(ValidationError, match="download_url"):
        ExportJob(
            id=uuid4(),
            report_type="utilization",
            format=ExportFormat.xlsx,
            status=ReportStatus.completed,
            requested_by=uuid4(),
            created_at=now,
            completed_at=now,
        )
