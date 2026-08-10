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
mkdir -p deliverables
for f in out/reports/*.md out/pack_proposals/*.yaml; do
  [ -f "$f" ] && cp "$f" deliverables/
done
echo "--- deliverables ---"
ls -1 deliverables
echo "stamp: $(grep -m1 'generated:' deliverables/STATUS.md)"
