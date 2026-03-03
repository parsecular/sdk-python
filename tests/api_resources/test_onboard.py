# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import OnboardCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnboard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ParsecAPI) -> None:
        onboard = client.onboard.create(
            exchange="exchange",
            mode="managed",
        )
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ParsecAPI) -> None:
        onboard = client.onboard.create(
            exchange="exchange",
            mode="managed",
            api_key_id="api_key_id",
            chain_id=0,
            clob_api_key="clob_api_key",
            clob_api_passphrase="clob_api_passphrase",
            clob_api_secret="clob_api_secret",
            eoa_address="eoa_address",
            private_key="private_key",
            wallet_type="wallet_type",
        )
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ParsecAPI) -> None:
        response = client.onboard.with_raw_response.create(
            exchange="exchange",
            mode="managed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboard = response.parse()
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ParsecAPI) -> None:
        with client.onboard.with_streaming_response.create(
            exchange="exchange",
            mode="managed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboard = response.parse()
            assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnboard:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncParsecAPI) -> None:
        onboard = await async_client.onboard.create(
            exchange="exchange",
            mode="managed",
        )
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        onboard = await async_client.onboard.create(
            exchange="exchange",
            mode="managed",
            api_key_id="api_key_id",
            chain_id=0,
            clob_api_key="clob_api_key",
            clob_api_passphrase="clob_api_passphrase",
            clob_api_secret="clob_api_secret",
            eoa_address="eoa_address",
            private_key="private_key",
            wallet_type="wallet_type",
        )
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.onboard.with_raw_response.create(
            exchange="exchange",
            mode="managed",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboard = await response.parse()
        assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.onboard.with_streaming_response.create(
            exchange="exchange",
            mode="managed",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboard = await response.parse()
            assert_matches_type(OnboardCreateResponse, onboard, path=["response"])

        assert cast(Any, response.is_closed) is True
