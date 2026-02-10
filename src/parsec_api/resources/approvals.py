# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import approval_set_params, approval_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.approval_set_response import ApprovalSetResponse
from ..types.approval_list_response import ApprovalListResponse

__all__ = ["ApprovalsResource", "AsyncApprovalsResource"]


class ApprovalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApprovalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#accessing-raw-response-data-eg-headers
        """
        return ApprovalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApprovalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#with_streaming_response
        """
        return ApprovalsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        exchange: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApprovalListResponse:
        """
        Polymarket-only helper for checking on-chain allowances required for trading.

        Args:
          exchange: Must be "polymarket".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/approvals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exchange": exchange}, approval_list_params.ApprovalListParams),
            ),
            cast_to=ApprovalListResponse,
        )

    def set(
        self,
        *,
        exchange: str,
        all: bool | Omit = omit,
        ctf: bool | Omit = omit,
        ctf_neg_risk: bool | Omit = omit,
        usdc: bool | Omit = omit,
        usdc_neg_risk: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApprovalSetResponse:
        """
        Polymarket-only helper for submitting approval transactions.

        Args:
          exchange: Must be "polymarket".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/approvals",
            body=maybe_transform(
                {
                    "all": all,
                    "ctf": ctf,
                    "ctf_neg_risk": ctf_neg_risk,
                    "usdc": usdc,
                    "usdc_neg_risk": usdc_neg_risk,
                },
                approval_set_params.ApprovalSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exchange": exchange}, approval_set_params.ApprovalSetParams),
            ),
            cast_to=ApprovalSetResponse,
        )


class AsyncApprovalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApprovalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApprovalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApprovalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/parsec-api-python#with_streaming_response
        """
        return AsyncApprovalsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        exchange: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApprovalListResponse:
        """
        Polymarket-only helper for checking on-chain allowances required for trading.

        Args:
          exchange: Must be "polymarket".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/approvals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exchange": exchange}, approval_list_params.ApprovalListParams),
            ),
            cast_to=ApprovalListResponse,
        )

    async def set(
        self,
        *,
        exchange: str,
        all: bool | Omit = omit,
        ctf: bool | Omit = omit,
        ctf_neg_risk: bool | Omit = omit,
        usdc: bool | Omit = omit,
        usdc_neg_risk: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApprovalSetResponse:
        """
        Polymarket-only helper for submitting approval transactions.

        Args:
          exchange: Must be "polymarket".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/approvals",
            body=await async_maybe_transform(
                {
                    "all": all,
                    "ctf": ctf,
                    "ctf_neg_risk": ctf_neg_risk,
                    "usdc": usdc,
                    "usdc_neg_risk": usdc_neg_risk,
                },
                approval_set_params.ApprovalSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exchange": exchange}, approval_set_params.ApprovalSetParams),
            ),
            cast_to=ApprovalSetResponse,
        )


class ApprovalsResourceWithRawResponse:
    def __init__(self, approvals: ApprovalsResource) -> None:
        self._approvals = approvals

        self.list = to_raw_response_wrapper(
            approvals.list,
        )
        self.set = to_raw_response_wrapper(
            approvals.set,
        )


class AsyncApprovalsResourceWithRawResponse:
    def __init__(self, approvals: AsyncApprovalsResource) -> None:
        self._approvals = approvals

        self.list = async_to_raw_response_wrapper(
            approvals.list,
        )
        self.set = async_to_raw_response_wrapper(
            approvals.set,
        )


class ApprovalsResourceWithStreamingResponse:
    def __init__(self, approvals: ApprovalsResource) -> None:
        self._approvals = approvals

        self.list = to_streamed_response_wrapper(
            approvals.list,
        )
        self.set = to_streamed_response_wrapper(
            approvals.set,
        )


class AsyncApprovalsResourceWithStreamingResponse:
    def __init__(self, approvals: AsyncApprovalsResource) -> None:
        self._approvals = approvals

        self.list = async_to_streamed_response_wrapper(
            approvals.list,
        )
        self.set = async_to_streamed_response_wrapper(
            approvals.set,
        )
