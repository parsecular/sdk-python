# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["OrderbookRetrieveResponse", "OrderbookResponse", "OrderbookHistoryResult", "OrderbookHistoryResultSnapshot"]


class OrderbookResponse(BaseModel):
    asks: List[List[float]]

    bids: List[List[float]]

    exchange: str

    market_id: str

    outcome: str

    parsec_id: str

    token_id: str

    min_order_size: Optional[float] = None
    """Minimum order size in contracts."""

    tick_size: Optional[float] = None
    """Minimum price increment for orders on this market."""

    timestamp: Optional[datetime] = None


class OrderbookHistoryResultSnapshot(BaseModel):
    asks: List[List[float]]

    bids: List[List[float]]

    timestamp: datetime

    hash: Optional[str] = None

    recorded_at: Optional[datetime] = None


class OrderbookHistoryResult(BaseModel):
    exchange: str

    has_more: bool

    market_id: str

    outcome: str

    parsec_id: str

    snapshots: List[OrderbookHistoryResultSnapshot]

    token_id: str

    min_order_size: Optional[float] = None

    next_cursor: Optional[str] = None

    tick_size: Optional[float] = None


OrderbookRetrieveResponse: TypeAlias = Union[OrderbookResponse, OrderbookHistoryResult]
