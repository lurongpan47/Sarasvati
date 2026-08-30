"""Persistent per-provider spend meter.

Tiny JSON file at results/.spend.json (gitignored). Concurrent-safe enough
for the coordinator's single-threaded outer loop.
"""

from __future__ import annotations
import json
import os
import time
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
SPEND_PATH = HERE / "results" / ".spend.json"

# Hard cap per mission spec
HARD_CAP_USD = 300.0
WARN_AT_USD = 250.0


def _empty() -> dict[str, Any]:
    return {
        "total_usd": 0.0,
        "by_provider": {},
        "by_hour": {},
        "warned_250": False,
        "halted_300": False,
        "updated_at": time.time(),
    }


def load() -> dict[str, Any]:
    if not SPEND_PATH.exists():
        return _empty()
    try:
        with open(SPEND_PATH) as f:
            return json.load(f)
    except Exception:
        return _empty()


def save(state: dict[str, Any]) -> None:
    SPEND_PATH.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = time.time()
    tmp = SPEND_PATH.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    os.replace(tmp, SPEND_PATH)


def add(provider: str, cost_usd: float) -> dict[str, Any]:
    state = load()
    state["total_usd"] = round(state["total_usd"] + cost_usd, 6)
    state["by_provider"][provider] = round(
        state["by_provider"].get(provider, 0.0) + cost_usd, 6
    )
    hour = time.strftime("%Y-%m-%dT%H", time.gmtime())
    state["by_hour"][hour] = round(state["by_hour"].get(hour, 0.0) + cost_usd, 6)
    save(state)
    return state


def remaining() -> float:
    return max(0.0, HARD_CAP_USD - load()["total_usd"])


def should_halt() -> bool:
    return load()["total_usd"] >= HARD_CAP_USD


def should_warn() -> bool:
    s = load()
    return s["total_usd"] >= WARN_AT_USD and not s["warned_250"]


def mark_warned() -> None:
    s = load()
    s["warned_250"] = True
    save(s)


def mark_halted() -> None:
    s = load()
    s["halted_300"] = True
    save(s)
