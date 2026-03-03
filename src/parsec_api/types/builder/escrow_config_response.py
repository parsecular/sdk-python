# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EscrowConfigResponse"]


class EscrowConfigResponse(BaseModel):
    affiliate_fee_bps: int
    """Affiliate fee rate in basis points."""

    escrow_contract_address: str
    """Escrow smart contract address."""

    fee_escrow_enabled: bool
    """Whether fee escrow is enabled for this builder."""

    min_fee_bps: int
    """Minimum fee in basis points."""

    min_fee_usdc: str
    """Minimum fee in USDC (human-readable)."""

    treasury_address: str
    """Treasury address for fee distribution."""

    affiliate_address: Optional[str] = None
    """Affiliate fee recipient address."""

    fee_bps: Optional[int] = None
    """Fee rate in basis points."""
