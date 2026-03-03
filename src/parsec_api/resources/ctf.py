# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ctf_merge_params, ctf_split_params, ctf_redeem_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.ctf_response import CtfResponse

__all__ = ["CtfResource", "AsyncCtfResource"]


class CtfResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return CtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return CtfResourceWithStreamingResponse(self)

    def merge(
        self,
        *,
        amount: str,
        condition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """Merges equal amounts of YES and NO outcome tokens back into USDC collateral.

        The
        transaction is submitted gaslessly through Polymarket's relayer.
        Polymarket-only.

        Args:
          amount: USDC amount in smallest unit (6 decimals).

          condition_id: Condition ID (bytes32 hex).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/polymarket/ctf/merge",
            body=maybe_transform(
                {
                    "amount": amount,
                    "condition_id": condition_id,
                },
                ctf_merge_params.CtfMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )

    def redeem(
        self,
        *,
        condition_id: str,
        amounts: SequenceNotStr[str] | Omit = omit,
        neg_risk: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """Redeems winning outcome tokens for USDC after a market has resolved.

        The
        transaction is submitted gaslessly through Polymarket's relayer. For neg-risk
        markets, set `neg_risk: true` and provide `amounts`. Polymarket-only.

        Args:
          condition_id: Condition ID (bytes32 hex).

          amounts: Token amounts for each outcome (required when neg_risk is true).

          neg_risk: Set to true for neg-risk (multi-outcome) markets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/polymarket/ctf/redeem",
            body=maybe_transform(
                {
                    "condition_id": condition_id,
                    "amounts": amounts,
                    "neg_risk": neg_risk,
                },
                ctf_redeem_params.CtfRedeemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )

    def split(
        self,
        *,
        amount: str,
        condition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """
        Splits USDC collateral into YES and NO outcome tokens for a binary market
        condition. The transaction is submitted gaslessly through Polymarket's relayer.
        Polymarket-only.

        Args:
          amount: USDC amount in smallest unit (6 decimals).

          condition_id: Condition ID (bytes32 hex).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/polymarket/ctf/split",
            body=maybe_transform(
                {
                    "amount": amount,
                    "condition_id": condition_id,
                },
                ctf_split_params.CtfSplitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )


class AsyncCtfResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCtfResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCtfResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCtfResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncCtfResourceWithStreamingResponse(self)

    async def merge(
        self,
        *,
        amount: str,
        condition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """Merges equal amounts of YES and NO outcome tokens back into USDC collateral.

        The
        transaction is submitted gaslessly through Polymarket's relayer.
        Polymarket-only.

        Args:
          amount: USDC amount in smallest unit (6 decimals).

          condition_id: Condition ID (bytes32 hex).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/polymarket/ctf/merge",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "condition_id": condition_id,
                },
                ctf_merge_params.CtfMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )

    async def redeem(
        self,
        *,
        condition_id: str,
        amounts: SequenceNotStr[str] | Omit = omit,
        neg_risk: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """Redeems winning outcome tokens for USDC after a market has resolved.

        The
        transaction is submitted gaslessly through Polymarket's relayer. For neg-risk
        markets, set `neg_risk: true` and provide `amounts`. Polymarket-only.

        Args:
          condition_id: Condition ID (bytes32 hex).

          amounts: Token amounts for each outcome (required when neg_risk is true).

          neg_risk: Set to true for neg-risk (multi-outcome) markets.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/polymarket/ctf/redeem",
            body=await async_maybe_transform(
                {
                    "condition_id": condition_id,
                    "amounts": amounts,
                    "neg_risk": neg_risk,
                },
                ctf_redeem_params.CtfRedeemParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )

    async def split(
        self,
        *,
        amount: str,
        condition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CtfResponse:
        """
        Splits USDC collateral into YES and NO outcome tokens for a binary market
        condition. The transaction is submitted gaslessly through Polymarket's relayer.
        Polymarket-only.

        Args:
          amount: USDC amount in smallest unit (6 decimals).

          condition_id: Condition ID (bytes32 hex).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/polymarket/ctf/split",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "condition_id": condition_id,
                },
                ctf_split_params.CtfSplitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CtfResponse,
        )


class CtfResourceWithRawResponse:
    def __init__(self, ctf: CtfResource) -> None:
        self._ctf = ctf

        self.merge = to_raw_response_wrapper(
            ctf.merge,
        )
        self.redeem = to_raw_response_wrapper(
            ctf.redeem,
        )
        self.split = to_raw_response_wrapper(
            ctf.split,
        )


class AsyncCtfResourceWithRawResponse:
    def __init__(self, ctf: AsyncCtfResource) -> None:
        self._ctf = ctf

        self.merge = async_to_raw_response_wrapper(
            ctf.merge,
        )
        self.redeem = async_to_raw_response_wrapper(
            ctf.redeem,
        )
        self.split = async_to_raw_response_wrapper(
            ctf.split,
        )


class CtfResourceWithStreamingResponse:
    def __init__(self, ctf: CtfResource) -> None:
        self._ctf = ctf

        self.merge = to_streamed_response_wrapper(
            ctf.merge,
        )
        self.redeem = to_streamed_response_wrapper(
            ctf.redeem,
        )
        self.split = to_streamed_response_wrapper(
            ctf.split,
        )


class AsyncCtfResourceWithStreamingResponse:
    def __init__(self, ctf: AsyncCtfResource) -> None:
        self._ctf = ctf

        self.merge = async_to_streamed_response_wrapper(
            ctf.merge,
        )
        self.redeem = async_to_streamed_response_wrapper(
            ctf.redeem,
        )
        self.split = async_to_streamed_response_wrapper(
            ctf.split,
        )
