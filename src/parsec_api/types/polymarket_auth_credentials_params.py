# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PolymarketAuthCredentialsParams"]


class PolymarketAuthCredentialsParams(TypedDict, total=False):
    address: Required[str]
    """Your Ethereum wallet address."""

    signature: Required[str]
    """EIP-712 signature of the ClobAuth typed data."""

    timestamp: Required[str]
    """Timestamp from the auth message response."""

    store: bool
    """Set to true to store derived credentials for future use."""
