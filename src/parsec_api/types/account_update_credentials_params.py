# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountUpdateCredentialsParams"]


class AccountUpdateCredentialsParams(TypedDict, total=False):
    evm_private_key: Optional[str]

    kalshi_api_key_id: Optional[str]

    kalshi_private_key: Optional[str]

    poly_funder: Optional[str]

    poly_signature_type: Optional[str]
