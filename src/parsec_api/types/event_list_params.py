# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (offset-based)."""

    exchanges: SequenceNotStr[str]
    """Exchanges to include (CSV). Defaults to all exchanges in the cache."""

    include_markets: bool
    """Include constituent markets in the response (default false)."""

    limit: int
    """Results per page (default 50, max 100)."""

    min_volume: float
    """Minimum total volume across all markets in event."""

    search: str
    """Keyword search in event title (case-insensitive)."""

    status: str
    """Status filter (e.g., active, closed, resolved, archived)."""
