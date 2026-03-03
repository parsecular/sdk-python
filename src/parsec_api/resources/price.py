# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import price_retrieve_params
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
from ..types.price_retrieve_response import PriceRetrieveResponse

__all__ = ["PriceResource", "AsyncPriceResource"]


class PriceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return PriceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        parsec_id: str,
        at_ts: int | Omit = omit,
        end_ts: int | Omit = omit,
        interval: Literal["1m", "1h", "6h", "1d", "1w", "max"] | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceRetrieveResponse:
        """
        Returns an array of candlesticks with timestamps at period start (UTC).
        Historical data is tier-gated: Free=5d, Pro=30d, Scale=unlimited.

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          at_ts: Point-in-time lookup (Unix seconds). Returns the single closest candle. Cannot
              be combined with start_ts/end_ts.

          end_ts: Unix seconds end timestamp (inclusive). Defaults to now.

          interval: Defaults to 1h for point-in-time (at_ts)

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
            "/api/v1/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "at_ts": at_ts,
                        "end_ts": end_ts,
                        "interval": interval,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    price_retrieve_params.PriceRetrieveParams,
                ),
            ),
            cast_to=PriceRetrieveResponse,
        )


class AsyncPriceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncPriceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        parsec_id: str,
        at_ts: int | Omit = omit,
        end_ts: int | Omit = omit,
        interval: Literal["1m", "1h", "6h", "1d", "1w", "max"] | Omit = omit,
        outcome: str | Omit = omit,
        start_ts: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceRetrieveResponse:
        """
        Returns an array of candlesticks with timestamps at period start (UTC).
        Historical data is tier-gated: Free=5d, Pro=30d, Scale=unlimited.

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          at_ts: Point-in-time lookup (Unix seconds). Returns the single closest candle. Cannot
              be combined with start_ts/end_ts.

          end_ts: Unix seconds end timestamp (inclusive). Defaults to now.

          interval: Defaults to 1h for point-in-time (at_ts)

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
            "/api/v1/price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "at_ts": at_ts,
                        "end_ts": end_ts,
                        "interval": interval,
                        "outcome": outcome,
                        "start_ts": start_ts,
                    },
                    price_retrieve_params.PriceRetrieveParams,
                ),
            ),
            cast_to=PriceRetrieveResponse,
        )


class PriceResourceWithRawResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.retrieve = to_raw_response_wrapper(
            price.retrieve,
        )


class AsyncPriceResourceWithRawResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.retrieve = async_to_raw_response_wrapper(
            price.retrieve,
        )


class PriceResourceWithStreamingResponse:
    def __init__(self, price: PriceResource) -> None:
        self._price = price

        self.retrieve = to_streamed_response_wrapper(
            price.retrieve,
        )


class AsyncPriceResourceWithStreamingResponse:
    def __init__(self, price: AsyncPriceResource) -> None:
        self._price = price

        self.retrieve = async_to_streamed_response_wrapper(
            price.retrieve,
        )
