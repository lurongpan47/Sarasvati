"""
Unified provider clients for the 7-model Buddhist AI Charter fuzz suite.

Each client exposes:
    .name              -> str (short alias, e.g. "claude")
    .model_id          -> str (canonical model id used at the API)
    .available         -> bool (set by ping())
    .ping()            -> bool   # cheap $0.001 test call
    .chat(prompt, system=None, max_tokens=256, timeout=60) -> dict
        returns {"text": str, "usage": {"input_tokens": int, "output_tokens": int},
                 "cost_usd": float, "latency_s": float, "error": str|None}

Design goals
------------
- Fail-open: any provider that errors is marked unavailable but doesn't take
  down the campaign.
- Cost-aware: every response carries a $USD estimate based on token counts.
- No key leakage: keys are loaded once at import from env / macOS keychain
  and never echoed.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
from dataclasses import dataclass
from typing import Any

import requests

# --------------------------------------------------------------------------- #
# Key loading                                                                  #
# --------------------------------------------------------------------------- #


def _keychain(name: str) -> str | None:
    try:
        r = subprocess.run(
            ["security", "find-generic-password", "-a", "sarasvati-fuzz",
             "-s", name, "-w"],
            capture_output=True, text=True, timeout=5,
        )
        if r.returncode == 0:
            return r.stdout.strip() or None
    except Exception:
        return None
    return None


def _load_env_file(path: str) -> dict[str, str]:
    out: dict[str, str] = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                out[k.strip()] = v.strip().strip('"').strip("'")
    except FileNotFoundError:
        pass
    return out


_FIN_ENV = _load_env_file(os.path.expanduser("~/clawd/skills/financial-analyst/.env"))


def get_key(*candidates: str) -> str | None:
    """Look up key in env, financial-analyst .env, then keychain."""
    for c in candidates:
        v = os.environ.get(c) or _FIN_ENV.get(c) or _keychain(c)
        if v:
            return v
    return None


# --------------------------------------------------------------------------- #
# Pricing (approximate, USD per 1M tokens)                                     #
# --------------------------------------------------------------------------- #

PRICING = {
    "claude":   {"in": 5.00,  "out": 25.00},   # claude opus 4.x-ish
    "gpt":      {"in": 2.50,  "out": 10.00},   # gpt-4o / gpt-5.5 approx
    "gemini":   {"in": 1.25,  "out": 5.00},    # gemini 2.x pro approx
    "grok":     {"in": 3.00,  "out": 15.00},   # grok-3/4 approx
    "minimax":  {"in": 0.30,  "out": 1.20},    # minimax M-series approx
    "deepseek": {"in": 0.27,  "out": 1.10},    # deepseek-chat v3
    "qwen":     {"in": 1.60,  "out": 6.40},    # qwen-max dashscope approx
}


def _cost(name: str, in_tok: int, out_tok: int) -> float:
    p = PRICING.get(name, {"in": 1.0, "out": 3.0})
    return round((in_tok * p["in"] + out_tok * p["out"]) / 1_000_000, 6)


# --------------------------------------------------------------------------- #
# Base client                                                                  #
# --------------------------------------------------------------------------- #


@dataclass
class Client:
    name: str
    model_id: str
    api_key: str | None
    available: bool = False
    last_error: str | None = None

    # Providers override these:
    def _call(self, prompt: str, system: str | None, max_tokens: int,
              timeout: int) -> tuple[str, int, int]:
        """Return (text, input_tokens, output_tokens)."""
        raise NotImplementedError

    def ping(self) -> bool:
        if not self.api_key:
            self.available = False
            self.last_error = "no api key"
            return False
        try:
            self._call("Reply with just: ok", system=None, max_tokens=8, timeout=30)
            self.available = True
            self.last_error = None
            return True
        except Exception as e:
            self.available = False
            self.last_error = f"{type(e).__name__}: {str(e)[:200]}"
            return False

    def chat(self, prompt: str, system: str | None = None,
             max_tokens: int = 256, timeout: int = 60) -> dict[str, Any]:
        t0 = time.time()
        if not self.available:
            return {
                "text": "", "usage": {"input_tokens": 0, "output_tokens": 0},
                "cost_usd": 0.0, "latency_s": 0.0,
                "error": self.last_error or "unavailable",
            }
        try:
            text, in_tok, out_tok = self._call(prompt, system, max_tokens, timeout)
            return {
                "text": text,
                "usage": {"input_tokens": in_tok, "output_tokens": out_tok},
                "cost_usd": _cost(self.name, in_tok, out_tok),
                "latency_s": round(time.time() - t0, 3),
                "error": None,
            }
        except Exception as e:
            return {
                "text": "", "usage": {"input_tokens": 0, "output_tokens": 0},
                "cost_usd": 0.0, "latency_s": round(time.time() - t0, 3),
                "error": f"{type(e).__name__}: {str(e)[:200]}",
            }


# --------------------------------------------------------------------------- #
# Anthropic                                                                    #
# --------------------------------------------------------------------------- #

class AnthropicClient(Client):
    def _call(self, prompt, system, max_tokens, timeout):
        import anthropic
        client = anthropic.Anthropic(api_key=self.api_key, timeout=timeout)
        kwargs = {
            "model": self.model_id,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system
        r = client.messages.create(**kwargs)
        text = "".join(b.text for b in r.content if getattr(b, "type", None) == "text")
        return text, r.usage.input_tokens, r.usage.output_tokens


# --------------------------------------------------------------------------- #
# OpenAI-compatible base (openai, deepseek, qwen)                              #
# --------------------------------------------------------------------------- #

class OpenAICompatClient(Client):
    base_url: str = "https://api.openai.com/v1"

    def _call(self, prompt, system, max_tokens, timeout):
        from openai import OpenAI
        client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=timeout)
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": prompt})
        r = client.chat.completions.create(
            model=self.model_id, messages=msgs, max_tokens=max_tokens,
        )
        text = r.choices[0].message.content or ""
        usage = r.usage
        return (text,
                getattr(usage, "prompt_tokens", 0) or 0,
                getattr(usage, "completion_tokens", 0) or 0)


class OpenAIClient(OpenAICompatClient):
    base_url = "https://api.openai.com/v1"


class DeepSeekClient(OpenAICompatClient):
    base_url = "https://api.deepseek.com/v1"


class QwenClient(OpenAICompatClient):
    base_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"


class XAIClient(OpenAICompatClient):
    base_url = "https://api.x.ai/v1"


class MiniMaxClient(OpenAICompatClient):
    # MiniMax offers an OpenAI-compat endpoint on api.minimax.chat
    base_url = "https://api.minimax.chat/v1"


# --------------------------------------------------------------------------- #
# Google Gemini (REST)                                                         #
# --------------------------------------------------------------------------- #

class GoogleClient(Client):
    def _call(self, prompt, system, max_tokens, timeout):
        url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
               f"{self.model_id}:generateContent?key={self.api_key}")
        body = {
            "contents": [{"role": "user", "parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": max_tokens, "temperature": 0.7},
        }
        if system:
            body["systemInstruction"] = {"parts": [{"text": system}]}
        r = requests.post(url, json=body, timeout=timeout)
        r.raise_for_status()
        data = r.json()
        cands = data.get("candidates", [])
        text = ""
        if cands:
            parts = cands[0].get("content", {}).get("parts", [])
            text = "".join(p.get("text", "") for p in parts)
        usage = data.get("usageMetadata", {})
        return (text,
                int(usage.get("promptTokenCount", 0)),
                int(usage.get("candidatesTokenCount", 0)))


# --------------------------------------------------------------------------- #
# Factory                                                                      #
# --------------------------------------------------------------------------- #


def build_all() -> list[Client]:
    clients: list[Client] = [
        AnthropicClient(
            name="claude", model_id="claude-opus-4-20250514",
            api_key=get_key("ANTHROPIC_API_KEY"),
        ),
        OpenAIClient(
            name="gpt", model_id="gpt-4o-mini",
            api_key=get_key("OPENAI_API_KEY"),
        ),
        GoogleClient(
            name="gemini", model_id="gemini-2.5-flash",
            api_key=get_key("GOOGLE_API_KEY", "GEMINI_API_KEY"),
        ),
        XAIClient(
            name="grok", model_id="grok-3-mini",
            api_key=get_key("XAI_API_KEY"),
        ),
        MiniMaxClient(
            name="minimax", model_id="MiniMax-Text-01",
            api_key=get_key("MINIMAX_API_KEY"),
        ),
        DeepSeekClient(
            name="deepseek", model_id="deepseek-chat",
            api_key=get_key("DEEPSEEK_API_KEY"),
        ),
        QwenClient(
            name="qwen", model_id="qwen-turbo",
            api_key=get_key("QWEN_API_KEY", "DASHSCOPE_API_KEY"),
        ),
    ]
    return clients
