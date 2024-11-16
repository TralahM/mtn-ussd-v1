# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    callback_url: Required[Annotated[str, PropertyInfo(alias="callbackUrl")]]
    """URL from which the 3PP will receive MO-generated USSD message."""

    service_code: Required[Annotated[str, PropertyInfo(alias="serviceCode")]]

    target_system: Required[Annotated[str, PropertyInfo(alias="targetSystem")]]
    """Name of the destined system for the callback url."""
