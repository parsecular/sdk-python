# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomerUsage"]


class CustomerUsage(BaseModel):
    active_connections: int

    active_subscriptions: int

    auth_failures_total: int

    bytes_sent_total: int

    connections_closed_total: int

    connections_opened_total: int

    customer_id: str

    messages_sent_total: int

    subscribe_requests_total: int

    unsubscribe_requests_total: int
