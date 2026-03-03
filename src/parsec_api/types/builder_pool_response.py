# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BuilderPoolResponse"]


class BuilderPoolResponse(BaseModel):
    end_user_count: int
    """Number of end-users created by this builder."""

    qps_pool: int
    """Total QPS available to this builder."""

    total_allocated_qps: int
    """Total QPS allocated to end-users."""
