# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PolymarketAuthCredentialsResponse"]


class PolymarketAuthCredentialsResponse(BaseModel):
    clob_api_key: str
    """Polymarket CLOB API key."""

    clob_api_passphrase: str
    """Polymarket CLOB API passphrase."""

    clob_api_secret: str
    """Polymarket CLOB API secret."""
