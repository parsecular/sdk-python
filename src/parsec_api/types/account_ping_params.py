# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountPingParams"]


class AccountPingParams(TypedDict, total=False):
    exchange: str
    """Optional exchange ID to ping; if omitted, pings all available exchanges."""
