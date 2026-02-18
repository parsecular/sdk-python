# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AccountCapabilitiesResponse"]


class AccountCapabilitiesResponse(BaseModel):
    linked_exchanges: List[str]
    """Exchange IDs the customer has credentials linked for."""

    tier: str
    """Customer tier (e.g., "free", "pro", "admin")."""
