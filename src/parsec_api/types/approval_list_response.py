# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ApprovalListResponse", "ApprovalListResponseItem"]


class ApprovalListResponseItem(BaseModel):
    token: Literal["usdc", "ctf"]

    approved: bool

    details: str

    target: Literal["ctf_exchange", "neg_risk_ctf_exchange", "neg_risk_adapter"]


ApprovalListResponse: TypeAlias = List[ApprovalListResponseItem]
