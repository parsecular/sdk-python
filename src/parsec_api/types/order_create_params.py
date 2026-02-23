# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrderCreateParams", "Credentials"]


class OrderCreateParams(TypedDict, total=False):
    exchange: Required[str]
    """Exchange identifier (e.g., kalshi, polymarket)."""

    market_id: Required[str]

    outcome: Required[str]

    price: Required[float]

    side: Required[Literal["buy", "sell"]]

    size: Required[float]

    credentials: Credentials
    """Per-request exchange credentials (Mode B).

    When provided, Parsec creates a transient exchange session instead of using
    stored credentials. Credentials are never persisted.
    """

    params: Dict[str, str]
    """Optional key-value parameters. Supported keys:

    - `order_type`: Order time-in-force. Values: `gtc` (default), `ioc`, `fok`.
      Unsupported types return 501 per exchange.
    """

    x_exchange_credentials: Annotated[str, PropertyInfo(alias="X-Exchange-Credentials")]


class Credentials(TypedDict, total=False):
    """Per-request exchange credentials (Mode B).

    When provided, Parsec creates a transient
    exchange session instead of using stored credentials. Credentials are never persisted.
    """

    api_key_id: str
    """Kalshi API key ID."""

    clob_api_key: str
    """Polymarket CLOB API key."""

    clob_api_passphrase: str
    """Polymarket CLOB API passphrase."""

    clob_api_secret: str
    """Polymarket CLOB API secret."""

    private_key: str
    """Kalshi RSA private key (PEM format)."""
