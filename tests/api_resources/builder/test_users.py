# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types.builder import (
    UserListResponse,
    UserCreateResponse,
    UserUpdateResponse,
    UserRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ParsecAPI) -> None:
        user = client.builder.users.create(
            external_id="external_id",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ParsecAPI) -> None:
        user = client.builder.users.create(
            external_id="external_id",
            email="email",
            eoa_address="eoa_address",
            qps_limit=0,
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ParsecAPI) -> None:
        response = client.builder.users.with_raw_response.create(
            external_id="external_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ParsecAPI) -> None:
        with client.builder.users.with_streaming_response.create(
            external_id="external_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        user = client.builder.users.retrieve(
            "customer_id",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.builder.users.with_raw_response.retrieve(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.builder.users.with_streaming_response.retrieve(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.builder.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: ParsecAPI) -> None:
        user = client.builder.users.update(
            customer_id="customer_id",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ParsecAPI) -> None:
        user = client.builder.users.update(
            customer_id="customer_id",
            qps_limit=0,
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ParsecAPI) -> None:
        response = client.builder.users.with_raw_response.update(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ParsecAPI) -> None:
        with client.builder.users.with_streaming_response.update(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.builder.users.with_raw_response.update(
                customer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ParsecAPI) -> None:
        user = client.builder.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ParsecAPI) -> None:
        user = client.builder.users.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ParsecAPI) -> None:
        response = client.builder.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ParsecAPI) -> None:
        with client.builder.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: ParsecAPI) -> None:
        user = client.builder.users.deactivate(
            "customer_id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: ParsecAPI) -> None:
        response = client.builder.users.with_raw_response.deactivate(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: ParsecAPI) -> None:
        with client.builder.users.with_streaming_response.deactivate(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: ParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.builder.users.with_raw_response.deactivate(
                "",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.create(
            external_id="external_id",
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.create(
            external_id="external_id",
            email="email",
            eoa_address="eoa_address",
            qps_limit=0,
        )
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.users.with_raw_response.create(
            external_id="external_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserCreateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.users.with_streaming_response.create(
            external_id="external_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserCreateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.retrieve(
            "customer_id",
        )
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.users.with_raw_response.retrieve(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.users.with_streaming_response.retrieve(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.builder.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.update(
            customer_id="customer_id",
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.update(
            customer_id="customer_id",
            qps_limit=0,
        )
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.users.with_raw_response.update(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUpdateResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.users.with_streaming_response.update(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUpdateResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.builder.users.with_raw_response.update(
                customer_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncParsecAPI) -> None:
        user = await async_client.builder.users.deactivate(
            "customer_id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.builder.users.with_raw_response.deactivate(
            "customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.builder.users.with_streaming_response.deactivate(
            "customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.builder.users.with_raw_response.deactivate(
                "",
            )
