# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import execution_price_retrieve_params
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
from ..types.execution_price_retrieve_response import ExecutionPriceRetrieveResponse

__all__ = ["ExecutionPriceResource", "AsyncExecutionPriceResource"]


class ExecutionPriceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExecutionPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExecutionPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return ExecutionPriceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        amount: float,
        parsec_id: str,
        side: Literal["buy", "sell"],
        outcome: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionPriceRetrieveResponse:
        """
        Walks the orderbook to estimate the volume-weighted average price (VWAP) for a
        hypothetical order of the given size. Does not place an order.

        Args:
          amount: Order size in contracts.

          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          side: Order side ("buy" or "sell").

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/execution-price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "parsec_id": parsec_id,
                        "side": side,
                        "outcome": outcome,
                    },
                    execution_price_retrieve_params.ExecutionPriceRetrieveParams,
                ),
            ),
            cast_to=ExecutionPriceRetrieveResponse,
        )


class AsyncExecutionPriceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExecutionPriceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExecutionPriceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionPriceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncExecutionPriceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        amount: float,
        parsec_id: str,
        side: Literal["buy", "sell"],
        outcome: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionPriceRetrieveResponse:
        """
        Walks the orderbook to estimate the volume-weighted average price (VWAP) for a
        hypothetical order of the given size. Does not place an order.

        Args:
          amount: Order size in contracts.

          parsec_id: Unified market ID in format `{exchange}:{native_id}`.

          side: Order side ("buy" or "sell").

          outcome: Outcome selector. For binary markets this is typically "yes" or "no"
              (case-insensitive). For categorical markets, this is required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/execution-price",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "amount": amount,
                        "parsec_id": parsec_id,
                        "side": side,
                        "outcome": outcome,
                    },
                    execution_price_retrieve_params.ExecutionPriceRetrieveParams,
                ),
            ),
            cast_to=ExecutionPriceRetrieveResponse,
        )


class ExecutionPriceResourceWithRawResponse:
    def __init__(self, execution_price: ExecutionPriceResource) -> None:
        self._execution_price = execution_price

        self.retrieve = to_raw_response_wrapper(
            execution_price.retrieve,
        )


class AsyncExecutionPriceResourceWithRawResponse:
    def __init__(self, execution_price: AsyncExecutionPriceResource) -> None:
        self._execution_price = execution_price

        self.retrieve = async_to_raw_response_wrapper(
            execution_price.retrieve,
        )


class ExecutionPriceResourceWithStreamingResponse:
    def __init__(self, execution_price: ExecutionPriceResource) -> None:
        self._execution_price = execution_price

        self.retrieve = to_streamed_response_wrapper(
            execution_price.retrieve,
        )


class AsyncExecutionPriceResourceWithStreamingResponse:
    def __init__(self, execution_price: AsyncExecutionPriceResource) -> None:
        self._execution_price = execution_price

        self.retrieve = async_to_streamed_response_wrapper(
            execution_price.retrieve,
        )
