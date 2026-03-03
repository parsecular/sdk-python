# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import CtfResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCtf:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_merge(self, client: ParsecAPI) -> None:
        ctf = client.ctf.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: ParsecAPI) -> None:
        response = client.ctf.with_raw_response.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: ParsecAPI) -> None:
        with client.ctf.with_streaming_response.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_redeem(self, client: ParsecAPI) -> None:
        ctf = client.ctf.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_redeem_with_all_params(self, client: ParsecAPI) -> None:
        ctf = client.ctf.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            amounts=["500000", "500000"],
            neg_risk=True,
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_redeem(self, client: ParsecAPI) -> None:
        response = client.ctf.with_raw_response.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_redeem(self, client: ParsecAPI) -> None:
        with client.ctf.with_streaming_response.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_split(self, client: ParsecAPI) -> None:
        ctf = client.ctf.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_split(self, client: ParsecAPI) -> None:
        response = client.ctf.with_raw_response.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_split(self, client: ParsecAPI) -> None:
        with client.ctf.with_streaming_response.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCtf:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncParsecAPI) -> None:
        ctf = await async_client.ctf.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.ctf.with_raw_response.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = await response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.ctf.with_streaming_response.merge(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = await response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_redeem(self, async_client: AsyncParsecAPI) -> None:
        ctf = await async_client.ctf.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_redeem_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        ctf = await async_client.ctf.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            amounts=["500000", "500000"],
            neg_risk=True,
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_redeem(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.ctf.with_raw_response.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = await response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_redeem(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.ctf.with_streaming_response.redeem(
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = await response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_split(self, async_client: AsyncParsecAPI) -> None:
        ctf = await async_client.ctf.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_split(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.ctf.with_raw_response.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ctf = await response.parse()
        assert_matches_type(CtfResponse, ctf, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_split(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.ctf.with_streaming_response.split(
            amount="1000000",
            condition_id="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ctf = await response.parse()
            assert_matches_type(CtfResponse, ctf, path=["response"])

        assert cast(Any, response.is_closed) is True
