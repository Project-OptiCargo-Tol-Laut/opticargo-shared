from uuid import UUID

from pydantic import AwareDatetime

from opticargo_shared.base import ContractModel
from opticargo_shared.enums import ExportFormat, ReportStatus


class ReportPayload(ContractModel):
    report_id: UUID
    report_type: str
    format: ExportFormat
    status: ReportStatus
    requested_by: UUID
    completed_at: AwareDatetime | None = None
    error: str | None = None


ReportRequestedPayload = ReportPayload
ReportCompletedPayload = ReportPayload
ReportFailedPayload = ReportPayload
