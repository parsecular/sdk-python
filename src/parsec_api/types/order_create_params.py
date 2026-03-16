# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderCreateParams", "Credentials", "FeeAuth"]


class OrderCreateParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., polymarket, kalshi, limitless, opinion, predictfun)."""

    market_id: Required[str]

    outcome: Required[str]

    price: Required[float]

    side: Required[Literal["buy", "sell"]]

    size: Required[float]

    affiliate: str
    """Affiliate address override. Builder-only."""

    credentials: Credentials
    """
    Per-request exchange credentials passed in the `X-Exchange-Credentials` header.
    Parsec creates a transient exchange session instead of using stored credentials.
    For Polymarket transient sessions, `private_key` is required; CLOB API
    credentials are optional. Credentials are never persisted.
    """

    fee_auth: FeeAuth
    """EIP-712 fee authorization signed by the end-user's wallet.

    Required to collect fees via fee escrow. Builder-only.
    """

    params: Dict[str, str]
    """Optional key-value parameters. Supported keys:

    - `order_type`: Order time-in-force. Values: `gtc` (default), `ioc`, `fok`,
      `gtd`. Unsupported types return 501 per exchange.
    - `expiration`: Unix timestamp in seconds. Required when `order_type` is `gtd`
      (must be at least 60s in the future). Polymarket only.
    """

    payer_address: str
    """End-user's wallet address (fee escrow payer). Builder-only."""

    signer_address: str
    """End-user's signing wallet address. Builder-only."""

    x_exchange_credentials: Annotated[str, PropertyInfo(alias="X-Exchange-Credentials")]


class Credentials(TypedDict, total=False):
    """
    Per-request exchange credentials passed in the `X-Exchange-Credentials` header.
    Parsec creates a transient exchange session instead of using stored credentials.
    For Polymarket transient sessions, `private_key` is required; CLOB API
    credentials are optional.
    Credentials are never persisted.
    """

    api_key_id: str
    """Kalshi API key ID."""

    clob_api_key: str
    """Optional Polymarket CLOB API key."""

    clob_api_passphrase: str
    """Optional Polymarket CLOB API passphrase."""

    clob_api_secret: str
    """Optional Polymarket CLOB API secret."""

    private_key: str
    """
    Kalshi RSA private key (PEM) or Polymarket wallet private key (`0x`-prefixed
    hex).
    """


class FeeAuth(TypedDict, total=False):
    """EIP-712 fee authorization signed by the end-user's wallet.

    Required to collect fees via fee escrow. Builder-only.
    """

    deadline: Required[int]
    """Unix timestamp after which the authorization expires."""

    fee_amount: Required[str]
    """Fee in USDC base units (6 decimals), as a string."""

    order_id: Required[str]
    """0x-prefixed hex bytes32 order identifier."""

    payer: Required[str]
    """0x-prefixed payer wallet address."""

    signature: Required[str]
    """0x-prefixed hex EIP-712 signature."""
