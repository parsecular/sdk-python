# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TradeListParams"]


class TradeListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response."""

    end_ts: int
    """Unix seconds end timestamp (inclusive)."""

    exchange: str
    """Exchange ID (alternative to parsec_id — use with market_id)."""

    limit: int
    """Max number of trades (default 200; server clamps to 1..=500)."""

    market_id: str
    """Exchange-native market ID (alternative to parsec_id — use with exchange)."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required and may be an outcome label or numeric
    index.
    """

    parsec_id: str
    """Unified market ID. Provide either `parsec_id` OR both `exchange` + `market_id`."""

    start_ts: int
    """Unix seconds start timestamp (inclusive)."""
