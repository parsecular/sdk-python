# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..types import orderbook_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.orderbook_retrieve_response import OrderbookRetrieveResponse

__all__ = ["OrderbookResource", "AsyncOrderbookResource"]


class OrderbookResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderbookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrderbookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderbookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return OrderbookResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        cursor: str | Omit = omit,
        depth: int | Omit = omit,
        end_ts: int | Omit = omit,
        exchange: str | Omit = omit,
        limit: int | Omit = omit,
        market_id: str | Omit = omit,
        outcome: str | Omit = omit,
        parsec_id: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderbookRetrieveResponse:
        """
        Use `/markets` to discover a market first, then query by either `parsec_id` or
        `exchange + market_id`. When start_ts or end_ts is provided, returns historical
        orderbook snapshots instead of a live L2 snapshot. Large time ranges are handled
        via internal chunking and may be slow for very wide windows. In historical mode,
        limit defaults to 500 (max 1000). Historical data is tier-gated: Free=5d,
        Pro=30d, Scale=unlimited.

        Args:
          cursor: Opaque pagination cursor for historical mode.

          depth: Alias for `limit` (REST/WS symmetry).

          end_ts: Unix seconds — end of time range. Defaults to now.

          exchange: Exchange ID (alternative to parsec_id — use with market_id).

          limit: Max depth per side (default 50; server clamps to 1..=100).

          market_id: Exchange-native market ID (alternative to parsec_id — use with exchange).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          parsec_id: Unified market ID. Provide either `parsec_id` OR both `exchange` + `market_id`.

          start_ts: Unix seconds — when present, switches to historical mode (returns snapshots
              instead of live book).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OrderbookRetrieveResponse,
            self._get(
                "/api/v1/orderbook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "cursor": cursor,
                            "depth": depth,
                            "end_ts": end_ts,
                            "exchange": exchange,
                            "limit": limit,
                            "market_id": market_id,
                            "outcome": outcome,
                            "parsec_id": parsec_id,
                            "start_ts": start_ts,
                        },
                        orderbook_retrieve_params.OrderbookRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, OrderbookRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOrderbookResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderbookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderbookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderbookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncOrderbookResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        cursor: str | Omit = omit,
        depth: int | Omit = omit,
        end_ts: int | Omit = omit,
        exchange: str | Omit = omit,
        limit: int | Omit = omit,
        market_id: str | Omit = omit,
        outcome: str | Omit = omit,
        parsec_id: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderbookRetrieveResponse:
        """
        Use `/markets` to discover a market first, then query by either `parsec_id` or
        `exchange + market_id`. When start_ts or end_ts is provided, returns historical
        orderbook snapshots instead of a live L2 snapshot. Large time ranges are handled
        via internal chunking and may be slow for very wide windows. In historical mode,
        limit defaults to 500 (max 1000). Historical data is tier-gated: Free=5d,
        Pro=30d, Scale=unlimited.

        Args:
          cursor: Opaque pagination cursor for historical mode.

          depth: Alias for `limit` (REST/WS symmetry).

          end_ts: Unix seconds — end of time range. Defaults to now.

          exchange: Exchange ID (alternative to parsec_id — use with market_id).

          limit: Max depth per side (default 50; server clamps to 1..=100).

          market_id: Exchange-native market ID (alternative to parsec_id — use with exchange).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          parsec_id: Unified market ID. Provide either `parsec_id` OR both `exchange` + `market_id`.

          start_ts: Unix seconds — when present, switches to historical mode (returns snapshots
              instead of live book).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            OrderbookRetrieveResponse,
            await self._get(
                "/api/v1/orderbook",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "cursor": cursor,
                            "depth": depth,
                            "end_ts": end_ts,
                            "exchange": exchange,
                            "limit": limit,
                            "market_id": market_id,
                            "outcome": outcome,
                            "parsec_id": parsec_id,
                            "start_ts": start_ts,
                        },
                        orderbook_retrieve_params.OrderbookRetrieveParams,
                    ),
                ),
                cast_to=cast(
                    Any, OrderbookRetrieveResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OrderbookResourceWithRawResponse:
    def __init__(self, orderbook: OrderbookResource) -> None:
        self._orderbook = orderbook

        self.retrieve = to_raw_response_wrapper(
            orderbook.retrieve,
        )


class AsyncOrderbookResourceWithRawResponse:
    def __init__(self, orderbook: AsyncOrderbookResource) -> None:
        self._orderbook = orderbook

        self.retrieve = async_to_raw_response_wrapper(
            orderbook.retrieve,
        )


class OrderbookResourceWithStreamingResponse:
    def __init__(self, orderbook: OrderbookResource) -> None:
        self._orderbook = orderbook

        self.retrieve = to_streamed_response_wrapper(
            orderbook.retrieve,
        )


class AsyncOrderbookResourceWithStreamingResponse:
    def __init__(self, orderbook: AsyncOrderbookResource) -> None:
        self._orderbook = orderbook

        self.retrieve = async_to_streamed_response_wrapper(
            orderbook.retrieve,
        )
