# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import price_history_retrieve_params
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
from ..types.price_history_retrieve_response import PriceHistoryRetrieveResponse

__all__ = ["PriceHistoryResource", "AsyncPriceHistoryResource"]


class PriceHistoryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PriceHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return PriceHistoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        interval: Literal["1m", "1h", "6h", "1d", "1w", "max"],
        parsec_id: str,
        end_ts: int | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceHistoryRetrieveResponse:
        """
        Returns an array of candlesticks with timestamps at period start (UTC).

        Args:
          interval: Price history interval.

          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          end_ts: Unix seconds end timestamp (inclusive). Defaults to now.

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          start_ts: Unix seconds start timestamp (inclusive). If omitted, the server selects a
              default range based on `interval`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/price-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "interval": interval,
                        "parsec_id": parsec_id,
                        "end_ts": end_ts,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    price_history_retrieve_params.PriceHistoryRetrieveParams,
                ),
            ),
            cast_to=PriceHistoryRetrieveResponse,
        )


class AsyncPriceHistoryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncPriceHistoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        interval: Literal["1m", "1h", "6h", "1d", "1w", "max"],
        parsec_id: str,
        end_ts: int | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceHistoryRetrieveResponse:
        """
        Returns an array of candlesticks with timestamps at period start (UTC).

        Args:
          interval: Price history interval.

          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          end_ts: Unix seconds end timestamp (inclusive). Defaults to now.

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          start_ts: Unix seconds start timestamp (inclusive). If omitted, the server selects a
              default range based on `interval`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/price-history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "interval": interval,
                        "parsec_id": parsec_id,
                        "end_ts": end_ts,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    price_history_retrieve_params.PriceHistoryRetrieveParams,
                ),
            ),
            cast_to=PriceHistoryRetrieveResponse,
        )


class PriceHistoryResourceWithRawResponse:
    def __init__(self, price_history: PriceHistoryResource) -> None:
        self._price_history = price_history

        self.retrieve = to_raw_response_wrapper(
            price_history.retrieve,
        )


class AsyncPriceHistoryResourceWithRawResponse:
    def __init__(self, price_history: AsyncPriceHistoryResource) -> None:
        self._price_history = price_history

        self.retrieve = async_to_raw_response_wrapper(
            price_history.retrieve,
        )


class PriceHistoryResourceWithStreamingResponse:
    def __init__(self, price_history: PriceHistoryResource) -> None:
        self._price_history = price_history

        self.retrieve = to_streamed_response_wrapper(
            price_history.retrieve,
        )


class AsyncPriceHistoryResourceWithStreamingResponse:
    def __init__(self, price_history: AsyncPriceHistoryResource) -> None:
        self._price_history = price_history

        self.retrieve = async_to_streamed_response_wrapper(
            price_history.retrieve,
        )
