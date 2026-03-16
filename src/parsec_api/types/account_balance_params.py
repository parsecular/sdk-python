# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountBalanceParams"]


class AccountBalanceParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., polymarket, kalshi, limitless, opinion, predictfun)."""

    refresh: bool
    """Refresh balance before returning (default false)."""

    x_exchange_credentials: Annotated[str, PropertyInfo(alias="X-Exchange-Credentials")]
