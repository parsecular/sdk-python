# Changelog

## 0.4.0 (2026-02-15)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/parsecular/sdk-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([7812685](https://github.com/parsecular/sdk-python/commit/7812685f9db3883665699b5e6e9e3e30d7cfa502))
* **api:** api update ([395fa8e](https://github.com/parsecular/sdk-python/commit/395fa8ec6f1fcdbfb9dbe0691631244612b4f574))
* **api:** api update ([9919e3e](https://github.com/parsecular/sdk-python/commit/9919e3ec1dda1fe91457b4755b1de7f38b9e5d47))
* **api:** api update ([d2cc12c](https://github.com/parsecular/sdk-python/commit/d2cc12c26519e29f30eb5585839f894d87819fb3))
* **api:** api update ([734cf98](https://github.com/parsecular/sdk-python/commit/734cf98642f17b1c738bd39044fe86c7bfed10b1))
* v0.4.0 streaming fixes, events resource, docs, and test updates ([75c746e](https://github.com/parsecular/sdk-python/commit/75c746e05494f4911c7ade4e6c781b35107b4a7f))


### Bug Fixes

* add type annotations for get_book() (pyright strict) ([58a4af3](https://github.com/parsecular/sdk-python/commit/58a4af3ae0aba2002abbcbe21237de36bc2ac9fb))
* sort imports in types/__init__.py (ruff I001) ([3f8145d](https://github.com/parsecular/sdk-python/commit/3f8145d321e171b31d7d6bf7ab77f9691ec70e9b))
* type annotation for off() listener dict (pyright strict) ([544ad37](https://github.com/parsecular/sdk-python/commit/544ad37552965fd9d3a5ee161940b8ea879a748c))


### Chores

* format all `api.md` files ([d92f361](https://github.com/parsecular/sdk-python/commit/d92f361128a47be116a64b6c8226b8fbb38f8eb6))
* **internal:** fix lint error on Python 3.14 ([e80583f](https://github.com/parsecular/sdk-python/commit/e80583f8e4614539753335eec01083998840d6d2))
* **internal:** version bump ([aefc392](https://github.com/parsecular/sdk-python/commit/aefc39286f0592b92d1fe49e131df97ec7033a15))
* **internal:** version bump ([af27e44](https://github.com/parsecular/sdk-python/commit/af27e44cfc02f7c6b77bc25f757a174653f39479))
* **internal:** version bump ([820ad76](https://github.com/parsecular/sdk-python/commit/820ad76023c4c30843ad67d48f4161b763d29a6a))

## 0.4.0 (2026-02-15)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/parsecular/sdk-python/compare/v0.3.0...v0.4.0)

### ⚠ BREAKING CHANGES

This release migrates the `Market` type to the new Silver layer schema. All field names have changed. See the **Migration Guide** below.

**Market field renames:**
* `id` has been renamed to `exchange_market_id`
* `title` has been renamed to `question`
* `volume` (integer) has been replaced by `volume_total` (number/float)
* `group_id` has been renamed to `exchange_group_id`
* `event_id` has been renamed to `parsec_group_id`
* `close_time` has been renamed to `end_date`
* `open_time` has been renamed to `event_start_time`
* `status` changed from enum (`active | closed | resolved`) to plain string

**Market field type changes:**
* `outcomes` changed from `list[str]` to `list[Outcome]` objects with `name`, `price`, and `token_id` attributes

**Removed Market fields:**
* `meta` (`ResponseMeta`) — removed from responses
* `outcome_tokens` — removed
* `token_id_yes` / `token_id_no` — removed (token IDs now inside `Outcome` objects)
* `outcome_prices` — removed
* `volume_1wk` / `volume_1mo` — removed

### Features

* **api:** add Events resource — `client.events.list()` for querying aggregated market groups
* **api:** new Market fields: `parsec_group_id`, `best_bid`, `best_ask`, `last_price`, `volume_24h`, `open_interest`, `created_at`, `updated_at`, `url`, `rules`, `group_title`, `outcome_count`, `xref`, `collection_date`, `last_collected`
* **ws:** add `get_book()` method to read current local orderbook state
* **ws:** add `off()` method to unregister event handlers

### Bug Fixes

* **ws:** add auth timeout — no longer hangs forever on unresponsive server
* **ws:** fix `connected` event firing before `auth_ok` received
* **ws:** callback exceptions are now logged instead of silently swallowed
* **ws:** WebSocket send failures are now logged

### Migration Guide

**Accessing market identity:**

```python
# v0.3.0
market_id = market.id
title = market.title

# v0.4.0
market_id = market.exchange_market_id
title = market.question
```

**Working with outcomes (most impactful change):**

```python
# v0.3.0
outcomes: list[str] = market.outcomes         # ["Yes", "No"]
yes_token = market.token_id_yes
no_token = market.token_id_no
prices = market.outcome_prices

# v0.4.0
outcomes: list[Outcome] = market.outcomes     # [Outcome(name="Yes", price=0.65, token_id="abc"), ...]
yes_outcome = next(o for o in outcomes if o.name == "Yes")
yes_token = yes_outcome.token_id
yes_price = yes_outcome.price
```

**Volume and timing fields:**

```python
# v0.3.0
vol = market.volume         # int
close = market.close_time
open_ = market.open_time

# v0.4.0
vol = market.volume_total   # float
close = market.end_date
open_ = market.event_start_time
# New volume field:
vol_24h = market.volume_24h
```

**Group and event references:**

```python
# v0.3.0
group_id = market.group_id
event_id = market.event_id

# v0.4.0
group_id = market.exchange_group_id
event_id = market.parsec_group_id
```

**Events (new resource):**

```python
events = client.events.list(exchange="polymarket")
for event in events.data:
    print(event.title, len(event.markets))
```

**WebSocket orderbook reading:**

```python
ws = client.ws(exchange="kalshi")
ws.subscribe("orderbook", parsec_id)

# Read current book state at any time
book = ws.get_book(parsec_id)

# Unregister a handler
def on_book(data):
    print(data)

ws.on("orderbook", on_book)
# Later:
ws.off("orderbook", on_book)
```

## 0.3.0 (2026-02-12)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/parsecular/sdk-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([38ae803](https://github.com/parsecular/sdk-python/commit/38ae8035ade7defc4f477fbd2fb854184c54571d))

## 0.2.0 (2026-02-12)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/parsecular/sdk-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([e888e12](https://github.com/parsecular/sdk-python/commit/e888e129d9c7d67a1ae70ea8f92627fea4edce4b))


### Bug Fixes

* use correct candle.timestamp field + resolve README merge conflict ([e7e6b54](https://github.com/parsecular/sdk-python/commit/e7e6b546de618727bcaf26587f42f90e0b1cce37))
* **ws:** add missing needs_refresh book state + fill activity tests ([16468a2](https://github.com/parsecular/sdk-python/commit/16468a2056173adc8bc799523070812063bfcfb5))


### Chores

* **internal:** fix lint error on Python 3.14 ([4e37033](https://github.com/parsecular/sdk-python/commit/4e370332461fdf2203a01a2ff290c6b02a90e333))


### Styles

* fix ruff import sorting in contract tests ([d48b74b](https://github.com/parsecular/sdk-python/commit/d48b74b05678dca25d7ada9749eca439d8838839))

## 0.1.0 (2026-02-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/parsecular/sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([709899f](https://github.com/parsecular/sdk-python/commit/709899f73261abc6fde51b4655b520e64c507ad8))
* **api:** api update ([071add8](https://github.com/parsecular/sdk-python/commit/071add84db413b0d35c6f8a7912c8eb8dc548bca))
* **api:** api update ([14ef974](https://github.com/parsecular/sdk-python/commit/14ef9741162ba90c2c7e3d990b2d1a8b63aebee0))
* **ws:** add WebSocket streaming client with stateful orderbook ([6ef9e5d](https://github.com/parsecular/sdk-python/commit/6ef9e5dc1463409ef08b8f10cabf1386c8aa932c))


### Bug Fixes

* resolve pyright strict mode errors in streaming client ([9310dd7](https://github.com/parsecular/sdk-python/commit/9310dd7b51146c22b3aa2fa7cc5931ab7a6f133d))
* resolve pyright strict mode errors in streaming module ([a6e8811](https://github.com/parsecular/sdk-python/commit/a6e8811af6552331504a0e87042bc6357466c814))
* resolve remaining pyright unknown argument errors ([e31e1b1](https://github.com/parsecular/sdk-python/commit/e31e1b16c58cc1f9a3099c687e105c42c281b4c6))


### Styles

* fix ruff import sorting and remove unused math import ([59c32dc](https://github.com/parsecular/sdk-python/commit/59c32dc6b8b52664dfa1d650d54abf92569a8280))
* fix ruff import sorting in _client.py ([0023d5c](https://github.com/parsecular/sdk-python/commit/0023d5c3425fd13f30a6c6a46d9ede3118857d70))
* fix ruff import sorting in types ([fab7e60](https://github.com/parsecular/sdk-python/commit/fab7e604e6660defc53706d3c2a4701677dd47b3))
