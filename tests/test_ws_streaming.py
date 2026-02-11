"""
Tests for the hand-written WebSocket streaming client.
Uses a local mock WS server to simulate the Parsec WS protocol.
"""

from __future__ import annotations

import json
import asyncio
from typing import Any, List

import pytest
import websockets
import websockets.asyncio.server

from parsec_api.streaming import (
    WsError,
    Activity,
    ParsecWebSocket,
    OrderbookSnapshot,
    MarketSubscription,
)

# ── Mock server helpers ──────────────────────────────────────


class MockServer:
    """Simple WS server that records received messages and allows sending."""

    def __init__(self) -> None:
        self._server: websockets.asyncio.server.Server | None = None
        self._clients: List[websockets.asyncio.server.ServerConnection] = []
        self._received: List[Any] = []
        self._client_connected: asyncio.Event = asyncio.Event()
        self.port: int = 0

    async def start(self) -> None:
        self._server = await websockets.asyncio.server.serve(
            self._handler,
            "127.0.0.1",
            0,
        )
        # Get the actual port
        sockets = self._server.sockets
        if sockets:
            self.port = sockets[0].getsockname()[1]

    async def stop(self) -> None:
        if self._server:
            self._server.close()
            await self._server.wait_closed()
        self._clients.clear()
        self._received.clear()
        self._client_connected = asyncio.Event()

    @property
    def url(self) -> str:
        return f"ws://127.0.0.1:{self.port}"

    @property
    def received(self) -> List[Any]:
        return self._received

    async def wait_for_client(self, timeout: float = 5.0) -> None:
        await asyncio.wait_for(self._client_connected.wait(), timeout=timeout)

    def send_to_all(self, msg: dict[str, Any]) -> None:
        data = json.dumps(msg)
        for client in self._clients:
            asyncio.ensure_future(client.send(data))

    def close_all_clients(self) -> None:
        for client in self._clients:
            asyncio.ensure_future(client.close())
        self._clients.clear()
        self._client_connected = asyncio.Event()

    async def _handler(self, ws: websockets.asyncio.server.ServerConnection) -> None:
        self._clients.append(ws)
        self._client_connected.set()
        try:
            async for raw in ws:
                try:
                    self._received.append(json.loads(raw))
                except json.JSONDecodeError:
                    pass
        except (
            websockets.exceptions.ConnectionClosed,
            websockets.exceptions.ConnectionClosedError,
            websockets.exceptions.ConnectionClosedOK,
        ):
            pass
        finally:
            if ws in self._clients:
                self._clients.remove(ws)


def sample_snapshot(**overrides: Any) -> dict[str, Any]:
    base = {
        "type": "orderbook",
        "parsec_id": "polymarket:0x123",
        "exchange": "polymarket",
        "outcome": "Yes",
        "token_id": "tok_abc",
        "market_id": "0x123",
        "tick_size": 0.01,
        "kind": "snapshot",
        "bids": [[0.65, 1000], [0.64, 2500], [0.63, 500]],
        "asks": [[0.66, 800], [0.67, 1500], [0.68, 300]],
        "book_state": "fresh",
        "server_seq": 1,
        "feed_state": "healthy",
        "stale_after_ms": 5000,
        "exchange_ts_ms": 1707044096000,
        "ingest_ts_ms": 1707044096005,
    }
    base.update(overrides)
    return base


# ── Fixtures ─────────────────────────────────────────────────


@pytest.fixture
async def server():
    srv = MockServer()
    await srv.start()
    yield srv
    await srv.stop()


async def connect_and_auth(server: MockServer, api_key: str = "pk_test") -> ParsecWebSocket:
    """Connect + auth helper. Sends auth_ok automatically after receiving auth message."""
    ws = ParsecWebSocket(api_key, server.url)

    async def _auth_responder() -> None:
        await server.wait_for_client()
        await asyncio.sleep(0.05)
        server.send_to_all({"type": "auth_ok", "customer_id": "cust_123"})

    task = asyncio.create_task(_auth_responder())
    await ws.connect()
    await task
    return ws


# ── Tests ────────────────────────────────────────────────────


class TestConnectionAuth:
    @pytest.mark.asyncio
    async def test_connect_resolves_after_auth_ok(self, server: MockServer) -> None:
        connected_events: List[bool] = []
        ws = ParsecWebSocket("pk_test", server.url)

        @ws.on("connected")
        async def on_connected() -> None:
            connected_events.append(True)

        async def _auth() -> None:
            await server.wait_for_client()
            await asyncio.sleep(0.05)
            server.send_to_all({"type": "auth_ok", "customer_id": "cust_123"})

        task = asyncio.create_task(_auth())
        await ws.connect()
        await task

        assert len(connected_events) >= 1
        auth_msg = next((m for m in server.received if m.get("type") == "auth"), None)
        assert auth_msg is not None
        assert auth_msg["api_key"] == "pk_test"

        await ws.close()

    @pytest.mark.asyncio
    async def test_connect_raises_on_auth_error(self, server: MockServer) -> None:
        errors: List[WsError] = []
        ws = ParsecWebSocket("pk_bad", server.url)

        @ws.on("error")
        async def on_error(err: WsError) -> None:
            errors.append(err)

        async def _auth() -> None:
            await server.wait_for_client()
            await asyncio.sleep(0.05)
            server.send_to_all({"type": "auth_error", "code": 1002, "message": "Invalid API key"})

        task = asyncio.create_task(_auth())
        with pytest.raises(ConnectionError, match="Invalid API key"):
            await ws.connect()
        await task

        assert len(errors) == 1
        assert errors[0].code == 1002

        await ws.close()


class TestOrderbookSnapshot:
    @pytest.mark.asyncio
    async def test_snapshot_applies_correctly(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)

        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot())
        await asyncio.sleep(0.1)

        assert len(books) == 1
        book = books[0]

        # Wire [[price, size]] → StreamingOrderbookLevel objects
        assert book.bids[0].price == 0.65
        assert book.bids[0].size == 1000
        assert book.asks[0].price == 0.66
        assert book.asks[0].size == 800

        # Sorted: bids desc, asks asc
        assert [l.price for l in book.bids] == [0.65, 0.64, 0.63]
        assert [l.price for l in book.asks] == [0.66, 0.67, 0.68]

        # Computed
        assert abs(book.mid_price - (0.65 + 0.66) / 2) < 1e-9
        assert abs(book.spread - 0.01) < 1e-9

        # Metadata
        assert book.kind == "snapshot"
        assert book.parsec_id == "polymarket:0x123"
        assert book.exchange == "polymarket"
        assert book.tick_size == 0.01
        assert book.server_seq == 1
        assert book.stale_after_ms == 5000

        await ws.close()


class TestDeltaApplication:
    @pytest.mark.asyncio
    async def test_set_level(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot())
        await asyncio.sleep(0.1)

        server.send_to_all({
            "type": "orderbook_delta",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
            "changes": [{"side": "bid", "price": 0.65, "size": 1500}],
            "server_seq": 2,
            "feed_state": "healthy",
            "book_state": "fresh",
            "stale_after_ms": 5000,
        })
        await asyncio.sleep(0.1)

        assert len(books) == 2
        delta = books[1]
        assert delta.kind == "delta"
        assert delta.bids[0].price == 0.65
        assert delta.bids[0].size == 1500

        await ws.close()

    @pytest.mark.asyncio
    async def test_add_level(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot())
        await asyncio.sleep(0.1)

        server.send_to_all({
            "type": "orderbook_delta",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
            "changes": [{"side": "bid", "price": 0.645, "size": 200}],
            "server_seq": 2,
            "feed_state": "healthy",
            "book_state": "fresh",
            "stale_after_ms": 5000,
        })
        await asyncio.sleep(0.1)

        delta = books[1]
        assert [l.price for l in delta.bids] == [0.65, 0.645, 0.64, 0.63]

        await ws.close()

    @pytest.mark.asyncio
    async def test_remove_level(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot())
        await asyncio.sleep(0.1)

        server.send_to_all({
            "type": "orderbook_delta",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
            "changes": [{"side": "bid", "price": 0.64, "size": 0}],
            "server_seq": 2,
            "feed_state": "healthy",
            "book_state": "fresh",
            "stale_after_ms": 5000,
        })
        await asyncio.sleep(0.1)

        delta = books[1]
        assert len(delta.bids) == 2
        assert [l.price for l in delta.bids] == [0.65, 0.63]

        await ws.close()


class TestDeltaEdgeCases:
    @pytest.mark.asyncio
    async def test_delta_before_snapshot_ignored(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all({
            "type": "orderbook_delta",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
            "changes": [{"side": "bid", "price": 0.65, "size": 1500}],
            "server_seq": 1,
            "feed_state": "healthy",
            "book_state": "fresh",
            "stale_after_ms": 5000,
        })
        await asyncio.sleep(0.1)

        assert len(books) == 0

        await ws.close()


class TestSequenceGap:
    @pytest.mark.asyncio
    async def test_sequence_gap_triggers_resync(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot(server_seq=1))
        await asyncio.sleep(0.1)

        # Clear received to isolate resync message
        server.received.clear()

        # Send delta with gap (seq=3, skipping 2)
        server.send_to_all({
            "type": "orderbook_delta",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
            "changes": [{"side": "bid", "price": 0.65, "size": 1500}],
            "server_seq": 3,
            "feed_state": "healthy",
            "book_state": "fresh",
            "stale_after_ms": 5000,
        })
        await asyncio.sleep(0.2)

        resync_msg = next((m for m in server.received if m.get("type") == "resync"), None)
        assert resync_msg is not None
        assert resync_msg["parsec_id"] == "polymarket:0x123"

        # Only 1 book event (the initial snapshot)
        assert len(books) == 1

        await ws.close()


class TestResyncRequired:
    @pytest.mark.asyncio
    async def test_resync_required_triggers_resync(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def on_book(b: OrderbookSnapshot) -> None:
            books.append(b)

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        server.send_to_all(sample_snapshot(server_seq=1))
        await asyncio.sleep(0.1)

        server.received.clear()

        server.send_to_all({
            "type": "resync_required",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
        })
        await asyncio.sleep(0.1)

        resync_msg = next((m for m in server.received if m.get("type") == "resync"), None)
        assert resync_msg is not None

        # Server sends fresh snapshot
        server.send_to_all(sample_snapshot(
            server_seq=10,
            bids=[[0.70, 2000], [0.69, 3000]],
            asks=[[0.71, 1000], [0.72, 500]],
        ))
        await asyncio.sleep(0.1)

        assert len(books) == 2
        assert books[1].kind == "snapshot"
        assert books[1].bids[0].price == 0.70

        await ws.close()


class TestReconnect:
    @pytest.mark.asyncio
    async def test_reconnects_and_resubscribes(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)

        reconnect_events: List[tuple[int, int]] = []

        @ws.on("reconnecting")
        async def on_reconnecting(attempt: int, delay_ms: int) -> None:
            reconnect_events.append((attempt, delay_ms))

        ws.subscribe(parsec_id="polymarket:0x123", outcome="Yes")
        await asyncio.sleep(0.05)

        # Drop all clients
        server.close_all_clients()
        await asyncio.sleep(0.2)

        assert len(reconnect_events) >= 1
        assert reconnect_events[0][0] == 1

        # Wait for reconnect
        await server.wait_for_client(timeout=5.0)
        await asyncio.sleep(0.1)

        # Send auth_ok on reconnect
        server.send_to_all({"type": "auth_ok", "customer_id": "cust_123"})
        await asyncio.sleep(0.2)

        # Should have resubscribed
        sub_msg = next((m for m in server.received if m.get("type") == "subscribe"), None)
        assert sub_msg is not None
        assert any(m.get("parsec_id") == "polymarket:0x123" for m in sub_msg["markets"])

        await ws.close()


class TestAuthErrorNoReconnect:
    @pytest.mark.asyncio
    async def test_auth_error_no_reconnect(self, server: MockServer) -> None:
        reconnect_events: List[Any] = []
        ws = ParsecWebSocket("pk_bad", server.url)

        @ws.on("reconnecting")
        async def on_reconnecting(attempt: int, delay_ms: int) -> None:
            reconnect_events.append((attempt, delay_ms))

        async def _auth() -> None:
            await server.wait_for_client()
            await asyncio.sleep(0.05)
            server.send_to_all({"type": "auth_error", "code": 1002, "message": "Invalid API key"})

        task = asyncio.create_task(_auth())
        with pytest.raises(ConnectionError):
            await ws.connect()
        await task

        await asyncio.sleep(0.5)
        assert len(reconnect_events) == 0

        await ws.close()


class TestCloseCancelsReconnect:
    @pytest.mark.asyncio
    async def test_close_cancels_reconnect(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)

        reconnect_events: List[Any] = []

        @ws.on("reconnecting")
        async def on_reconnecting(attempt: int, delay_ms: int) -> None:
            reconnect_events.append((attempt, delay_ms))

        server.close_all_clients()
        await asyncio.sleep(0.2)

        assert len(reconnect_events) >= 1

        await ws.close()

        await asyncio.sleep(2.0)
        # Should not have accumulated more reconnect attempts
        assert len(reconnect_events) == 1


class TestBatchSubscribe:
    @pytest.mark.asyncio
    async def test_batch_subscribe_sends_one_message(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)

        server.received.clear()

        ws.subscribe([
            MarketSubscription(parsec_id="polymarket:0x123", outcome="Yes"),
            MarketSubscription(parsec_id="kalshi:KXBTC", outcome="Yes", depth=50),
            MarketSubscription(parsec_id="polymarket:0x456", outcome="No"),
        ])
        await asyncio.sleep(0.1)

        sub_msgs = [m for m in server.received if m.get("type") == "subscribe"]
        assert len(sub_msgs) == 1
        assert len(sub_msgs[0]["markets"]) == 3

        await ws.close()


class TestActivityEvents:
    @pytest.mark.asyncio
    async def test_trade_activity(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        activities: List[Activity] = []

        @ws.on("activity")
        async def on_activity(a: Activity) -> None:
            activities.append(a)

        server.send_to_all({
            "type": "activity",
            "parsec_id": "polymarket:0x123",
            "exchange": "polymarket",
            "outcome": "Yes",
            "token_id": "tok_abc",
            "market_id": "0x123",
            "kind": "trade",
            "price": 0.65,
            "size": 100,
            "trade_id": "trade_123",
            "side": "buy",
            "aggressor_side": "buy",
            "server_seq": 5,
            "feed_state": "healthy",
            "exchange_ts_ms": 1707044096100,
            "ingest_ts_ms": 1707044096105,
            "source_channel": "trades",
        })
        await asyncio.sleep(0.1)

        assert len(activities) == 1
        assert activities[0].kind == "trade"
        assert activities[0].price == 0.65
        assert activities[0].source_channel == "trades"

        await ws.close()


class TestSlowReaderHeartbeat:
    @pytest.mark.asyncio
    async def test_slow_reader_event(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        slow_events: List[tuple[str, str]] = []

        @ws.on("slow_reader")
        async def on_slow(parsec_id: str, outcome: str) -> None:
            slow_events.append((parsec_id, outcome))

        server.send_to_all({
            "type": "slow_reader",
            "parsec_id": "polymarket:0x123",
            "outcome": "Yes",
        })
        await asyncio.sleep(0.1)

        assert len(slow_events) == 1
        assert slow_events[0] == ("polymarket:0x123", "Yes")

        await ws.close()

    @pytest.mark.asyncio
    async def test_heartbeat_event(self, server: MockServer) -> None:
        ws = await connect_and_auth(server)
        heartbeats: List[int] = []

        @ws.on("heartbeat")
        async def on_heartbeat(ts_ms: int) -> None:
            heartbeats.append(ts_ms)

        server.send_to_all({"type": "heartbeat", "ts_ms": 1707044096000})
        await asyncio.sleep(0.1)

        assert len(heartbeats) == 1
        assert heartbeats[0] == 1707044096000

        await ws.close()
