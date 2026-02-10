# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrderCreateParams"]


class OrderCreateParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., kalshi, polymarket)."""

    market_id: Required[str]

    outcome: Required[str]

    price: Required[float]

    side: Required[Literal["buy", "sell"]]

    size: Required[float]

    params: Dict[str, str]
