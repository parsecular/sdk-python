# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OnboardCreateResponse"]


class OnboardCreateResponse(BaseModel):
    exchange: str
    """Exchange that was onboarded."""

    linked_exchanges: List[str]
    """All exchanges linked to this account."""

    mode: str
    """Onboard mode used ("managed" or "self")."""

    status: str
    """Onboard status ("complete" or "already_linked")."""

    steps_completed: List[str]
    """Steps completed during this call."""

    eoa_address: Optional[str] = None
    """EOA wallet address (managed mode only)."""

    safe_address: Optional[str] = None
    """Safe wallet address (present when wallet_type is "safe")."""
