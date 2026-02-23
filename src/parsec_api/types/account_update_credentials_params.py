# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountUpdateCredentialsParams"]


class AccountUpdateCredentialsParams(TypedDict, total=False):
    api_key_id: Optional[str]
    """Kalshi API key ID."""

    clob_api_key: Optional[str]
    """Polymarket CLOB API key."""

    clob_api_passphrase: Optional[str]
    """Polymarket CLOB API passphrase."""

    clob_api_secret: Optional[str]
    """Polymarket CLOB API secret."""

    private_key: Optional[str]
    """Kalshi RSA private key (PEM format)."""
