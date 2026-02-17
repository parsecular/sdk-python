"""
Order Lifecycle: Place, Check, Cancel

Places a $0.01 limit order that won't fill, retrieves it, then cancels it.
Requires exchange credentials configured on your Parsec account.

Run:
    PARSEC_API_KEY=pk_live_xxx PARSEC_ENABLE_TRADING=1 python examples/order_lifecycle.py
"""

import os
import sys

from parsec_api import ParsecAPI

if not os.environ.get("PARSEC_ENABLE_TRADING"):
    print("Set PARSEC_ENABLE_TRADING=1 to run this example (places a real order).")
    sys.exit(0)

client = ParsecAPI()  # reads PARSEC_API_KEY from env
EXCHANGE = "kalshi"  # or "polymarket"

# 1. Find an active market with orderbook depth
res = client.markets.list(exchanges=[EXCHANGE], status="active", min_volume=10_000, limit=10)
target = None
for m in res.markets:
    ob = client.orderbook.retrieve(parsec_id=m.parsec_id)
    if ob.bids and len(ob.bids) > 0:
        target = m
        break

if not target:
    print("No tradeable market found")
    sys.exit(1)
print(f"Market: {target.parsec_id} — {target.question}\n")

# 2. Place a limit buy at $0.01 (won't fill)
order = client.orders.create(
    exchange=EXCHANGE,
    market_id=target.exchange_market_id,
    outcome="yes",
    side="buy",
    price=0.01,
    size=1,
)
print(f"Created order: {order.id}  status={order.status}")

# 3. Retrieve order status
fetched = client.orders.retrieve(order.id, exchange=EXCHANGE)
print(f"Fetched order: {fetched.id}  status={fetched.status}")

# 4. Cancel the order
cancelled = client.orders.cancel(order.id, exchange=EXCHANGE)
print(f"Cancelled:     {cancelled.id}  status={cancelled.status}")
