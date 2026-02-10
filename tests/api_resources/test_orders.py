# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parsec_api import ParsecAPI, AsyncParsecAPI
from tests.utils import assert_matches_type
from parsec_api.types import (
    Order,
    OrderListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ParsecAPI) -> None:
        order = client.orders.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ParsecAPI) -> None:
        order = client.orders.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
            params={"foo": "string"},
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ParsecAPI) -> None:
        response = client.orders.with_raw_response.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ParsecAPI) -> None:
        with client.orders.with_streaming_response.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ParsecAPI) -> None:
        order = client.orders.retrieve(
            order_id="order_id",
            exchange="exchange",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ParsecAPI) -> None:
        response = client.orders.with_raw_response.retrieve(
            order_id="order_id",
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ParsecAPI) -> None:
        with client.orders.with_streaming_response.retrieve(
            order_id="order_id",
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.orders.with_raw_response.retrieve(
                order_id="",
                exchange="exchange",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ParsecAPI) -> None:
        order = client.orders.list(
            exchange="exchange",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ParsecAPI) -> None:
        order = client.orders.list(
            exchange="exchange",
            market_id="market_id",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ParsecAPI) -> None:
        response = client.orders.with_raw_response.list(
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ParsecAPI) -> None:
        with client.orders.with_streaming_response.list(
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: ParsecAPI) -> None:
        order = client.orders.cancel(
            order_id="order_id",
            exchange="exchange",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: ParsecAPI) -> None:
        response = client.orders.with_raw_response.cancel(
            order_id="order_id",
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: ParsecAPI) -> None:
        with client.orders.with_streaming_response.cancel(
            order_id="order_id",
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: ParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.orders.with_raw_response.cancel(
                order_id="",
                exchange="exchange",
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
            params={"foo": "string"},
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.orders.with_raw_response.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.orders.with_streaming_response.create(
            exchange="exchange",
            market_id="market_id",
            outcome="outcome",
            price=0,
            side="buy",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.retrieve(
            order_id="order_id",
            exchange="exchange",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.orders.with_raw_response.retrieve(
            order_id="order_id",
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.orders.with_streaming_response.retrieve(
            order_id="order_id",
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.orders.with_raw_response.retrieve(
                order_id="",
                exchange="exchange",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.list(
            exchange="exchange",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.list(
            exchange="exchange",
            market_id="market_id",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.orders.with_raw_response.list(
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.orders.with_streaming_response.list(
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncParsecAPI) -> None:
        order = await async_client.orders.cancel(
            order_id="order_id",
            exchange="exchange",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncParsecAPI) -> None:
        response = await async_client.orders.with_raw_response.cancel(
            order_id="order_id",
            exchange="exchange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncParsecAPI) -> None:
        async with async_client.orders.with_streaming_response.cancel(
            order_id="order_id",
            exchange="exchange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncParsecAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.orders.with_raw_response.cancel(
                order_id="",
                exchange="exchange",
            )
