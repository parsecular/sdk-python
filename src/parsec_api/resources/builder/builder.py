# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .escrow import (
    EscrowResource,
    AsyncEscrowResource,
    EscrowResourceWithRawResponse,
    AsyncEscrowResourceWithRawResponse,
    EscrowResourceWithStreamingResponse,
    AsyncEscrowResourceWithStreamingResponse,
)
from .onboard import (
    OnboardResource,
    AsyncOnboardResource,
    OnboardResourceWithRawResponse,
    AsyncOnboardResourceWithRawResponse,
    OnboardResourceWithStreamingResponse,
    AsyncOnboardResourceWithStreamingResponse,
)
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
from ...types.builder_pool_response import BuilderPoolResponse

__all__ = ["BuilderResource", "AsyncBuilderResource"]


class BuilderResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def onboard(self) -> OnboardResource:
        return OnboardResource(self._client)

    @cached_property
    def escrow(self) -> EscrowResource:
        return EscrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> BuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return BuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return BuilderResourceWithStreamingResponse(self)

    def pool(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuilderPoolResponse:
        """
        Returns the builder's QPS pool allocation, end-user count, and total allocated
        QPS.
        """
        return self._get(
            "/api/v1/builder/pool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuilderPoolResponse,
        )


class AsyncBuilderResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def onboard(self) -> AsyncOnboardResource:
        return AsyncOnboardResource(self._client)

    @cached_property
    def escrow(self) -> AsyncEscrowResource:
        return AsyncEscrowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBuilderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBuilderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBuilderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncBuilderResourceWithStreamingResponse(self)

    async def pool(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BuilderPoolResponse:
        """
        Returns the builder's QPS pool allocation, end-user count, and total allocated
        QPS.
        """
        return await self._get(
            "/api/v1/builder/pool",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BuilderPoolResponse,
        )


class BuilderResourceWithRawResponse:
    def __init__(self, builder: BuilderResource) -> None:
        self._builder = builder

        self.pool = to_raw_response_wrapper(
            builder.pool,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._builder.users)

    @cached_property
    def onboard(self) -> OnboardResourceWithRawResponse:
        return OnboardResourceWithRawResponse(self._builder.onboard)

    @cached_property
    def escrow(self) -> EscrowResourceWithRawResponse:
        return EscrowResourceWithRawResponse(self._builder.escrow)


class AsyncBuilderResourceWithRawResponse:
    def __init__(self, builder: AsyncBuilderResource) -> None:
        self._builder = builder

        self.pool = async_to_raw_response_wrapper(
            builder.pool,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._builder.users)

    @cached_property
    def onboard(self) -> AsyncOnboardResourceWithRawResponse:
        return AsyncOnboardResourceWithRawResponse(self._builder.onboard)

    @cached_property
    def escrow(self) -> AsyncEscrowResourceWithRawResponse:
        return AsyncEscrowResourceWithRawResponse(self._builder.escrow)


class BuilderResourceWithStreamingResponse:
    def __init__(self, builder: BuilderResource) -> None:
        self._builder = builder

        self.pool = to_streamed_response_wrapper(
            builder.pool,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._builder.users)

    @cached_property
    def onboard(self) -> OnboardResourceWithStreamingResponse:
        return OnboardResourceWithStreamingResponse(self._builder.onboard)

    @cached_property
    def escrow(self) -> EscrowResourceWithStreamingResponse:
        return EscrowResourceWithStreamingResponse(self._builder.escrow)


class AsyncBuilderResourceWithStreamingResponse:
    def __init__(self, builder: AsyncBuilderResource) -> None:
        self._builder = builder

        self.pool = async_to_streamed_response_wrapper(
            builder.pool,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._builder.users)

    @cached_property
    def onboard(self) -> AsyncOnboardResourceWithStreamingResponse:
        return AsyncOnboardResourceWithStreamingResponse(self._builder.onboard)

    @cached_property
    def escrow(self) -> AsyncEscrowResourceWithStreamingResponse:
        return AsyncEscrowResourceWithStreamingResponse(self._builder.escrow)
