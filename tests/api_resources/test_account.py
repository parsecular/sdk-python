# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import (
    AccountPingResponse,
    AccountBalanceResponse,
    AccountUserActivityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_balance(self, client: ParsecAPI) -> None:
        account = client.account.balance(
            exchange="exchange",
        )
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_balance_with_all_params(self, client: ParsecAPI) -> None:
        account = client.account.balance(
            exchange="exchange",
            refresh=True,
        )
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_balance(self, client: ParsecAPI) -> None:
        response = client.account.with_raw_response.balance(
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_balance(self, client: ParsecAPI) -> None:
        with client.account.with_streaming_response.balance(
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountBalanceResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_ping(self, client: ParsecAPI) -> None:
        account = client.account.ping()
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_ping_with_all_params(self, client: ParsecAPI) -> None:
        account = client.account.ping(
            exchange="exchange",
        )
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_ping(self, client: ParsecAPI) -> None:
        response = client.account.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_ping(self, client: ParsecAPI) -> None:
        with client.account.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountPingResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_credentials(self, client: ParsecAPI) -> None:
        account = client.account.update_credentials()
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_credentials_with_all_params(self, client: ParsecAPI) -> None:
        account = client.account.update_credentials(
            evm_private_key="evm_private_key",
            kalshi_api_key_id="kalshi_api_key_id",
            kalshi_private_key="kalshi_private_key",
            poly_funder="poly_funder",
            poly_signature_type="poly_signature_type",
        )
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_credentials(self, client: ParsecAPI) -> None:
        response = client.account.with_raw_response.update_credentials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_credentials(self, client: ParsecAPI) -> None:
        with client.account.with_streaming_response.update_credentials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_user_activity(self, client: ParsecAPI) -> None:
        account = client.account.user_activity(
            address="address",
        )
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_user_activity_with_all_params(self, client: ParsecAPI) -> None:
        account = client.account.user_activity(
            address="address",
            exchanges=["string"],
            limit=1,
        )
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_user_activity(self, client: ParsecAPI) -> None:
        response = client.account.with_raw_response.user_activity(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_user_activity(self, client: ParsecAPI) -> None:
        with client.account.with_streaming_response.user_activity(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUserActivityResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_balance(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.balance(
            exchange="exchange",
        )
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_balance_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.balance(
            exchange="exchange",
            refresh=True,
        )
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_balance(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.account.with_raw_response.balance(
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountBalanceResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_balance(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.account.with_streaming_response.balance(
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountBalanceResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_ping(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.ping()
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_ping_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.ping(
            exchange="exchange",
        )
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_ping(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.account.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountPingResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_ping(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.account.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountPingResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_credentials(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.update_credentials()
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_credentials_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.update_credentials(
            evm_private_key="evm_private_key",
            kalshi_api_key_id="kalshi_api_key_id",
            kalshi_private_key="kalshi_private_key",
            poly_funder="poly_funder",
            poly_signature_type="poly_signature_type",
        )
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_credentials(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.account.with_raw_response.update_credentials()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert account is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_credentials(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.account.with_streaming_response.update_credentials() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_user_activity(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.user_activity(
            address="address",
        )
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_user_activity_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        account = await async_client.account.user_activity(
            address="address",
            exchanges=["string"],
            limit=1,
        )
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_user_activity(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.account.with_raw_response.user_activity(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUserActivityResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_user_activity(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.account.with_streaming_response.user_activity(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUserActivityResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
