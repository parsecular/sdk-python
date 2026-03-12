# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExecutionPriceRetrieveParams"]


class ExecutionPriceRetrieveParams(TypedDict, total=False):
    amount: Required[float]
    """Order size in contracts."""

    side: Required[Literal["buy", "sell"]]
    """Order side ("buy" or "sell")."""

    exchange: str
    """Exchange ID (alternative to parsec_id — use with market_id)."""

    market_id: str
    """Exchange-native market ID (alternative to parsec_id — use with exchange)."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required.
    """

    parsec_id: str
    """Unified market ID. Provide either `parsec_id` OR both `exchange` + `market_id`."""
