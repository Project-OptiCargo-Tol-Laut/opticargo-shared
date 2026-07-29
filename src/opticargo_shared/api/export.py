from typing import Annotated, Any, Self
from uuid import UUID

from pydantic import AwareDatetime, Field, model_validator

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import ExportFormat, ReportStatus


class ExportRequest(ContractModel):
    format: ExportFormat
    filters: dict[str, Any] = Field(default_factory=dict)


class ExportJob(ContractModel):
    id: UUID
    report_type: Annotated[str, Field(min_length=1)]
    format: ExportFormat
    status: ReportStatus
    requested_by: UUID
    created_at: AwareDatetime
    completed_at: AwareDatetime | None = None
    download_url: str | None = None
    expires_at: AwareDatetime | None = None
    error: str | None = None

    @model_validator(mode="after")
    def validate_result(self) -> Self:
        if self.status == ReportStatus.completed:
            if self.completed_at is None or self.download_url is None:
                raise ValueError(
                    "completed_at and download_url are required for a completed export"
                )
        if self.status == ReportStatus.failed and not self.error:
            raise ValueError("error is required for a failed export")
        return self
