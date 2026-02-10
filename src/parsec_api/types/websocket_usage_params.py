# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebsocketUsageParams"]


class WebsocketUsageParams(TypedDict, total=False):
    limit: int
    """
    Max number of markets/customers returned (default 20; server clamps to 1..=100).
    """

    scope: str
    """\"self" (default) or "global" (admin only)."""
