# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["OutboundCreateResponse", "_Link", "_LinkSelf", "Data"]


class _LinkSelf(BaseModel):
    href: str


class _Link(BaseModel):
    self: _LinkSelf


class Data(BaseModel):
    msisdn: str
    """Mobile user msisdn."""

    outbound_response: str = FieldInfo(alias="outboundResponse")
    """Value 0 indicates success."""

    session_id: str = FieldInfo(alias="sessionId")
    """Unique identifier of the session."""


class OutboundCreateResponse(BaseModel):
    api_link: _Link = FieldInfo(alias="_link")

    data: Data

    status_code: str = FieldInfo(alias="statusCode")

    status_message: str = FieldInfo(alias="statusMessage")

    transaction_id: str = FieldInfo(alias="transactionId")
