# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["PositionListResponse", "PositionListResponseItem"]


class PositionListResponseItem(BaseModel):
    average_price: float

    current_price: float

    market_id: str

    outcome: str

    size: float


PositionListResponse: TypeAlias = List[PositionListResponseItem]
