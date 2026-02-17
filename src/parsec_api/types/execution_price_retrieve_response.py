# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExecutionPriceRetrieveResponse"]


class ExecutionPriceRetrieveResponse(BaseModel):
    filled_amount: float
    """Number of contracts that would be filled."""

    fully_filled: bool
    """True when the full requested amount is fillable from current depth."""

    levels_consumed: int
    """Number of orderbook levels consumed."""

    total_cost: float
    """Total notional cost of the filled amount."""

    avg_price: Optional[float] = None
    """Volume-weighted average execution price, or null when no liquidity is available."""

    slippage: Optional[float] = None
    """Price impact vs best price, or null when no liquidity is available."""
