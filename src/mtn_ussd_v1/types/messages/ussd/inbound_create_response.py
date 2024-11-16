# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["InboundCreateResponse", "_Link", "_LinkSelf", "Data"]


class _LinkSelf(BaseModel):
    href: str


class _Link(BaseModel):
    self: _LinkSelf


class Data(BaseModel):
    inbound_response: Optional[str] = FieldInfo(alias="inboundResponse", default=None)
    """Response value."""

    message_type: Optional[int] = FieldInfo(alias="messageType", default=None)
    """The messageType to send"""

    msisdn: Optional[str] = None
    """The msisdn to send the response to."""

    service_code: Optional[str] = FieldInfo(alias="serviceCode", default=None)
    """The service code or short code of the service."""

    user_input_required: Optional[bool] = FieldInfo(alias="userInputRequired", default=None)
    """Is user input required."""


class InboundCreateResponse(BaseModel):
    api_link: _Link = FieldInfo(alias="_link")

    data: Data

    status_code: str = FieldInfo(alias="statusCode")

    status_message: str = FieldInfo(alias="statusMessage")

    transaction_id: str = FieldInfo(alias="transactionId")
