# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CtfRedeemParams"]


class CtfRedeemParams(TypedDict, total=False):
    condition_id: Required[str]
    """Condition ID (bytes32 hex)."""

    amounts: SequenceNotStr[str]
    """Token amounts for each outcome (required when neg_risk is true)."""

    neg_risk: bool
    """Set to true for neg-risk (multi-outcome) markets."""
