---
name: replica
description: >-
  Orchestrates the full Replica clean-room product reconstruction workflow in
  Codex and ChatGPT: recon, architecture, design, build, backend, test, parity
  diff, evidence-led product improvement, brand, launch and deployment. Use
  when the user asks to recreate, rebuild, reverse engineer, clone clean-room,
  improve, or launch their own version of an existing app or digital product.
---

# Replica orchestrator

Use this skill as the front door for the Replica pack. It coordinates the
specialist skills and keeps one evidence trail in the user's project under
`replica/`.

## Non-negotiable boundary

Rebuild functionality and UX patterns clean-room style. Do not copy source
code, private APIs, proprietary assets, trademarks, licensed content, or
another user's account data. Use public sources and the user's own authorised
account only. Never bypass a login, paywall, access control, robots policy, or
terms restriction.

If the requested target cannot be reconstructed lawfully or safely, narrow
the scope to public behaviour, interoperable concepts, and original
implementation.

## Default workflow

Run the stages in this order unless the user explicitly asks for one stage:

1. `$replica-recon`
2. `$replica-architect`
3. `$replica-design`
4. `$replica-build`
5. `$replica-backend`
6. `$replica-test`
7. `$replica-diff`
8. `$replica-entrepreneur`
9. `$replica-brand`
10. `$replica-launch`
11. `$replica-deploy`

Each stage must read the outputs of the previous stage rather than starting
from memory.

## Codex-native tool routing

Use the best available first-party or connected capability:

- public product research: web search and official public documentation
- authenticated walkthroughs: a browser tool only with the user's own account
- code and repository work: GitHub and the local project workspace
- application verification: browser automation and end-to-end tests
- deployment: the user's connected hosting provider such as Vercel or Netlify
- database and auth: the user's selected provider, such as Supabase
- current prices, policies, store limits or terms: verify from current sources

Do not invent access to a connector that is not available. If a specialist
connector is unavailable, produce the exact files and commands the user can
run locally.

## Stage gate

Before moving to the next stage, record:

- outputs created
- evidence used
- assumptions and confidence
- unresolved blockers
- explicit out-of-scope items
- the next stage and why it is ready

Use `replica/stage-gates.md` for the running record.

## Evidence ledger

Maintain `replica/evidence.md` with one row per material finding:

`ID | claim | source | source type | observed date | confidence | used by`

Prefer direct evidence from official docs, public product surfaces and the
user's own authorised walkthrough over commentary about the product.

## Completion

The final result is not a pixel copy. It is a clean-room product that:

- completes the same important user jobs
- has verified feature parity for the agreed scope
- fixes evidence-backed user complaints where sensible
- has its own brand, copy and assets
- passes tests and accessibility checks
- has no open S1 or S2 bugs
- passes the rebrand sweep
- is deployed only after the user approves the production step
