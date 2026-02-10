# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import position_list_params
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
from ..types.position_list_response import PositionListResponse

__all__ = ["PositionsResource", "AsyncPositionsResource"]


class PositionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return PositionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        exchange: str,
        market_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionListResponse:
        """
        Lists positions for the authenticated customer on the selected exchange.

        Args:
          exchange: Exchange identifier (e.g., kalshi, polymarket).

          market_id: Optional market ID filter (exchange-native).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/positions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exchange": exchange,
                        "market_id": market_id,
                    },
                    position_list_params.PositionListParams,
                ),
            ),
            cast_to=PositionListResponse,
        )


class AsyncPositionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPositionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncPositionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        exchange: str,
        market_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PositionListResponse:
        """
        Lists positions for the authenticated customer on the selected exchange.

        Args:
          exchange: Exchange identifier (e.g., kalshi, polymarket).

          market_id: Optional market ID filter (exchange-native).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/positions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exchange": exchange,
                        "market_id": market_id,
                    },
                    position_list_params.PositionListParams,
                ),
            ),
            cast_to=PositionListResponse,
        )


class PositionsResourceWithRawResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.list = to_raw_response_wrapper(
            positions.list,
        )


class AsyncPositionsResourceWithRawResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.list = async_to_raw_response_wrapper(
            positions.list,
        )


class PositionsResourceWithStreamingResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.list = to_streamed_response_wrapper(
            positions.list,
        )


class AsyncPositionsResourceWithStreamingResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.list = async_to_streamed_response_wrapper(
            positions.list,
        )
