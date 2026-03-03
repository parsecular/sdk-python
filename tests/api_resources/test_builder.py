# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import BuilderPoolResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBuilder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pool(self, client: ParsecAPI) -> None:
        builder = client.builder.pool()
        assert_matches_type(BuilderPoolResponse, builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pool(self, client: ParsecAPI) -> None:
        response = client.builder.with_raw_response.pool()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        builder = response.parse()
        assert_matches_type(BuilderPoolResponse, builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pool(self, client: ParsecAPI) -> None:
        with client.builder.with_streaming_response.pool() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            builder = response.parse()
            assert_matches_type(BuilderPoolResponse, builder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBuilder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pool(self, async_client: AsyncParsecAPI) -> None:
        builder = await async_client.builder.pool()
        assert_matches_type(BuilderPoolResponse, builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pool(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.with_raw_response.pool()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        builder = await response.parse()
        assert_matches_type(BuilderPoolResponse, builder, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pool(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.with_streaming_response.pool() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            builder = await response.parse()
            assert_matches_type(BuilderPoolResponse, builder, path=["response"])

        assert cast(Any, response.is_closed) is True
