# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import trade_list_params
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
from ..types.trade_list_response import TradeListResponse

__all__ = ["TradesResource", "AsyncTradesResource"]


class TradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return TradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return TradesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        parsec_id: str,
        end_ts: int | Omit = omit,
        limit: int | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TradeListResponse:
        """
        Returns an array of recent trades for the requested market+outcome (normalized
        prices 0.0-1.0).

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          end_ts: Unix seconds end timestamp (inclusive).

          limit: Max number of trades (default 200; server clamps to 1..=500).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          start_ts: Unix seconds start timestamp (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "end_ts": end_ts,
                        "limit": limit,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    trade_list_params.TradeListParams,
                ),
            ),
            cast_to=TradeListResponse,
        )


class AsyncTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncTradesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        parsec_id: str,
        end_ts: int | Omit = omit,
        limit: int | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TradeListResponse:
        """
        Returns an array of recent trades for the requested market+outcome (normalized
        prices 0.0-1.0).

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          end_ts: Unix seconds end timestamp (inclusive).

          limit: Max number of trades (default 200; server clamps to 1..=500).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          start_ts: Unix seconds start timestamp (inclusive).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "end_ts": end_ts,
                        "limit": limit,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    trade_list_params.TradeListParams,
                ),
            ),
            cast_to=TradeListResponse,
        )


class TradesResourceWithRawResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.list = to_raw_response_wrapper(
            trades.list,
        )


class AsyncTradesResourceWithRawResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.list = async_to_raw_response_wrapper(
            trades.list,
        )


class TradesResourceWithStreamingResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.list = to_streamed_response_wrapper(
            trades.list,
        )


class AsyncTradesResourceWithStreamingResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.list = async_to_streamed_response_wrapper(
            trades.list,
        )
