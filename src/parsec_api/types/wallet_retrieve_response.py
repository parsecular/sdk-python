# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WalletRetrieveResponse", "LinkedExchange", "Wallet", "WalletBalance", "SessionSigner"]


class LinkedExchange(BaseModel):
    exchange: str
    """Exchange identifier."""

    has_credentials: bool
    """Whether credentials are stored for this exchange."""


class WalletBalance(BaseModel):
    token: str
    """Token symbol (e.g. "USDC")."""

    balance: str
    """Human-readable balance (e.g. "100.50")."""

    decimals: int
    """Token decimal places."""

    raw_balance: str
    """Raw balance in smallest unit (e.g. "100500000")."""

    contract_address: Optional[str] = None
    """ERC-20 contract address. Null for native token."""


class Wallet(BaseModel):
    eoa_address: str
    """EVM wallet address on Polygon."""

    privy_wallet_id: str
    """Privy wallet identifier."""

    wallet_type: str
    """Wallet type ("eoa" or "safe")."""

    balances: Optional[List[WalletBalance]] = None
    """Token balances for this wallet."""

    chain_id: Optional[int] = None
    """Chain ID for the wallet (e.g. 137 for Polygon)."""

    created_at: Optional[datetime] = None
    """Wallet creation timestamp."""

    safe_address: Optional[str] = None
    """Safe wallet address (present when wallet_type is "safe")."""


class SessionSigner(BaseModel):
    active: bool
    """Whether the session signer is currently active."""

    expires_at: Optional[datetime] = None
    """Session signer expiration timestamp."""

    signer_id: Optional[str] = None
    """Session signer identifier."""


class WalletRetrieveResponse(BaseModel):
    linked_exchanges: List[LinkedExchange]

    wallets: List[Wallet]
    """All wallets associated with this account."""

    session_signer: Optional[SessionSigner] = None

    wallet: Optional[Wallet] = None
