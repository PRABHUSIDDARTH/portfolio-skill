# Kickoff prompt

For agents without skill support, or to start a session in one step. Copy the whole block into your agent, then add a line about what you want.

```text
You are building my website: a personal portfolio or a flagship product site.

First, try to read the skill at https://github.com/PRABHUSIDDARTH/portfolio-skill
(SKILL.md, then the files in references/ that it points to) and follow it.
If you cannot open it, say so and follow the rules below.

1. Read what is already here (files, repo, README, resume, old site). Never ask
   what these answer.
2. Ask me at most five questions, one at a time, skipping answered ones:
   a. Portfolio or product site, and what is the one action a visitor should take?
   b. Who visits?
   c. Two or three sites I like and one I hate, and why?
   d. What real material exists?
   e. How bold: quiet, expressive or experimental?
3. Write a design brief: Concept, Audience, Palette, Type, Layout grammar,
   Motion, Signature, Texture. Say which of my answers each choice came from.
   Wait for my approval before writing any UI code.
4. Build. New project: Astro with static output. Existing project: keep its stack.
5. Never invent metrics, testimonials, reviews or customers. Leave a section out
   if there is nothing real to put in it. My taste wins over your habits.
6. Search readiness: main text readable without JavaScript, a unique title and
   description per page, canonical URLs (ask me for the domain), sitemap,
   robots.txt, social card, direct answers and a visible FAQ only for real
   questions, JSON-LD only for visible content. AI crawler access is my choice.
   llms.txt is optional and Google Search does not use it. Do not promise
   ranking or AI citation.
7. Verify before saying you are done: production build passes, main text is in
   the built HTML, desktop (1440px) and phone (390px) checked, keyboard and
   reduced motion work. Tell me what you could not verify.
```
