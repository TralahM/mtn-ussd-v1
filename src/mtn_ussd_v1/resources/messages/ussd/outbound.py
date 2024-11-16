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
from ....types.messages.ussd import outbound_create_params
from ....types.messages.ussd.outbound_create_response import OutboundCreateResponse

__all__ = ["OutboundResource", "AsyncOutboundResource"]


class OutboundResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return OutboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return OutboundResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message_type: str,
        msisdn: str,
        service_code: str,
        session_id: str,
        ussd_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundCreateResponse:
        """
        This function is used to send/push USSD MT Message to USSDGW for 3PPs with
        subscription on MADAPI.

        Args:
          message_type: Message type. 0-Begin|1-Continue|2-End|3-Notification|4-Cancel|5-Timeout.

          msisdn: Mobile number of the message recipient.

          session_id: Unique identifier of the session.

          ussd_string: USSD message content. If messageType is of type 4-Abort, this attribute will
              contain the abort reason or message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messages/ussd/outbound",
            body=maybe_transform(
                {
                    "message_type": message_type,
                    "msisdn": msisdn,
                    "service_code": service_code,
                    "session_id": session_id,
                    "ussd_string": ussd_string,
                },
                outbound_create_params.OutboundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundCreateResponse,
        )


class AsyncOutboundResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutboundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return AsyncOutboundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutboundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return AsyncOutboundResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message_type: str,
        msisdn: str,
        service_code: str,
        session_id: str,
        ussd_string: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutboundCreateResponse:
        """
        This function is used to send/push USSD MT Message to USSDGW for 3PPs with
        subscription on MADAPI.

        Args:
          message_type: Message type. 0-Begin|1-Continue|2-End|3-Notification|4-Cancel|5-Timeout.

          msisdn: Mobile number of the message recipient.

          session_id: Unique identifier of the session.

          ussd_string: USSD message content. If messageType is of type 4-Abort, this attribute will
              contain the abort reason or message.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messages/ussd/outbound",
            body=await async_maybe_transform(
                {
                    "message_type": message_type,
                    "msisdn": msisdn,
                    "service_code": service_code,
                    "session_id": session_id,
                    "ussd_string": ussd_string,
                },
                outbound_create_params.OutboundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OutboundCreateResponse,
        )


class OutboundResourceWithRawResponse:
    def __init__(self, outbound: OutboundResource) -> None:
        self._outbound = outbound

        self.create = to_raw_response_wrapper(
            outbound.create,
        )


class AsyncOutboundResourceWithRawResponse:
    def __init__(self, outbound: AsyncOutboundResource) -> None:
        self._outbound = outbound

        self.create = async_to_raw_response_wrapper(
            outbound.create,
        )


class OutboundResourceWithStreamingResponse:
    def __init__(self, outbound: OutboundResource) -> None:
        self._outbound = outbound

        self.create = to_streamed_response_wrapper(
            outbound.create,
        )


class AsyncOutboundResourceWithStreamingResponse:
    def __init__(self, outbound: AsyncOutboundResource) -> None:
        self._outbound = outbound

        self.create = async_to_streamed_response_wrapper(
            outbound.create,
        )
