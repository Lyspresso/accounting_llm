#!/usr/bin/env python3
"""
Path resolution — one place, no absolute paths in source.

Eight modules hardcoded absolute paths under a specific home directory. That
made the code unrunnable by anyone else, and it published a local filesystem
layout (and a university, course and semester) the moment the repo went public.
Both problems have the same fix: resolve paths at runtime, from config or
environment, and keep the answer out of the source.

Resolution order, first hit wins:

    QBV_<NAME> environment variable
    the `paths:` block of config.yaml   (gitignored; copy config.template.yaml)
    the built-in default, relative to this file

so a checkout runs with no configuration at all, and a real corpus is attached
by pointing config.yaml at it.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.yaml")

DEFAULTS = {
    "questions": os.path.join(HERE, "corpus"),
    "pack": os.path.join(HERE, "pack"),
    "output": os.path.join(HERE, "out"),
    "goldens": os.path.join(HERE, "goldens"),
    "transcripts": os.path.join(HERE, "transcripts"),
    "verdicts": os.path.join(HERE, "reviewer", "hand_check_verdicts_v1.json"),
}


def _config_paths():
    """
    The `paths:` block of config.yaml. Deliberately not a YAML dependency: this
    module has to work in a fresh checkout before anything is installed, and one
    more import is one more way for path resolution to fail at import time.
    """
    out = {}
    if not os.path.exists(CONFIG):
        return out
    in_block = False
    for raw in open(CONFIG, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("paths:"):
            in_block = True
            continue
        if in_block:
            if not line.startswith((" ", "\t")):      # dedent ends the block
                break
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def resolve(name):
    """Absolute path for a named location. Never returns None."""
    env = os.environ.get(f"QBV_{name.upper()}")
    if env:
        return os.path.expanduser(env)
    cfg = _config_paths().get(name)
    if cfg and not cfg.startswith("<"):               # "<SET ME ...>" placeholder
        return os.path.expanduser(cfg)
    return DEFAULTS.get(name, os.path.join(HERE, name))


if __name__ == "__main__":
    for k in DEFAULTS:
        v = resolve(k)
        print(f"  {k:12s} {v}   {'(exists)' if os.path.exists(v) else '(missing)'}")
