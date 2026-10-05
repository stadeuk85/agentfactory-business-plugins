# AGENTS.md

## Purpose

This directory is the OpenAI/Codex port of the Replica clean-room product
reconstruction workflow.

## Operating rule

Start with the `replica` skill for end-to-end requests. Use the specialist
skills directly for focused work.

Never copy a target application's source code, private endpoints, proprietary
assets, trademarks, licensed content, or another user's data. Public behaviour,
public documentation, public APIs, and the user's own authorised account are
the allowed evidence base.

## Workspace outputs

Write project-specific outputs under `replica/` in the user's working
project, not inside this plugin package.

Maintain:

- `replica/evidence.md`
- `replica/stage-gates.md`
- the files required by each specialist skill

## Verification

Use current sources for time-sensitive facts and product policies. Use browser
automation to verify the rebuilt application, not to stress or scrape the
target application. Prefer official APIs and connected tools where available.
