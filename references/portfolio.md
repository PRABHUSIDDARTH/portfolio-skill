# Portfolio mode

Read when the site is about a person. Copy rules apply to product sites too.

## Content Strategy

### Information architecture

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

### Copy rules

- First person, plain, specific. Lead with what was built and why it matters, then how.
- Good: "Connect your own AWS, GCP and Azure accounts and their free tiers act as one disk." Bad: "A revolutionary cloud solution leveraging cutting-edge technology."
- Banned filler: passionate, cutting-edge, leverage, seamless, robust, innovative, journey, delve, "I love to code".
- Every metric is sourced or omitted. Never fabricate.
- Microcopy has personality but stays clear ("Lost in the reel." on 404, "Scroll to pan" hints).

### Single content module

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



## Anti-patterns (reject these)

- Generic templates: centered "Hi, I'm X" hero, gradient blob, three identical skill cards, progress-bar skill percentages ("Java 90%").
- Fake stats, fake testimonials, placeholder projects.
- Scroll-jacking that traps the user or breaks on mobile.
- Animations on every element; fades with no mask; bouncy eases on a serious editorial concept.
- Content hidden in CSS until JS runs; WebGL required to see text.
- Icons and emoji standing in for design; skill logo walls with 40 technologies.
- Hard-coded copy scattered across components; secrets in the repo.
- Adding blogs, CMS, auth, or extra tracking without asking.


