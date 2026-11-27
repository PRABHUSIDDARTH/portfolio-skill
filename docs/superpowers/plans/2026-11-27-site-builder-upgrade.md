# Site Builder Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn portfolio-skill into one skill that builds a portfolio or a flagship product site from a short interview, with SEO/AEO/GEO built in.

**Architecture:** A short `SKILL.md` routes to focused files under `references/`. `KICKOFF.md` is a paste-ready prompt for agents without skill support. A stdlib Python script checks structure and links.

**Tech Stack:** Markdown (Agent Skills format), Python 3 stdlib, Astro (static output) for new sites.

**Spec:** docs/superpowers/specs/2026-11-27-site-builder-upgrade-design.md

## Global Constraints

- Skill name stays `portfolio-skill`; frontmatter has `name` and `description`.
- At most 5 interview questions, one at a time, answered ones skipped.
- A design brief is approved before any UI code.
- New projects default to Astro with static output; an existing stack is kept.
- Main text of every page is readable without JavaScript.
- No invented metrics, testimonials, reviews or customers; no promise of ranking or AI citation.
- `llms.txt` is optional and labelled as not used by Google Search.
- JSON-LD only matches visible content.
- Examples are generic; none use the owner's projects.
- Work on branch `feat/site-builder-upgrade`; open a pull request; never push to `main`.

## Review Focus

- Two users with different answers get look-alike sites: the briefs must differ in palette, type and layout (Task 4). The current example accent and fixed motion catalogue push toward sameness (Task 1).
- User has no real material: sections without proof are omitted, not filled (Task 2).
- Agent reads only `SKILL.md` or only the pasted prompt: the approval gate and the no-invention rule appear in both (Task 3).
- Existing client-rendered SPA: the agent adds pre-rendering or says the text is not crawlable without JS, and does not migrate unasked (Task 2).
- User answers "you decide" or dumps everything at once: the agent states its choices and skips answered questions (Task 2).

---

### Task 1: Split the skill

**Files:**
- Create: `scripts/check_skill.py`, `references/portfolio.md`, `references/design-motion.md`, `references/ship.md`
- Modify: `SKILL.md`

**Interfaces:**
- Produces: `python3 scripts/check_skill.py` (exit 0 = pass). Reference names: `interview.md`, `portfolio.md`, `product-site.md`, `design-motion.md`, `search.md`, `ship.md`.

- [ ] **Step 1: Write the check.** It fails unless: `SKILL.md` has frontmatter `name: portfolio-skill` and a non-empty `description`; `SKILL.md` is under 150 lines; all six references and `KICKOFF.md` exist; `SKILL.md` links each reference; every relative Markdown link in the repo resolves.
- [ ] **Step 2: Run it.** Expected: FAIL, listing the missing files.
- [ ] **Step 3: Move content, mapped by current section.** §3, §6, §6A, §8 → `design-motion.md`; §4, §10 portfolio items → `portfolio.md`; §5, §7, §9, §11 → `ship.md`. Replace `#ff4d1c` and the other example token values with placeholders. State that the signature catalogue is a menu, not a default. Replace Vite and the history-router default with Astro static output; keep the contact API requirements unchanged. Section number references become file links.
- [ ] **Step 4: Rewrite `SKILL.md`:** when to use (portfolio or flagship product site; not dashboards, e-commerce, app UIs), mode choice, workflow (interview → brief → approval → build → search → verify → report), quality bar, links to all six references.
- [ ] **Step 5: Commit** `refactor: split skill into references`.

### Task 2: New behaviour

**Files:**
- Create: `references/interview.md`, `references/product-site.md`, `references/search.md`
- Modify: `references/ship.md`

**Interfaces:**
- Consumes: file names from Task 1.
- Produces: brief fields (Concept, Audience, Palette, Type, Layout grammar, Motion, Signature, Texture) and the five questions, both used by `KICKOFF.md`.

- [ ] **Step 1: `interview.md`:** the five questions from the spec verbatim; skip answered ones; "you decide" means state the choice; how each answer changes the brief.
- [ ] **Step 2: `product-site.md`:** hero, problem, demo, proof, pricing only if real, FAQ, docs link; omit any section with no real material.
- [ ] **Step 3: `search.md`:** the spec's SEO, AEO and GEO checklist, each item with how to check it; crawler access is the user's choice; rule for existing SPAs from Review Focus.
- [ ] **Step 4: Add to `ship.md` verification:** `curl` the built page (or read the built HTML) and find the main text; confirm sitemap, robots, canonical.
- [ ] **Step 5: Run** the check. Expected: only `KICKOFF.md` missing. Commit `feat: interview, product site and search references`.

### Task 3: Kickoff prompt and README

**Files:**
- Create: `KICKOFF.md`
- Modify: `README.md`

- [ ] **Step 1: `KICKOFF.md`:** one fenced block that stands alone (repo URL, read `SKILL.md` and references, the five questions, approval gate, no invention, verification). It works if the agent cannot fetch the URL.
- [ ] **Step 2: `README.md`:** both modes; install paths for Claude Code (`~/.claude/skills`), Codex (`~/.codex/skills`), shared (`~/.agents/skills`), Antigravity workspace (`.agents/skills/`) and global (`~/.gemini/config/skills/`); kickoff usage; new layout; state which agents were not tested.
- [ ] **Step 3: Run** `python3 scripts/check_skill.py`. Expected: PASS. Commit `docs: kickoff prompt and install guide`.

### Task 4: Verify and open the pull request

**Files:** none in the repo; test work goes in a scratch folder.

- [ ] **Step 1: Test build** an invented product from `KICKOFF.md` with stated answers. Run `npm run build`; expected exit 0.
- [ ] **Step 2:** Search the built HTML for the headline and FAQ answers; expected present with no JS.
- [ ] **Step 3:** Screenshot at 1440px and 390px; check for overflow and clipped text.
- [ ] **Step 4:** Write a second brief from opposite taste answers; palette, type and layout grammar must all differ.
- [ ] **Step 5:** Fix what fails, rerun the check, push the branch, open the pull request listing what was not tested (Antigravity, Codex).
