# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["AccountUserActivityResponse", "Status"]


class Status(BaseModel):
    success: bool

    error: Optional[str] = None


class AccountUserActivityResponse(BaseModel):
    exchanges: Dict[str, object]

    status: Dict[str, Status]
