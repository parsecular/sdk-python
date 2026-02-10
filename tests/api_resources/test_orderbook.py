# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import OrderbookRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrderbook:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        orderbook = client.orderbook.retrieve(
            parsec_id="parsec_id",
        )
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ParsecAPI) -> None:
        orderbook = client.orderbook.retrieve(
            parsec_id="parsec_id",
            depth=1,
            limit=1,
            outcome="outcome",
        )
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.orderbook.with_raw_response.retrieve(
            parsec_id="parsec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orderbook = response.parse()
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.orderbook.with_streaming_response.retrieve(
            parsec_id="parsec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orderbook = response.parse()
            assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrderbook:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        orderbook = await async_client.orderbook.retrieve(
            parsec_id="parsec_id",
        )
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        orderbook = await async_client.orderbook.retrieve(
            parsec_id="parsec_id",
            depth=1,
            limit=1,
            outcome="outcome",
        )
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.orderbook.with_raw_response.retrieve(
            parsec_id="parsec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        orderbook = await response.parse()
        assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.orderbook.with_streaming_response.retrieve(
            parsec_id="parsec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            orderbook = await response.parse()
            assert_matches_type(OrderbookRetrieveResponse, orderbook, path=["response"])

        assert cast(Any, response.is_closed) is True
