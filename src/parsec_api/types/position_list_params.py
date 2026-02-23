# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PositionListParams"]


class PositionListParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., kalshi, polymarket)."""

    market_id: str
    """Optional market ID filter (exchange-native)."""

    x_exchange_credentials: Annotated[str, PropertyInfo(alias="X-Exchange-Credentials")]
