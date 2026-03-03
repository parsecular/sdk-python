# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PolymarketAuthMessageResponse"]


class PolymarketAuthMessageResponse(BaseModel):
    timestamp: str
    """Timestamp used in the typed data."""

    typed_data: object
    """EIP-712 typed data to sign with your wallet."""
