# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MarketListResponse", "Market", "MarketOutcome", "Pagination"]


class MarketOutcome(BaseModel):
    name: str
    """Outcome label (e.g., "Yes", "No", or a categorical name)."""

    price: Optional[float] = None
    """Last known price for this outcome (normalized 0.0-1.0)."""

    token_id: Optional[str] = None
    """Exchange-native token ID for this outcome."""


class Market(BaseModel):
    exchange: str

    exchange_group_id: str
    """Source-native exchange event/group ID."""

    exchange_market_id: str
    """Native exchange market ID."""

    group_title: str
    """Title of the group/event this market belongs to."""

    market_type: str
    """Market type (e.g., binary, categorical)."""

    outcomes: List[MarketOutcome]
    """Market outcomes with optional price and token ID."""

    parsec_group_id: str
    """Parsec group ID for cross-exchange event grouping."""

    parsec_id: str
    """Primary key in format `{exchange}:{native_id}`."""

    question: str
    """Market question text."""

    status: str
    """Market status. Common values: active, closed, resolved, archived."""

    volume_total: float
    """Total trading volume (USDC)."""

    best_ask: Optional[float] = None
    """Best ask price (normalized 0.0-1.0)."""

    best_bid: Optional[float] = None
    """Best bid price (normalized 0.0-1.0)."""

    collection_date: Optional[datetime] = None
    """Date when this market was first collected."""

    condition_id: Optional[str] = None
    """Exchange-native condition ID."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """Detailed market description."""

    end_date: Optional[datetime] = None
    """Market end/close date."""

    event_start_time: Optional[datetime] = None
    """Event start time."""

    last_collected: Optional[datetime] = None
    """Date of last data collection."""

    last_price: Optional[float] = None
    """Last traded price (normalized 0.0-1.0)."""

    liquidity: Optional[float] = None
    """Current liquidity (USDC)."""

    min_order_size: Optional[float] = None
    """Minimum order size in contracts.

    Varies per market on Polymarket (e.g. 5, 15); typically 1 on Kalshi.
    """

    open_interest: Optional[float] = None
    """Current open interest (contracts/pairs)."""

    outcome_count: Optional[int] = None
    """Number of outcomes in this market."""

    rules: Optional[str] = None
    """Market resolution rules."""

    slug: Optional[str] = None

    tick_size: Optional[float] = None
    """Minimum price increment for orders on this market."""

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
    """Direct URL to the market on the exchange."""

    volume_24h: Optional[float] = None
    """24-hour trading volume (USDC)."""

    xref: Optional[Dict[str, object]] = None
    """Cross-reference data (exchange-specific metadata)."""

    def _outcome(self, label: str) -> Optional[MarketOutcome]:
        target = label.lower()
        for outcome in self.outcomes:
            if outcome.name.lower() == target:
                return outcome
        return None

    @property
    def yes(self) -> Optional[MarketOutcome]:
        """Convenience getter for binary markets: outcome where name is \"Yes\"."""
        return self._outcome("yes")

    @property
    def no(self) -> Optional[MarketOutcome]:
        """Convenience getter for binary markets: outcome where name is \"No\"."""
        return self._outcome("no")


class Pagination(BaseModel):
    count: int
    """Number of items in this response."""

    has_more: bool
    """True if there are more results."""

    total: int
    """Total number of items matching the filters (before pagination)."""

    next_cursor: Optional[str] = None
    """Cursor for the next page (offset-based)."""


class MarketListResponse(BaseModel):
    markets: List[Market]

    pagination: Pagination
