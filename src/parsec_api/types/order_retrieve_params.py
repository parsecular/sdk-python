# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrderRetrieveParams"]


class OrderRetrieveParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., kalshi, polymarket)."""
