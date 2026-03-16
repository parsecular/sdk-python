# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (offset-based). Only valid for list mode."""

    event_id: str
    """Exact event lookup by stored event-group ID.

    The `ev:{event_id}` alias form is also accepted. Mutually exclusive with
    `exchange` + `exchange_group_id`.
    """

    exchange: str
    """Exchange selector for exact external event lookup.

    Must be paired with `exchange_group_id`.
    """

    exchange_group_id: str
    """Exchange-native event/group ID. Must be paired with `exchange`."""

    exchanges: SequenceNotStr[str]
    """Exchanges to include (CSV).

    Defaults to all exchanges in the cache. Only valid for list mode.
    """

    include_markets: bool
    """Include constituent markets in the response (default false)."""

    limit: int
    """Results per page (default 50, max 100). Only valid for list mode."""

    min_volume: float
    """Minimum total volume across all markets in event. Only valid for list mode."""

    search: str
    """Keyword search in event title (case-insensitive). Only valid for list mode."""

    status: str
    """Status filter (e.g., active, closed, resolved, archived).

    Only valid for list mode.
    """
