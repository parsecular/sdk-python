# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderListParams"]


class OrderListParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., polymarket, kalshi, limitless, opinion, predictfun)."""

    end_ts: int
    """Filter orders created at or before this Unix timestamp (seconds)."""

    limit: int
    """Max orders to return.

    For `status=closed|all`, defaults to 100 and clamps to 1..=500.
    """

    market_id: str
    """Optional market ID filter (exchange-native)."""

    start_ts: int
    """Filter orders created at or after this Unix timestamp (seconds)."""

    status: Literal["open", "closed", "all"]
    """Order status view.

    `open` returns active orders, `closed` returns terminal orders, and `all`
    returns both. Defaults to `open`.
    """

    x_exchange_credentials: Annotated[str, PropertyInfo(alias="X-Exchange-Credentials")]
