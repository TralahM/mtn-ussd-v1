# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.messages.ussd import inbound_create_params
from ....types.messages.ussd.inbound_create_response import InboundCreateResponse

__all__ = ["InboundResource", "AsyncInboundResource"]


class InboundResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return InboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return InboundResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message_type: str,
        msisdn: str,
        service_code: str,
        session_id: str,
        ussd_string: str,
        cell_id: str | NotGiven = NOT_GIVEN,
        imsi: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundCreateResponse:
        """
        This function sends USSD MO-generated message to a 3PP with subscription on
        MADAPI.

        Args:
          message_type: Message type. 0-Begin|1-Continue|2-End|3-Notification|4-Cancel|5-Timeout.

          msisdn: Mobile number of the message recipient.

          session_id: Unique identifier of the session.

          ussd_string: USSD message content. If messageType is of type 4-Abort, this attribute will
              contain the abort reason or message.

          cell_id: Cell Id of the subscriber. A GSM Cell ID (CID) is a unique number used to
              identify each base transceiver station (BTS) or sector of a BTS within a
              location area code (LAC) if not within a GSM network.

          imsi: IMSI of the subscriber. An international mobile subscriber identity (IMSI) is a
              unique number, usually fifteen digits, associated with Global System for Mobile
              Communications (GSM) and Universal Mobile Telecommunications System (UMTS)
              network mobile phone users. The IMSI is a unique number identifying a GSM
              subscriber.

          language: Language of preference of the subscriber

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/ussd/inbound",
            body=maybe_transform(
                {
                    "message_type": message_type,
                    "msisdn": msisdn,
                    "service_code": service_code,
                    "session_id": session_id,
                    "ussd_string": ussd_string,
                    "cell_id": cell_id,
                    "imsi": imsi,
                    "language": language,
                },
                inbound_create_params.InboundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundCreateResponse,
        )


class AsyncInboundResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return AsyncInboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return AsyncInboundResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message_type: str,
        msisdn: str,
        service_code: str,
        session_id: str,
        ussd_string: str,
        cell_id: str | NotGiven = NOT_GIVEN,
        imsi: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InboundCreateResponse:
        """
        This function sends USSD MO-generated message to a 3PP with subscription on
        MADAPI.

        Args:
          message_type: Message type. 0-Begin|1-Continue|2-End|3-Notification|4-Cancel|5-Timeout.

          msisdn: Mobile number of the message recipient.

          session_id: Unique identifier of the session.

          ussd_string: USSD message content. If messageType is of type 4-Abort, this attribute will
              contain the abort reason or message.

          cell_id: Cell Id of the subscriber. A GSM Cell ID (CID) is a unique number used to
              identify each base transceiver station (BTS) or sector of a BTS within a
              location area code (LAC) if not within a GSM network.

          imsi: IMSI of the subscriber. An international mobile subscriber identity (IMSI) is a
              unique number, usually fifteen digits, associated with Global System for Mobile
              Communications (GSM) and Universal Mobile Telecommunications System (UMTS)
              network mobile phone users. The IMSI is a unique number identifying a GSM
              subscriber.

          language: Language of preference of the subscriber

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/ussd/inbound",
            body=await async_maybe_transform(
                {
                    "message_type": message_type,
                    "msisdn": msisdn,
                    "service_code": service_code,
                    "session_id": session_id,
                    "ussd_string": ussd_string,
                    "cell_id": cell_id,
                    "imsi": imsi,
                    "language": language,
                },
                inbound_create_params.InboundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InboundCreateResponse,
        )


class InboundResourceWithRawResponse:
    def __init__(self, inbound: InboundResource) -> None:
        self._inbound = inbound

        self.create = to_raw_response_wrapper(
            inbound.create,
        )


class AsyncInboundResourceWithRawResponse:
    def __init__(self, inbound: AsyncInboundResource) -> None:
        self._inbound = inbound

        self.create = async_to_raw_response_wrapper(
            inbound.create,
        )


class InboundResourceWithStreamingResponse:
    def __init__(self, inbound: InboundResource) -> None:
        self._inbound = inbound

        self.create = to_streamed_response_wrapper(
            inbound.create,
        )


class AsyncInboundResourceWithStreamingResponse:
    def __init__(self, inbound: AsyncInboundResource) -> None:
        self._inbound = inbound

        self.create = async_to_streamed_response_wrapper(
            inbound.create,
        )
