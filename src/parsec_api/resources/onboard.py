# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import onboard_create_params
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
from ..types.onboard_create_response import OnboardCreateResponse

__all__ = ["OnboardResource", "AsyncOnboardResource"]


class OnboardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return OnboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return OnboardResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        exchange: str,
        mode: Literal["managed", "self"],
        api_key_id: str | Omit = omit,
        chain_id: int | Omit = omit,
        clob_api_key: str | Omit = omit,
        clob_api_passphrase: str | Omit = omit,
        clob_api_secret: str | Omit = omit,
        eoa_address: str | Omit = omit,
        private_key: str | Omit = omit,
        wallet_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardCreateResponse:
        """Unified onboarding endpoint.

        Managed mode creates wallet + exchange credentials
        (Polymarket only). Self mode stores user-provided credentials (Polymarket or
        Kalshi). Idempotent and resumable.

        Args:
          exchange: Exchange to onboard ("polymarket" or "kalshi").

          mode: Managed = Parsec creates wallet + credentials. Self = you provide credentials.

          api_key_id: Kalshi API key ID (self mode).

          chain_id: Chain ID for Safe wallet creation. Only used with wallet_type "safe".

          clob_api_key: Polymarket CLOB API key (self mode).

          clob_api_passphrase: Polymarket CLOB API passphrase (self mode).

          clob_api_secret: Polymarket CLOB API secret (self mode).

          eoa_address: External wallet address (42-char hex, 0x-prefixed). Required when wallet_type is
              "safe". Parsec skips embedded EOA creation and uses this address as the Safe
              owner. Must not be provided when wallet_type is "eoa".

          private_key: Kalshi RSA private key in PEM format (self mode).

          wallet_type: Wallet type for managed mode. "eoa" (default) creates an embedded EOA wallet.
              "safe" creates a Safe wallet owned by the external address in eoa_address.
              "safe" requires eoa_address. Providing eoa_address with "eoa" returns 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/onboard",
            body=maybe_transform(
                {
                    "exchange": exchange,
                    "mode": mode,
                    "api_key_id": api_key_id,
                    "chain_id": chain_id,
                    "clob_api_key": clob_api_key,
                    "clob_api_passphrase": clob_api_passphrase,
                    "clob_api_secret": clob_api_secret,
                    "eoa_address": eoa_address,
                    "private_key": private_key,
                    "wallet_type": wallet_type,
                },
                onboard_create_params.OnboardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardCreateResponse,
        )


class AsyncOnboardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnboardResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncOnboardResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        exchange: str,
        mode: Literal["managed", "self"],
        api_key_id: str | Omit = omit,
        chain_id: int | Omit = omit,
        clob_api_key: str | Omit = omit,
        clob_api_passphrase: str | Omit = omit,
        clob_api_secret: str | Omit = omit,
        eoa_address: str | Omit = omit,
        private_key: str | Omit = omit,
        wallet_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardCreateResponse:
        """Unified onboarding endpoint.

        Managed mode creates wallet + exchange credentials
        (Polymarket only). Self mode stores user-provided credentials (Polymarket or
        Kalshi). Idempotent and resumable.

        Args:
          exchange: Exchange to onboard ("polymarket" or "kalshi").

          mode: Managed = Parsec creates wallet + credentials. Self = you provide credentials.

          api_key_id: Kalshi API key ID (self mode).

          chain_id: Chain ID for Safe wallet creation. Only used with wallet_type "safe".

          clob_api_key: Polymarket CLOB API key (self mode).

          clob_api_passphrase: Polymarket CLOB API passphrase (self mode).

          clob_api_secret: Polymarket CLOB API secret (self mode).

          eoa_address: External wallet address (42-char hex, 0x-prefixed). Required when wallet_type is
              "safe". Parsec skips embedded EOA creation and uses this address as the Safe
              owner. Must not be provided when wallet_type is "eoa".

          private_key: Kalshi RSA private key in PEM format (self mode).

          wallet_type: Wallet type for managed mode. "eoa" (default) creates an embedded EOA wallet.
              "safe" creates a Safe wallet owned by the external address in eoa_address.
              "safe" requires eoa_address. Providing eoa_address with "eoa" returns 400.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/onboard",
            body=await async_maybe_transform(
                {
                    "exchange": exchange,
                    "mode": mode,
                    "api_key_id": api_key_id,
                    "chain_id": chain_id,
                    "clob_api_key": clob_api_key,
                    "clob_api_passphrase": clob_api_passphrase,
                    "clob_api_secret": clob_api_secret,
                    "eoa_address": eoa_address,
                    "private_key": private_key,
                    "wallet_type": wallet_type,
                },
                onboard_create_params.OnboardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardCreateResponse,
        )


class OnboardResourceWithRawResponse:
    def __init__(self, onboard: OnboardResource) -> None:
        self._onboard = onboard

        self.create = to_raw_response_wrapper(
            onboard.create,
        )


class AsyncOnboardResourceWithRawResponse:
    def __init__(self, onboard: AsyncOnboardResource) -> None:
        self._onboard = onboard

        self.create = async_to_raw_response_wrapper(
            onboard.create,
        )


class OnboardResourceWithStreamingResponse:
    def __init__(self, onboard: OnboardResource) -> None:
        self._onboard = onboard

        self.create = to_streamed_response_wrapper(
            onboard.create,
        )


class AsyncOnboardResourceWithStreamingResponse:
    def __init__(self, onboard: AsyncOnboardResource) -> None:
        self._onboard = onboard

        self.create = async_to_streamed_response_wrapper(
            onboard.create,
        )
