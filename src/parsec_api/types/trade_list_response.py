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

    id: Optional[str] = None

    aggressor_side: Optional[str] = None
    """Aggressor side (typically "buy" or "sell")."""

    no_price: Optional[float] = None
    """NO-side price from exchange data (never derived).

    May be null if the trade was on the YES side.
    """

    outcome: Optional[str] = None
    """Trade outcome side (e.g. "Yes", "No", "yes", "no")."""

    side: Optional[str] = None
    """Trade side (typically "buy" or "sell")."""

    taker_address: Optional[str] = None
    """Taker wallet address (Polymarket proxy_wallet).

    Null for exchanges that don't expose this.
    """

    tx_hash: Optional[str] = None
    """Transaction hash (Polymarket only)."""

    yes_price: Optional[float] = None
    """YES-side price from exchange data (never derived).

    May be null if the trade was on the NO side.
    """


class TradeListResponse(BaseModel):
    exchange: str

    market_id: str

    outcome: str

    parsec_id: str

    trades: List[Trade]

    has_more: Optional[bool] = None
    """True if there are more results available"""

    next_cursor: Optional[str] = None

    reason: Optional[str] = None
    """Explanatory field for empty results.

    Values: null (normal), "no_data_yet" (market exists but has no trade data for
    the requested range).
    """

    token_id: Optional[str] = None
    """Exchange-specific token/asset identifier.

    Null for exchanges that do not use token IDs (e.g., Kalshi).
    """
