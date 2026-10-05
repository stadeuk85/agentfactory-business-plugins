# Replica Skill for Codex and ChatGPT

A Codex/OpenAI-native port and extension of Jake Schincariol's Replica skill
pack. It provides a clean-room workflow for understanding an existing app,
rebuilding the agreed functionality from scratch, testing parity, learning
from public user feedback, rebranding the result, and shipping it.

This port preserves the original MIT-licensed helper scripts and specialist
methods while adapting the package to OpenAI Agent Skills and Plugins.

## What is included

The plugin contains 12 skills:

- `$replica` - orchestrates the complete workflow
- `$replica-recon` - evidence-led product reconnaissance
- `$replica-architect` - stack, schema, APIs and build order
- `$replica-design` - design tokens and accessible primitives
- `$replica-build` - clean-room implementation
- `$replica-backend` - auth, data, payments and integrations
- `$replica-test` - QA, Playwright and bug triage
- `$replica-diff` - feature and layout parity
- `$replica-entrepreneur` - public review evidence and product gaps
- `$replica-brand` - independent naming, voice and rebrand sweep
- `$replica-launch` - landing page, pricing and store listing
- `$replica-deploy` - production preflight and deployment

The Python utilities remain standard-library only.

## Install from this GitHub marketplace

After this change is on `main`:

```bash
codex plugin marketplace add stadeuk85/agentfactory-business-plugins
```

Then open the Plugins Directory in a supported ChatGPT desktop/Codex surface,
select **AgentFactory Business Plugins**, and install **Replica Codex**.

## Workflow

```text
recon -> architect -> design -> build -> backend -> test -> diff
      -> entrepreneur -> brand -> launch -> deploy
```

Use `$replica` when you want Codex to coordinate the whole sequence.

## Clean-room rules

Replica reconstructs product functionality and UX patterns. It does not copy
source code, proprietary assets, private APIs, trademarks, licensed content,
or data the target owns. Research uses public sources and the user's own
authorised account only.

The reference screenshots and research artefacts belong in the project's
`replica/` planning folder and are not shipped with the rebuilt product.

## Validation

Run:

```bash
python3 -m unittest discover -s tests -v
```

## Origin and licence

The original Replica pack is by Jake Schincariol:
https://github.com/Jakeschincariol/replica-skill

The original code is MIT licensed. See `LICENSE` and `NOTICE.md`.
This port adds OpenAI/Codex packaging, an orchestrator skill, evidence and
stage-gate conventions, and layout adaptations needed by the OpenAI plugin
format.
