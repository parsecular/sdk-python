# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MarketListParams"]


class MarketListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (offset-based)."""

    exchanges: SequenceNotStr[str]
    """Exchanges to query.

    In SDKs this is typically an array encoded as CSV on the wire. Required unless
    `parsec_ids` is provided.
    """

    limit: int
    """Results per page (default 100)."""

    min_liquidity: int
    """Minimum liquidity filter."""

    min_volume: int
    """Minimum volume filter."""

    parsec_ids: SequenceNotStr[str]
    """
    Parsec market IDs to fetch directly (format: `{exchange}:{native_id}`). In SDKs
    this is typically an array encoded as CSV on the wire. Required unless
    `exchanges` is provided.
    """

    search: str
    """Keyword search in title/description/question (case-insensitive)."""

    status: Literal["active", "closed", "resolved"]
    """Status filter."""
