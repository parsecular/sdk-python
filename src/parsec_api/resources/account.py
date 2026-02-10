# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    account_ping_params,
    account_balance_params,
    account_user_activity_params,
    account_update_credentials_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.account_ping_response import AccountPingResponse
from ..types.account_balance_response import AccountBalanceResponse
from ..types.account_user_activity_response import AccountUserActivityResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def balance(
        self,
        *,
        exchange: str,
        refresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBalanceResponse:
        """
        Returns the raw balance payload from the exchange (opaque JSON).

        Args:
          exchange: Exchange identifier (e.g., kalshi, polymarket).

          refresh: Refresh balance before returning (default false).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exchange": exchange,
                        "refresh": refresh,
                    },
                    account_balance_params.AccountBalanceParams,
                ),
            ),
            cast_to=AccountBalanceResponse,
        )

    def ping(
        self,
        *,
        exchange: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountPingResponse:
        """
        Performs a lightweight balance fetch per exchange to verify connectivity/auth
        status.

        Args:
          exchange: Optional exchange ID to ping; if omitted, pings all available exchanges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/ping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exchange": exchange}, account_ping_params.AccountPingParams),
            ),
            cast_to=AccountPingResponse,
        )

    def update_credentials(
        self,
        *,
        evm_private_key: Optional[str] | Omit = omit,
        kalshi_api_key_id: Optional[str] | Omit = omit,
        kalshi_private_key: Optional[str] | Omit = omit,
        poly_funder: Optional[str] | Omit = omit,
        poly_signature_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Updates stored credentials for this API key.

        Returns 204 on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/api/v1/credentials",
            body=maybe_transform(
                {
                    "evm_private_key": evm_private_key,
                    "kalshi_api_key_id": kalshi_api_key_id,
                    "kalshi_private_key": kalshi_private_key,
                    "poly_funder": poly_funder,
                    "poly_signature_type": poly_signature_type,
                },
                account_update_credentials_params.AccountUpdateCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def user_activity(
        self,
        *,
        address: str,
        exchanges: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUserActivityResponse:
        """
        Fetches user activity data from each requested exchange and returns a
        per-exchange status map.

        Args:
          address: User address (typically an EVM address).

          exchanges: Exchanges to query (CSV). Defaults to: polymarket, opinion, limitless,
              predictfun. In SDKs this is typically an array encoded as CSV on the wire.

          limit: Max number of items per exchange (default 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/user-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "address": address,
                        "exchanges": exchanges,
                        "limit": limit,
                    },
                    account_user_activity_params.AccountUserActivityParams,
                ),
            ),
            cast_to=AccountUserActivityResponse,
        )


class AsyncAccountResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def balance(
        self,
        *,
        exchange: str,
        refresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountBalanceResponse:
        """
        Returns the raw balance payload from the exchange (opaque JSON).

        Args:
          exchange: Exchange identifier (e.g., kalshi, polymarket).

          refresh: Refresh balance before returning (default false).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/balance",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exchange": exchange,
                        "refresh": refresh,
                    },
                    account_balance_params.AccountBalanceParams,
                ),
            ),
            cast_to=AccountBalanceResponse,
        )

    async def ping(
        self,
        *,
        exchange: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountPingResponse:
        """
        Performs a lightweight balance fetch per exchange to verify connectivity/auth
        status.

        Args:
          exchange: Optional exchange ID to ping; if omitted, pings all available exchanges.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/ping",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exchange": exchange}, account_ping_params.AccountPingParams),
            ),
            cast_to=AccountPingResponse,
        )

    async def update_credentials(
        self,
        *,
        evm_private_key: Optional[str] | Omit = omit,
        kalshi_api_key_id: Optional[str] | Omit = omit,
        kalshi_private_key: Optional[str] | Omit = omit,
        poly_funder: Optional[str] | Omit = omit,
        poly_signature_type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Updates stored credentials for this API key.

        Returns 204 on success.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/api/v1/credentials",
            body=await async_maybe_transform(
                {
                    "evm_private_key": evm_private_key,
                    "kalshi_api_key_id": kalshi_api_key_id,
                    "kalshi_private_key": kalshi_private_key,
                    "poly_funder": poly_funder,
                    "poly_signature_type": poly_signature_type,
                },
                account_update_credentials_params.AccountUpdateCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def user_activity(
        self,
        *,
        address: str,
        exchanges: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUserActivityResponse:
        """
        Fetches user activity data from each requested exchange and returns a
        per-exchange status map.

        Args:
          address: User address (typically an EVM address).

          exchanges: Exchanges to query (CSV). Defaults to: polymarket, opinion, limitless,
              predictfun. In SDKs this is typically an array encoded as CSV on the wire.

          limit: Max number of items per exchange (default 100).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/user-activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "address": address,
                        "exchanges": exchanges,
                        "limit": limit,
                    },
                    account_user_activity_params.AccountUserActivityParams,
                ),
            ),
            cast_to=AccountUserActivityResponse,
        )


class AccountResourceWithRawResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.balance = to_raw_response_wrapper(
            account.balance,
        )
        self.ping = to_raw_response_wrapper(
            account.ping,
        )
        self.update_credentials = to_raw_response_wrapper(
            account.update_credentials,
        )
        self.user_activity = to_raw_response_wrapper(
            account.user_activity,
        )


class AsyncAccountResourceWithRawResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.balance = async_to_raw_response_wrapper(
            account.balance,
        )
        self.ping = async_to_raw_response_wrapper(
            account.ping,
        )
        self.update_credentials = async_to_raw_response_wrapper(
            account.update_credentials,
        )
        self.user_activity = async_to_raw_response_wrapper(
            account.user_activity,
        )


class AccountResourceWithStreamingResponse:
    def __init__(self, account: AccountResource) -> None:
        self._account = account

        self.balance = to_streamed_response_wrapper(
            account.balance,
        )
        self.ping = to_streamed_response_wrapper(
            account.ping,
        )
        self.update_credentials = to_streamed_response_wrapper(
            account.update_credentials,
        )
        self.user_activity = to_streamed_response_wrapper(
            account.user_activity,
        )


class AsyncAccountResourceWithStreamingResponse:
    def __init__(self, account: AsyncAccountResource) -> None:
        self._account = account

        self.balance = async_to_streamed_response_wrapper(
            account.balance,
        )
        self.ping = async_to_streamed_response_wrapper(
            account.ping,
        )
        self.update_credentials = async_to_streamed_response_wrapper(
            account.update_credentials,
        )
        self.user_activity = async_to_streamed_response_wrapper(
            account.user_activity,
        )
