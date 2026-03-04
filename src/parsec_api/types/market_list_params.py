# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MarketListParams"]


class MarketListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (offset-based)."""

    event_id: str
    """Canonical Parsec event ID filter (exact match)."""

    exchanges: SequenceNotStr[str]
    """Exchanges to query.

    In SDKs this is typically an array encoded as CSV on the wire. Required unless
    `parsec_ids` is provided.
    """

    group_id: str
    """Source-native exchange event/group ID filter (exact match)."""

    include_matches: bool
    """
    When true, each market includes a `matched_markets` array with cross-exchange
    same-market relations.
    """

    include_related: bool
    """
    When true, each market includes a `related_markets` array with co-dependent
    market relations.
    """

    limit: int
    """Results per page (default 100, max 100)."""

    min_liquidity: float
    """Minimum liquidity filter."""

    min_volume: float
    """Minimum volume filter."""

    parsec_ids: SequenceNotStr[str]
    """
    Parsec market IDs to fetch directly (format: `{exchange}:{native_id}`). In SDKs
    this is typically an array encoded as CSV on the wire. Required unless
    `exchanges` is provided.
    """

    search: str
    """Keyword search in question/description (case-insensitive)."""

    status: str
    """Status filter (e.g., active, closed, resolved, archived)."""
