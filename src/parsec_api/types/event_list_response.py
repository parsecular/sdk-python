# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "EventListResponse",
    "Event",
    "EventMarket",
    "EventMarketOutcome",
    "EventMarketMatchedMarket",
    "EventMarketRelatedMarket",
    "Pagination",
]


class EventMarketOutcome(BaseModel):
    name: str
    """Outcome label (e.g., "Yes", "No", or a categorical name)."""

    price: Optional[float] = None
    """Last known price for this outcome (normalized 0.0-1.0)."""

    token_id: Optional[str] = None
    """Exchange-native token ID for this outcome."""


class EventMarketMatchedMarket(BaseModel):
    confidence: float
    """Match confidence score (0.0–1.0)."""

    confidence_tier: str
    """Confidence tier: HIGH, MEDIUM, or LOW."""

    exchange: str
    """Exchange of the related market."""

    parsec_id: str
    """Parsec ID of the related market."""

    source: str
    """Source of the match (e.g., embedding, llm)."""

    dependency_direction: Optional[str] = None
    """Direction of dependency (for related markets only)."""

    dependency_type: Optional[str] = None
    """Type of dependency (for related markets only)."""


class EventMarketRelatedMarket(BaseModel):
    confidence: float
    """Match confidence score (0.0–1.0)."""

    confidence_tier: str
    """Confidence tier: HIGH, MEDIUM, or LOW."""

    exchange: str
    """Exchange of the related market."""

    parsec_id: str
    """Parsec ID of the related market."""

    source: str
    """Source of the match (e.g., embedding, llm)."""

    dependency_direction: Optional[str] = None
    """Direction of dependency (for related markets only)."""

    dependency_type: Optional[str] = None
    """Type of dependency (for related markets only)."""


class EventMarket(BaseModel):
    exchange: str

    exchange_group_id: str
    """Source-native exchange event/group ID."""

    exchange_market_id: str
    """Native exchange market ID."""

    group_title: str
    """Title of the group/event this market belongs to."""

    market_type: str
    """Market type (e.g., binary, categorical)."""

    outcomes: List[EventMarketOutcome]
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

    icon_url: Optional[str] = None
    """Market icon URL."""

    image_url: Optional[str] = None
    """Market image URL."""

    last_collected: Optional[datetime] = None
    """Date of last data collection."""

    last_price: Optional[float] = None
    """Last traded price (normalized 0.0-1.0)."""

    liquidity: Optional[float] = None
    """Current liquidity (USDC)."""

    matched_markets: Optional[List[EventMarketMatchedMarket]] = None
    """Cross-exchange same-market relations.

    Only included when `include_matches=true`.
    """

    min_order_size: Optional[float] = None
    """Minimum order size in contracts.

    Varies per market on Polymarket (e.g. 5, 15); typically 1 on Kalshi.
    """

    open_interest: Optional[float] = None
    """Current open interest (contracts/pairs)."""

    outcome_count: Optional[int] = None
    """Number of outcomes in this market."""

    price_updated_at: Optional[datetime] = None
    """
    When bid/ask/last_price was last refreshed (upgraded to now when live WS data
    overlays the snapshot).
    """

    related_markets: Optional[List[EventMarketRelatedMarket]] = None
    """Co-dependent market relations. Only included when `include_related=true`."""

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


class Event(BaseModel):
    event_id: str
    """Canonical Parsec event ID."""

    exchanges: List[str]
    """Deduplicated list of exchanges with markets in this event."""

    market_count: int
    """Number of markets in this event."""

    status: str
    """Event status. Common values: active, closed, resolved, archived."""

    title: str
    """Event title (derived from shortest constituent market title)."""

    total_volume: float
    """Sum of volume across all markets in this event."""

    close_time: Optional[datetime] = None
    """Earliest close time across constituent markets."""

    markets: Optional[List[EventMarket]] = None
    """Constituent markets (only included when `include_markets=true`)."""


class Pagination(BaseModel):
    count: int
    """Number of items in this response."""

    has_more: bool
    """True if there are more results."""

    total: int
    """Total number of items matching the filters (before pagination)."""

    next_cursor: Optional[str] = None
    """Cursor for the next page (offset-based)."""


class EventListResponse(BaseModel):
    events: List[Event]

    pagination: Pagination
