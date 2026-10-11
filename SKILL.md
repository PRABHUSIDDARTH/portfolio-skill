---
name: portfolio-skill
description: Design and build professional, award-level personal portfolio websites (developer, designer, researcher, creative, founder, student) with a bespoke art direction chosen for the person, real content, choreographed motion, case-study pages, a working contact form, SEO, accessibility, and deployment. Use when the user asks to create, redesign, or substantially upgrade a personal portfolio or personal-brand site. Not for generic company landing pages, dashboards, or e-commerce.
metadata:
  short-description: Build award-level personal portfolio sites
---

# Portfolio Skill

Build a portfolio that a hiring manager, recruiter, or client remembers after closing the tab: one confident visual idea, specific copy, motion with a reason, and engineering that holds up when someone opens DevTools.

The theme is chosen per person. Nothing here fixes colors, fonts, or layout style. Every concrete value in this file is an example of the *pattern*, not a default to copy.

---

## 1. Quality Bar (check all before finishing)

1. **One art direction, executed consistently.** A named concept drives type, color, layout, motion, and copy tone. Never mix unrelated styles (glass + neon + brutalism + gradients) on one site.
2. **Real, specific content.** Every claim comes from the user's resume, repos, profiles, or messages. Concrete numbers, stack names, roles, dates. No lorem ipsum, no invented metrics, no "passionate developer who loves to code".
3. **The work is the hero.** Top 2-4 projects get the most space and ideally their own case-study page with something interactive. Everything else lives in a scannable, filterable index.
4. **Typography carries the design.** Expressive display face + readable text face + optional mono/utility face. Fluid `clamp()` sizes. Inter, Roboto, Arial, or system stacks are never the display voice.
5. **Motion is choreographed, not sprinkled.** An intro, scroll reveals, and 1-2 signature moments. Everything respects `prefers-reduced-motion` and degrades cleanly.
6. **Works everywhere.** 360px to ultrawide, keyboard operable, WCAG AA contrast, fast first paint, fully readable without WebGL or JS animation.
7. **Ships.** Zero type errors, production build passes, per-route meta/OG tags, resume link, contact path that delivers, deploy config.

---

## 2. Workflow

1. **Gather material.** Read everything provided: resume PDF/DOCX, existing site, READMEs, GitHub data, notes. Ask only for missing essentials (name, role, target audience, 2-4 flagship projects, links, visual preference). If no preference is given, choose a direction yourself and say which one and why.
2. **Pick the archetype and ambition level** (Section 6A.2) that fits the person and timeline, then **write a design brief** (Section 3) before any UI code.
3. **Build the foundation** (Section 5): content module, tokens, type, router, smooth scroll.
4. **Compose pages in a presentable order:** content -> tokens/type -> nav/footer -> hero -> flagships -> work index -> about/capabilities/timeline -> contact -> case-study pages -> 404. Then motion (Section 6). WebGL and signature effects last.
5. **Verify** (Section 9) in a real browser at ~1440px and ~390px. Never declare done from reading code alone.

If the repo already uses a stack (Next.js, Astro, SvelteKit, plain HTML), keep it. All patterns below translate.

---

## 3. Art Direction

### 3.1 Derive the theme from the person

Ask: who will view this, what should they feel in 5 seconds, what does this person's work look like? Map that to a concept. User-specified brand colors, fonts, or themes always win.

| Person / signal | Example directions (pick one, or invent) |
| --- | --- |
| Backend / systems / infra | Editorial paper + ink; blueprint/technical drawing; terminal brutalism; Swiss grid with data-viz accents |
| Frontend / creative dev | Bold kinetic type; WebGL-led immersive; playful sticker/zine; high-contrast monochrome with one neon |
| Product / UX designer | Calm gallery whitespace; warm studio (cream, terracotta, soft serif); case-study magazine |
| ML / research / data | Lab notebook (grid paper, mono annotations); scientific journal; dark observatory with plotted lines |
| Mobile developer | Device-forward showcase; soft tactile surfaces; app-store polish with live phone mockups |
| Photographer / artist | Image-first full-bleed; minimal chrome; dark cinema; contact-sheet grid |
| Founder / generalist | Confident editorial; manifesto typography; metrics-led credibility |
| Student / early career | Clean, energetic, honest; emphasize projects and learning path over job titles |

Avoid defaults that read as AI-generated: purple-to-blue gradients on white, generic glassmorphism cards, centered hero with "Hi, I'm X" + wave emoji, three equal feature cards, stock 3D blobs.

### 3.2 Design brief template (write this first)

```
Concept:        <name + one sentence of intent>
Audience:       <who, what they must take away>
Palette:        bg, bg-2, fg, fg-2, muted, line, accent (+ per-project accents if used)
Type:           display / text / mono (with fallbacks), scale ratio
Layout grammar: grid, gutters, section rhythm, rules/borders vs cards
Motion:         personality (crisp/elastic/slow/mechanical), main ease, durations
Signature:      the 1-2 moments people will remember
Texture:        grain / grid lines / none / shader
```

### 3.3 Tokens (structure is fixed, values are per-theme)

```css
:root {
  /* palette: replace values per theme */
  --bg: #eeeae2;  --bg-2: #e5e0d5;
  --fg: #121210;  --fg-2: #2a2925;
  --muted: #6d695f;
  --line: rgba(18,18,16,.14);
  --accent: #ff4d1c;
  /* type voices */
  --display: 'Instrument Serif', 'Times New Roman', serif;
  --text: 'Geist', 'Helvetica Neue', sans-serif;
  --mono: 'Geist Mono', ui-monospace, monospace;
  /* rhythm */
  --gutter: clamp(1.1rem, 3.2vw, 2.75rem);
  --ease: cubic-bezier(.16, 1, .3, 1);
  /* page-level aliases so case-study pages can re-theme by overriding these */
  --page-bg: var(--bg); --page-fg: var(--fg); --page-muted: var(--muted);
  --page-line: var(--line); --page-accent: var(--accent);
}
```

Components only reference `--page-*`. A case-study page sets new `--page-*` values on its `<main>` and the whole UI (buttons, rules, cursor, selection) re-themes for free.

### 3.4 Typography rules

- Pair with contrast: serif display + grotesk text, or heavy grotesk display + mono, or condensed display + humanist text. Load via Google Fonts or self-hosted woff2 with `display=swap` and `preconnect`.
- Fluid scale with clamp, e.g. `h-xl: clamp(3.6rem, 14.5vw, 15rem)`, `h-lg: clamp(2.8rem, 8vw, 8.5rem)`, `h-md: clamp(2.1rem, 5vw, 4.6rem)`, `lede: clamp(1.05rem, 1.45vw, 1.3rem)`.
- Display: tight leading (0.85-0.95) and negative tracking (-0.02 to -0.04em). Body: 1.5-1.65 leading, `max-width` 38-62ch.
- Metadata in small uppercase mono with slight tracking ("(02) Selected work", "2024 - Present").
- Use italics or a weight shift on one word in a headline for voice ("The ones I'd *demo first.*").
- `font-variant-numeric: tabular-nums` for counters and stats.

### 3.5 Layout grammar

- Full-bleed hero (`min-height: 100svh`), content anchored bottom-left or across a grid, not dead-centered.
- Section headers as a thin rule with numbered mono label left and context right.
- Prefer hairline rules and grids over drop-shadowed cards (unless the concept is tactile/soft).
- Vary section rhythm: big statement, dense index, horizontal reel, two-column split. Never six identical sections in a row.
- Consistent `--gutter` everywhere; section padding `clamp(5rem, 13vw, 11rem)`.

### 3.6 Texture options

Film grain (SVG feTurbulence data-URI on `body::after`, opacity 0.04-0.08, `pointer-events:none`), blueprint grid lines, subtle radial gradients, or a WebGL field. Pick one; do not stack.

---

## 4. Content Strategy

### 4.1 Information architecture

Home (single scroll):
1. **Hero:** name, one-line positioning, 1-2 sentence lede, primary CTA (see work) + secondary (resume / contact), small meta row (role, focus areas, location, availability).
2. **Statement / About:** 2-4 sentences in the person's voice, plus 3-4 stats that are true (projects shipped, years, users, stars, CGPA if a student).
3. **Flagships:** 2-4 hero projects, large cards, each linking to a case-study page.
4. **Work index:** every other project as rows (number, name, one-line blurb, stack, year/link), filterable by kind.
5. **Capabilities:** grouped skills (e.g. Backend, Mobile, AI, Tooling), only things they can defend in an interview.
6. **Path / timeline:** education, roles, notable achievements.
7. **Contact:** big CTA headline, email, form, social links, resume download.

Case-study page per flagship: themed hero (name, tagline, role, stack, links), problem, what was built, an **interactive demo** (simulator, playground, live mockup, architecture diagram you can hover), key decisions/tradeoffs, metrics/outcomes, then a "next project" handoff and contact.

404 page in the same voice.

### 4.2 Copy rules

- First person, plain, specific. Lead with what was built and why it matters, then how.
- Good: "Connect your own AWS, GCP and Azure accounts and their free tiers act as one disk." Bad: "A revolutionary cloud solution leveraging cutting-edge technology."
- Banned filler: passionate, cutting-edge, leverage, seamless, robust, innovative, journey, delve, "I love to code".
- Every metric is sourced or omitted. Never fabricate.
- Microcopy has personality but stays clear ("Lost in the reel." on 404, "Scroll to pan" hints).

### 4.3 Single content module

All copy and data lives in `src/content.ts`. Components never hard-code biography text.

```ts
export const PROFILE = { name, role, location, email, github, linkedin, resume: '/resume.pdf', statement };
export type Metric = { value: string; label: string };
export type Flagship = {
  slug: string; path: string; index: string; name: string; kicker: string; tagline: string;
  summary: string; role: string; stack: string[]; metrics: Metric[]; repo: string;
  accent: string; bg: string; fg: string;          // per-project theme
};
export const FLAGSHIPS: Flagship[] = [ /* 2-4 */ ];
export type WorkKind = 'Systems' | 'AI' | 'Mobile' | 'Web'; // adapt to the person
export const WORKS: { name: string; blurb: string; stack: string[]; kind: WorkKind; year: string; href: string; route?: string }[] = [];
export const CAPABILITIES: { title: string; items: string[] }[] = [];
export const PATH: { when: string; what: string; detail: string }[] = [];
export const STATS: Metric[] = [];
```

---

## 5. Architecture

### 5.1 Default stack

Vite + React + TypeScript; plain CSS with custom properties (Tailwind allowed if the team prefers); `gsap` + `@gsap/react` (ScrollTrigger); `lenis` for smooth scroll; `three` only if the direction uses WebGL; `nodemailer` for contact; deploy on Vercel/Netlify.

### 5.2 Structure

```
index.html                 fonts, base meta/OG, noscript fallback text
public/                    favicon.svg, resume.pdf, og-image
src/content.ts             all copy and data
src/index.css              tokens, type, layout, components, responsive, reduced-motion
src/lib/smooth.ts          Lenis + GSAP ticker, reduced-motion flag, scroll velocity
src/lib/motion.tsx         useReveals, useHeroIntro, <Split>, useMeta
src/lib/router.tsx         history router + curtain transition + <Link>
src/components/Chrome.tsx  Nav, mobile Menu, Cursor, Preloader, Footer/Contact
src/components/Field.tsx   optional WebGL hero background
src/components/CaseShell.tsx shared case-study scaffold
src/pages/*.tsx            Home, one page per flagship, NotFound
api/contact.ts             serverless mail handler
vercel.json                SPA rewrites
```

### 5.3 Routing

A tiny history router is enough for a portfolio and lets you own transitions:
- `normalizePath` (strip trailing slash, lowercase).
- `navigate(to)`: same path + hash -> smooth-scroll to anchor; different path -> play curtain, swap page while covered, scroll to top, then reveal.
- Listen to `popstate`; call `ScrollTrigger.refresh()` after each route change; handle pending `#hash` after swap.
- `<Link>`: external (`http`, `mailto`) renders a plain anchor with `target="_blank" rel="noopener noreferrer"`; internal intercepts click unless `metaKey/ctrlKey/shiftKey` or non-left button, so new-tab still works.
- Next.js/Astro: use their router and implement the curtain in a layout/transition hook instead.

### 5.4 Per-route SEO

`useMeta(title, description, themeColor)` updates `document.title`, description, `og:*`, `twitter:*`, `theme-color`, and canonical on each route. `index.html` contains complete defaults plus a `<noscript>` text summary. Add `summary_large_image` Twitter card and an OG image if possible. Consider JSON-LD `Person` schema.

### 5.5 Contact API (serverless, `api/contact.ts`)

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

### 5.6 Deployment

Vercel `vercel.json`:
```json
{ "cleanUrls": true,
  "rewrites": [{ "source": "/((?!api/|assets/|.*\\..*).*)", "destination": "/" }] }
```
Netlify: `/* /index.html 200` in `_redirects`. Resume lives at `public/resume.pdf`; every resume button links there with `download`.

---

## 6. Motion System

### 6.1 Principles

- One house ease (e.g. `expo.out` / `cubic-bezier(.16,1,.3,1)`), durations 0.6-1.4s for reveals, 0.3-0.6s for hovers.
- Animate `transform`, `opacity`, `clip-path` only. Never animate layout properties.
- Masked reveals (text rising out of an `overflow:hidden` box) look premium; plain fades look cheap.
- Choreograph: hero intro waits for the preloader/curtain to clear (shared `intro.delay`).
- Every effect is gated by `prefersReducedMotion`; pointer effects also by `(pointer: coarse)`.
- Use `gsap.from()` inside `useGSAP` so content is visible if JS fails. Never leave content at `opacity:0` in CSS.

### 6.2 Smooth scroll (`src/lib/smooth.ts`)

```ts
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

export const prefersReducedMotion =
  typeof window !== 'undefined' && matchMedia('(prefers-reduced-motion: reduce)').matches;
export const scrollState = { velocity: 0, scroll: 0 }; // read by WebGL
export const intro = { delay: 0 };                     // hero waits for preloader/curtain

let lenis: Lenis | null = null;
export function initSmoothScroll() {
  if (lenis || prefersReducedMotion) return;
  lenis = new Lenis({ lerp: 0.085, smoothWheel: true });
  lenis.on('scroll', (l: Lenis) => { scrollState.velocity = l.velocity; scrollState.scroll = l.scroll; ScrollTrigger.update(); });
  gsap.ticker.add((t) => lenis?.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
}
export const scrollToTop = () => (lenis ? lenis.scrollTo(0, { immediate: true, force: true }) : scrollTo(0, 0));
export function scrollToTarget(target: string | HTMLElement) {
  const el = typeof target === 'string' ? document.querySelector<HTMLElement>(target) : target;
  if (!el) return;
  if (lenis) lenis.scrollTo(el, { duration: 1.6, easing: (t) => 1 - Math.pow(1 - t, 4) });
  else el.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth' });
}
export const stopScroll = () => lenis?.stop();
export const startScroll = () => lenis?.start();
export { gsap, ScrollTrigger };
```
CSS: `html.lenis, html.lenis body { height:auto } .lenis.lenis-smooth { scroll-behavior:auto !important } .lenis.lenis-stopped { overflow:hidden }`.

### 6.3 Reveals and split text (`src/lib/motion.tsx`)

```tsx
export function useReveals(scope: RefObject<HTMLElement | null>) {
  useGSAP(() => {
    if (prefersReducedMotion) return;
    gsap.utils.toArray<HTMLElement>('[data-reveal]').forEach((el) =>
      gsap.from(el, { y: 44, autoAlpha: 0, duration: 1.2, ease: 'expo.out',
        delay: parseFloat(el.dataset.delay || '0'),
        scrollTrigger: { trigger: el, start: 'top 92%', once: true } }));
    gsap.utils.toArray<HTMLElement>('[data-split]').forEach((el) =>
      gsap.from(el.querySelectorAll('.w > span'), { yPercent: 118, duration: 1.15, ease: 'expo.out', stagger: 0.045,
        scrollTrigger: { trigger: el, start: 'top 90%', once: true } }));
  }, { scope });
}

export function useHeroIntro(scope: RefObject<HTMLElement | null>) {
  useGSAP(() => {
    if (prefersReducedMotion) return;
    gsap.timeline({ delay: intro.delay })
      .from('[data-hero-line] > span', { yPercent: 120, duration: 1.4, ease: 'expo.out', stagger: 0.08 })
      .from('[data-hero-fade]', { autoAlpha: 0, y: 24, duration: 1.1, ease: 'expo.out', stagger: 0.06 }, '-=1.0');
    intro.delay = 0.1;
  }, { scope });
}

// Word-masked heading. Screen readers read aria-label; per-word spans are hidden.
export function Split({ text, as: Tag = 'h2', className }: { text: string; as?: 'h1'|'h2'|'h3'|'p'; className?: string }) {
  const words = text.split(' ');
  return (
    <Tag className={className} data-split="" aria-label={text}>
      {words.map((w, i) => (<Fragment key={i}><span className="w" aria-hidden="true"><span>{w}</span></span>{i < words.length - 1 ? ' ' : null}</Fragment>))}
    </Tag>
  );
}
```
CSS: `.w{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.08em;margin-bottom:-.08em} .w>span{display:inline-block} [data-hero-line]{display:block;overflow:hidden} [data-hero-line]>span{display:inline-block}`.

### 6.4 Signature moment catalog (pick 1-2 that fit the concept)

- **Preloader counter:** 000->100 counter + progress bar, real readiness = `document.fonts.ready` raced against a ~1.2s cap; exits with `clipPath: inset(0 0 100% 0)`; sets `intro.delay` so the hero starts as it lifts; stops scroll while visible. Skip entirely under reduced motion.
- **Route curtain:** fixed full-screen layer, `clip-path` wipes in from bottom (0.8s expo.inOut), destination name rises in a mask, page swaps while covered, curtain wipes out the top. Curtain color = destination project's accent. Guard with a `busy` ref.
- **Pinned horizontal reel:** inside `gsap.matchMedia('(min-width:1001px) and (prefers-reduced-motion:no-preference)')`, pin the section and tween the track `x` to `-(scrollWidth - innerWidth)` with `scrub: 0.6`, `invalidateOnRefresh: true`, `end: () => '+=' + distance()`. Parallax inner visuals with `containerAnimation`. Add a progress hairline. Below breakpoint: vertical stack, `transform:none !important`.
- **Scrubbed statement:** split statement into words at `opacity:.16`, scrub to 1 with stagger from `top 80%` to `bottom 45%`. Reduced motion: CSS sets words to opacity 1.
- **Lerped cursor:** small accent dot with `gsap.quickTo` x/y (0.45s power3); grows into a labeled circle over `[data-cursor="Open"]`. Disabled on coarse pointers and reduced motion. Keep native cursor accessible.
- **Mobile menu:** full-screen overlay revealed by clip-path, big staggered links, stops scroll, Escape closes, closes on route change, `aria-expanded`/`aria-controls` on the button.
- **Hover language:** pill buttons with a fill sliding up from below (`::before translateY(101%) -> 0`), underline links scaling from right to left, index rows with a full-width fill wiping up and the name nudging right, arrows translating diagonally.
- **Nav with `mix-blend-mode: difference`:** stays legible over any section color.
- **Interactive case-study demo:** small, honest re-implementation of the project's core logic (a router score simulator, an SDK playground, a themed phone mockup, a sortable benchmark table). Keyboard operable. Label it illustrative if simplified.

### 6.5 WebGL background (optional, `Field.tsx`)

Use only if the concept benefits (generative/tech/immersive). Pattern: full-screen quad with a fragment shader (fbm noise contours, gradient mesh, particles), uniforms for time, scroll velocity, mouse, resolution, and theme colors so it re-themes per page.

Non-negotiable lifecycle:
- `try { new WebGLRenderer({ alpha:true, antialias:false, powerPreference:'high-performance' }) } catch { return }`: layout must be complete without it.
- Pixel ratio `min(devicePixelRatio, lowTier ? 1 : 1.5)`; low tier = `hardwareConcurrency <= 4` or coarse pointer.
- `ResizeObserver` for size; `IntersectionObserver` + `visibilitychange` to stop the rAF loop when not visible.
- Lerp mouse and velocity uniforms for smoothness.
- Reduced motion: render one static frame.
- Cleanup: cancel rAF, disconnect observers, remove listeners, dispose material/geometry/renderer, remove canvas.
- Container `position:absolute; inset:0; pointer-events:none; aria-hidden="true"`; keep it low-contrast so text stays readable.

---

## 6A. Research-Backed Patterns From Award-Winning Portfolios

Distilled from a study of Awwwards SOTD/SOTY and FWA-recognized developer portfolios. Use these as references for *techniques and ambition*, never as templates to clone. Verify URLs are live before citing them to the user.

### 6A.1 How award juries judge (design toward this)

Awwwards scores roughly: **Design 40%, Usability 30%, Creativity 20%, Content 10%**. Its separate Developer Award weighs web performance, code quality, responsiveness, and the technical execution of rendering systems. Lesson: a cinematic site with frame drops or confusing navigation scores badly on both. Spectacle never excuses broken usability or slow loads.

### 6A.2 Reference library by archetype

Pick the archetype that fits the person, then study 1-2 references for technique.

| Archetype | References | What to learn |
| --- | --- | --- |
| Editorial 2D motion + typography | jesperlandberg.com, dennissnellenberg.com, leoparpeix.com | Type and spacing perfection, staggered masked reveals, horizontal scroll, seamless index-to-project transitions, micro-interactions |
| Continuous "tracking shot" navigation | aristidebenoist.com | Routes never visually break; outgoing and incoming states animate together |
| Tactile / scroll-velocity WebGL | robinmastromarino.com | Images rendered in WebGL that stretch and warp with scroll/drag speed |
| Gamified 3D world | bruno-simon.com, thibault-introvigne.com, jreyes-mc-portfolio.com | Physics sandbox, hidden collectibles that unlock bio details, scroll-navigated circuits |
| Narrative 3D scene | henryheffernan.com, jordan-breton.com, bilal.show, sebastien-lempens.com, worawork.vercel.app | A baked Blender scene; fixed point-to-point camera moves; guided story path; cozy stylized rooms with clickable objects |
| High-fidelity sci-fi / WebGPU | samsy.ninja | Emissive materials, holographic UI, volumetric lighting on WebGPU |
| Minimal, content-first developer | leerob.io, kentcdodds.com, brittanychiang.com | Speed, clarity, writing, clean information architecture (right choice for many engineers) |

Ambition must match the person and the timeline. A full 3D world takes weeks of Blender and optimization work and suits creative technologists. Most engineers are better served by the editorial-motion archetype done perfectly, plus one WebGL accent.

### 6A.3 Techniques worth stealing

- **Inertial smooth scroll:** `position += (target - position) * ease` every frame (Lenis `lerp` ~0.07-0.1). This lerp is what makes a site feel "smooth". Feed scroll velocity to other systems (shaders, skew, displacement).
- **Seamless route transitions:** keep the outgoing DOM mounted until its exit animation completes, animate the incoming page in (or under a curtain), and destroy the old state only at the end. Animate only `transform`, `opacity`, `clip-path`. With prefetching and client routing there is no white flash between pages.
- **Shared-element handoff:** the clicked project's thumbnail scales and moves into the next page's hero position (FLIP: measure first/last, invert, play; or GSAP Flip plugin).
- **Velocity-driven image distortion:** render key images as textured planes in a WebGL layer synced to DOM positions. A fragment shader takes scroll velocity as a uniform and bends or RGB-shifts edges. Keep real `<img>` elements in the DOM (visually hidden or as fallback) for accessibility and SEO.
- **Shader-on-enter:** images bend or color-shift slightly as they enter the viewport, a subtle post-processing layer CSS can't do.
- **Horizontal pan:** translate vertical scroll into horizontal movement of a track, like a camera panning (pinned ScrollTrigger; see 6.4).
- **DOM over WebGL for text:** never rebuild long text or UI inside a canvas. Layer real HTML over the 3D scene, or use three.js `CSS3DRenderer` to place an HTML/iframe "screen" inside the 3D perspective (Henry Heffernan's retro computer monitor). Text stays crisp, selectable, and accessible.
- **Gamified bio:** turn About details into discoverable objects (collectibles, clickable props). Always provide a plain, accessible fallback path (a "skip to info" or standard page) so recruiters can get facts in 10 seconds.
- **Shared presence (optional):** small, moderated, asynchronous social touches (global counters, short notes left by visitors) make a site feel alive. Moderate user text before rendering. Treat this as scope expansion and ask first.
- **Spatial/UI audio (optional):** only with an explicit mute toggle, off by default or started on first user interaction, never autoplaying with sound.

### 6A.4 3D / WebGL performance pipeline (when using real 3D scenes)

- **Stack:** three.js; React Three Fiber + drei for declarative scenes in React; WebGPU renderer + TSL (Three Shading Language) for advanced work, with a WebGL fallback because WebGPU support is not universal.
- **Assets:** model and bake lighting/shadows in Blender (baked textures look photoreal and cost nothing at runtime); export GLB; compress geometry with **Draco** (or Meshopt); compress textures to **KTX2 / Basis (ETC1S for color, UASTC for normals/detail)**, which stay compressed in GPU memory and prevent mobile crashes. Use `gltf-transform` to automate.
- **Draw calls:** merge static geometry; use `InstancedMesh` for repeated objects (grass, trees, particles). For huge fields, recycle instances around the camera instead of creating more.
- **Frame budget:** pause the render loop when an HTML overlay, project page, or modal covers the canvas, when the canvas is offscreen, and when the tab is hidden. Throttle raycasting to ~30Hz instead of every frame. Rely on frustum culling (keep correct bounding volumes). Limit post-processing.
- **Quality tiers:** detect low-tier devices (coarse pointer, low `hardwareConcurrency`, small screens, optionally a quick FPS probe) and drop to a lower preset: lower DPR, smaller textures, no shadows/DOF/bloom, simpler physics. Preserve the narrative, not pixel fidelity.
- **Loading:** show a meaningful, honest progress loader tied to real asset loading (drei `useProgress` / `LoadingManager`); keep the initial payload small and lazy-load secondary scenes. A 30-second load ruins any amount of spectacle.
- **Accessibility for 3D:** provide keyboard controls and a non-3D route to all content; respect reduced motion by freezing cameras and disabling auto-motion.

## 7. Accessibility Requirements

- Skip link to `#main`; landmarks (`header`, `nav`, `main`, `footer`); one `h1` per route; `aria-labelledby` on sections.
- Visible `:focus-visible` outline in the accent color; `::selection` themed.
- Filters are buttons with `aria-pressed`; lists with `role="list"` if styled.
- All interactive demos keyboard operable with labels.
- Contrast AA for body text (watch muted grays on tinted backgrounds and text over shaders).
- `@media (prefers-reduced-motion: reduce) { *,*::before,*::after { animation-duration:.001ms !important; transition-duration:.001ms !important } }` plus JS gates.
- Images: meaningful `alt`, decorative ones `alt=""` / `aria-hidden`.

---

## 8. Responsive Rules

- Breakpoints around 1000px (tablet: hide desktop nav links, show Menu button, collapse grids to 2 cols, unpin horizontal reel) and 600px (phone: single column, stacked hero footer).
- Use `100svh` not `100vh`. Test long names and long words with `clamp()` sizes at 360px; no horizontal overflow (`overflow-x:hidden` on body is a safety net, not a fix).
- Touch: no hover-only information; cursor hidden on `(pointer: coarse)`.

---

## 9. Verification Checklist

Run and fix before reporting:
- [ ] `tsc --noEmit` (or project lint) passes with zero errors.
- [ ] Production build succeeds; preview the built site, not just the dev server.
- [ ] Browser check at ~1440px and ~390px (Playwright/screenshots if available): hero, reel, index, contact, each case study, 404.
- [ ] No horizontal scroll at 360px; no text clipped by masks (check descenders: `padding-bottom` on masks).
- [ ] Reduced motion emulated: everything visible, no pinned traps, statement fully opaque.
- [ ] Keyboard only: skip link, nav, menu (Escape), filters, demos, form all reachable with visible focus.
- [ ] Direct load and refresh on every deep route works (SPA rewrite); browser back/forward works; hash links scroll correctly after route change.
- [ ] Console is clean (no errors, no React key warnings, no WebGL context leaks after navigating several times).
- [ ] Contact: validation errors show; honeypot works; missing SMTP shows fallback; with SMTP set, mail arrives.
- [ ] Meta: title/description/OG update per route; favicon; resume downloads.
- [ ] Every fact on the site traces to provided material.
- [ ] Lighthouse (if available): performance and accessibility 90+ on desktop; fix large regressions on mobile.

---

## 10. Anti-patterns (reject these)

- Generic templates: centered "Hi, I'm X" hero, gradient blob, three identical skill cards, progress-bar skill percentages ("Java 90%").
- Fake stats, fake testimonials, placeholder projects.
- Scroll-jacking that traps the user or breaks on mobile.
- Animations on every element; fades with no mask; bouncy eases on a serious editorial concept.
- Content hidden in CSS until JS runs; WebGL required to see text.
- Icons and emoji standing in for design; skill logo walls with 40 technologies.
- Hard-coded copy scattered across components; secrets in the repo.
- Adding blogs, CMS, auth, or extra tracking without asking.

---

## 11. Final Report to the User

Keep it short: the art direction in 1-2 sentences, the routes, how to edit content (`src/content.ts`), how to run/build/deploy, required environment variables, what was verified (build, widths, reduced motion, keyboard) and anything not verified.
