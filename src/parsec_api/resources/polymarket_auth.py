# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import polymarket_auth_message_params, polymarket_auth_credentials_params
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
from ..types.polymarket_auth_message_response import PolymarketAuthMessageResponse
from ..types.polymarket_auth_credentials_response import PolymarketAuthCredentialsResponse

__all__ = ["PolymarketAuthResource", "AsyncPolymarketAuthResource"]


class PolymarketAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PolymarketAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return PolymarketAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolymarketAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return PolymarketAuthResourceWithStreamingResponse(self)

    def credentials(
        self,
        *,
        address: str,
        signature: str,
        timestamp: str,
        store: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolymarketAuthCredentialsResponse:
        """
        Submits a signed EIP-712 ClobAuth message and derives Polymarket CLOB API
        credentials. Optionally stores them with ?store=true.

        Args:
          address: Your Ethereum wallet address.

          signature: EIP-712 signature of the ClobAuth typed data.

          timestamp: Timestamp from the auth message response.

          store: Set to true to store derived credentials for future use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/exchange/polymarket/auth-credentials",
            body=maybe_transform(
                {
                    "address": address,
                    "signature": signature,
                    "timestamp": timestamp,
                },
                polymarket_auth_credentials_params.PolymarketAuthCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"store": store}, polymarket_auth_credentials_params.PolymarketAuthCredentialsParams
                ),
            ),
            cast_to=PolymarketAuthCredentialsResponse,
        )

    def message(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolymarketAuthMessageResponse:
        """Returns the EIP-712 ClobAuth typed data to sign with your wallet.

        Use the
        signature with POST /exchange/polymarket/auth-credentials.

        Args:
          address: Your Ethereum wallet address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/exchange/polymarket/auth-message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"address": address}, polymarket_auth_message_params.PolymarketAuthMessageParams),
            ),
            cast_to=PolymarketAuthMessageResponse,
        )


class AsyncPolymarketAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPolymarketAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolymarketAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolymarketAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncPolymarketAuthResourceWithStreamingResponse(self)

    async def credentials(
        self,
        *,
        address: str,
        signature: str,
        timestamp: str,
        store: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolymarketAuthCredentialsResponse:
        """
        Submits a signed EIP-712 ClobAuth message and derives Polymarket CLOB API
        credentials. Optionally stores them with ?store=true.

        Args:
          address: Your Ethereum wallet address.

          signature: EIP-712 signature of the ClobAuth typed data.

          timestamp: Timestamp from the auth message response.

          store: Set to true to store derived credentials for future use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/exchange/polymarket/auth-credentials",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "signature": signature,
                    "timestamp": timestamp,
                },
                polymarket_auth_credentials_params.PolymarketAuthCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"store": store}, polymarket_auth_credentials_params.PolymarketAuthCredentialsParams
                ),
            ),
            cast_to=PolymarketAuthCredentialsResponse,
        )

    async def message(
        self,
        *,
        address: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolymarketAuthMessageResponse:
        """Returns the EIP-712 ClobAuth typed data to sign with your wallet.

        Use the
        signature with POST /exchange/polymarket/auth-credentials.

        Args:
          address: Your Ethereum wallet address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/exchange/polymarket/auth-message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"address": address}, polymarket_auth_message_params.PolymarketAuthMessageParams
                ),
            ),
            cast_to=PolymarketAuthMessageResponse,
        )


class PolymarketAuthResourceWithRawResponse:
    def __init__(self, polymarket_auth: PolymarketAuthResource) -> None:
        self._polymarket_auth = polymarket_auth

        self.credentials = to_raw_response_wrapper(
            polymarket_auth.credentials,
        )
        self.message = to_raw_response_wrapper(
            polymarket_auth.message,
        )


class AsyncPolymarketAuthResourceWithRawResponse:
    def __init__(self, polymarket_auth: AsyncPolymarketAuthResource) -> None:
        self._polymarket_auth = polymarket_auth

        self.credentials = async_to_raw_response_wrapper(
            polymarket_auth.credentials,
        )
        self.message = async_to_raw_response_wrapper(
            polymarket_auth.message,
        )


class PolymarketAuthResourceWithStreamingResponse:
    def __init__(self, polymarket_auth: PolymarketAuthResource) -> None:
        self._polymarket_auth = polymarket_auth

        self.credentials = to_streamed_response_wrapper(
            polymarket_auth.credentials,
        )
        self.message = to_streamed_response_wrapper(
            polymarket_auth.message,
        )


class AsyncPolymarketAuthResourceWithStreamingResponse:
    def __init__(self, polymarket_auth: AsyncPolymarketAuthResource) -> None:
        self._polymarket_auth = polymarket_auth

        self.credentials = async_to_streamed_response_wrapper(
            polymarket_auth.credentials,
        )
        self.message = async_to_streamed_response_wrapper(
            polymarket_auth.message,
        )
