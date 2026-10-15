# thinking-ops

Versioned operating system for agents, ideas and decisions. Open `BOARD.md` for the dashboard. Agents read `AGENTS.md`.

Flow: edit or add a file in `board/` or `tasks/` -> push -> GitHub Action validates and regenerates `BOARD.md` -> Codex or Claude pick up `ready` tasks and commit results back.

Local check: `python scripts/board.py`

College model API (optional): set repo variables `LLM_BASE_URL` and `LLM_MODEL` and secret `LLM_API_KEY`, then run the `digest` workflow.
