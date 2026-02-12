# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Tuple, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrderbookRetrieveResponse", "OrderbookLevel"]

# Stainless currently models `[price, size]` levels as `List[List[float]]`.
# The wire format is still a JSON array, but the fixed length is important for
# consumers and we can enforce it at runtime via pydantic.
OrderbookLevel = Tuple[float, float]


class OrderbookRetrieveResponse(BaseModel):
    asks: List[OrderbookLevel]

    bids: List[OrderbookLevel]

    exchange: str

    market_id: str

    outcome: str

    parsec_id: str

    timestamp: Optional[datetime] = None

    token_id: str
