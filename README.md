# portfolio-skill

An agent skill that builds a personal portfolio or a flagship product website from your own taste and idea. It asks up to five questions, shows you a design brief, and builds only after you approve it. SEO, AEO and GEO basics are part of the build.

It works for developers, designers, researchers, creatives, founders and students, and for single apps, tools, libraries and services. It isn't meant for dashboards, e-commerce or app interfaces.

## What you get

- A design direction drawn from your answers, not a template
- Only real content: no invented metrics, testimonials or customers
- Pages whose text is readable without JavaScript, with titles, canonical URLs, sitemap, robots.txt and social cards
- A build checked at desktop and phone widths

Nothing here can guarantee search ranking or that an AI assistant will cite your site.

## Install

Clone, then copy the folder into your agent's skills directory.

```bash
git clone https://github.com/PRABHUSIDDARTH/portfolio-skill.git
```

| Agent | Folder to create |
| --- | --- |
| Claude Code | `~/.claude/skills/portfolio-skill` |
| Codex | `~/.codex/skills/portfolio-skill` |
| Shared agents directory | `~/.agents/skills/portfolio-skill` |
| Antigravity, one project | `<project>/.agents/skills/portfolio-skill` |
| Antigravity, all projects | `~/.gemini/config/skills/portfolio-skill` |

```bash
mkdir -p ~/.claude/skills && cp -r portfolio-skill ~/.claude/skills/portfolio-skill
```

Antigravity paths are from its [skills documentation](https://antigravity.google/docs/skills). Check your agent's documentation if a path doesn't work.

**Not yet tested:** the skill has not been run inside Antigravity or Codex. Reports are welcome.

## Use

With the skill installed:

```text
Build a site for my project. The README in this folder describes it.
```

Without skill support, copy the prompt in [KICKOFF.md](KICKOFF.md).

## Repository layout

```text
SKILL.md                    entry point: modes, workflow, quality bar
KICKOFF.md                  paste-ready prompt
references/interview.md     the five questions
references/portfolio.md     portfolio mode and copy rules
references/product-site.md  product site mode
references/design-motion.md design brief, type, layout, motion, WebGL
references/search.md        SEO, AEO, GEO checklist
references/ship.md          stack, contact form, accessibility, verification
scripts/check_skill.py      structure and link check
```

## Contributing

Issues and pull requests are welcome. Useful contributions include new archetype directions, signature motion patterns that hold up on mobile, stack-specific notes (Next.js, Astro, SvelteKit), and fixes to anything in the verification checklist that turns out to be wrong in practice. Run `python3 scripts/check_skill.py` before opening a pull request. Keep additions as patterns rather than fixed values so the skill doesn't drift toward one house style.
