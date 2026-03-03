# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OnboardCreateParams"]


class OnboardCreateParams(TypedDict, total=False):
    customer_id: Required[str]
    """Parsec customer ID of the end-user to onboard."""

    exchange: Required[str]
    """Exchange to onboard ("polymarket" or "kalshi")."""

    mode: Required[Literal["managed", "self"]]
    """Managed = Parsec creates wallet + credentials. Self = you provide credentials."""

    api_key_id: str
    """Kalshi API key ID (self mode)."""

    chain_id: int
    """Chain ID for Safe wallet creation."""

    clob_api_key: str
    """Polymarket CLOB API key (self mode)."""

    clob_api_passphrase: str
    """Polymarket CLOB API passphrase (self mode)."""

    clob_api_secret: str
    """Polymarket CLOB API secret (self mode)."""

    eoa_address: str
    """External wallet address (required when wallet_type is "safe")."""

    private_key: str
    """Kalshi RSA private key in PEM format (self mode)."""

    wallet_type: str
    """Wallet type for managed mode ("eoa" or "safe")."""
