"""Prompt-injection defence: treat retrieved content as data, not instructions.

ARGUS - Autonomous Risk & Global Unified Surveillance Agent (class build).

  Work-stream / owner : Guardrails / governance (Pair E)
  Blueprint reference : §21, §25

TODO (tomorrow):
  - Sanitise/escape retrieved text; detect instruction-like payloads;
    isolate from the system prompt.
"""
