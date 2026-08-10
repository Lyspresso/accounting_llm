#!/bin/sh
# The standing fixture suite. Any stack edit proves neutrality against all of it.
set -e
cd "$(dirname "$0")"
echo "=== matcher ==="; python3 test_matcher.py | tail -1
echo "=== canon   ==="; python3 test_canon.py   | tail -1
echo "=== wiring  ==="; python3 test_wiring.py  | tail -1
echo "=== chart invariants ==="; python3 test_chart.py | tail -1
echo "=== provenance ==="; python3 test_provenance.py | tail -1
echo "=== write path ==="; python3 test_writepath.py | tail -1
echo "=== sentinel fault-injection ==="; python3 test_sentinel.py | tail -1
echo "=== ledger sentinel ==="; python3 sentinel.py --check | tail -2
echo "=== dispatcher ==="; python3 dispatcher.py | head -2
