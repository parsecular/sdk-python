"""
WebSocket Streaming

Connects to the Parsec real-time feed, subscribes to a market,
and prints orderbook snapshots and trade activity as they arrive.

Run:  PARSEC_API_KEY=pk_live_xxx python examples/websocket_streaming.py
"""

import asyncio

from parsec_api import AsyncParsecAPI

client = AsyncParsecAPI()  # reads PARSEC_API_KEY from env


async def main():
    # Pick an active market with depth
    res = await client.markets.list(
        exchanges=["kalshi"], status="active", min_volume=50_000, limit=1,
    )
    if not res.markets:
        raise RuntimeError("No markets returned from API.")
    market = res.markets[0]
    outcome = market.outcomes[0].name if market.outcomes else "yes"
    print(f"Streaming: {market.parsec_id} — {market.question}\n")

    # Create the WebSocket client and wire up event handlers
    ws = client.ws()

    @ws.on("connected")
    async def on_connected():
        print("Connected — subscribing...")
        ws.subscribe(parsec_id=market.parsec_id, outcome=outcome)

    @ws.on("orderbook")
    async def on_orderbook(book):
        bids = getattr(book, "bids", []) or []
        asks = getattr(book, "asks", []) or []
        mid = getattr(book, "mid_price", None)
        spread = getattr(book, "spread", None)
        print(
            f"[orderbook] {book.parsec_id}/{book.outcome}  "
            f"mid={mid}  spread={spread}  bids={len(bids)}  asks={len(asks)}"
        )

    @ws.on("activity")
    async def on_activity(trade):
        print(
            f"[activity]  {trade.parsec_id}  {trade.kind}  "
            f"price={trade.price}  size={trade.size}  side={getattr(trade, 'side', '—')}"
        )

    @ws.on("error")
    async def on_error(err):
        print(f"[error] {err}")

    @ws.on("disconnected")
    async def on_disconnected(*args):
        print("[disconnected]")

    # Connect and keep alive until Ctrl-C
    await ws.connect()
    print("Press Ctrl-C to stop.\n")
    await ws.run_forever()  # blocks until the connection is permanently closed


asyncio.run(main())
