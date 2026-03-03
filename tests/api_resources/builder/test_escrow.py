# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types.builder import EscrowConfigResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEscrow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_config(self, client: ParsecAPI) -> None:
        escrow = client.builder.escrow.config()
        assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_config(self, client: ParsecAPI) -> None:
        response = client.builder.escrow.with_raw_response.config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        escrow = response.parse()
        assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_config(self, client: ParsecAPI) -> None:
        with client.builder.escrow.with_streaming_response.config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            escrow = response.parse()
            assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEscrow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_config(self, async_client: AsyncParsecAPI) -> None:
        escrow = await async_client.builder.escrow.config()
        assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_config(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.escrow.with_raw_response.config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        escrow = await response.parse()
        assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_config(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.escrow.with_streaming_response.config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            escrow = await response.parse()
            assert_matches_type(EscrowConfigResponse, escrow, path=["response"])

        assert cast(Any, response.is_closed) is True
