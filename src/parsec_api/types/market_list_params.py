# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["MarketListParams"]


class MarketListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor (offset-based). Only valid for `scope=list`."""

    event_id: str
    """Canonical Parsec event ID (exact match).

    Used for `scope=event`. Mutually exclusive with `exchange` +
    `exchange_group_id`.
    """

    exchange: str
    """
    Exchange selector for external-ID lookups. Used with `exchange_market_id` for
    `scope=market`, or with `exchange_group_id` for `scope=event`.
    """

    exchange_group_id: str
    """Exchange-native event/group ID.

    Must be paired with `exchange` for `scope=event`. Mutually exclusive with
    `event_id`.
    """

    exchange_market_id: str
    """Exchange-native market ID.

    Must be paired with `exchange` for `scope=market`. Mutually exclusive with
    `parsec_id`.
    """

    exchanges: SequenceNotStr[str]
    """
    Comma-separated exchange IDs to query (e.g., `polymarket,kalshi`). Only valid
    for `scope=list`. In SDKs this is typically an array encoded as CSV on the wire.
    """

    external_market_keys: str
    """
    Comma-separated external market keys in format
    `{exchange}:{exchange_market_id}`. Only valid for `scope=market_batch`. Mutually
    exclusive with `parsec_ids`.
    """

    include_matches: bool
    """
    When true, each market includes a `matched_markets` array with cross-exchange
    same-market relations.
    """

    include_related: bool
    """
    When true, each market includes a `related_markets` array with co-dependent
    market relations.
    """

    limit: int
    """Results per page (default 100, max 100)."""

    min_liquidity: float
    """Minimum liquidity filter. Only valid for `scope=list`."""

    min_volume: float
    """Minimum volume filter. Only valid for `scope=list`."""

    parsec_id: str
    """
    Single canonical parsec ID for direct lookup (format: `{exchange}:{native_id}`).
    Only valid for `scope=market`. Mutually exclusive with `exchange` +
    `exchange_market_id`.
    """

    parsec_ids: SequenceNotStr[str]
    """
    Comma-separated parsec IDs for batch lookup (format: `{exchange}:{native_id}`).
    Only valid for `scope=market_batch`. Max 100 IDs. Mutually exclusive with
    `external_market_keys`. In SDKs this is typically an array encoded as CSV on the
    wire.
    """

    scope: Literal["list", "market", "market_batch", "event"]
    """Query scope.

    Determines which parameters are valid and how results are returned. One of:
    `list` (default), `market`, `market_batch`, `event`.
    """

    search: str
    """Keyword search in question/description (case-insensitive).

    Only valid for `scope=list`.
    """

    status: str
    """Status filter (e.g., active, closed, resolved, archived).

    Defaults to `active` for `scope=list`.
    """
