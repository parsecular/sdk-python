# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AccountPingResponse", "AccountPingResponseItem"]


class AccountPingResponseItem(BaseModel):
    authenticated: bool

    exchange: str

    has_credentials: bool

    message: str


AccountPingResponse: TypeAlias = List[AccountPingResponseItem]
