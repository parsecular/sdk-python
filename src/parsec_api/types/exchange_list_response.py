# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExchangeListResponse", "ExchangeCapability", "CapabilityMap"]


class CapabilityMap(BaseModel):
    create_order: bool
    fetch_markets: bool
    websocket: bool


class ExchangeCapability(BaseModel):
    id: str
    """Exchange identifier (e.g., "polymarket", "kalshi")."""

    name: str
    """Human-readable exchange name."""

    has: CapabilityMap


ExchangeListResponse: TypeAlias = List[ExchangeCapability]
