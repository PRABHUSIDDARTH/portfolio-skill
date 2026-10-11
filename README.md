# portfolio-skill

An agent skill that turns a resume, a few repos and some links into a personal portfolio site that doesn't look like every other AI-generated portfolio.

Drop [`SKILL.md`](SKILL.md) into any coding agent that supports skills (Codex, Claude Code, ByteAsk, or anything that reads `SKILL.md` files) and ask it to build or redesign a portfolio. The skill gives the agent a working method: pick an art direction for the specific person, write a design brief before touching UI code, build on a single content module, add motion with a purpose, and verify the result in a real browser before calling it done.

It works for developers, designers, researchers, creatives, founders and students. It isn't meant for company landing pages, dashboards or e-commerce.

## Why this exists

Ask an agent for "a portfolio" and you usually get a centered "Hi, I'm X" hero with a wave emoji, a purple-to-blue gradient, three identical skill cards and a progress bar claiming "Java 90%". This skill rejects that output by name and gives the agent concrete rules to follow instead.

## What the skill covers

| Area | What the agent gets |
| --- | --- |
| Art direction | A mapping from the person's field to candidate visual concepts, a design brief template, and token structure (palette, type voices, rhythm) where only the values change per theme |
| Typography and layout | Font pairing rules, fluid `clamp()` scales, section rhythm, texture options |
| Content | Information architecture for home, case-study and 404 pages; copy rules; a single `src/content.ts` module so components never hard-code biography text |
| Architecture | Default Vite + React + TypeScript stack, file layout, a small history router with page transitions, per-route SEO |
| Contact form | A serverless `api/contact.ts` spec with honeypot, header-injection protection, rate limiting and an SMTP-missing fallback |
| Motion | Lenis + GSAP smooth scroll, masked reveals, split text, a catalog of signature moments, optional WebGL backgrounds with quality tiers |
| Reference patterns | Notes on how award juries judge portfolios, archetype references, and a 3D performance checklist |
| Accessibility and responsive | Skip links, landmarks, focus styles, reduced-motion handling, 360px to ultrawide breakpoints |
| Verification | A pre-ship checklist: type check, production build, browser checks at ~1440px and ~390px, keyboard-only pass, console, meta tags, Lighthouse |

Nothing in the skill fixes a color, font or layout. Every concrete value is an example of a pattern, and user-provided brand choices always win.

## Install

Copy the skill folder into your agent's skills directory. The directory name should match the skill name, `portfolio-skill`.

```bash
git clone https://github.com/PRABHUSIDDARTH/portfolio-skill.git

# Codex
cp -r portfolio-skill ~/.codex/skills/portfolio-skill

# Claude Code
cp -r portfolio-skill ~/.claude/skills/portfolio-skill

# Agents that read the shared ~/.agents/skills directory
cp -r portfolio-skill ~/.agents/skills/portfolio-skill
```

Check your agent's documentation if it uses a different location. Some agents also pick up skills placed inside a project, for example `.agents/skills/` or `.claude/skills/` at the repo root.

## Usage

Start a session in an empty folder (or an existing site's repo) and describe what you want. The skill triggers on requests to create, redesign or substantially upgrade a personal portfolio.

```text
Build my portfolio. My resume is in ./resume.pdf and my GitHub is github.com/<you>.
I'm a backend engineer applying for infra roles. Flagship projects: <repo-a>, <repo-b>.
```

Give it as much real material as you can: resume, project READMEs, links, an old site. The skill tells the agent to use only facts it can trace back to what you provided, so thin input produces a thinner site rather than invented metrics.

If you don't state a visual preference, the agent picks a direction itself and tells you which one and why.

## What you end up with

With the default stack, a typical build looks like this:

```text
index.html                  fonts, base meta/OG, noscript fallback
public/                     favicon, resume.pdf, OG image
src/content.ts              all copy and data
src/index.css               tokens, type, layout, responsive, reduced motion
src/lib/                    smooth scroll, motion helpers, router
src/components/             nav, menu, cursor, footer/contact, case-study shell
src/pages/                  home, one page per flagship project, 404
api/contact.ts              serverless mail handler
vercel.json                 SPA rewrites
```

To update the site later, edit `src/content.ts`. The contact form needs `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` and `CONTACT_TO`; without them it falls back to showing your email address.

If your repo already uses Next.js, Astro, SvelteKit or plain HTML, the agent keeps that stack and adapts the patterns.

## Repository layout

```text
SKILL.md    the skill itself (frontmatter + instructions)
README.md   this file
```

## Contributing

Issues and pull requests are welcome. Useful contributions include new archetype directions, signature motion patterns that hold up on mobile, stack-specific notes (Next.js, Astro, SvelteKit), and fixes to anything in the verification checklist that turns out to be wrong in practice. Keep additions as patterns rather than fixed values so the skill doesn't drift toward one house style.
