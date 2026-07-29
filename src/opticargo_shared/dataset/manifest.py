from typing import Annotated

from pydantic import AwareDatetime, Field

from opticargo_shared.base import ContractModel


class DatasetManifest(ContractModel):
    dataset_name: Annotated[str, Field(min_length=1)]
    dataset_version: Annotated[str, Field(min_length=1)]
    created_at: AwareDatetime
    source_type: Annotated[str, Field(min_length=1)]
    source_references: list[str] = Field(default_factory=list)
    is_synthetic: bool
    record_count: int = Field(ge=0)
    schema_package_version: Annotated[str, Field(min_length=1)]
    checksum: Annotated[str, Field(min_length=1)]
