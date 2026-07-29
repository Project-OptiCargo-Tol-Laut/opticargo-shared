"""Deprecated import path for ML contracts; use :mod:`opticargo_shared.ml`."""

from opticargo_shared.ml import (
    AnomalyRequest,
    AnomalyResponse,
    ForecastRequest,
    ForecastResponse,
    ScoringRequest,
    ScoringResponse,
)

__all__ = [
    "AnomalyRequest",
    "AnomalyResponse",
    "ForecastRequest",
    "ForecastResponse",
    "ScoringRequest",
    "ScoringResponse",
]
