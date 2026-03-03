# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CtfResponse"]


class CtfResponse(BaseModel):
    status: Optional[str] = None
    """Relayer transaction status."""

    transaction_hash: Optional[str] = None
    """On-chain transaction hash."""
