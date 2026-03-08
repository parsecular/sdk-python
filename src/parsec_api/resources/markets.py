# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import market_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.market_list_response import MarketListResponse

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        exchange: str | Omit = omit,
        exchange_group_id: str | Omit = omit,
        exchange_market_id: str | Omit = omit,
        exchanges: SequenceNotStr[str] | Omit = omit,
        external_market_keys: str | Omit = omit,
        include_matches: bool | Omit = omit,
        include_related: bool | Omit = omit,
        limit: int | Omit = omit,
        min_liquidity: float | Omit = omit,
        min_volume: float | Omit = omit,
        parsec_id: str | Omit = omit,
        parsec_ids: SequenceNotStr[str] | Omit = omit,
        scope: Literal["list", "market", "market_batch", "event"] | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Query markets using one of four scopes:

        - **`list`** (default) — Browse markets with optional filters. Pass `exchanges`
          to restrict to specific exchanges.
        - **`market`** — Fetch a single market by `parsec_id` or by `exchange` +
          `exchange_market_id`.
        - **`market_batch`** — Fetch up to 100 markets by `parsec_ids` or
          `external_market_keys`.
        - **`event`** — Fetch all markets in an event by `event_id` or by `exchange` +
          `exchange_group_id`.

        Each scope accepts a different set of parameters; see parameter descriptions for
        details.

        Args:
          cursor: Pagination cursor (offset-based). Only valid for `scope=list`.

          event_id: Canonical Parsec event ID (exact match). Used for `scope=event`. Mutually
              exclusive with `exchange` + `exchange_group_id`.

          exchange: Exchange selector for external-ID lookups. Used with `exchange_market_id` for
              `scope=market`, or with `exchange_group_id` for `scope=event`.

          exchange_group_id: Exchange-native event/group ID. Must be paired with `exchange` for
              `scope=event`. Mutually exclusive with `event_id`.

          exchange_market_id: Exchange-native market ID. Must be paired with `exchange` for `scope=market`.
              Mutually exclusive with `parsec_id`.

          exchanges: Comma-separated exchange IDs to query (e.g., `polymarket,kalshi`). Only valid
              for `scope=list`. In SDKs this is typically an array encoded as CSV on the wire.

          external_market_keys: Comma-separated external market keys in format
              `{exchange}:{exchange_market_id}`. Only valid for `scope=market_batch`. Mutually
              exclusive with `parsec_ids`.

          include_matches: When true, each market includes a `matched_markets` array with cross-exchange
              same-market relations.

          include_related: When true, each market includes a `related_markets` array with co-dependent
              market relations.

          limit: Results per page (default 100, max 100).

          min_liquidity: Minimum liquidity filter. Only valid for `scope=list`.

          min_volume: Minimum volume filter. Only valid for `scope=list`.

          parsec_id: Single canonical parsec ID for direct lookup (format: `{exchange}:{native_id}`).
              Only valid for `scope=market`. Mutually exclusive with `exchange` +
              `exchange_market_id`.

          parsec_ids: Comma-separated parsec IDs for batch lookup (format: `{exchange}:{native_id}`).
              Only valid for `scope=market_batch`. Max 100 IDs. Mutually exclusive with
              `external_market_keys`. In SDKs this is typically an array encoded as CSV on the
              wire.

          scope: Query scope. Determines which parameters are valid and how results are returned.
              One of: `list` (default), `market`, `market_batch`, `event`.

          search: Keyword search in question/description (case-insensitive). Only valid for
              `scope=list`.

          status: Status filter (e.g., active, closed, resolved, archived). Defaults to `active`
              for `scope=list`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "exchange": exchange,
                        "exchange_group_id": exchange_group_id,
                        "exchange_market_id": exchange_market_id,
                        "exchanges": exchanges,
                        "external_market_keys": external_market_keys,
                        "include_matches": include_matches,
                        "include_related": include_related,
                        "limit": limit,
                        "min_liquidity": min_liquidity,
                        "min_volume": min_volume,
                        "parsec_id": parsec_id,
                        "parsec_ids": parsec_ids,
                        "scope": scope,
                        "search": search,
                        "status": status,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )


class AsyncMarketsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        exchange: str | Omit = omit,
        exchange_group_id: str | Omit = omit,
        exchange_market_id: str | Omit = omit,
        exchanges: SequenceNotStr[str] | Omit = omit,
        external_market_keys: str | Omit = omit,
        include_matches: bool | Omit = omit,
        include_related: bool | Omit = omit,
        limit: int | Omit = omit,
        min_liquidity: float | Omit = omit,
        min_volume: float | Omit = omit,
        parsec_id: str | Omit = omit,
        parsec_ids: SequenceNotStr[str] | Omit = omit,
        scope: Literal["list", "market", "market_batch", "event"] | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """
        Query markets using one of four scopes:

        - **`list`** (default) — Browse markets with optional filters. Pass `exchanges`
          to restrict to specific exchanges.
        - **`market`** — Fetch a single market by `parsec_id` or by `exchange` +
          `exchange_market_id`.
        - **`market_batch`** — Fetch up to 100 markets by `parsec_ids` or
          `external_market_keys`.
        - **`event`** — Fetch all markets in an event by `event_id` or by `exchange` +
          `exchange_group_id`.

        Each scope accepts a different set of parameters; see parameter descriptions for
        details.

        Args:
          cursor: Pagination cursor (offset-based). Only valid for `scope=list`.

          event_id: Canonical Parsec event ID (exact match). Used for `scope=event`. Mutually
              exclusive with `exchange` + `exchange_group_id`.

          exchange: Exchange selector for external-ID lookups. Used with `exchange_market_id` for
              `scope=market`, or with `exchange_group_id` for `scope=event`.

          exchange_group_id: Exchange-native event/group ID. Must be paired with `exchange` for
              `scope=event`. Mutually exclusive with `event_id`.

          exchange_market_id: Exchange-native market ID. Must be paired with `exchange` for `scope=market`.
              Mutually exclusive with `parsec_id`.

          exchanges: Comma-separated exchange IDs to query (e.g., `polymarket,kalshi`). Only valid
              for `scope=list`. In SDKs this is typically an array encoded as CSV on the wire.

          external_market_keys: Comma-separated external market keys in format
              `{exchange}:{exchange_market_id}`. Only valid for `scope=market_batch`. Mutually
              exclusive with `parsec_ids`.

          include_matches: When true, each market includes a `matched_markets` array with cross-exchange
              same-market relations.

          include_related: When true, each market includes a `related_markets` array with co-dependent
              market relations.

          limit: Results per page (default 100, max 100).

          min_liquidity: Minimum liquidity filter. Only valid for `scope=list`.

          min_volume: Minimum volume filter. Only valid for `scope=list`.

          parsec_id: Single canonical parsec ID for direct lookup (format: `{exchange}:{native_id}`).
              Only valid for `scope=market`. Mutually exclusive with `exchange` +
              `exchange_market_id`.

          parsec_ids: Comma-separated parsec IDs for batch lookup (format: `{exchange}:{native_id}`).
              Only valid for `scope=market_batch`. Max 100 IDs. Mutually exclusive with
              `external_market_keys`. In SDKs this is typically an array encoded as CSV on the
              wire.

          scope: Query scope. Determines which parameters are valid and how results are returned.
              One of: `list` (default), `market`, `market_batch`, `event`.

          search: Keyword search in question/description (case-insensitive). Only valid for
              `scope=list`.

          status: Status filter (e.g., active, closed, resolved, archived). Defaults to `active`
              for `scope=list`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/markets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "exchange": exchange,
                        "exchange_group_id": exchange_group_id,
                        "exchange_market_id": exchange_market_id,
                        "exchanges": exchanges,
                        "external_market_keys": external_market_keys,
                        "include_matches": include_matches,
                        "include_related": include_related,
                        "limit": limit,
                        "min_liquidity": min_liquidity,
                        "min_volume": min_volume,
                        "parsec_id": parsec_id,
                        "parsec_ids": parsec_ids,
                        "scope": scope,
                        "search": search,
                        "status": status,
                    },
                    market_list_params.MarketListParams,
                ),
            ),
            cast_to=MarketListResponse,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_raw_response_wrapper(
            markets.list,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_raw_response_wrapper(
            markets.list,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.list = to_streamed_response_wrapper(
            markets.list,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.list = async_to_streamed_response_wrapper(
            markets.list,
        )
