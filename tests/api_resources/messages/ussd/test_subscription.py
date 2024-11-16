# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from mtn_ussd_v1 import MtnUssdV1, AsyncMtnUssdV1
from tests.utils import assert_matches_type
from mtn_ussd_v1.types.messages.ussd import SubscriptionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: MtnUssdV1) -> None:
        subscription = client.messages.ussd.subscription.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        )
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: MtnUssdV1) -> None:
        response = client.messages.ussd.subscription.with_raw_response.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: MtnUssdV1) -> None:
        with client.messages.ussd.subscription.with_streaming_response.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unsubscribe(self, client: MtnUssdV1) -> None:
        subscription = client.messages.ussd.subscription.unsubscribe(
            "subscriptionId",
        )
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_unsubscribe(self, client: MtnUssdV1) -> None:
        response = client.messages.ussd.subscription.with_raw_response.unsubscribe(
            "subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_unsubscribe(self, client: MtnUssdV1) -> None:
        with client.messages.ussd.subscription.with_streaming_response.unsubscribe(
            "subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unsubscribe(self, client: MtnUssdV1) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.messages.ussd.subscription.with_raw_response.unsubscribe(
                "",
            )


class TestAsyncSubscription:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMtnUssdV1) -> None:
        subscription = await async_client.messages.ussd.subscription.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        )
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMtnUssdV1) -> None:
        response = await async_client.messages.ussd.subscription.with_raw_response.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMtnUssdV1) -> None:
        async with async_client.messages.ussd.subscription.with_streaming_response.create(
            callback_url="http://10.138.40.69:11400/xportal/services/NetworkNotify",
            service_code="*1234*356#",
            target_system="AYO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unsubscribe(self, async_client: AsyncMtnUssdV1) -> None:
        subscription = await async_client.messages.ussd.subscription.unsubscribe(
            "subscriptionId",
        )
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_unsubscribe(self, async_client: AsyncMtnUssdV1) -> None:
        response = await async_client.messages.ussd.subscription.with_raw_response.unsubscribe(
            "subscriptionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_unsubscribe(self, async_client: AsyncMtnUssdV1) -> None:
        async with async_client.messages.ussd.subscription.with_streaming_response.unsubscribe(
            "subscriptionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unsubscribe(self, async_client: AsyncMtnUssdV1) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.messages.ussd.subscription.with_raw_response.unsubscribe(
                "",
            )
