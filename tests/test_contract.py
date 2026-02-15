"""
Contract tests that run against a real Parsec API server.
Opt-in: set PARSEC_CONTRACT_TESTS=1 and PARSEC_API_KEY=pk_live_...

  PARSEC_CONTRACT_TESTS=1 \
  PARSEC_API_KEY=pk_live_... \
  PARSEC_BASE_URL=https://api.parsecapi.com \
  pytest tests/test_contract.py -v
"""

from __future__ import annotations

import os
import time
import asyncio
from typing import Any, List

import pytest

# ── Gate: skip when not opted in ────────────────────────────

RUN_LIVE = os.environ.get("PARSEC_CONTRACT_TESTS") == "1"
BASE_URL = os.environ.get("PARSEC_BASE_URL") or os.environ.get("TEST_API_BASE_URL") or "http://localhost:3000"
API_KEY = os.environ.get("PARSEC_API_KEY", "")

pytestmark = pytest.mark.skipif(not RUN_LIVE, reason="set PARSEC_CONTRACT_TESTS=1 to enable")


# ── Fixtures ────────────────────────────────────────────────


@pytest.fixture(scope="module")
def client():  # type: ignore[no-untyped-def]
    from parsec_api import ParsecAPI

    if not API_KEY:
        pytest.fail("PARSEC_API_KEY must be set when PARSEC_CONTRACT_TESTS=1")
    c = ParsecAPI(api_key=API_KEY, base_url=BASE_URL)
    yield c
    c.close()


# ── REST contract tests ────────────────────────────────────


class TestRESTExchanges:
    def test_list_exchanges(self, client: Any) -> None:
        exchanges = client.exchanges.list()
        assert isinstance(exchanges, list)
        assert len(exchanges) > 0
        assert isinstance(exchanges[0], str)
        # Should include known exchanges
        assert "kalshi" in exchanges


class TestRESTMarkets:
    def test_list_markets_shape(self, client: Any) -> None:
        resp = client.markets.list(exchanges=["kalshi"], limit=3)
        assert hasattr(resp, "markets")
        assert isinstance(resp.markets, list)
        assert len(resp.markets) > 0
        assert len(resp.markets) <= 3  # limit respected

        market = resp.markets[0]
        assert isinstance(market.parsec_id, str)
        assert market.parsec_id.startswith("kalshi:")  # parsec_id has exchange prefix
        assert market.exchange == "kalshi"  # filtered to kalshi
        assert len(market.outcomes) > 0
        assert hasattr(market.outcomes[0], "name")
        assert isinstance(market.outcomes[0].name, str)
        assert isinstance(market.status, str)
        assert len(market.status) > 0
        assert isinstance(market.question, str)
        assert len(market.question) > 0

    def test_list_markets_multi_exchange(self, client: Any) -> None:
        resp = client.markets.list(exchanges=["kalshi", "polymarket"], limit=20)
        assert len(resp.markets) > 0
        exchange_set = {m.exchange for m in resp.markets}
        # Multi-exchange filter should return results — ideally from both,
        # but Polymarket relay can be slow, so we require at least 1 exchange
        # and verify the filter doesn't return exchanges we didn't ask for.
        assert len(exchange_set) >= 1
        assert exchange_set <= {"kalshi", "polymarket"}, f"Unexpected exchanges: {exchange_set}"


class TestRESTEvents:
    def test_list_events_shape(self, client: Any) -> None:
        resp = client.events.list(exchanges=["kalshi"], limit=3)
        assert hasattr(resp, "events")
        assert isinstance(resp.events, list)
        assert len(resp.events) > 0
        assert len(resp.events) <= 3

        event = resp.events[0]
        assert isinstance(event.event_id, str)
        assert isinstance(event.title, str)
        assert len(event.title) > 0
        assert isinstance(event.market_count, int)
        assert event.market_count > 0
        assert isinstance(event.total_volume, (int, float))
        assert isinstance(event.exchanges, list)
        assert isinstance(event.status, str)

    def test_list_events_with_markets(self, client: Any) -> None:
        resp = client.events.list(exchanges=["kalshi"], limit=1, include_markets=True)
        event = resp.events[0]
        assert event.markets is not None
        assert isinstance(event.markets, list)
        if len(event.markets) > 0:
            market = event.markets[0]
            assert isinstance(market.parsec_id, str)
            assert isinstance(market.question, str)


class TestRESTOrderbook:
    @staticmethod
    def _find_market_with_depth(client: Any) -> Any:
        """Find an active market that actually has orderbook depth (non-empty bids or asks).
        Some 'active' markets on Kalshi have zero liquidity (e.g. esports)."""
        resp = client.markets.list(exchanges=["kalshi"], limit=20)
        for m in resp.markets:
            if m.status != "active" or len(m.outcomes) == 0:
                continue
            ob = client.orderbook.retrieve(parsec_id=m.parsec_id, outcome=m.outcomes[0].name)
            if len(ob.bids) + len(ob.asks) > 0:
                return m, ob
        return None, None

    def test_get_orderbook_structure_and_ordering(self, client: Any) -> None:
        market, ob = self._find_market_with_depth(client)
        assert market is not None, "No active market with orderbook depth found in top 20"

        assert isinstance(ob.bids, list)
        assert isinstance(ob.asks, list)

        total_levels = len(ob.bids) + len(ob.asks)
        assert total_levels > 0, "Market should have at least one level (pre-filtered)"

        # REST orderbook returns raw wire format: [[price, size], ...]
        if len(ob.bids) > 0:
            bid = ob.bids[0]
            assert len(bid) == 2
            assert isinstance(bid[0], (int, float))  # price
            assert isinstance(bid[1], (int, float))  # size
            assert 0 < bid[0] < 1, f"Prediction market price should be (0,1), got {bid[0]}"
            assert bid[1] > 0, f"Size should be positive, got {bid[1]}"

        # Bids sorted descending by price
        for i in range(1, len(ob.bids)):
            assert ob.bids[i - 1][0] >= ob.bids[i][0], "Bids should be sorted descending"
        # Asks sorted ascending by price
        for i in range(1, len(ob.asks)):
            assert ob.asks[i - 1][0] <= ob.asks[i][0], "Asks should be sorted ascending"


class TestRESTPriceHistory:
    def test_get_price_history_structure(self, client: Any) -> None:
        resp = client.markets.list(exchanges=["kalshi"], limit=5)
        market = next((m for m in resp.markets if m.status == "active" and len(m.outcomes) > 0), None)
        assert market is not None, "No active market found"

        history = client.price_history.retrieve(
            parsec_id=market.parsec_id,
            outcome=market.outcomes[0].name,
            interval="1h",
        )
        assert hasattr(history, "candles")
        assert isinstance(history.candles, list)

        if len(history.candles) > 0:
            candle = history.candles[0]
            assert hasattr(candle, "timestamp")
            assert candle.timestamp is not None


class TestRESTWsUsage:
    def test_ws_usage_metering(self, client: Any) -> None:
        usage = client.websocket.usage()
        assert isinstance(usage.scope, str)
        assert len(usage.scope) > 0
        assert isinstance(usage.updated_at_ms, (int, float))
        assert usage.updated_at_ms > 0
        assert usage.totals is not None


class TestRESTOrders:
    def test_invalid_order_returns_400(self, client: Any) -> None:
        from parsec_api._exceptions import BadRequestError

        with pytest.raises(BadRequestError) as exc_info:
            client.orders.create(
                exchange="kalshi",
                market_id="does-not-matter",
                outcome="yes",
                side="buy",
                price=0.5,
                size=1,
                params={"order_type": "fok"},
            )
        assert exc_info.value.status_code == 400

    def test_list_orders(self, client: Any) -> None:
        orders = client.orders.list(exchange="kalshi")
        # API returns a bare array (empty when no active orders)
        assert isinstance(orders, list)
        # If any orders exist, verify structure
        if len(orders) > 0:
            assert hasattr(orders[0], "order_id")
            assert hasattr(orders[0], "exchange")


class TestRESTPositions:
    def test_list_positions(self, client: Any) -> None:
        positions = client.positions.list(exchange="kalshi")
        # API returns a bare array (empty when no positions)
        assert isinstance(positions, list)
        # If any positions exist, verify structure
        if len(positions) > 0:
            assert hasattr(positions[0], "market_id")
            assert hasattr(positions[0], "exchange")


class TestRESTAccount:
    def test_ping_returns_object(self, client: Any) -> None:
        ping = client.account.ping(exchange="kalshi")
        assert ping is not None
        # Should be an object, not a bare primitive
        assert not isinstance(ping, (str, int, float, bool))


class TestRESTAuth:
    def test_invalid_api_key_401(self) -> None:
        from parsec_api import ParsecAPI
        from parsec_api._exceptions import AuthenticationError

        bad = ParsecAPI(api_key="invalid-api-key", base_url=BASE_URL)
        with pytest.raises(AuthenticationError) as exc_info:
            bad.exchanges.list()
        assert exc_info.value.status_code == 401


# ── WebSocket contract tests ───────────────────────────────


class TestWebSocketContract:
    @staticmethod
    def _find_active_markets_with_depth(client: Any, count: int = 1) -> List[Any]:
        """Find active markets that have actual orderbook depth.
        Probes each market's orderbook to avoid picking empty/illiquid ones."""
        resp = client.markets.list(exchanges=["kalshi"], limit=30)
        result = []
        for m in resp.markets:
            if m.status != "active" or len(m.outcomes) == 0:
                continue
            ob = client.orderbook.retrieve(parsec_id=m.parsec_id, outcome=m.outcomes[0].name)
            if len(ob.bids) + len(ob.asks) > 0:
                result.append(m)
                if len(result) >= count:
                    break
        assert len(result) >= count, f"Need {count} markets with depth, found {len(result)}"
        return result

    @pytest.mark.asyncio
    async def test_snapshot_identity_structure_ordering_consistency(self, client: Any) -> None:
        """Full validation of a live orderbook snapshot from connect through data."""
        from parsec_api.streaming import OrderbookSnapshot

        markets = self._find_active_markets_with_depth(client, 1)
        parsec_id = markets[0].parsec_id
        outcome = markets[0].outcomes[0].name

        ws = client.ws()
        books: List[OrderbookSnapshot] = []
        errors: List[Any] = []

        @ws.on("orderbook")
        async def _on_book(book: OrderbookSnapshot) -> None:
            books.append(book)

        @ws.on("error")
        async def _on_error(err: Any) -> None:
            errors.append(err)

        await ws.connect()
        try:
            ws.subscribe(parsec_id=parsec_id, outcome=outcome)

            deadline = asyncio.get_event_loop().time() + 15.0
            while len(books) == 0 and asyncio.get_event_loop().time() < deadline:
                await asyncio.sleep(0.2)

            assert len(errors) == 0, f"WS errors: {errors}"
            assert len(books) >= 1, "No orderbook snapshot received within 15s"

            book = books[0]

            # ── Identity: matches what we subscribed to ──
            assert book.parsec_id == parsec_id
            assert book.outcome == outcome
            assert book.kind == "snapshot"

            # ── Structure: all expected fields present with correct types ──
            assert isinstance(book.bids, list)
            assert isinstance(book.asks, list)
            assert isinstance(book.server_seq, int)
            assert book.server_seq > 0
            assert book.feed_state in ("healthy", "degraded", "disconnected")
            assert book.book_state in ("fresh", "stale")
            assert isinstance(book.mid_price, (int, float))
            assert isinstance(book.spread, (int, float))
            assert book.spread >= 0

            # ── Content: at least one side should have levels for an active market ──
            total_levels = len(book.bids) + len(book.asks)
            assert total_levels > 0, "Active market should have at least one level"

            # ── Level structure: WS client transforms [[p,s]] → objects ──
            if len(book.bids) > 0:
                assert isinstance(book.bids[0].price, (int, float))
                assert isinstance(book.bids[0].size, (int, float))
                assert 0 < book.bids[0].price < 1
                assert book.bids[0].size > 0
            if len(book.asks) > 0:
                assert isinstance(book.asks[0].price, (int, float))
                assert isinstance(book.asks[0].size, (int, float))
                assert 0 < book.asks[0].price <= 1
                assert book.asks[0].size > 0

            # ── Ordering: bids descending, asks ascending ──
            for i in range(1, len(book.bids)):
                assert book.bids[i - 1].price >= book.bids[i].price, "Bids should be sorted descending"
            for i in range(1, len(book.asks)):
                assert book.asks[i - 1].price <= book.asks[i].price, "Asks should be sorted ascending"

            # ── Consistency: midPrice and spread match the actual book ──
            if len(book.bids) > 0 and len(book.asks) > 0:
                best_bid = book.bids[0].price
                best_ask = book.asks[0].price
                assert abs(book.mid_price - (best_bid + best_ask) / 2) < 1e-4
                assert abs(book.spread - (best_ask - best_bid)) < 1e-4
                assert best_ask >= best_bid, "Book should not be crossed"
        finally:
            await ws.close()

    @pytest.mark.asyncio
    async def test_batch_subscribe_2_distinct_snapshots(self, client: Any) -> None:
        """Batch subscribe to 2 markets, receive independent snapshots."""
        from parsec_api.streaming import OrderbookSnapshot, MarketSubscription

        markets = self._find_active_markets_with_depth(client, 2)
        expected_ids = {m.parsec_id for m in markets}

        ws = client.ws()
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def _on_book(book: OrderbookSnapshot) -> None:
            books.append(book)

        await ws.connect()
        try:
            ws.subscribe([
                MarketSubscription(parsec_id=m.parsec_id, outcome=m.outcomes[0].name)
                for m in markets
            ])

            deadline = asyncio.get_event_loop().time() + 15.0
            while len(books) < 2 and asyncio.get_event_loop().time() < deadline:
                await asyncio.sleep(0.2)

            assert len(books) >= 2, f"Expected 2+ snapshots, got {len(books)}"

            # Each market should have its own snapshot — verify distinct parsecIds
            received_ids = {b.parsec_id for b in books}
            assert received_ids == expected_ids, f"Expected {expected_ids}, got {received_ids}"

            for book in books[:2]:
                assert book.kind == "snapshot"
                assert isinstance(book.bids, list)
                assert isinstance(book.asks, list)
                assert isinstance(book.server_seq, int)
        finally:
            await ws.close()

    @pytest.mark.asyncio
    async def test_unsubscribe_stops_updates(self, client: Any) -> None:
        """Subscribe, get snapshot, unsubscribe, verify updates stop."""
        from parsec_api.streaming import OrderbookSnapshot

        markets = self._find_active_markets_with_depth(client, 1)
        parsec_id = markets[0].parsec_id
        outcome = markets[0].outcomes[0].name

        ws = client.ws()
        books: List[OrderbookSnapshot] = []

        @ws.on("orderbook")
        async def _on_book(book: OrderbookSnapshot) -> None:
            books.append(book)

        await ws.connect()
        try:
            ws.subscribe(parsec_id=parsec_id, outcome=outcome)

            deadline = asyncio.get_event_loop().time() + 15.0
            while len(books) == 0 and asyncio.get_event_loop().time() < deadline:
                await asyncio.sleep(0.2)
            assert len(books) >= 1
            assert books[0].kind == "snapshot"  # got the initial snapshot

            count_after_sub = len(books)
            ws.unsubscribe(parsec_id=parsec_id, outcome=outcome)

            # Wait 3s — should get at most 1-2 in-flight messages
            await asyncio.sleep(3.0)
            assert len(books) <= count_after_sub + 2
        finally:
            await ws.close()

    @pytest.mark.asyncio
    async def test_heartbeat_received_with_valid_timestamp(self, client: Any) -> None:
        """Connect and wait for a heartbeat within 35s. Validates timestamp is recent."""
        ws = client.ws()
        heartbeats: List[int] = []

        @ws.on("heartbeat")
        async def _on_heartbeat(ts_ms: int) -> None:
            heartbeats.append(ts_ms)

        await ws.connect()
        try:
            deadline = asyncio.get_event_loop().time() + 35.0
            while len(heartbeats) == 0 and asyncio.get_event_loop().time() < deadline:
                await asyncio.sleep(0.5)

            assert len(heartbeats) >= 1, "No heartbeat received within 35s"
            assert isinstance(heartbeats[0], int)
            # Timestamp should be a recent epoch ms (within last 60s)
            now_ms = int(time.time() * 1000)
            assert heartbeats[0] > now_ms - 60_000, f"Heartbeat ts {heartbeats[0]} is too old (now={now_ms})"
            assert heartbeats[0] < now_ms + 5_000, f"Heartbeat ts {heartbeats[0]} is in the future"
        finally:
            await ws.close()

    @pytest.mark.asyncio
    async def test_auth_error_on_invalid_key(self) -> None:
        """WS connect with invalid API key should raise ConnectionError."""
        from parsec_api import ParsecAPI

        bad = ParsecAPI(api_key="pk_invalid_key", base_url=BASE_URL)
        ws = bad.ws()

        with pytest.raises(ConnectionError):
            await ws.connect()

        await ws.close()
