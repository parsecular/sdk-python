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
        exchanges: SequenceNotStr[str] | Omit = omit,
        group_id: str | Omit = omit,
        limit: int | Omit = omit,
        min_liquidity: int | Omit = omit,
        min_volume: int | Omit = omit,
        parsec_ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "closed", "resolved"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """Provide either `exchanges` (CSV) or `parsec_ids` (CSV).

        When `parsec_ids` is
        provided, other filters are not allowed.

        Args:
          cursor: Pagination cursor (offset-based).

          event_id: Canonical Parsec event ID filter (exact match).

          exchanges: Exchanges to query. In SDKs this is typically an array encoded as CSV on the
              wire. Required unless `parsec_ids` is provided.

          group_id: Source-native exchange event/group ID filter (exact match).

          limit: Results per page (default 100).

          min_liquidity: Minimum liquidity filter.

          min_volume: Minimum volume filter.

          parsec_ids: Parsec market IDs to fetch directly (format: `{exchange}:{native_id}`). In SDKs
              this is typically an array encoded as CSV on the wire. Required unless
              `exchanges` is provided.

          search: Keyword search in title/description/question (case-insensitive).

          status: Status filter.

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
                        "exchanges": exchanges,
                        "group_id": group_id,
                        "limit": limit,
                        "min_liquidity": min_liquidity,
                        "min_volume": min_volume,
                        "parsec_ids": parsec_ids,
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
        exchanges: SequenceNotStr[str] | Omit = omit,
        group_id: str | Omit = omit,
        limit: int | Omit = omit,
        min_liquidity: int | Omit = omit,
        min_volume: int | Omit = omit,
        parsec_ids: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        status: Literal["active", "closed", "resolved"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarketListResponse:
        """Provide either `exchanges` (CSV) or `parsec_ids` (CSV).

        When `parsec_ids` is
        provided, other filters are not allowed.

        Args:
          cursor: Pagination cursor (offset-based).

          event_id: Canonical Parsec event ID filter (exact match).

          exchanges: Exchanges to query. In SDKs this is typically an array encoded as CSV on the
              wire. Required unless `parsec_ids` is provided.

          group_id: Source-native exchange event/group ID filter (exact match).

          limit: Results per page (default 100).

          min_liquidity: Minimum liquidity filter.

          min_volume: Minimum volume filter.

          parsec_ids: Parsec market IDs to fetch directly (format: `{exchange}:{native_id}`). In SDKs
              this is typically an array encoded as CSV on the wire. Required unless
              `exchanges` is provided.

          search: Keyword search in title/description/question (case-insensitive).

          status: Status filter.

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
                        "exchanges": exchanges,
                        "group_id": group_id,
                        "limit": limit,
                        "min_liquidity": min_liquidity,
                        "min_volume": min_volume,
                        "parsec_ids": parsec_ids,
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
