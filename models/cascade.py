"""Model-cascading router: send each task to the cheapest adequate tier; escalate on low confidence.

ARGUS - Autonomous Risk & Global Unified Surveillance Agent (class build).

  Work-stream / owner : Model economics (Pair F)
  Blueprint reference : §13, §14

TODO (tomorrow):
  - route(task_type, context) -> tier; implement the §14 routing policy
    and escalation triggers.
"""
