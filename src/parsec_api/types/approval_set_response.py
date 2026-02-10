# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ApprovalSetResponse", "Result"]


class Result(BaseModel):
    token: Literal["usdc", "ctf"]

    success: bool

    target: Literal["ctf_exchange", "neg_risk_ctf_exchange", "neg_risk_adapter"]

    tx_hash: Optional[str] = None

    error: Optional[str] = None


class ApprovalSetResponse(BaseModel):
    all_succeeded: bool

    results: List[Result]
