#!/usr/bin/env python3
"""Pluggable model adapter. Works with any OpenAI-compatible endpoint (college API, vLLM, etc).
Env: LLM_BASE_URL (e.g. https://host/v1), LLM_API_KEY, LLM_MODEL. Stdlib only.
Usage: python scripts/llm.py "prompt"   or   echo "prompt" | python scripts/llm.py
"""
import os, sys, json, urllib.request

def complete(prompt, system="You are a concise research assistant. Never invent facts or sources."):
    base, key, model = os.getenv("LLM_BASE_URL"), os.getenv("LLM_API_KEY"), os.getenv("LLM_MODEL")
    if not (base and key and model):
        raise SystemExit("LLM_BASE_URL, LLM_API_KEY and LLM_MODEL are not set. Add them as repo secrets/variables.")
    body = json.dumps({"model": model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}], "temperature": 0.2}).encode()
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions", body, {"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print(complete(" ".join(sys.argv[1:]) or sys.stdin.read()))
