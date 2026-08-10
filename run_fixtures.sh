#!/bin/sh
# The standing fixture suite. Any stack edit proves neutrality against all of it.
set -e
cd "$(dirname "$0")"

# COLD CACHE, ALWAYS (ORDER-002 item 7). A run of this suite once reported 8/8
# GREEN while compare_stage1_v3.py held a SyntaxError, because Python served
# stale .pyc files. A fixture claim made against bytecode that no longer matches
# the source is not evidence of anything. Clearing is cheap; a false green is not.
find . -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null || true

echo "=== matcher ==="; python3 -B test_matcher.py | tail -1
echo "=== canon   ==="; python3 -B test_canon.py   | tail -1
echo "=== wiring  ==="; python3 -B test_wiring.py  | tail -1
echo "=== chart invariants ==="; python3 -B test_chart.py | tail -1
echo "=== provenance ==="; python3 -B test_provenance.py | tail -1
echo "=== write path ==="; python3 -B test_writepath.py | tail -1
echo "=== sentinel fault-injection ==="; python3 -B test_sentinel.py | tail -1
echo "=== family aggregation ==="; python3 -B test_aggregation.py | tail -1
echo "=== evidence registry ==="; python3 -B test_registry.py | tail -1
echo "=== tool parity ==="; python3 -B test_tool_parity.py | tail -1
echo "=== ledger sentinel ==="; python3 -B sentinel.py --check | tail -2
echo "=== dispatcher ==="; python3 -B dispatcher.py | head -2
