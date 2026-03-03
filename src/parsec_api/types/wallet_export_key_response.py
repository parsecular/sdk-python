# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WalletExportKeyResponse"]


class WalletExportKeyResponse(BaseModel):
    private_key: str
    """Hex-encoded private key (0x-prefixed)."""
