# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
        parsec_id: str,
        depth: int | Omit = omit,
        limit: int | Omit = omit,
        outcome: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderbookRetrieveResponse:
        """
        Returns bids/asks as `[price, size]` tuples.

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          depth: Alias for `limit` (REST/WS symmetry).

          limit: Max depth per side (default 50; server clamps to 1..=100).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/orderbook",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "depth": depth,
                        "limit": limit,
                        "outcome": outcome,
                    },
                    orderbook_retrieve_params.OrderbookRetrieveParams,
                ),
            ),
            cast_to=OrderbookRetrieveResponse,
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
        parsec_id: str,
        depth: int | Omit = omit,
        limit: int | Omit = omit,
        outcome: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrderbookRetrieveResponse:
        """
        Returns bids/asks as `[price, size]` tuples.

        Args:
          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          depth: Alias for `limit` (REST/WS symmetry).

          limit: Max depth per side (default 50; server clamps to 1..=100).

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required and may be an
              outcome label or numeric index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/orderbook",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "parsec_id": parsec_id,
                        "depth": depth,
                        "limit": limit,
                        "outcome": outcome,
                    },
                    orderbook_retrieve_params.OrderbookRetrieveParams,
                ),
            ),
            cast_to=OrderbookRetrieveResponse,
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
