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
from typing import Any, List, Tuple

import pytest

from parsec_api._exceptions import APIStatusError

# ── Gate: skip when not opted in ────────────────────────────

RUN_LIVE = os.environ.get("PARSEC_CONTRACT_TESTS") == "1"
BASE_URL = os.environ.get("PARSEC_BASE_URL") or os.environ.get("TEST_API_BASE_URL") or "http://localhost:3000"
API_KEY = os.environ.get("PARSEC_API_KEY", "")

PUBLIC_ENDPOINT_CONTRACT_COVERAGE = (
    "GET /api/v1/exchanges",
    "GET /api/v1/markets",
    "GET /api/v1/orderbook",
    "GET /api/v1/price",
    "GET /api/v1/trades",
    "GET /api/v1/events",
    "GET /api/v1/ws/usage",
    "GET /api/v1/execution-price",
    "POST /api/v1/orders",
    "GET /api/v1/orders",
    "GET /api/v1/orders/{order_id}",
    "DELETE /api/v1/orders/{order_id}",
    "GET /api/v1/positions",
    "GET /api/v1/balance",
    "GET /api/v1/ping",
    "GET /api/v1/user-activity",
    "GET /api/v1/approvals",
    "POST /api/v1/approvals",
    "PUT /api/v1/credentials",
    "GET /api/v1/session/capabilities",
)

pytestmark = [
    pytest.mark.skipif(not RUN_LIVE, reason="set PARSEC_CONTRACT_TESTS=1 to enable"),
    # Python 3.14 + asyncio transport teardown can emit unraisable warnings after WS tests
    # complete, even when all assertions pass. Track and fix in streaming internals separately.
    pytest.mark.filterwarnings("ignore::pytest.PytestUnraisableExceptionWarning"),
]


# ── Fixtures ────────────────────────────────────────────────


@pytest.fixture(scope="module")
def client():  # type: ignore[no-untyped-def]
    from parsec_api import ParsecAPI

    if not API_KEY:
        pytest.fail("PARSEC_API_KEY must be set when PARSEC_CONTRACT_TESTS=1")
    c = ParsecAPI(api_key=API_KEY, base_url=BASE_URL)
    yield c
    c.close()


def _find_private_exchange(client: Any) -> Tuple[str, bool]:
    ping = client.account.ping()
    if isinstance(ping, list) and len(ping) > 0:
        authenticated = next((entry for entry in ping if entry.has_credentials and entry.authenticated), None)
        with_creds = next((entry for entry in ping if entry.has_credentials), None)
        selected = authenticated or with_creds or ping[0]
        return selected.exchange, bool(authenticated or with_creds)
    return "kalshi", False


def _find_active_market_with_outcome(client: Any) -> Tuple[Any, str]:
    for exchange in ["kalshi", "polymarket"]:
        resp = client.markets.list(exchanges=[exchange], status="active", limit=50)
        for market in resp.markets:
            if len(market.outcomes) > 0:
                return market, market.outcomes[0].name
    raise AssertionError("No active market with outcomes found")


def _find_active_markets_with_depth(client: Any, count: int = 1) -> List[Any]:
    result: List[Any] = []
    for exchange in ["kalshi", "polymarket"]:
        if len(result) >= count:
            break
        resp = client.markets.list(
            exchanges=[exchange], status="active", min_volume=10000, limit=50,
        )
        for market in resp.markets:
            if len(market.outcomes) == 0:
                continue
            ob = client.orderbook.retrieve(parsec_id=market.parsec_id, outcome=market.outcomes[0].name)
            if len(ob.bids) + len(ob.asks) > 0:
                result.append(market)
                if len(result) >= count:
                    break

    assert len(result) >= count, f"Need {count} markets with depth, found {len(result)}"
    return result


# ── REST contract tests ────────────────────────────────────


class TestRESTCoverageManifest:
    def test_public_endpoint_manifest_is_unique(self) -> None:
        assert len(PUBLIC_ENDPOINT_CONTRACT_COVERAGE) == len(set(PUBLIC_ENDPOINT_CONTRACT_COVERAGE))


class TestRESTExchanges:
    def test_list_exchanges(self, client: Any) -> None:
        exchanges = client.exchanges.list()
        assert isinstance(exchanges, list)
        assert len(exchanges) > 0
        first = exchanges[0]
        assert isinstance(first.id, str)
        assert isinstance(first.name, str)
        caps = first.has
        assert isinstance(caps.fetch_markets, bool)
        assert isinstance(caps.create_order, bool)
        assert isinstance(caps.cancel_order, bool)
        assert isinstance(caps.fetch_positions, bool)
        assert isinstance(caps.fetch_balance, bool)
        assert isinstance(caps.fetch_orderbook, bool)
        assert isinstance(caps.fetch_price_history, bool)
        assert isinstance(caps.fetch_trades, bool)
        assert isinstance(caps.fetch_events, bool)
        assert isinstance(caps.fetch_user_activity, bool)
        assert isinstance(caps.approvals, bool)
        assert isinstance(caps.refresh_balance, bool)
        assert isinstance(caps.websocket, bool)
        assert any(ex.id == "kalshi" for ex in exchanges)


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
    def test_get_orderbook_structure_and_ordering(self, client: Any) -> None:
        markets = _find_active_markets_with_depth(client, 1)
        market = markets[0]
        ob = client.orderbook.retrieve(parsec_id=market.parsec_id, outcome=market.outcomes[0].name)
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


class TestRESTExecutionPrice:
    def test_get_execution_price_shape(self, client: Any) -> None:
        resp = client.markets.list(exchanges=["kalshi"], limit=5)
        market = next((m for m in resp.markets if len(m.outcomes) > 0), None)
        assert market is not None, "No market found with outcomes"

        estimate = client.execution_price.retrieve(
            parsec_id=market.parsec_id,
            outcome=market.outcomes[0].name,
            side="buy",
            amount=1,
        )
        assert isinstance(estimate.filled_amount, (int, float))
        assert isinstance(estimate.total_cost, (int, float))
        assert isinstance(estimate.fully_filled, bool)
        assert isinstance(estimate.levels_consumed, int)
        if estimate.avg_price is not None:
            assert isinstance(estimate.avg_price, (int, float))
        if estimate.slippage is not None:
            assert isinstance(estimate.slippage, (int, float))
        if estimate.worst_price is not None:
            assert isinstance(estimate.worst_price, (int, float))
        if estimate.fee_estimate is not None:
            assert isinstance(estimate.fee_estimate, (int, float))
        if estimate.net_cost is not None:
            assert isinstance(estimate.net_cost, (int, float))
        if estimate.fee_estimate is not None and estimate.net_cost is not None:
            assert abs(estimate.net_cost - (estimate.total_cost + estimate.fee_estimate)) < 1e-8


class TestRESTPrice:
    def test_get_price_structure(self, client: Any) -> None:
        resp = client.markets.list(exchanges=["kalshi"], limit=5)
        market = next((m for m in resp.markets if m.status == "active" and len(m.outcomes) > 0), None)
        assert market is not None, "No active market found"

        history = client.price.retrieve(
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


class TestRESTTrades:
    def test_get_trades_structure(self, client: Any) -> None:
        market, outcome = _find_active_market_with_outcome(client)
        trades = client.trades.list(
            parsec_id=market.parsec_id,
            outcome=outcome,
            limit=10,
        )
        assert trades.parsec_id == market.parsec_id
        assert isinstance(trades.exchange, str)
        assert isinstance(trades.outcome, str)
        assert isinstance(trades.trades, list)

        if len(trades.trades) > 0:
            trade = trades.trades[0]
            assert isinstance(getattr(trade, "id", None), str)
            assert isinstance(trade.price, (int, float))
            assert isinstance(trade.size, (int, float))


class TestRESTWsUsage:
    def test_ws_usage_metering(self, client: Any) -> None:
        usage = client.websocket.usage()
        assert isinstance(usage.scope, str)
        assert len(usage.scope) > 0
        assert isinstance(usage.updated_at_ms, (int, float))
        assert usage.updated_at_ms > 0
        assert usage.totals is not None


class TestRESTOrders:
    def test_create_order_contract_path(self, client: Any) -> None:
        # Use a deterministic exchange for negative-path coverage.
        exchange = "kalshi"
        with pytest.raises(APIStatusError) as exc_info:
            client.orders.create(
                exchange=exchange,
                market_id="does-not-matter",
                outcome="yes",
                side="buy",
                price=0.5,
                size=1,
                params={"order_type": "fok"},
            )
        assert exc_info.value.status_code in (400, 401, 403, 404, 501, 503)

    def test_list_orders(self, client: Any) -> None:
        exchange, _ = _find_private_exchange(client)
        try:
            orders = client.orders.list(exchange=exchange)
            assert isinstance(orders, list)
            if len(orders) > 0:
                assert hasattr(orders[0], "id")
                assert hasattr(orders[0], "market_id")
                assert hasattr(orders[0], "status")
        except APIStatusError as err:
            assert err.status_code in (401, 403, 503)

    def test_retrieve_missing_order(self, client: Any) -> None:
        exchange = "kalshi"
        missing_order_id = f"contract-missing-{int(time.time() * 1000)}"
        with pytest.raises(APIStatusError) as exc_info:
            client.orders.retrieve(missing_order_id, exchange=exchange)
        assert exc_info.value.status_code in (400, 401, 403, 404, 503)

    def test_cancel_missing_order(self, client: Any) -> None:
        exchange = "kalshi"
        missing_order_id = f"contract-missing-{int(time.time() * 1000) + 1}"
        with pytest.raises(APIStatusError) as exc_info:
            client.orders.cancel(missing_order_id, exchange=exchange)
        assert exc_info.value.status_code in (400, 401, 403, 404, 503)


class TestRESTPositions:
    def test_list_positions(self, client: Any) -> None:
        exchange, _ = _find_private_exchange(client)
        try:
            positions = client.positions.list(exchange=exchange)
            assert isinstance(positions, list)
            if len(positions) > 0:
                assert hasattr(positions[0], "market_id")
                assert hasattr(positions[0], "outcome")
                assert hasattr(positions[0], "size")
        except APIStatusError as err:
            assert err.status_code in (401, 403, 503)


class TestRESTAccount:
    def test_ping_returns_exchange_statuses(self, client: Any) -> None:
        ping = client.account.ping()
        assert isinstance(ping, list)
        assert len(ping) > 0
        assert isinstance(ping[0].exchange, str)
        assert isinstance(ping[0].has_credentials, bool)
        assert isinstance(ping[0].authenticated, bool)

    def test_capabilities_returns_tier_and_linked_exchanges(self, client: Any) -> None:
        caps = client.account.capabilities()
        assert isinstance(caps.tier, str)
        assert isinstance(caps.linked_exchanges, list)

    def test_balance_returns_raw_payload_or_auth_error(self, client: Any) -> None:
        exchange, has_credentials = _find_private_exchange(client)
        try:
            balance = client.account.balance(exchange=exchange)
            assert hasattr(balance, "raw")
            assert isinstance(balance.raw, dict)
        except APIStatusError as err:
            allowed = (401, 403, 503) if has_credentials else (401, 403, 503)
            assert err.status_code in allowed

    def test_user_activity_returns_status_map(self, client: Any) -> None:
        activity = client.account.user_activity(
            address="0x0000000000000000000000000000000000000000",
            exchanges=["polymarket"],
            limit=1,
        )
        assert isinstance(activity.exchanges, dict)
        assert isinstance(activity.status, dict)
        assert "polymarket" in activity.status

    def test_update_credentials_rejects_invalid_kalshi_private_key(self, client: Any) -> None:
        with pytest.raises(APIStatusError) as exc_info:
            client.account.update_credentials(
                kalshi_api_key_id="bad-key-id",
                kalshi_private_key="not-a-pem",
            )
        assert exc_info.value.status_code == 400


class TestRESTApprovals:
    def test_list_approvals_rejects_unsupported_exchange(self, client: Any) -> None:
        with pytest.raises(APIStatusError) as exc_info:
            client.approvals.list(exchange="kalshi")
        assert exc_info.value.status_code == 501

    def test_set_approvals_rejects_unsupported_exchange(self, client: Any) -> None:
        with pytest.raises(APIStatusError) as exc_info:
            client.approvals.set(exchange="kalshi", all=True)
        assert exc_info.value.status_code == 501


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
    @pytest.mark.asyncio
    async def test_snapshot_identity_structure_ordering_consistency(self, client: Any) -> None:
        """Full validation of a live orderbook snapshot from connect through data."""
        from parsec_api.streaming import OrderbookSnapshot

        markets = _find_active_markets_with_depth(client, 1)
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

        markets = _find_active_markets_with_depth(client, 2)
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

        markets = _find_active_markets_with_depth(client, 1)
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
        """Connect and wait for a heartbeat within 45s. Validates timestamp is recent.
        Server sends heartbeats in response to WS Ping frames (~20s default interval)."""
        ws = client.ws()
        heartbeats: List[int] = []

        @ws.on("heartbeat")
        async def _on_heartbeat(ts_ms: int) -> None:
            heartbeats.append(ts_ms)

        await ws.connect()
        try:
            deadline = asyncio.get_event_loop().time() + 45.0
            while len(heartbeats) == 0 and asyncio.get_event_loop().time() < deadline:
                await asyncio.sleep(0.5)

            assert len(heartbeats) >= 1, "No heartbeat received within 45s"
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
