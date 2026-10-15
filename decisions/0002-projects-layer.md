# 0002. Add a projects layer to the operating board

Date: 2026-10-15
Context: Existing agents, ideas, tasks and decisions lack a single place to summarize the broader projects they support.
Options: (a) infer projects from ideas, (b) add a separate markdown-backed projects collection, (c) add a hosted database.
Choice: (b). Add one file per project in `board/projects/`; validate and export it through the existing board generator and display it above Agents on the static site.
Why: Git remains the audited system of record. Project names, goals, statuses, next actions and linked agent/idea IDs become visible without changing the existing four collections. Unknown external project paths and repository URLs are left empty rather than guessed.
What would change my mind: A verified need for cross-repository synchronization or richer many-to-many references that markdown cannot maintain reliably.
