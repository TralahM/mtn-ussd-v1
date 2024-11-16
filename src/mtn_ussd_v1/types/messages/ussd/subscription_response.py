# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SubscriptionResponse", "_Link", "_LinkSelf", "Data"]


class _LinkSelf(BaseModel):
    href: str


class _Link(BaseModel):
    self: _LinkSelf


class Data(BaseModel):
    subscription_id: Optional[str] = FieldInfo(alias="subscriptionId", default=None)
    """The value is a random number defined by MADAPI and must be unique.

    Associated with the registered USSD.
    """


class SubscriptionResponse(BaseModel):
    api_link: _Link = FieldInfo(alias="_link")

    data: Data

    status_code: str = FieldInfo(alias="statusCode")

    status_message: str = FieldInfo(alias="statusMessage")

    transaction_id: str = FieldInfo(alias="transactionId")
