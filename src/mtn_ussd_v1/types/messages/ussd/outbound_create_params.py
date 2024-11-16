# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["OutboundCreateParams"]


class OutboundCreateParams(TypedDict, total=False):
    message_type: Required[Annotated[str, PropertyInfo(alias="messageType")]]
    """Message type. 0-Begin|1-Continue|2-End|3-Notification|4-Cancel|5-Timeout."""

    msisdn: Required[str]
    """Mobile number of the message recipient."""

    service_code: Required[Annotated[str, PropertyInfo(alias="serviceCode")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionId")]]
    """Unique identifier of the session."""

    ussd_string: Required[Annotated[str, PropertyInfo(alias="ussdString")]]
    """USSD message content.

    If messageType is of type 4-Abort, this attribute will contain the abort reason
    or message.
    """
