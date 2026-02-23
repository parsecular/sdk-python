"""
Getting Started with the Parsec API

Demonstrates: listing markets, fetching an orderbook, and reading price history.
Run:  PARSEC_API_KEY=pk_live_xxx python examples/getting_started.py
"""

from parsec_api import ParsecAPI

client = ParsecAPI()  # reads PARSEC_API_KEY from env

# 1. List active, high-volume Kalshi markets
res = client.markets.list(exchanges=["kalshi"], status="active", min_volume=50_000, limit=5)
print(f"Found {res.pagination.total} markets (showing {len(res.markets)}):\n")
for m in res.markets:
    print(f"  {m.parsec_id}  {m.question}")
    vol = f"${m.volume_total:,.0f}" if m.volume_total else "n/a"
    print(f"    volume: {vol}  last: {m.last_price or 'n/a'}\n")

# 2. Fetch the orderbook for the first market
if not res.markets:
    raise RuntimeError("No markets returned from API.")
market = res.markets[0]
outcome = market.outcomes[0].name if market.outcomes else "yes"
book = client.orderbook.retrieve(parsec_id=market.parsec_id, outcome=outcome)
best_bid = book.bids[0][0] if book.bids else "—"
best_ask = book.asks[0][0] if book.asks else "—"
print(f"Orderbook for {market.parsec_id} ({outcome.upper()}):")
print(f"  Best bid: {best_bid}  Best ask: {best_ask}")
print(f"  Depth: {len(book.bids or [])} bids, {len(book.asks or [])} asks\n")

# 3. Get hourly price candles (OHLCV)
hist = client.price.retrieve(parsec_id=market.parsec_id, outcome=outcome, interval="1h")
print(f"Loaded {len(hist.candles)} hourly candles:")
for c in hist.candles:
    print(f"  {c.timestamp}  O={c.open} H={c.high} L={c.low} C={c.close} V={c.volume}")
