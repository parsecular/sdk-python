# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    id: str

    created_at: datetime

    filled: float

    market_id: str

    outcome: str

    price: float

    side: Literal["buy", "sell"]

    size: float

    status: Literal["pending", "open", "filled", "partially_filled", "cancelled", "rejected"]

    updated_at: Optional[datetime] = None
