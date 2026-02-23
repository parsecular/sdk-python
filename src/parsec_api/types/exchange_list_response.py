# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExchangeListResponse", "ExchangeListResponseItem", "ExchangeListResponseItemHas"]


class ExchangeListResponseItemHas(BaseModel):
    approvals: bool

    cancel_order: bool

    create_order: bool

    fetch_balance: bool

    fetch_events: bool

    fetch_markets: bool

    fetch_orderbook: bool

    fetch_orderbook_history: bool

    fetch_positions: bool

    fetch_price_history: bool

    fetch_trades: bool

    fetch_user_activity: bool

    refresh_balance: bool

    websocket: bool


class ExchangeListResponseItem(BaseModel):
    id: str
    """Exchange identifier (e.g., "polymarket", "kalshi")."""

    has: ExchangeListResponseItemHas

    name: str
    """Human-readable exchange name."""


ExchangeListResponse: TypeAlias = List[ExchangeListResponseItem]
