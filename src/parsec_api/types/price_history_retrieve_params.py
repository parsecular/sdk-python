# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PriceHistoryRetrieveParams"]


class PriceHistoryRetrieveParams(TypedDict, total=False):
    interval: Required[Literal["1m", "1h", "6h", "1d", "1w", "max"]]
    """Price history interval."""

    parsec_id: Required[str]
    """Unified market ID in format `{exchange}:{native_id}`."""

    end_ts: int
    """Unix seconds end timestamp (inclusive). Defaults to now."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required and may be an outcome label or numeric
    index.
    """

    start_ts: int
    """Unix seconds start timestamp (inclusive).

    If omitted, the server selects a default range based on `interval`.
    """
