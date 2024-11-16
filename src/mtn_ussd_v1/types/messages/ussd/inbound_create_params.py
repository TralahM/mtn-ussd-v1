# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InboundCreateParams"]


class InboundCreateParams(TypedDict, total=False):
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

    cell_id: Annotated[str, PropertyInfo(alias="cellId")]
    """Cell Id of the subscriber.

    A GSM Cell ID (CID) is a unique number used to identify each base transceiver
    station (BTS) or sector of a BTS within a location area code (LAC) if not within
    a GSM network.
    """

    imsi: str
    """IMSI of the subscriber.

    An international mobile subscriber identity (IMSI) is a unique number, usually
    fifteen digits, associated with Global System for Mobile Communications (GSM)
    and Universal Mobile Telecommunications System (UMTS) network mobile phone
    users. The IMSI is a unique number identifying a GSM subscriber.
    """

    language: str
    """Language of preference of the subscriber"""
