#!/bin/sh
# The deliverables command. STATUS is REGENERATED here, not copied: a stale
# stamp shipped five batches running because the export was a separate step
# someone had to remember. It is no longer a separate step.
#
# The target is lowercase `deliverables/` because that is the path git tracks.
# It was DELIVERABLES/, which is the SAME directory on macOS (case-insensitive)
# and a DIFFERENT one everywhere else - so on Linux or CI the export would land
# in an untracked directory and STATUS.md would never update, which is exactly
# the stale-stamp failure 01-COMMUNICATION.md exists to make impossible.
set -e
cd "$(dirname "$0")"
python3 emit_status.py
python3 emit_worksheet.py
mkdir -p deliverables
for f in out/reports/*.md out/pack_proposals/*.yaml; do
  [ -f "$f" ] && cp "$f" deliverables/
done
# ORDER-002 item 6: identifier gate. Count MUST be 0 or the export fails.
# Patterns live in .identifier_scan_local (gitignored) so this guard never
# publishes the strings it guards.
SCAN=".identifier_scan_local"
if [ -f "$SCAN" ]; then
  hits=0
  while IFS= read -r pat; do
    case "$pat" in ''|\#*) continue ;; esac
    n=$(git grep -ciE "$pat" -- . 2>/dev/null | awk -F: '{s+=$NF} END{print s+0}')
    hits=$((hits + n))
  done < "$SCAN"
  if [ "$hits" -ne 0 ]; then
    echo "IDENTIFIER GATE FAILED: $hits match(es) in tracked content. Export aborted." >&2
    exit 1
  fi
  echo "identifier gate: 0 matches"
fi

echo "--- deliverables ---"
ls -1 deliverables
echo "stamp: $(grep -m1 'generated:' deliverables/STATUS.md)"
