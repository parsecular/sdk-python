# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrderbookRetrieveResponse"]


class OrderbookRetrieveResponse(BaseModel):
    asks: List[List[float]]

    bids: List[List[float]]

    exchange: str

    market_id: str

    outcome: str

    parsec_id: str

    timestamp: Optional[datetime] = None

    token_id: str
