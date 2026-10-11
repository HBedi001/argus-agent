"""Conditional-edge functions — above all the evidence-sufficiency gate (graph, not LLM, decides when to stop).

ARGUS - Autonomous Risk & Global Unified Surveillance Agent (class build).

  Work-stream / owner : Orchestration (Pair A / tech lead)
  Blueprint reference : §17

TODO (tomorrow):
  - Implement next_step(state) from §17: iteration cap, confidence floor,
    missing info, unresolved conflicts.
"""

# These defaults can be overridden per state with ``max_iterations`` and
# ``confidence_floor``.
MAX_ITERATIONS = 5
CONFIDENCE_FLOOR = 0.75


def material_unresolved_conflicts(state):
  """Return whether the state contains unresolved material conflicts."""
  return bool(state.get("unresolved_conflicts"))


def next_step(state):
  """Route based on evidence sufficiency; the graph controls termination."""
  if state["investigation_iterations"] >= state.get("max_iterations", MAX_ITERATIONS):
    return "risk_assessment_with_uncertainty"

  if state["confidence_score"] < state.get("confidence_floor", CONFIDENCE_FLOOR):
    return "continue_research"

  if state["missing_information"]:
    return "continue_research"

  if material_unresolved_conflicts(state):
    return "continue_research"

  return "risk_assessment"
