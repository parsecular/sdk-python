# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import MarketListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ParsecAPI) -> None:
        market = client.markets.list()
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ParsecAPI) -> None:
        market = client.markets.list(
            cursor="cursor",
            event_id="event_id",
            exchanges=["string"],
            group_id="group_id",
            limit=1,
            min_liquidity=0,
            min_volume=0,
            parsec_ids=["string"],
            search="search",
            status="active",
        )
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ParsecAPI) -> None:
        response = client.markets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ParsecAPI) -> None:
        with client.markets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(MarketListResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMarkets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncParsecAPI) -> None:
        market = await async_client.markets.list()
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        market = await async_client.markets.list(
            cursor="cursor",
            event_id="event_id",
            exchanges=["string"],
            group_id="group_id",
            limit=1,
            min_liquidity=0,
            min_volume=0,
            parsec_ids=["string"],
            search="search",
            status="active",
        )
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.markets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(MarketListResponse, market, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.markets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(MarketListResponse, market, path=["response"])

        assert cast(Any, response.is_closed) is True
