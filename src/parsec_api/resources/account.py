# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import account_ping_params, account_balance_params, account_user_activity_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.account_usage_response import AccountUsageResponse
from ..types.account_balance_response import AccountBalanceResponse
from ..types.account_user_activity_response import AccountUserActivityResponse

__all__ = ["AccountResource", "AsyncAccountResource"]


class AccountResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AccountResourceWithStreamingResponse(self)

    def balance(
        self,
        *,
        exchange: str,
        refresh: bool | Omit = omit,
        x_exchange_credentials: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"X-Exchange-Credentials": x_exchange_credentials}), **(extra_headers or {})}
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

    def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUsageResponse:
        """
        Returns the authenticated customer's tier, billing period, rate limits, and
        current consumption (monthly requests, WebSocket connections/subscriptions).
        Values of 0 for limits indicate unlimited.
        """
        return self._get(
            "/api/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUsageResponse,
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

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncAccountResourceWithStreamingResponse(self)

    async def balance(
        self,
        *,
        exchange: str,
        refresh: bool | Omit = omit,
        x_exchange_credentials: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"X-Exchange-Credentials": x_exchange_credentials}), **(extra_headers or {})}
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

    async def usage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountUsageResponse:
        """
        Returns the authenticated customer's tier, billing period, rate limits, and
        current consumption (monthly requests, WebSocket connections/subscriptions).
        Values of 0 for limits indicate unlimited.
        """
        return await self._get(
            "/api/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountUsageResponse,
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
        self.usage = to_raw_response_wrapper(
            account.usage,
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
        self.usage = async_to_raw_response_wrapper(
            account.usage,
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
        self.usage = to_streamed_response_wrapper(
            account.usage,
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
        self.usage = async_to_streamed_response_wrapper(
            account.usage,
        )
        self.user_activity = async_to_streamed_response_wrapper(
            account.user_activity,
        )
