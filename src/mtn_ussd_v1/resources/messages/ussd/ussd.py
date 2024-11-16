# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .inbound import (
    InboundResource,
    AsyncInboundResource,
    InboundResourceWithRawResponse,
    AsyncInboundResourceWithRawResponse,
    InboundResourceWithStreamingResponse,
    AsyncInboundResourceWithStreamingResponse,
)
from .outbound import (
    OutboundResource,
    AsyncOutboundResource,
    OutboundResourceWithRawResponse,
    AsyncOutboundResourceWithRawResponse,
    OutboundResourceWithStreamingResponse,
    AsyncOutboundResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .subscription import (
    SubscriptionResource,
    AsyncSubscriptionResource,
    SubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
)

__all__ = ["UssdResource", "AsyncUssdResource"]


class UssdResource(SyncAPIResource):
    @cached_property
    def subscription(self) -> SubscriptionResource:
        return SubscriptionResource(self._client)

    @cached_property
    def inbound(self) -> InboundResource:
        return InboundResource(self._client)

    @cached_property
    def outbound(self) -> OutboundResource:
        return OutboundResource(self._client)

    @cached_property
    def with_raw_response(self) -> UssdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return UssdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UssdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return UssdResourceWithStreamingResponse(self)


class AsyncUssdResource(AsyncAPIResource):
    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def inbound(self) -> AsyncInboundResource:
        return AsyncInboundResource(self._client)

    @cached_property
    def outbound(self) -> AsyncOutboundResource:
        return AsyncOutboundResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUssdResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#accessing-raw-response-data-eg-headers
        """
        return AsyncUssdResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUssdResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/TralahM/mtn-ussd-v1#with_streaming_response
        """
        return AsyncUssdResourceWithStreamingResponse(self)


class UssdResourceWithRawResponse:
    def __init__(self, ussd: UssdResource) -> None:
        self._ussd = ussd

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        return SubscriptionResourceWithRawResponse(self._ussd.subscription)

    @cached_property
    def inbound(self) -> InboundResourceWithRawResponse:
        return InboundResourceWithRawResponse(self._ussd.inbound)

    @cached_property
    def outbound(self) -> OutboundResourceWithRawResponse:
        return OutboundResourceWithRawResponse(self._ussd.outbound)


class AsyncUssdResourceWithRawResponse:
    def __init__(self, ussd: AsyncUssdResource) -> None:
        self._ussd = ussd

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        return AsyncSubscriptionResourceWithRawResponse(self._ussd.subscription)

    @cached_property
    def inbound(self) -> AsyncInboundResourceWithRawResponse:
        return AsyncInboundResourceWithRawResponse(self._ussd.inbound)

    @cached_property
    def outbound(self) -> AsyncOutboundResourceWithRawResponse:
        return AsyncOutboundResourceWithRawResponse(self._ussd.outbound)


class UssdResourceWithStreamingResponse:
    def __init__(self, ussd: UssdResource) -> None:
        self._ussd = ussd

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        return SubscriptionResourceWithStreamingResponse(self._ussd.subscription)

    @cached_property
    def inbound(self) -> InboundResourceWithStreamingResponse:
        return InboundResourceWithStreamingResponse(self._ussd.inbound)

    @cached_property
    def outbound(self) -> OutboundResourceWithStreamingResponse:
        return OutboundResourceWithStreamingResponse(self._ussd.outbound)


class AsyncUssdResourceWithStreamingResponse:
    def __init__(self, ussd: AsyncUssdResource) -> None:
        self._ussd = ussd

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        return AsyncSubscriptionResourceWithStreamingResponse(self._ussd.subscription)

    @cached_property
    def inbound(self) -> AsyncInboundResourceWithStreamingResponse:
        return AsyncInboundResourceWithStreamingResponse(self._ussd.inbound)

    @cached_property
    def outbound(self) -> AsyncOutboundResourceWithStreamingResponse:
        return AsyncOutboundResourceWithStreamingResponse(self._ussd.outbound)
