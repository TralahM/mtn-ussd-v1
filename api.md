# Messages

## Ussd

### Subscription

Types:

```python
from mtn_ussd_v1.types.messages.ussd import SubscriptionResponse
```

Methods:

- <code title="post /messages/ussd/subscription">client.messages.ussd.subscription.<a href="./src/mtn_ussd_v1/resources/messages/ussd/subscription.py">create</a>(\*\*<a href="src/mtn_ussd_v1/types/messages/ussd/subscription_create_params.py">params</a>) -> <a href="./src/mtn_ussd_v1/types/messages/ussd/subscription_response.py">SubscriptionResponse</a></code>
- <code title="delete /messages/ussd/subscription/{subscriptionId}">client.messages.ussd.subscription.<a href="./src/mtn_ussd_v1/resources/messages/ussd/subscription.py">unsubscribe</a>(subscription_id) -> <a href="./src/mtn_ussd_v1/types/messages/ussd/subscription_response.py">SubscriptionResponse</a></code>

### Inbound

Types:

```python
from mtn_ussd_v1.types.messages.ussd import InboundCreateResponse
```

Methods:

- <code title="post /messages/ussd/inbound">client.messages.ussd.inbound.<a href="./src/mtn_ussd_v1/resources/messages/ussd/inbound.py">create</a>(\*\*<a href="src/mtn_ussd_v1/types/messages/ussd/inbound_create_params.py">params</a>) -> <a href="./src/mtn_ussd_v1/types/messages/ussd/inbound_create_response.py">InboundCreateResponse</a></code>

### Outbound

Types:

```python
from mtn_ussd_v1.types.messages.ussd import OutboundCreateResponse
```

Methods:

- <code title="post /messages/ussd/outbound">client.messages.ussd.outbound.<a href="./src/mtn_ussd_v1/resources/messages/ussd/outbound.py">create</a>(\*\*<a href="src/mtn_ussd_v1/types/messages/ussd/outbound_create_params.py">params</a>) -> <a href="./src/mtn_ussd_v1/types/messages/ussd/outbound_create_response.py">OutboundCreateResponse</a></code>
