# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UserUpdateResponse", "Wallet", "WalletBalance"]


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


class UserUpdateResponse(BaseModel):
    api_key: str
    """API key for this user."""

    customer_id: str
    """Parsec customer ID."""

    external_id: str
    """Your application's identifier for this user."""

    fee_escrow_enabled: bool
    """Whether fee escrow is enabled for this user."""

    linked_exchanges: List[str]
    """Exchanges linked to this user."""

    tier: str
    """User's tier."""

    affiliate_address: Optional[str] = None
    """Affiliate fee recipient address."""

    created_at: Optional[datetime] = None
    """User creation timestamp."""

    fee_bps: Optional[int] = None
    """Fee rate in basis points."""

    qps_limit: Optional[int] = None
    """Per-second rate limit allocated from builder's pool."""

    wallet: Optional[Wallet] = None
