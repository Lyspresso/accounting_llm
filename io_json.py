"""One JSON I/O helper (2.5): atomic writes in the house style (indent=1).

Half-written artifacts are the failure class the ledger already solved for
itself; this extends the cure to every tool artifact. Reads raise loudly —
a corrupt artifact must never be mistaken for a missing one (2.6).
"""
import json
import os


def load(path, default=None, *, required=False):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        if required:
            raise
        return default


def dump(path, obj, *, indent=1, sort_keys=False):
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=indent, sort_keys=sort_keys)
    os.replace(tmp, path)
    return path
