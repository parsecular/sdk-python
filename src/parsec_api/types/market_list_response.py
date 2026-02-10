# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MarketListResponse", "Market", "MarketOutcomeToken", "Meta", "Pagination"]


class MarketOutcomeToken(BaseModel):
    outcome: str

    token_id: str


class Market(BaseModel):
    id: str
    """Native exchange market ID."""

    description: str

    exchange: str

    market_type: str

    outcome_tokens: List[MarketOutcomeToken]

    outcomes: List[str]

    parsec_id: str
    """Primary key in format `{exchange}:{native_id}`."""

    status: Literal["active", "closed", "resolved"]

    title: str

    volume: int

    close_time: Optional[datetime] = None

    condition_id: Optional[str] = None

    group_id: Optional[str] = None

    liquidity: Optional[int] = None

    open_time: Optional[datetime] = None

    question: Optional[str] = None

    slug: Optional[str] = None

    token_id_no: Optional[str] = None

    token_id_yes: Optional[str] = None


class Meta(BaseModel):
    exchanges_queried: List[str]

    exchanges_succeeded: List[str]

    exchanges_failed: Optional[Dict[str, str]] = None


class Pagination(BaseModel):
    count: int

    has_more: bool

    total: int

    next_cursor: Optional[str] = None


class MarketListResponse(BaseModel):
    markets: List[Market]

    meta: Meta

    pagination: Pagination
