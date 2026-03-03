# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    external_id: Required[str]
    """Your application's unique identifier for this user."""

    email: str
    """Optional email address for the user."""

    eoa_address: str
    """External EOA address (42-char hex, 0x-prefixed).

    Skips embedded wallet creation.
    """

    qps_limit: int
    """Per-second rate limit for this user. Deducted from builder's QPS pool."""
