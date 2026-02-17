# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExecutionPriceRetrieveParams"]


class ExecutionPriceRetrieveParams(TypedDict, total=False):
    amount: Required[float]
    """Requested order size in contracts."""

    parsec_id: Required[str]
    """Unified market ID in format `{exchange}:{native_id}`."""

    side: Required[Literal["buy", "sell"]]
    """Order side."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required.
    """
