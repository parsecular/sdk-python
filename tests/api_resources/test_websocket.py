# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import WebsocketUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebsocket:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_usage(self, client: ParsecAPI) -> None:
        websocket = client.websocket.usage()
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_usage_with_all_params(self, client: ParsecAPI) -> None:
        websocket = client.websocket.usage(
            limit=1,
            scope="scope",
        )
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_usage(self, client: ParsecAPI) -> None:
        response = client.websocket.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websocket = response.parse()
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_usage(self, client: ParsecAPI) -> None:
        with client.websocket.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websocket = response.parse()
            assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebsocket:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_usage(self, async_client: AsyncParsecAPI) -> None:
        websocket = await async_client.websocket.usage()
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_usage_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        websocket = await async_client.websocket.usage(
            limit=1,
            scope="scope",
        )
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.websocket.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        websocket = await response.parse()
        assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.websocket.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            websocket = await response.parse()
            assert_matches_type(WebsocketUsageResponse, websocket, path=["response"])

        assert cast(Any, response.is_closed) is True
