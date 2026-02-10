# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrderbookRetrieveParams"]


class OrderbookRetrieveParams(TypedDict, total=False):
    parsec_id: Required[str]
    """Unified market ID in format `{exchange}:{native_id}`."""

    depth: int
    """Alias for `limit` (REST/WS symmetry)."""

    limit: int
    """Max depth per side (default 50; server clamps to 1..=100)."""

    outcome: str
    """Outcome selector.

    For binary markets this is typically "yes" or "no" (case-insensitive). For
    categorical markets, this is required and may be an outcome label or numeric
    index.
    """
