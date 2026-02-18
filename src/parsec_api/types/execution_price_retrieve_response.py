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

    slippage: Optional[float] = None
    """Price impact vs best price (null if no liquidity)."""
