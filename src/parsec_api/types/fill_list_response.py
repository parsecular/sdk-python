# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["FillListResponse", "FillListResponseItem"]


class FillListResponseItem(BaseModel):
    created_at: datetime
    """Timestamp of the fill (ISO 8601)."""

    fee: float
    """Fee charged for this fill."""

    fill_id: str
    """Unique fill identifier."""

    is_taker: bool
    """Whether this fill was a taker (market order hitting resting liquidity)."""

    market_id: str
    """Market the fill occurred on (exchange-native ID)."""

    order_id: str
    """ID of the order that was filled."""

    outcome: str
    """The outcome traded (e.g., "Yes" or "No")."""

    price: float
    """Execution price."""

    side: Literal["buy", "sell"]

    size: float
    """Number of contracts filled."""


FillListResponse: TypeAlias = List[FillListResponseItem]
