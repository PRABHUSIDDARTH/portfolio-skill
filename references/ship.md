# Build, ship and verify

Read when setting up the project and before reporting it done.

## Architecture

### Default stack

New projects use Astro with static output, so every page ships its text as HTML. Plain CSS with custom properties. Add `gsap` and `lenis` only if the brief asks for motion, `three` only if it uses WebGL, and an interactive island (React or similar) only where something needs state.

If the project already has a stack, keep it and apply the same rules there.

### Structure

```
public/                 favicon.svg, social image, robots.txt, resume.pdf (portfolio)
src/content.ts          all copy and data
src/styles/global.css   tokens, type, layout, responsive, reduced motion
src/layouts/Base.astro  head tags, skip link, nav, footer
src/components/         page sections and optional islands
src/pages/              index, one page per project or feature, 404
api/contact.ts          serverless mail handler, only if there is a form
```

### Pages and head tags

Each page is a real route that loads directly. The base layout takes a title and description per page and writes the canonical URL, Open Graph and social card tags. Set `site` in the Astro config and add `@astrojs/sitemap`. The full search checklist is in [search.md](search.md).

### Contact API (serverless, `api/contact.ts`)

Requirements:
- POST only (405 otherwise), `Cache-Control: no-store`.
- Honeypot field (e.g. hidden `website`): if filled, return 200 and drop.
- Trim and length-limit every field; validate email with a simple regex; minimum message length.
- Strip `\r\n` from anything used in headers/subject (header injection); HTML-escape anything in the HTML body.
- `replyTo` = sender; `from` = your SMTP user.
- Best-effort rate limit per IP (e.g. 3 per 10 min via in-memory Map, IP from `x-forwarded-for`).
- If SMTP env vars are missing, return 503 with a friendly "email me directly" message; the UI must show the email as fallback.
- Env vars: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `CONTACT_TO`. Provide `.env.example`. Never commit secrets.
- Frontend form: idle/sending/sent/error states, `aria-live="polite"` status, disabled submit while sending, labels on every input.

### Deployment

Vercel and Netlify both serve Astro's static output without rewrites. A root `api/` folder works as functions on Vercel; Netlify needs the handler in its own functions folder. In portfolio mode the resume lives at `public/resume.pdf` and every resume button links there with `download`.

## Accessibility Requirements

- Skip link to `#main`; landmarks (`header`, `nav`, `main`, `footer`); one `h1` per route; `aria-labelledby` on sections.
- Visible `:focus-visible` outline in the accent color; `::selection` themed.
- Filters are buttons with `aria-pressed`; lists with `role="list"` if styled.
- All interactive demos keyboard operable with labels.
- Contrast AA for body text (watch muted grays on tinted backgrounds and text over shaders).
- `@media (prefers-reduced-motion: reduce) { *,*::before,*::after { animation-duration:.001ms !important; transition-duration:.001ms !important } }` plus JS gates.
- Images: meaningful `alt`, decorative ones `alt=""` / `aria-hidden`.



## Verification Checklist

Run and fix before reporting:
- [ ] `astro check` or `tsc --noEmit` (or the project's lint) passes with zero errors.
- [ ] Production build succeeds; preview the built site, not just the dev server.
- [ ] Browser check at ~1440px and ~390px (Playwright/screenshots if available): every page, including 404.
- [ ] No horizontal scroll at 360px; no text clipped by masks (check descenders: `padding-bottom` on masks).
- [ ] Reduced motion emulated: everything visible, no pinned traps, statement fully opaque.
- [ ] Keyboard only: skip link, nav, menu (Escape), filters, demos, form all reachable with visible focus.
- [ ] Direct load and refresh work on every route; back/forward and hash links work.
- [ ] Console is clean (no errors, no React key warnings, no WebGL context leaks after navigating several times).
- [ ] Contact: validation errors show; honeypot works; missing SMTP shows fallback; with SMTP set, mail arrives.
- [ ] Meta: each page has its own title, description and social tags; favicon; resume downloads.
- [ ] Every fact on the site traces to provided material.
- [ ] Lighthouse (if available): performance and accessibility 90+ on desktop; fix large regressions on mobile.



## Final Report to the User

Keep it short: the art direction in 1-2 sentences, the pages, how to edit content (`src/content.ts`), how to run/build/deploy, required environment variables, what was verified (build, widths, reduced motion, keyboard) and anything not verified.
