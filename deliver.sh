#!/bin/sh
# The deliverables command. STATUS is REGENERATED here, not copied: a stale
# stamp shipped five batches running because the export was a separate step
# someone had to remember. It is no longer a separate step.
set -e
cd "$(dirname "$0")"
python3 emit_status.py
mkdir -p DELIVERABLES
for f in out/reports/*.md out/pack_proposals/*.yaml; do
  [ -f "$f" ] && cp "$f" DELIVERABLES/
done
echo "--- DELIVERABLES ---"
ls -1 DELIVERABLES
echo "stamp: $(grep -m1 'generated:' DELIVERABLES/STATUS.md)"
