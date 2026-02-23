# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import PriceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        price = client.price.retrieve(
            parsec_id="parsec_id",
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ParsecAPI) -> None:
        price = client.price.retrieve(
            parsec_id="parsec_id",
            at_ts=0,
            end_ts=0,
            interval="1m",
            outcome="outcome",
            start_ts=0,
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.price.with_raw_response.retrieve(
            parsec_id="parsec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.price.with_streaming_response.retrieve(
            parsec_id="parsec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceRetrieveResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        price = await async_client.price.retrieve(
            parsec_id="parsec_id",
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        price = await async_client.price.retrieve(
            parsec_id="parsec_id",
            at_ts=0,
            end_ts=0,
            interval="1m",
            outcome="outcome",
            start_ts=0,
        )
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.price.with_raw_response.retrieve(
            parsec_id="parsec_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = await response.parse()
        assert_matches_type(PriceRetrieveResponse, price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.price.with_streaming_response.retrieve(
            parsec_id="parsec_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceRetrieveResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True
