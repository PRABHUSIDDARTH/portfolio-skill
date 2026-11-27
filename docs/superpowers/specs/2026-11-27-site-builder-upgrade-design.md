# Design: upgrade portfolio-skill (draft, awaiting approval)

## Intent
One skill that any coding agent can follow to build a personal portfolio or a flagship
product site from the user's own taste and idea, with SEO/AEO/GEO built in.
Audience: other people using their own agents.

## Goals
- Ask a few questions, then build. Never ask what the user's files already answer.
- Two modes: portfolio, flagship product site.
- Pages readable without JavaScript.
- Works as a skill (Claude Code, Codex, Antigravity) or as a pasted prompt.

## Non-goals and anti-goals
- No dashboards, e-commerce or app UIs.
- No promise of search ranking or AI citation.
- No invented metrics, testimonials, reviews or customers.
- Failure: two different users get sites that look alike.

## Approaches
- A. Upgrade the existing repo. One link, existing work kept; name undersells product sites.
- B. New repo. Cleaner name; two skills to maintain.
- C. Several skills. Modular; harder to install.
Picked by the author: A.

## Changes
    SKILL.md              short entry point: mode, interview, workflow, quality bar
    references/interview.md      the questions and how answers map to design choices
    references/portfolio.md      portfolio structure
    references/product-site.md   hero, problem, demo, proof, pricing if real, FAQ, docs link
    references/design-motion.md  existing art direction, type, motion, WebGL material
    references/search.md         SEO / AEO / GEO checklist
    references/ship.md           contact form, deploy, verification
    KICKOFF.md            paste-ready prompt for agents without skill support
    README.md             install paths incl. Antigravity, usage

## Interview (at most 5, one at a time, skipped if already answered)
1. Portfolio or product site, and the one action a visitor should take?
2. Who visits?
3. Two or three sites you like and one you hate, and why?
4. What real material exists (resume, repo, screenshots, numbers)?
5. How bold: quiet, expressive, or experimental?
Then the agent writes a design brief and waits for approval before UI code.

## Search checklist
- SEO: pre-rendered HTML, titles, descriptions, canonical, sitemap, robots, social image,
  internal links, performance.
- AEO: direct answers and a real FAQ in visible text.
- GEO: consistent name and facts across site and profiles; crawler access is the user's choice.
- JSON-LD only where it matches visible content. llms.txt optional and labelled as not used
  by Google Search.

## Decisions (author of this draft; correct any)
- Keep the repo name `portfolio-skill`.
- New projects default to Astro (static output). An existing stack is kept.
- Work goes on a branch with a pull request; nothing lands on main without the owner.

## Verification
- Frontmatter and relative links checked by script; every reference file reachable from SKILL.md.
- One test build of an invented product from KICKOFF.md in a scratch folder: build passes,
  main text present in raw HTML, screenshots at desktop and phone widths.
- Antigravity and Codex cannot be run here; the owner tests those.

## Left to the builder
Wording, file split details, checklist order.
