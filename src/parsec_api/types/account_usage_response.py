# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AccountUsageResponse", "Limits", "Usage"]


class Limits(BaseModel):
    history_max_age_days: int
    """Max historical data age in days. 0 = unlimited."""

    monthly_requests: int
    """Monthly REST request cap. 0 = unlimited."""

    rest_qps: int
    """REST queries per second. 0 = unlimited."""

    rest_qps_burst: int
    """REST burst QPS allowance. 0 = unlimited."""

    ws_max_depth: int
    """Max orderbook depth per WebSocket subscription."""

    ws_max_subscriptions: int
    """Max WebSocket subscriptions across all connections. 0 = unlimited."""


class Usage(BaseModel):
    monthly_requests: int
    """REST requests consumed this billing period."""

    ws_active_connections: int
    """Currently active WebSocket connections."""

    ws_active_subscriptions: int
    """Currently active WebSocket subscriptions."""


class AccountUsageResponse(BaseModel):
    billing_period_end: int
    """Unix seconds — 1st of next month UTC."""

    billing_period_start: int
    """Unix seconds — 1st of current month UTC."""

    limits: Limits

    tier: str
    """Current tier (free, pro, scale)."""

    usage: Usage
