from uuid import UUID

from pydantic import AliasChoices, Field

from opticargo_shared.base import ContractModel


class BaseAgentState(ContractModel):
    correlation_id: UUID = Field(validation_alias=AliasChoices("correlation_id", "request_id"))
    voyage_id: UUID | None = None
    trace: list[str] = Field(default_factory=list)

    @property
    def request_id(self) -> UUID:
        """Deprecated source compatibility alias for pre-v1 consumers."""

        return self.correlation_id
