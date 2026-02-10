# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AccountUserActivityParams"]


class AccountUserActivityParams(TypedDict, total=False):
    address: Required[str]
    """User address (typically an EVM address)."""

    exchanges: SequenceNotStr[str]
    """Exchanges to query (CSV).

    Defaults to: polymarket, opinion, limitless, predictfun. In SDKs this is
    typically an array encoded as CSV on the wire.
    """

    limit: int
    """Max number of items per exchange (default 100)."""
