# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ParsecAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        orders,
        account,
        markets,
        approvals,
        exchanges,
        orderbook,
        positions,
        websocket,
        price_history,
    )
    from .resources.orders import OrdersResource, AsyncOrdersResource
    from .resources.account import AccountResource, AsyncAccountResource
    from .resources.markets import MarketsResource, AsyncMarketsResource
    from .resources.approvals import ApprovalsResource, AsyncApprovalsResource
    from .resources.exchanges import ExchangesResource, AsyncExchangesResource
    from .resources.orderbook import OrderbookResource, AsyncOrderbookResource
    from .resources.positions import PositionsResource, AsyncPositionsResource
    from .resources.websocket import WebsocketResource, AsyncWebsocketResource
    from .resources.price_history import PriceHistoryResource, AsyncPriceHistoryResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ParsecAPI",
    "AsyncParsecAPI",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://api.parsecapi.com",
    "local": "http://localhost:3000",
}


class ParsecAPI(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ParsecAPI client instance.

        This automatically infers the `api_key` argument from the `PARSEC_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PARSEC_API_KEY")
        if api_key is None:
            raise ParsecAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PARSEC_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("PARSEC_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PARSEC_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def exchanges(self) -> ExchangesResource:
        from .resources.exchanges import ExchangesResource

        return ExchangesResource(self)

    @cached_property
    def markets(self) -> MarketsResource:
        from .resources.markets import MarketsResource

        return MarketsResource(self)

    @cached_property
    def orderbook(self) -> OrderbookResource:
        from .resources.orderbook import OrderbookResource

        return OrderbookResource(self)

    @cached_property
    def price_history(self) -> PriceHistoryResource:
        from .resources.price_history import PriceHistoryResource

        return PriceHistoryResource(self)

    @cached_property
    def websocket(self) -> WebsocketResource:
        from .resources.websocket import WebsocketResource

        return WebsocketResource(self)

    @cached_property
    def orders(self) -> OrdersResource:
        from .resources.orders import OrdersResource

        return OrdersResource(self)

    @cached_property
    def positions(self) -> PositionsResource:
        from .resources.positions import PositionsResource

        return PositionsResource(self)

    @cached_property
    def account(self) -> AccountResource:
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def approvals(self) -> ApprovalsResource:
        from .resources.approvals import ApprovalsResource

        return ApprovalsResource(self)

    def ws(self, *, url: str | None = None) -> "ParsecWebSocket":
        """Create a WebSocket client for real-time orderbook and trade streaming.

        Inherits ``api_key`` and derives the WebSocket URL from ``base_url``.

        Args:
            url: Override the WebSocket URL (derived from base_url by default).

        Returns:
            A new :class:`ParsecWebSocket` instance.
        """
        from .streaming import ParsecWebSocket

        ws_url = url or self._derive_ws_url()
        return ParsecWebSocket(self.api_key, ws_url)

    def _derive_ws_url(self) -> str:
        base = str(self.base_url).rstrip("/")
        if base.startswith("https://"):
            return base.replace("https://", "wss://", 1) + "/ws"
        if base.startswith("http://"):
            return base.replace("http://", "ws://", 1) + "/ws"
        return "wss://" + base + "/ws"

    @cached_property
    def with_raw_response(self) -> ParsecAPIWithRawResponse:
        return ParsecAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsecAPIWithStreamedResponse:
        return ParsecAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncParsecAPI(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["production", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncParsecAPI client instance.

        This automatically infers the `api_key` argument from the `PARSEC_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PARSEC_API_KEY")
        if api_key is None:
            raise ParsecAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PARSEC_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("PARSEC_API_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `PARSEC_API_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def exchanges(self) -> AsyncExchangesResource:
        from .resources.exchanges import AsyncExchangesResource

        return AsyncExchangesResource(self)

    @cached_property
    def markets(self) -> AsyncMarketsResource:
        from .resources.markets import AsyncMarketsResource

        return AsyncMarketsResource(self)

    @cached_property
    def orderbook(self) -> AsyncOrderbookResource:
        from .resources.orderbook import AsyncOrderbookResource

        return AsyncOrderbookResource(self)

    @cached_property
    def price_history(self) -> AsyncPriceHistoryResource:
        from .resources.price_history import AsyncPriceHistoryResource

        return AsyncPriceHistoryResource(self)

    @cached_property
    def websocket(self) -> AsyncWebsocketResource:
        from .resources.websocket import AsyncWebsocketResource

        return AsyncWebsocketResource(self)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        from .resources.orders import AsyncOrdersResource

        return AsyncOrdersResource(self)

    @cached_property
    def positions(self) -> AsyncPositionsResource:
        from .resources.positions import AsyncPositionsResource

        return AsyncPositionsResource(self)

    @cached_property
    def account(self) -> AsyncAccountResource:
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def approvals(self) -> AsyncApprovalsResource:
        from .resources.approvals import AsyncApprovalsResource

        return AsyncApprovalsResource(self)

    def ws(self, *, url: str | None = None) -> "ParsecWebSocket":
        """Create a WebSocket client for real-time orderbook and trade streaming.

        Inherits ``api_key`` and derives the WebSocket URL from ``base_url``.

        Args:
            url: Override the WebSocket URL (derived from base_url by default).

        Returns:
            A new :class:`ParsecWebSocket` instance.
        """
        from .streaming import ParsecWebSocket

        ws_url = url or self._derive_ws_url()
        return ParsecWebSocket(self.api_key, ws_url)

    def _derive_ws_url(self) -> str:
        base = str(self.base_url).rstrip("/")
        if base.startswith("https://"):
            return base.replace("https://", "wss://", 1) + "/ws"
        if base.startswith("http://"):
            return base.replace("http://", "ws://", 1) + "/ws"
        return "wss://" + base + "/ws"

    @cached_property
    def with_raw_response(self) -> AsyncParsecAPIWithRawResponse:
        return AsyncParsecAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsecAPIWithStreamedResponse:
        return AsyncParsecAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-Key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ParsecAPIWithRawResponse:
    _client: ParsecAPI

    def __init__(self, client: ParsecAPI) -> None:
        self._client = client

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithRawResponse:
        from .resources.exchanges import ExchangesResourceWithRawResponse

        return ExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def markets(self) -> markets.MarketsResourceWithRawResponse:
        from .resources.markets import MarketsResourceWithRawResponse

        return MarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def orderbook(self) -> orderbook.OrderbookResourceWithRawResponse:
        from .resources.orderbook import OrderbookResourceWithRawResponse

        return OrderbookResourceWithRawResponse(self._client.orderbook)

    @cached_property
    def price_history(self) -> price_history.PriceHistoryResourceWithRawResponse:
        from .resources.price_history import PriceHistoryResourceWithRawResponse

        return PriceHistoryResourceWithRawResponse(self._client.price_history)

    @cached_property
    def websocket(self) -> websocket.WebsocketResourceWithRawResponse:
        from .resources.websocket import WebsocketResourceWithRawResponse

        return WebsocketResourceWithRawResponse(self._client.websocket)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithRawResponse:
        from .resources.orders import OrdersResourceWithRawResponse

        return OrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def positions(self) -> positions.PositionsResourceWithRawResponse:
        from .resources.positions import PositionsResourceWithRawResponse

        return PositionsResourceWithRawResponse(self._client.positions)

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def approvals(self) -> approvals.ApprovalsResourceWithRawResponse:
        from .resources.approvals import ApprovalsResourceWithRawResponse

        return ApprovalsResourceWithRawResponse(self._client.approvals)


class AsyncParsecAPIWithRawResponse:
    _client: AsyncParsecAPI

    def __init__(self, client: AsyncParsecAPI) -> None:
        self._client = client

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithRawResponse:
        from .resources.exchanges import AsyncExchangesResourceWithRawResponse

        return AsyncExchangesResourceWithRawResponse(self._client.exchanges)

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithRawResponse:
        from .resources.markets import AsyncMarketsResourceWithRawResponse

        return AsyncMarketsResourceWithRawResponse(self._client.markets)

    @cached_property
    def orderbook(self) -> orderbook.AsyncOrderbookResourceWithRawResponse:
        from .resources.orderbook import AsyncOrderbookResourceWithRawResponse

        return AsyncOrderbookResourceWithRawResponse(self._client.orderbook)

    @cached_property
    def price_history(self) -> price_history.AsyncPriceHistoryResourceWithRawResponse:
        from .resources.price_history import AsyncPriceHistoryResourceWithRawResponse

        return AsyncPriceHistoryResourceWithRawResponse(self._client.price_history)

    @cached_property
    def websocket(self) -> websocket.AsyncWebsocketResourceWithRawResponse:
        from .resources.websocket import AsyncWebsocketResourceWithRawResponse

        return AsyncWebsocketResourceWithRawResponse(self._client.websocket)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithRawResponse:
        from .resources.orders import AsyncOrdersResourceWithRawResponse

        return AsyncOrdersResourceWithRawResponse(self._client.orders)

    @cached_property
    def positions(self) -> positions.AsyncPositionsResourceWithRawResponse:
        from .resources.positions import AsyncPositionsResourceWithRawResponse

        return AsyncPositionsResourceWithRawResponse(self._client.positions)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def approvals(self) -> approvals.AsyncApprovalsResourceWithRawResponse:
        from .resources.approvals import AsyncApprovalsResourceWithRawResponse

        return AsyncApprovalsResourceWithRawResponse(self._client.approvals)


class ParsecAPIWithStreamedResponse:
    _client: ParsecAPI

    def __init__(self, client: ParsecAPI) -> None:
        self._client = client

    @cached_property
    def exchanges(self) -> exchanges.ExchangesResourceWithStreamingResponse:
        from .resources.exchanges import ExchangesResourceWithStreamingResponse

        return ExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def markets(self) -> markets.MarketsResourceWithStreamingResponse:
        from .resources.markets import MarketsResourceWithStreamingResponse

        return MarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def orderbook(self) -> orderbook.OrderbookResourceWithStreamingResponse:
        from .resources.orderbook import OrderbookResourceWithStreamingResponse

        return OrderbookResourceWithStreamingResponse(self._client.orderbook)

    @cached_property
    def price_history(self) -> price_history.PriceHistoryResourceWithStreamingResponse:
        from .resources.price_history import PriceHistoryResourceWithStreamingResponse

        return PriceHistoryResourceWithStreamingResponse(self._client.price_history)

    @cached_property
    def websocket(self) -> websocket.WebsocketResourceWithStreamingResponse:
        from .resources.websocket import WebsocketResourceWithStreamingResponse

        return WebsocketResourceWithStreamingResponse(self._client.websocket)

    @cached_property
    def orders(self) -> orders.OrdersResourceWithStreamingResponse:
        from .resources.orders import OrdersResourceWithStreamingResponse

        return OrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def positions(self) -> positions.PositionsResourceWithStreamingResponse:
        from .resources.positions import PositionsResourceWithStreamingResponse

        return PositionsResourceWithStreamingResponse(self._client.positions)

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def approvals(self) -> approvals.ApprovalsResourceWithStreamingResponse:
        from .resources.approvals import ApprovalsResourceWithStreamingResponse

        return ApprovalsResourceWithStreamingResponse(self._client.approvals)


class AsyncParsecAPIWithStreamedResponse:
    _client: AsyncParsecAPI

    def __init__(self, client: AsyncParsecAPI) -> None:
        self._client = client

    @cached_property
    def exchanges(self) -> exchanges.AsyncExchangesResourceWithStreamingResponse:
        from .resources.exchanges import AsyncExchangesResourceWithStreamingResponse

        return AsyncExchangesResourceWithStreamingResponse(self._client.exchanges)

    @cached_property
    def markets(self) -> markets.AsyncMarketsResourceWithStreamingResponse:
        from .resources.markets import AsyncMarketsResourceWithStreamingResponse

        return AsyncMarketsResourceWithStreamingResponse(self._client.markets)

    @cached_property
    def orderbook(self) -> orderbook.AsyncOrderbookResourceWithStreamingResponse:
        from .resources.orderbook import AsyncOrderbookResourceWithStreamingResponse

        return AsyncOrderbookResourceWithStreamingResponse(self._client.orderbook)

    @cached_property
    def price_history(self) -> price_history.AsyncPriceHistoryResourceWithStreamingResponse:
        from .resources.price_history import AsyncPriceHistoryResourceWithStreamingResponse

        return AsyncPriceHistoryResourceWithStreamingResponse(self._client.price_history)

    @cached_property
    def websocket(self) -> websocket.AsyncWebsocketResourceWithStreamingResponse:
        from .resources.websocket import AsyncWebsocketResourceWithStreamingResponse

        return AsyncWebsocketResourceWithStreamingResponse(self._client.websocket)

    @cached_property
    def orders(self) -> orders.AsyncOrdersResourceWithStreamingResponse:
        from .resources.orders import AsyncOrdersResourceWithStreamingResponse

        return AsyncOrdersResourceWithStreamingResponse(self._client.orders)

    @cached_property
    def positions(self) -> positions.AsyncPositionsResourceWithStreamingResponse:
        from .resources.positions import AsyncPositionsResourceWithStreamingResponse

        return AsyncPositionsResourceWithStreamingResponse(self._client.positions)

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def approvals(self) -> approvals.AsyncApprovalsResourceWithStreamingResponse:
        from .resources.approvals import AsyncApprovalsResourceWithStreamingResponse

        return AsyncApprovalsResourceWithStreamingResponse(self._client.approvals)


Client = ParsecAPI

AsyncClient = AsyncParsecAPI
