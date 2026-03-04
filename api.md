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

# ExecutionPrice

Types:

```python
from parsec_api.types import ExecutionPriceRetrieveResponse
```

Methods:

- <code title="get /api/v1/execution-price">client.execution_price.<a href="./src/parsec_api/resources/execution_price.py">retrieve</a>(\*\*<a href="src/parsec_api/types/execution_price_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/execution_price_retrieve_response.py">ExecutionPriceRetrieveResponse</a></code>

# Orderbook

Types:

```python
from parsec_api.types import OrderbookRetrieveResponse
```

Methods:

- <code title="get /api/v1/orderbook">client.orderbook.<a href="./src/parsec_api/resources/orderbook.py">retrieve</a>(\*\*<a href="src/parsec_api/types/orderbook_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/orderbook_retrieve_response.py">OrderbookRetrieveResponse</a></code>

# Price

Types:

```python
from parsec_api.types import PriceRetrieveResponse
```

Methods:

- <code title="get /api/v1/price">client.price.<a href="./src/parsec_api/resources/price.py">retrieve</a>(\*\*<a href="src/parsec_api/types/price_retrieve_params.py">params</a>) -> <a href="./src/parsec_api/types/price_retrieve_response.py">PriceRetrieveResponse</a></code>

# Trades

Types:

```python
from parsec_api.types import TradeListResponse
```

Methods:

- <code title="get /api/v1/trades">client.trades.<a href="./src/parsec_api/resources/trades.py">list</a>(\*\*<a href="src/parsec_api/types/trade_list_params.py">params</a>) -> <a href="./src/parsec_api/types/trade_list_response.py">TradeListResponse</a></code>

# Events

Types:

```python
from parsec_api.types import EventListResponse
```

Methods:

- <code title="get /api/v1/events">client.events.<a href="./src/parsec_api/resources/events.py">list</a>(\*\*<a href="src/parsec_api/types/event_list_params.py">params</a>) -> <a href="./src/parsec_api/types/event_list_response.py">EventListResponse</a></code>

# Websocket

Types:

```python
from parsec_api.types import CustomerUsage, WebsocketUsageResponse
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

# Fills

Types:

```python
from parsec_api.types import FillListResponse
```

Methods:

- <code title="get /api/v1/fills">client.fills.<a href="./src/parsec_api/resources/fills.py">list</a>(\*\*<a href="src/parsec_api/types/fill_list_params.py">params</a>) -> <a href="./src/parsec_api/types/fill_list_response.py">FillListResponse</a></code>

# Account

Types:

```python
from parsec_api.types import (
    AccountBalanceResponse,
    AccountCapabilitiesResponse,
    AccountPingResponse,
    AccountUsageResponse,
    AccountUserActivityResponse,
)
```

Methods:

- <code title="get /api/v1/balance">client.account.<a href="./src/parsec_api/resources/account.py">balance</a>(\*\*<a href="src/parsec_api/types/account_balance_params.py">params</a>) -> <a href="./src/parsec_api/types/account_balance_response.py">AccountBalanceResponse</a></code>
- <code title="get /api/v1/session/capabilities">client.account.<a href="./src/parsec_api/resources/account.py">capabilities</a>() -> <a href="./src/parsec_api/types/account_capabilities_response.py">AccountCapabilitiesResponse</a></code>
- <code title="get /api/v1/ping">client.account.<a href="./src/parsec_api/resources/account.py">ping</a>(\*\*<a href="src/parsec_api/types/account_ping_params.py">params</a>) -> <a href="./src/parsec_api/types/account_ping_response.py">AccountPingResponse</a></code>
- <code title="get /api/v1/usage">client.account.<a href="./src/parsec_api/resources/account.py">usage</a>() -> <a href="./src/parsec_api/types/account_usage_response.py">AccountUsageResponse</a></code>
- <code title="get /api/v1/user-activity">client.account.<a href="./src/parsec_api/resources/account.py">user_activity</a>(\*\*<a href="src/parsec_api/types/account_user_activity_params.py">params</a>) -> <a href="./src/parsec_api/types/account_user_activity_response.py">AccountUserActivityResponse</a></code>

# Onboard

Types:

```python
from parsec_api.types import OnboardCreateResponse
```

Methods:

- <code title="post /api/v1/onboard">client.onboard.<a href="./src/parsec_api/resources/onboard.py">create</a>(\*\*<a href="src/parsec_api/types/onboard_create_params.py">params</a>) -> <a href="./src/parsec_api/types/onboard_create_response.py">OnboardCreateResponse</a></code>

# Wallet

Types:

```python
from parsec_api.types import WalletRetrieveResponse, WalletExportKeyResponse
```

Methods:

- <code title="get /api/v1/wallet">client.wallet.<a href="./src/parsec_api/resources/wallet.py">retrieve</a>() -> <a href="./src/parsec_api/types/wallet_retrieve_response.py">WalletRetrieveResponse</a></code>
- <code title="post /api/v1/wallet/export-key">client.wallet.<a href="./src/parsec_api/resources/wallet.py">export_key</a>(\*\*<a href="src/parsec_api/types/wallet_export_key_params.py">params</a>) -> <a href="./src/parsec_api/types/wallet_export_key_response.py">WalletExportKeyResponse</a></code>

# Ctf

Types:

```python
from parsec_api.types import CtfResponse
```

Methods:

- <code title="post /api/v1/polymarket/ctf/merge">client.ctf.<a href="./src/parsec_api/resources/ctf.py">merge</a>(\*\*<a href="src/parsec_api/types/ctf_merge_params.py">params</a>) -> <a href="./src/parsec_api/types/ctf_response.py">CtfResponse</a></code>
- <code title="post /api/v1/polymarket/ctf/redeem">client.ctf.<a href="./src/parsec_api/resources/ctf.py">redeem</a>(\*\*<a href="src/parsec_api/types/ctf_redeem_params.py">params</a>) -> <a href="./src/parsec_api/types/ctf_response.py">CtfResponse</a></code>
- <code title="post /api/v1/polymarket/ctf/split">client.ctf.<a href="./src/parsec_api/resources/ctf.py">split</a>(\*\*<a href="src/parsec_api/types/ctf_split_params.py">params</a>) -> <a href="./src/parsec_api/types/ctf_response.py">CtfResponse</a></code>

# Builder

Types:

```python
from parsec_api.types import BuilderPoolResponse
```

Methods:

- <code title="get /api/v1/builder/pool">client.builder.<a href="./src/parsec_api/resources/builder/builder.py">pool</a>() -> <a href="./src/parsec_api/types/builder_pool_response.py">BuilderPoolResponse</a></code>

## Users

Types:

```python
from parsec_api.types.builder import (
    UserCreateResponse,
    UserRetrieveResponse,
    UserUpdateResponse,
    UserListResponse,
)
```

Methods:

- <code title="post /api/v1/builder/users">client.builder.users.<a href="./src/parsec_api/resources/builder/users.py">create</a>(\*\*<a href="src/parsec_api/types/builder/user_create_params.py">params</a>) -> <a href="./src/parsec_api/types/builder/user_create_response.py">UserCreateResponse</a></code>
- <code title="get /api/v1/builder/users/{customer_id}">client.builder.users.<a href="./src/parsec_api/resources/builder/users.py">retrieve</a>(customer_id) -> <a href="./src/parsec_api/types/builder/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="patch /api/v1/builder/users/{customer_id}">client.builder.users.<a href="./src/parsec_api/resources/builder/users.py">update</a>(customer_id, \*\*<a href="src/parsec_api/types/builder/user_update_params.py">params</a>) -> <a href="./src/parsec_api/types/builder/user_update_response.py">UserUpdateResponse</a></code>
- <code title="get /api/v1/builder/users">client.builder.users.<a href="./src/parsec_api/resources/builder/users.py">list</a>(\*\*<a href="src/parsec_api/types/builder/user_list_params.py">params</a>) -> <a href="./src/parsec_api/types/builder/user_list_response.py">UserListResponse</a></code>
- <code title="delete /api/v1/builder/users/{customer_id}">client.builder.users.<a href="./src/parsec_api/resources/builder/users.py">deactivate</a>(customer_id) -> None</code>

## Onboard

Types:

```python
from parsec_api.types.builder import OnboardCreateResponse
```

Methods:

- <code title="post /api/v1/builder/onboard">client.builder.onboard.<a href="./src/parsec_api/resources/builder/onboard.py">create</a>(\*\*<a href="src/parsec_api/types/builder/onboard_create_params.py">params</a>) -> <a href="./src/parsec_api/types/builder/onboard_create_response.py">OnboardCreateResponse</a></code>

## Escrow

Types:

```python
from parsec_api.types.builder import EscrowConfigResponse
```

Methods:

- <code title="get /api/v1/builder/escrow/config">client.builder.escrow.<a href="./src/parsec_api/resources/builder/escrow.py">config</a>() -> <a href="./src/parsec_api/types/builder/escrow_config_response.py">EscrowConfigResponse</a></code>
