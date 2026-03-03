# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import (
    PolymarketAuthMessageResponse,
    PolymarketAuthCredentialsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPolymarketAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_credentials(self, client: ParsecAPI) -> None:
        polymarket_auth = client.polymarket_auth.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        )
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_credentials_with_all_params(self, client: ParsecAPI) -> None:
        polymarket_auth = client.polymarket_auth.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
            store=True,
        )
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_credentials(self, client: ParsecAPI) -> None:
        response = client.polymarket_auth.with_raw_response.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polymarket_auth = response.parse()
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_credentials(self, client: ParsecAPI) -> None:
        with client.polymarket_auth.with_streaming_response.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polymarket_auth = response.parse()
            assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_message(self, client: ParsecAPI) -> None:
        polymarket_auth = client.polymarket_auth.message(
            address="address",
        )
        assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_message(self, client: ParsecAPI) -> None:
        response = client.polymarket_auth.with_raw_response.message(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polymarket_auth = response.parse()
        assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_message(self, client: ParsecAPI) -> None:
        with client.polymarket_auth.with_streaming_response.message(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polymarket_auth = response.parse()
            assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPolymarketAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_credentials(self, async_client: AsyncParsecAPI) -> None:
        polymarket_auth = await async_client.polymarket_auth.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        )
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_credentials_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        polymarket_auth = await async_client.polymarket_auth.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
            store=True,
        )
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_credentials(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.polymarket_auth.with_raw_response.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polymarket_auth = await response.parse()
        assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_credentials(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.polymarket_auth.with_streaming_response.credentials(
            address="address",
            signature="signature",
            timestamp="timestamp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polymarket_auth = await response.parse()
            assert_matches_type(PolymarketAuthCredentialsResponse, polymarket_auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_message(self, async_client: AsyncParsecAPI) -> None:
        polymarket_auth = await async_client.polymarket_auth.message(
            address="address",
        )
        assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_message(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.polymarket_auth.with_raw_response.message(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        polymarket_auth = await response.parse()
        assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_message(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.polymarket_auth.with_streaming_response.message(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            polymarket_auth = await response.parse()
            assert_matches_type(PolymarketAuthMessageResponse, polymarket_auth, path=["response"])

        assert cast(Any, response.is_closed) is True
