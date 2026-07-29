"""Framework-independent contracts shared across OptiCargo services."""

from .base import ContractModel
from .version import __version__

__all__ = ["ContractModel", "__version__"]
