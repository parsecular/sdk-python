# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ApprovalSetParams"]


class ApprovalSetParams(TypedDict, total=False):
    exchange: Required[str]
    """Must be "polymarket"."""

    all: bool

    ctf: bool

    ctf_neg_risk: bool

    usdc: bool

    usdc_neg_risk: bool
