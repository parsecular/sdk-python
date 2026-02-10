# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import ExchangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExchanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ParsecAPI) -> None:
        exchange = client.exchanges.list()
        assert_matches_type(ExchangeListResponse, exchange, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ParsecAPI) -> None:
        response = client.exchanges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = response.parse()
        assert_matches_type(ExchangeListResponse, exchange, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ParsecAPI) -> None:
        with client.exchanges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = response.parse()
            assert_matches_type(ExchangeListResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExchanges:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncParsecAPI) -> None:
        exchange = await async_client.exchanges.list()
        assert_matches_type(ExchangeListResponse, exchange, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.exchanges.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exchange = await response.parse()
        assert_matches_type(ExchangeListResponse, exchange, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.exchanges.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exchange = await response.parse()
            assert_matches_type(ExchangeListResponse, exchange, path=["response"])

        assert cast(Any, response.is_closed) is True
