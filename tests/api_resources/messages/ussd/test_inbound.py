# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mtn_ussd_v1 import MtnUssdV1, AsyncMtnUssdV1
from tests.utils import assert_matches_type
from mtn_ussd_v1.types.messages.ussd import InboundCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInbound:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MtnUssdV1) -> None:
        inbound = client.messages.ussd.inbound.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        )
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: MtnUssdV1) -> None:
        inbound = client.messages.ussd.inbound.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
            cell_id="cellId",
            imsi="imsi",
            language="language",
        )
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MtnUssdV1) -> None:
        response = client.messages.ussd.inbound.with_raw_response.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound = response.parse()
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MtnUssdV1) -> None:
        with client.messages.ussd.inbound.with_streaming_response.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound = response.parse()
            assert_matches_type(InboundCreateResponse, inbound, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInbound:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMtnUssdV1) -> None:
        inbound = await async_client.messages.ussd.inbound.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        )
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMtnUssdV1) -> None:
        inbound = await async_client.messages.ussd.inbound.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
            cell_id="cellId",
            imsi="imsi",
            language="language",
        )
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMtnUssdV1) -> None:
        response = await async_client.messages.ussd.inbound.with_raw_response.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound = await response.parse()
        assert_matches_type(InboundCreateResponse, inbound, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMtnUssdV1) -> None:
        async with async_client.messages.ussd.inbound.with_streaming_response.create(
            message_type="0",
            msisdn="2252312345",
            service_code="321123",
            session_id="01235",
            ussd_string="Please vote for xxx.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound = await response.parse()
            assert_matches_type(InboundCreateResponse, inbound, path=["response"])

        assert cast(Any, response.is_closed) is True
