# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TradeListParams"]


class TradeListParams(TypedDict, total=False):
    parsec_id: Required[str]
    """Unified market ID in format `{exchange}:{native_id}`."""

    end_ts: int
    """Unix seconds end timestamp (inclusive)."""

    limit: int
    """Max number of trades (default 200; server clamps to 1..=500)."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required and may be an outcome label or numeric
    index.
    """

    start_ts: int
    """Unix seconds start timestamp (inclusive)."""
