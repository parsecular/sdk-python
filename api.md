# Exchanges

Types:

```python
from parsec_api.types import ExchangeListResponse
```

Methods:

- <code title="get /api/v1/exchanges">client.exchanges.<a href="./src/parsec_api/resources/exchanges.py">list</a>() -> <a href="./src/parsec_api/types/exchange_list_response.py">ExchangeListResponse</a></code>

# Markets

Types:

```python
from parsec_api.types import MarketListResponse
```

Methods:

- <code title="get /api/v1/markets">client.markets.<a href="./src/parsec_api/resources/markets.py">list</a>(\*\*<a href="src/parsec_api/types/market_list_params.py">params</a>) -> <a href="./src/parsec_api/types/market_list_response.py">MarketListResponse</a></code>

# Orderbook

Types:

```python
from parsec_api.types import OrderbookRetrieveResponse
```

Methods:

- <code title="get /api/v1/orderbook">client.orderbook.<a href="./src/parsec_api/resources/orderbook.py">retrieve</a>(\*\*<a href="src/parsec_api/types/orderbook_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/orderbook_retrieve_response.py">OrderbookRetrieveResponse</a></code>

# PriceHistory

Types:

```python
from parsec_api.types import PriceHistoryRetrieveResponse
```

Methods:

- <code title="get /api/v1/price-history">client.price_history.<a href="./src/parsec_api/resources/price_history.py">retrieve</a>(\*\*<a href="src/parsec_api/types/price_history_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/price_history_retrieve_response.py">PriceHistoryRetrieveResponse</a></code>

# Websocket

Types:

```python
from parsec_api.types import WebsocketUsageResponse
```

Methods:

- <code title="get /api/v1/ws/usage">client.websocket.<a href="./src/parsec_api/resources/websocket.py">usage</a>(\*\*<a href="src/parsec_api/types/websocket_usage_params.py">params</a>) -> <a href="./src/parsec_api/types/websocket_usage_response.py">WebsocketUsageResponse</a></code>

# Orders

Types:

```python
from parsec_api.types import Order, OrderListResponse
```

Methods:

- <code title="post /api/v1/orders">client.orders.<a href="./src/parsec_api/resources/orders.py">create</a>(\*\*<a href="src/parsec_api/types/order_create_params.py">params</a>) -> <a href="./src/parsec_api/types/order.py">Order</a></code>
- <code title="get /api/v1/orders/{order_id}">client.orders.<a href="./src/parsec_api/resources/orders.py">retrieve</a>(order_id, \*\*<a href="src/parsec_api/types/order_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/order.py">Order</a></code>
- <code title="get /api/v1/orders">client.orders.<a href="./src/parsec_api/resources/orders.py">list</a>(\*\*<a href="src/parsec_api/types/order_list_params.py">params</a>) -> <a href="./src/parsec_api/types/order_list_response.py">OrderListResponse</a></code>
- <code title="delete /api/v1/orders/{order_id}">client.orders.<a href="./src/parsec_api/resources/orders.py">cancel</a>(order_id, \*\*<a href="src/parsec_api/types/order_cancel_params.py">params</a>) -> <a href="./src/parsec_api/types/order.py">Order</a></code>

# Positions

Types:

```python
from parsec_api.types import PositionListResponse
```

Methods:

- <code title="get /api/v1/positions">client.positions.<a href="./src/parsec_api/resources/positions.py">list</a>(\*\*<a href="src/parsec_api/types/position_list_params.py">params</a>) -> <a href="./src/parsec_api/types/position_list_response.py">PositionListResponse</a></code>

# Account

Types:

```python
from parsec_api.types import (
    AccountBalanceResponse,
    AccountPingResponse,
    AccountUserActivityResponse,
)
```

Methods:

- <code title="get /api/v1/balance">client.account.<a href="./src/parsec_api/resources/account.py">balance</a>(\*\*<a href="src/parsec_api/types/account_balance_params.py">params</a>) -> <a href="./src/parsec_api/types/account_balance_response.py">AccountBalanceResponse</a></code>
- <code title="get /api/v1/ping">client.account.<a href="./src/parsec_api/resources/account.py">ping</a>(\*\*<a href="src/parsec_api/types/account_ping_params.py">params</a>) -> <a href="./src/parsec_api/types/account_ping_response.py">AccountPingResponse</a></code>
- <code title="put /api/v1/credentials">client.account.<a href="./src/parsec_api/resources/account.py">update_credentials</a>(\*\*<a href="src/parsec_api/types/account_update_credentials_params.py">params</a>) -> None</code>
- <code title="get /api/v1/user-activity">client.account.<a href="./src/parsec_api/resources/account.py">user_activity</a>(\*\*<a href="src/parsec_api/types/account_user_activity_params.py">params</a>) -> <a href="./src/parsec_api/types/account_user_activity_response.py">AccountUserActivityResponse</a></code>

# Approvals

Types:

```python
from parsec_api.types import ApprovalListResponse, ApprovalSetResponse
```

Methods:

- <code title="get /api/v1/approvals">client.approvals.<a href="./src/parsec_api/resources/approvals.py">list</a>(\*\*<a href="src/parsec_api/types/approval_list_params.py">params</a>) -> <a href="./src/parsec_api/types/approval_list_response.py">ApprovalListResponse</a></code>
- <code title="post /api/v1/approvals">client.approvals.<a href="./src/parsec_api/resources/approvals.py">set</a>(\*\*<a href="src/parsec_api/types/approval_set_params.py">params</a>) -> <a href="./src/parsec_api/types/approval_set_response.py">ApprovalSetResponse</a></code>
