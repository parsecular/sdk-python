# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CtfMergeParams"]


class CtfMergeParams(TypedDict, total=False):
    amount: Required[str]
    """USDC amount in smallest unit (6 decimals)."""

    condition_id: Required[str]
    """Condition ID (bytes32 hex)."""
