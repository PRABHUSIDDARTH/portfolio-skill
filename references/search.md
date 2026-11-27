# Search readiness: SEO, AEO, GEO

SEO helps pages be found by search engines. AEO (answer engines) and GEO (generative engines) are about being quoted correctly by assistants. They rest on the same work. Nothing here guarantees ranking or citation; say so if asked.

## SEO

| Do | Check |
| --- | --- |
| Pre-rendered HTML | The built HTML file contains the headline and body text |
| Unique title and description per page | Compare them across built pages |
| Canonical URL on the real domain | Read the built head tags. Ask for the domain; never guess it |
| Sitemap and robots.txt | Both load; robots.txt points to the sitemap |
| Social card image and tags | The image URL is absolute and loads |
| Internal links as real `<a href>` | Every page is reachable from the home page |
| Performance | Sized and compressed images, little blocking JavaScript, Lighthouse if available |

## AEO

- Say what the product or person is in the first sentences, in plain words. Check: that text alone answers "what is this?"
- Headings that match what people ask, each followed by a direct answer.
- A FAQ only if the questions are real, visible on the page, and answered there.

## GEO

- One spelling of the name and one set of facts across the site and the user's profiles. Check: list the differences and let the user fix them.
- State facts as text, not only inside images or video.
- Whether AI crawlers may access the site is **the user's choice**. Explain it and set robots.txt as they decide.

## Structured data and llms.txt

- JSON-LD (`Person`, `SoftwareApplication`, `Organization`, `FAQPage`) only describes content visible on that page. No invented ratings or reviews.
- `llms.txt` is optional. Google Search does not use it. Add it only if the user wants it, and say this.

## Existing client-rendered apps

If the project is a single-page app that renders in the browser, do not migrate it unasked. Add pre-rendering within its stack, or tell the user plainly that the text is not readable without JavaScript and offer the options.
