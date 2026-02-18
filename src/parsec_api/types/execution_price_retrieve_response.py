# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExecutionPriceRetrieveResponse"]


class ExecutionPriceRetrieveResponse(BaseModel):
    filled_amount: float
    """Number of contracts that would be filled."""

    fully_filled: bool
    """True if the entire requested amount can be filled."""

    levels_consumed: int
    """Number of orderbook levels consumed."""

    total_cost: float
    """Total cost of the filled portion."""

    avg_price: Optional[float] = None
    """Volume-weighted average execution price (null if no liquidity)."""

    fee_estimate: Optional[float] = None
    """Estimated exchange fee (null when fee rate is unknown)."""

    net_cost: Optional[float] = None
    """Total cost including fees (total_cost + fee_estimate).

    Null when fee rate is unknown.
    """

    slippage: Optional[float] = None
    """Price impact vs best price (null if no liquidity)."""

    worst_price: Optional[float] = None
    """Price of the last consumed orderbook level (worst fill price).

    Null if no liquidity.
    """
