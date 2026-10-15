# Operating manual (read by Codex and Claude)

This repo is the single source of truth for Devanshu's agents, ideas, decisions and tasks.
Git history is the audit trail. Never keep state anywhere else.

## Layout
- `board/agents/*.md`  one file per agent. Frontmatter: name, status (queued|running|blocked|done), owner, progress (0-100), blocker, next, done_when.
- `board/ideas/*.md`   one file per idea. Frontmatter: title, area, impact, confidence, effort (1-5), status (open|promoted|dropped).
- `tasks/*.md`         work items. Frontmatter: title, status (draft|ready|in_progress|review|done), assignee (codex|claude|human), agent.
- `decisions/NNNN-*.md` one short record per decision: context, options, choice, why, what would change my mind.
- `BOARD.md`           generated dashboard. Never edit by hand.
- `digests/`           generated research digests.

## Rules for any agent
1. Pick only tasks with `status: ready` and your `assignee`. Set `in_progress`, commit, then work.
2. Never fabricate data or results. If access (network, data, keys) is missing, set the agent to `blocked`, fill `blocker`, and stop.
3. Cite sources for claims; give the denominator for every number.
4. Finish by setting the task to `review` (not `done`), update the agent's `next`, and add a decision record if you made a non-obvious choice.
5. One logical change per commit. Message format: `area: what and why`.
6. Run `python scripts/board.py` before committing; it validates files and regenerates BOARD.md.
7. Human gate only for publishing, spending money, or deleting data.
