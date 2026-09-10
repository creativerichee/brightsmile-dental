# BrightSmile Dental

A premium single-page website for a dental clinic. One self-contained
`index.html` — no build step, no dependencies, no external assets.

## Run it

Open `index.html` in any browser. That's the whole setup.

## What's in it

- **Sections:** utility bar, sticky nav, hero, quick-action cards, six services,
  cosmetic feature, values, stats, dentist team, before/after transformations,
  technology, new-patient offer, gallery, testimonials, emergency band, FAQ,
  booking form, footer.
- **Interactive:** drag-to-compare before/after cases, a VITA shade guide,
  animated counters, FAQ accordion, validated booking form, scroll progress,
  light/dark theme toggle, mobile menu.
- **Type:** Outfit — one geometric sans across headings, body and labels, with
  weight carrying the hierarchy. Loaded from Google Fonts.
- **Accessibility:** skip link, visible focus states, ARIA on the comparison
  sliders and accordion, `prefers-reduced-motion` support, 44px touch targets.

## Editing it

Everything lives in one file, in this order: design tokens, component CSS, an
SVG icon sprite, the page markup, then the scripts.

- **Colours** — the `:root` block at the top. Change a token once and it updates
  everywhere, in both light and dark themes.
- **Clinic details** — name, address, phone and hours appear in the utility bar,
  the contact section and the footer.
- **Photos** — every illustrated block is also a photo slot. Drop a file into
  `assets/` with the name listed in `assets/README.md` and it takes over
  automatically; remove it and the illustration comes back.

## Note on content

Clinic name, staff, reviews and case results are placeholders for demonstration.
Replace them with real details before publishing, and keep before/after imagery
compliant with your local dental advertising rules.

## Live Google rating

The testimonials section ships with a static Google badge image. To show the
clinic's real rating instead, open `index.html`, find `GOOGLE_REVIEWS` near the
bottom, and fill in both values:

```js
var GOOGLE_REVIEWS = { apiKey: "", placeId: "" };
```

1. **Google Cloud project** — enable **Places API (New)** and **Maps JavaScript
   API**, then create an API key.
2. **Restrict the key** to HTTP referrers for your domain (e.g.
   `brightsmile.dental/*`). A browser key is visible in page source by design;
   the referrer restriction is what stops other sites spending your quota.
   Never reuse a key that has billing-heavy APIs enabled.
3. **Place ID** — look the practice up with Google's Place ID finder:
   https://developers.google.com/maps/documentation/places/web-service/place-id

With both set, the page fetches the live rating and review count and swaps the
static badge for them. If the key is wrong, quota is exhausted, or the script is
blocked, it logs a warning and keeps the static badge — the section never ends
up empty.

Note that Google publishes no drop-in "reviews widget"; the Places API is the
supported route. Billing applies per request, and Google's terms require the
data be shown as coming from Google.
