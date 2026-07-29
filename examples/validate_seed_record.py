from datetime import UTC, datetime

from opticargo_shared.dataset import DatasetManifest
from opticargo_shared.version import __version__

manifest = DatasetManifest(
    dataset_name="competition-seed",
    dataset_version="2026.07.29",
    created_at=datetime.now(UTC),
    source_type="synthetic",
    source_references=["generator:opticargo-data:v1"],
    is_synthetic=True,
    record_count=100,
    schema_package_version=__version__,
    checksum="sha256:example",
)
print(manifest.model_dump_json(indent=2))
