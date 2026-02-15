# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PriceHistoryRetrieveResponse", "Candle"]


class Candle(BaseModel):
    close: float
    """Close price (normalized 0.0-1.0)."""

    high: float
    """High price (normalized 0.0-1.0)."""

    low: float
    """Low price (normalized 0.0-1.0)."""

    open: float
    """Open price (normalized 0.0-1.0)."""

    timestamp: datetime
    """Period start timestamp (UTC)."""

    volume: float
    """Trade volume in contracts."""

    open_interest: Optional[float] = None
    """Open interest at this candle's close."""


class PriceHistoryRetrieveResponse(BaseModel):
    candles: List[Candle]

    exchange: str

    interval: Literal["1m", "1h", "6h", "1d", "1w", "max"]

    outcome: str

    parsec_id: str
