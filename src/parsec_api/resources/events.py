# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import event_list_params
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
from ..types.event_list_response import EventListResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        exchange: str | Omit = omit,
        exchange_group_id: str | Omit = omit,
        exchanges: SequenceNotStr[str] | Omit = omit,
        include_markets: bool | Omit = omit,
        limit: int | Omit = omit,
        min_volume: float | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """Aggregates markets by event ID from the DuckDB gold layer.

        Returns event
        summaries sorted by total volume (descending). Markets without an event_id are
        excluded.

        Exact lookup mode is available via either `event_id` or `exchange` +
        `exchange_group_id`. Exact lookup returns the normal `EventsResponse` wrapper
        with either zero or one event. Returned `event_id` values are the stored
        gold-layer event-group IDs (typically `parsec_group_id`); lookup also accepts
        `ev:{event_id}` aliases.

        Args:
          cursor: Pagination cursor (offset-based). Only valid for list mode.

          event_id: Exact event lookup by stored event-group ID. The `ev:{event_id}` alias form is
              also accepted. Mutually exclusive with `exchange` + `exchange_group_id`.

          exchange: Exchange selector for exact external event lookup. Must be paired with
              `exchange_group_id`.

          exchange_group_id: Exchange-native event/group ID. Must be paired with `exchange`.

          exchanges: Exchanges to include (CSV). Defaults to all exchanges in the cache. Only valid
              for list mode.

          include_markets: Include constituent markets in the response (default false).

          limit: Results per page (default 50, max 100). Only valid for list mode.

          min_volume: Minimum total volume across all markets in event. Only valid for list mode.

          search: Keyword search in event title (case-insensitive). Only valid for list mode.

          status: Status filter (e.g., active, closed, resolved, archived). Only valid for list
              mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "exchange": exchange,
                        "exchange_group_id": exchange_group_id,
                        "exchanges": exchanges,
                        "include_markets": include_markets,
                        "limit": limit,
                        "min_volume": min_volume,
                        "search": search,
                        "status": status,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parsecular/sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parsecular/sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_id: str | Omit = omit,
        exchange: str | Omit = omit,
        exchange_group_id: str | Omit = omit,
        exchanges: SequenceNotStr[str] | Omit = omit,
        include_markets: bool | Omit = omit,
        limit: int | Omit = omit,
        min_volume: float | Omit = omit,
        search: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """Aggregates markets by event ID from the DuckDB gold layer.

        Returns event
        summaries sorted by total volume (descending). Markets without an event_id are
        excluded.

        Exact lookup mode is available via either `event_id` or `exchange` +
        `exchange_group_id`. Exact lookup returns the normal `EventsResponse` wrapper
        with either zero or one event. Returned `event_id` values are the stored
        gold-layer event-group IDs (typically `parsec_group_id`); lookup also accepts
        `ev:{event_id}` aliases.

        Args:
          cursor: Pagination cursor (offset-based). Only valid for list mode.

          event_id: Exact event lookup by stored event-group ID. The `ev:{event_id}` alias form is
              also accepted. Mutually exclusive with `exchange` + `exchange_group_id`.

          exchange: Exchange selector for exact external event lookup. Must be paired with
              `exchange_group_id`.

          exchange_group_id: Exchange-native event/group ID. Must be paired with `exchange`.

          exchanges: Exchanges to include (CSV). Defaults to all exchanges in the cache. Only valid
              for list mode.

          include_markets: Include constituent markets in the response (default false).

          limit: Results per page (default 50, max 100). Only valid for list mode.

          min_volume: Minimum total volume across all markets in event. Only valid for list mode.

          search: Keyword search in event title (case-insensitive). Only valid for list mode.

          status: Status filter (e.g., active, closed, resolved, archived). Only valid for list
              mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_id": event_id,
                        "exchange": exchange,
                        "exchange_group_id": exchange_group_id,
                        "exchanges": exchanges,
                        "include_markets": include_markets,
                        "limit": limit,
                        "min_volume": min_volume,
                        "search": search,
                        "status": status,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
