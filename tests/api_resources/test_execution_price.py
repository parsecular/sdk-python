# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import ExecutionPriceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutionPrice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        execution_price = client.execution_price.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        )
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ParsecAPI) -> None:
        execution_price = client.execution_price.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
            outcome="outcome",
        )
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.execution_price.with_raw_response.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution_price = response.parse()
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.execution_price.with_streaming_response.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution_price = response.parse()
            assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecutionPrice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        execution_price = await async_client.execution_price.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        )
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        execution_price = await async_client.execution_price.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
            outcome="outcome",
        )
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.execution_price.with_raw_response.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution_price = await response.parse()
        assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.execution_price.with_streaming_response.retrieve(
            amount=0,
            parsec_id="parsec_id",
            side="buy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution_price = await response.parse()
            assert_matches_type(ExecutionPriceRetrieveResponse, execution_price, path=["response"])

        assert cast(Any, response.is_closed) is True
