# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.builder.escrow_config_response import EscrowConfigResponse

__all__ = ["EscrowResource", "AsyncEscrowResource"]


class EscrowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EscrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return EscrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EscrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return EscrowResourceWithStreamingResponse(self)

    def config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EscrowConfigResponse:
        """
        Returns the builder's fee escrow configuration including contract address, fee
        rates, and treasury address. Read-only — fee escrow is configured by Parsec
        admins during onboarding.
        """
        return self._get(
            "/api/v1/builder/escrow/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EscrowConfigResponse,
        )


class AsyncEscrowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEscrowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEscrowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEscrowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncEscrowResourceWithStreamingResponse(self)

    async def config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EscrowConfigResponse:
        """
        Returns the builder's fee escrow configuration including contract address, fee
        rates, and treasury address. Read-only — fee escrow is configured by Parsec
        admins during onboarding.
        """
        return await self._get(
            "/api/v1/builder/escrow/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EscrowConfigResponse,
        )


class EscrowResourceWithRawResponse:
    def __init__(self, escrow: EscrowResource) -> None:
        self._escrow = escrow

        self.config = to_raw_response_wrapper(
            escrow.config,
        )


class AsyncEscrowResourceWithRawResponse:
    def __init__(self, escrow: AsyncEscrowResource) -> None:
        self._escrow = escrow

        self.config = async_to_raw_response_wrapper(
            escrow.config,
        )


class EscrowResourceWithStreamingResponse:
    def __init__(self, escrow: EscrowResource) -> None:
        self._escrow = escrow

        self.config = to_streamed_response_wrapper(
            escrow.config,
        )


class AsyncEscrowResourceWithStreamingResponse:
    def __init__(self, escrow: AsyncEscrowResource) -> None:
        self._escrow = escrow

        self.config = async_to_streamed_response_wrapper(
            escrow.config,
        )
