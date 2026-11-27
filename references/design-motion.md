# Design and motion

Read when writing the design brief and building the UI. Used by both modes.

## Art Direction

### Derive the theme from the subject

For a product, derive it from who uses it, what it is for, the objects and language of that world, and the sites the user likes and hates. The table below is for people.

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

### Design brief template (write this first)

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

### Tokens (structure is fixed, values are per-theme)

```css
:root {
  /* palette: every value comes from the approved brief */
  --bg: <color>;  --bg-2: <color>;
  --fg: <color>;  --fg-2: <color>;
  --muted: <color>;
  --line: <color at low alpha>;
  --accent: <color>;
  /* type voices: chosen for this person or product */
  --display: <display face>, <fallbacks>;
  --text: <text face>, <fallbacks>;
  --mono: <mono face>, <fallbacks>;
  /* rhythm */
  --gutter: <from the brief's layout grammar>;
  --ease: <from the brief's motion personality>;
  /* page-level aliases so case-study pages can re-theme by overriding these */
  --page-bg: var(--bg); --page-fg: var(--fg); --page-muted: var(--muted);
  --page-line: var(--line); --page-accent: var(--accent);
}
```

Components only reference `--page-*`. A case-study page sets new `--page-*` values on its `<main>` and the whole UI (buttons, rules, cursor, selection) re-themes for free.

### Typography rules

- Pair with contrast: serif display + grotesk text, or heavy grotesk display + mono, or condensed display + humanist text. Load via Google Fonts or self-hosted woff2 with `display=swap` and `preconnect`.
- Fluid scale with clamp, e.g. `h-xl: clamp(3.6rem, 14.5vw, 15rem)`, `h-lg: clamp(2.8rem, 8vw, 8.5rem)`, `h-md: clamp(2.1rem, 5vw, 4.6rem)`, `lede: clamp(1.05rem, 1.45vw, 1.3rem)`.
- Display: tight leading (0.85-0.95) and negative tracking (-0.02 to -0.04em). Body: 1.5-1.65 leading, `max-width` 38-62ch.
- Metadata in small uppercase mono with slight tracking ("(02) Selected work", "2024 - Present").
- Use italics or a weight shift on one word in a headline for voice ("The ones I'd *demo first.*").
- `font-variant-numeric: tabular-nums` for counters and stats.

### Example: editorial layout

Use the approved brief's Layout grammar and Motion. The rules in this section and the motion values below describe one editorial direction; apply them only if the brief asks for it.

- Full-bleed hero (`min-height: 100svh`), content anchored bottom-left or across a grid, not dead-centered.
- Section headers as a thin rule with numbered mono label left and context right.
- Prefer hairline rules and grids over drop-shadowed cards (unless the concept is tactile/soft).
- Vary section rhythm: big statement, dense index, horizontal reel, two-column split. Never six identical sections in a row.
- Consistent `--gutter` everywhere; section padding `clamp(5rem, 13vw, 11rem)`.

### Texture options

Film grain (SVG feTurbulence data-URI on `body::after`, opacity 0.04-0.08, `pointer-events:none`), blueprint grid lines, subtle radial gradients, or a WebGL field. Pick one; do not stack.



## Motion System

The code examples use React hooks. Without React, run the same GSAP calls from a client `<script>`. Load these libraries only if the brief asks for motion.

### Principles

The brief decides the motion. Accessibility and performance rules here always apply; style choices (ease, durations, masked reveals, preloader) are examples.

- One house ease, from the brief (e.g. `expo.out` / `cubic-bezier(.16,1,.3,1)`), durations 0.6-1.4s for reveals, 0.3-0.6s for hovers.
- Animate `transform`, `opacity`, `clip-path` only. Never animate layout properties.
- Choose the reveal style from the concept: masked reveals, plain fades or none.
- If there is a preloader or curtain, the hero intro waits for the preloader/curtain to clear (shared `intro.delay`).
- Every effect is gated by `prefersReducedMotion`; pointer effects also by `(pointer: coarse)`.
- Use `gsap.from()` inside `useGSAP` so content is visible if JS fails. Never leave content at `opacity:0` in CSS.

### Smooth scroll (`src/lib/smooth.ts`)

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

### Reveals and split text (`src/lib/motion.tsx`)

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

### Signature moment catalog (pick 1-2 that fit the concept)

This is a menu, not a default. Inventing a moment from the subject beats picking one, and quiet sites may need none. If the brief would suit any other person or product, change it.

Astro builds a multi-page site. Page transitions (route curtain, shared-element handoff) need Astro's `<ClientRouter />`, and scripts must set up again on `astro:page-load`. Otherwise skip them.

- **Preloader counter:** 000->100 counter + progress bar, real readiness = `document.fonts.ready` raced against a ~1.2s cap; exits with `clipPath: inset(0 0 100% 0)`; sets `intro.delay` so the hero starts as it lifts; stops scroll while visible. Skip entirely under reduced motion.
- **Route curtain:** fixed full-screen layer, `clip-path` wipes in from bottom (0.8s expo.inOut), destination name rises in a mask, page swaps while covered, curtain wipes out the top. Curtain color = destination project's accent. Guard with a `busy` ref.
- **Pinned horizontal reel:** inside `gsap.matchMedia('(min-width:1001px) and (prefers-reduced-motion:no-preference)')`, pin the section and tween the track `x` to `-(scrollWidth - innerWidth)` with `scrub: 0.6`, `invalidateOnRefresh: true`, `end: () => '+=' + distance()`. Parallax inner visuals with `containerAnimation`. Add a progress hairline. Below breakpoint: vertical stack, `transform:none !important`.
- **Scrubbed statement:** split statement into words at `opacity:.16`, scrub to 1 with stagger from `top 80%` to `bottom 45%`. Reduced motion: CSS sets words to opacity 1.
- **Lerped cursor:** small accent dot with `gsap.quickTo` x/y (0.45s power3); grows into a labeled circle over `[data-cursor="Open"]`. Disabled on coarse pointers and reduced motion. Keep native cursor accessible.
- **Mobile menu:** full-screen overlay revealed by clip-path, big staggered links, stops scroll, Escape closes, closes on route change, `aria-expanded`/`aria-controls` on the button.
- **Hover language:** pill buttons with a fill sliding up from below (`::before translateY(101%) -> 0`), underline links scaling from right to left, index rows with a full-width fill wiping up and the name nudging right, arrows translating diagonally.
- **Nav with `mix-blend-mode: difference`:** stays legible over any section color.
- **Interactive case-study demo:** small, honest re-implementation of the project's core logic (a pricing calculator, an API playground, a themed phone mockup, a sortable benchmark table). Keyboard operable. Label it illustrative if simplified.

### WebGL background (optional, `Field.tsx`)

Use only if the concept benefits (generative/tech/immersive). Pattern: full-screen quad with a fragment shader (fbm noise contours, gradient mesh, particles), uniforms for time, scroll velocity, mouse, resolution, and theme colors so it re-themes per page.

Non-negotiable lifecycle:
- `try { new WebGLRenderer({ alpha:true, antialias:false, powerPreference:'high-performance' }) } catch { return }`: layout must be complete without it.
- Pixel ratio `min(devicePixelRatio, lowTier ? 1 : 1.5)`; low tier = `hardwareConcurrency <= 4` or coarse pointer.
- `ResizeObserver` for size; `IntersectionObserver` + `visibilitychange` to stop the rAF loop when not visible.
- Lerp mouse and velocity uniforms for smoothness.
- Reduced motion: render one static frame.
- Cleanup: cancel rAF, disconnect observers, remove listeners, dispose material/geometry/renderer, remove canvas.
- Container `position:absolute; inset:0; pointer-events:none; aria-hidden="true"`; keep it low-contrast so text stays readable.



## Research-Backed Patterns From Award-Winning Portfolios

Distilled from a study of Awwwards SOTD/SOTY and FWA-recognized developer portfolios. Use these as references for *techniques and ambition*, never as templates to clone. Verify URLs are live before citing them to the user.

### How award juries judge (design toward this)

Awwwards scores roughly: **Design 40%, Usability 30%, Creativity 20%, Content 10%**. Its separate Developer Award weighs web performance, code quality, responsiveness, and the technical execution of rendering systems. Lesson: a cinematic site with frame drops or confusing navigation scores badly on both. Spectacle never excuses broken usability or slow loads.

### Reference library by archetype

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

### Techniques worth stealing

- **Inertial smooth scroll:** `position += (target - position) * ease` every frame (Lenis `lerp` ~0.07-0.1). This lerp is what makes a site feel "smooth". Feed scroll velocity to other systems (shaders, skew, displacement).
- **Seamless route transitions:** keep the outgoing DOM mounted until its exit animation completes, animate the incoming page in (or under a curtain), and destroy the old state only at the end. Animate only `transform`, `opacity`, `clip-path`. With prefetching and client routing there is no white flash between pages.
- **Shared-element handoff:** the clicked project's thumbnail scales and moves into the next page's hero position (FLIP: measure first/last, invert, play; or GSAP Flip plugin).
- **Velocity-driven image distortion:** render key images as textured planes in a WebGL layer synced to DOM positions. A fragment shader takes scroll velocity as a uniform and bends or RGB-shifts edges. Keep real `<img>` elements in the DOM (visually hidden or as fallback) for accessibility and SEO.
- **Shader-on-enter:** images bend or color-shift slightly as they enter the viewport, a subtle post-processing layer CSS can't do.
- **Horizontal pan:** translate vertical scroll into horizontal movement of a track, like a camera panning (pinned ScrollTrigger; see Pinned horizontal reel above).
- **DOM over WebGL for text:** never rebuild long text or UI inside a canvas. Layer real HTML over the 3D scene, or use three.js `CSS3DRenderer` to place an HTML/iframe "screen" inside the 3D perspective (Henry Heffernan's retro computer monitor). Text stays crisp, selectable, and accessible.
- **Gamified bio:** turn About details into discoverable objects (collectibles, clickable props). Always provide a plain, accessible fallback path (a "skip to info" or standard page) so recruiters can get facts in 10 seconds.
- **Shared presence (optional):** small, moderated, asynchronous social touches (global counters, short notes left by visitors) make a site feel alive. Moderate user text before rendering. Treat this as scope expansion and ask first.
- **Spatial/UI audio (optional):** only with an explicit mute toggle, off by default or started on first user interaction, never autoplaying with sound.

### 3D / WebGL performance pipeline (when using real 3D scenes)

- **Stack:** three.js; React Three Fiber + drei for declarative scenes in React; WebGPU renderer + TSL (Three Shading Language) for advanced work, with a WebGL fallback because WebGPU support is not universal.
- **Assets:** model and bake lighting/shadows in Blender (baked textures look photoreal and cost nothing at runtime); export GLB; compress geometry with **Draco** (or Meshopt); compress textures to **KTX2 / Basis (ETC1S for color, UASTC for normals/detail)**, which stay compressed in GPU memory and prevent mobile crashes. Use `gltf-transform` to automate.
- **Draw calls:** merge static geometry; use `InstancedMesh` for repeated objects (grass, trees, particles). For huge fields, recycle instances around the camera instead of creating more.
- **Frame budget:** pause the render loop when an HTML overlay, project page, or modal covers the canvas, when the canvas is offscreen, and when the tab is hidden. Throttle raycasting to ~30Hz instead of every frame. Rely on frustum culling (keep correct bounding volumes). Limit post-processing.
- **Quality tiers:** detect low-tier devices (coarse pointer, low `hardwareConcurrency`, small screens, optionally a quick FPS probe) and drop to a lower preset: lower DPR, smaller textures, no shadows/DOF/bloom, simpler physics. Preserve the narrative, not pixel fidelity.
- **Loading:** show a meaningful, honest progress loader tied to real asset loading (drei `useProgress` / `LoadingManager`); keep the initial payload small and lazy-load secondary scenes. A 30-second load ruins any amount of spectacle.
- **Accessibility for 3D:** provide keyboard controls and a non-3D route to all content; respect reduced motion by freezing cameras and disabling auto-motion.

## Responsive Rules

- Breakpoints around 1000px (tablet: hide desktop nav links, show Menu button, collapse grids to 2 cols, unpin horizontal reel) and 600px (phone: single column, stacked hero footer).
- Use `100svh` not `100vh`. Test long names and long words with `clamp()` sizes at 360px; no horizontal overflow (`overflow-x:hidden` on body is a safety net, not a fix).
- Touch: no hover-only information; cursor hidden on `(pointer: coarse)`.


