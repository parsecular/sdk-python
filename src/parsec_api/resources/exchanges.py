# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.exchange_list_response import ExchangeListResponse

__all__ = ["ExchangesResource", "AsyncExchangesResource"]


class ExchangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExchangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExchangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return ExchangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListResponse:
        """Returns the exchange IDs that the current API key can access."""
        return self._get(
            "/api/v1/exchanges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeListResponse,
        )


class AsyncExchangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExchangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExchangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExchangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncExchangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExchangeListResponse:
        """Returns the exchange IDs that the current API key can access."""
        return await self._get(
            "/api/v1/exchanges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeListResponse,
        )


class ExchangesResourceWithRawResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = to_raw_response_wrapper(
            exchanges.list,
        )


class AsyncExchangesResourceWithRawResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = async_to_raw_response_wrapper(
            exchanges.list,
        )


class ExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: ExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = to_streamed_response_wrapper(
            exchanges.list,
        )


class AsyncExchangesResourceWithStreamingResponse:
    def __init__(self, exchanges: AsyncExchangesResource) -> None:
        self._exchanges = exchanges

        self.list = async_to_streamed_response_wrapper(
            exchanges.list,
        )
