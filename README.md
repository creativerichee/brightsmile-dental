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
- **Type:** Fraunces (display), Instrument Sans (UI), IBM Plex Mono (clinical
  labels), loaded from Google Fonts.
- **Accessibility:** skip link, visible focus states, ARIA on the comparison
  sliders and accordion, `prefers-reduced-motion` support, 44px touch targets.

## Editing it

Everything lives in one file, in this order: design tokens, component CSS, an
SVG icon sprite, the page markup, then the scripts.

- **Colours** — the `:root` block at the top. Change a token once and it updates
  everywhere, in both light and dark themes.
- **Clinic details** — name, address, phone and hours appear in the utility bar,
  the contact section and the footer.
- **Artwork** — the illustrations are inline SVG. To use real photography,
  replace an `<svg>` block with an `<img>` of the same aspect ratio.

## Note on content

Clinic name, staff, reviews and case results are placeholders for demonstration.
Replace them with real details before publishing, and keep before/after imagery
compliant with your local dental advertising rules.
