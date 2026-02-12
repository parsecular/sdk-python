# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TradeListResponse", "Trade"]


class Trade(BaseModel):
    price: float
    """Trade price (normalized 0.0-1.0)."""

    size: float
    """Trade size in contracts."""

    source_channel: str

    timestamp: datetime

    aggressor_side: Optional[str] = None
    """Aggressor side (typically "buy" or "sell")."""

    side: Optional[str] = None
    """Trade side (typically "buy" or "sell")."""

    trade_id: Optional[str] = None


class TradeListResponse(BaseModel):
    exchange: str

    market_id: str

    outcome: str

    parsec_id: str

    token_id: str

    trades: List[Trade]
