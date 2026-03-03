# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import WalletRetrieveResponse, WalletExportKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        wallet = client.wallet.retrieve()
        assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.wallet.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.wallet.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_key(self, client: ParsecAPI) -> None:
        wallet = client.wallet.export_key()
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_export_key_with_all_params(self, client: ParsecAPI) -> None:
        wallet = client.wallet.export_key(
            wallet_type="eoa",
        )
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_export_key(self, client: ParsecAPI) -> None:
        response = client.wallet.with_raw_response.export_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_export_key(self, client: ParsecAPI) -> None:
        with client.wallet.with_streaming_response.export_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWallet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        wallet = await async_client.wallet.retrieve()
        assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.wallet.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.wallet.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRetrieveResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_key(self, async_client: AsyncParsecAPI) -> None:
        wallet = await async_client.wallet.export_key()
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_export_key_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        wallet = await async_client.wallet.export_key(
            wallet_type="eoa",
        )
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_export_key(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.wallet.with_raw_response.export_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_export_key(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.wallet.with_streaming_response.export_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletExportKeyResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True
