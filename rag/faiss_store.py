"""Vector store wrapper (FAISS for the POC; see README note on pgvector/Qdrant for metadata filtering).

ARGUS - Autonomous Risk & Global Unified Surveillance Agent (class build).

  Work-stream / owner : RAG / knowledge (Pair B)
  Blueprint reference : §11

TODO (tomorrow):
  - Build/load the index; expose add() and similarity_search(). Keep the
    interface swappable.
"""
