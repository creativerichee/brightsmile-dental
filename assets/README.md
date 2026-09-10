# Photos

Every illustrated block on the page is also a photo slot. Drop a file in here
with the matching name and it replaces the illustration automatically — no code
changes. Delete a file and the illustration comes back. A missing or broken
image removes itself, so the page never shows a broken-image icon.

## Hero and features

| Filename | Where it appears | Aspect ratio | Subject |
|---|---|---|---|
| `hero-smile.jpg` | Hero, right side | 4 : 4.4 (portrait) | The lead dentist, or a confident patient |
| `featured-treatment.webm` + `.mp4` | "Smiles you'll love to share" | 858 x 1072 (portrait) | Short silent loop; both formats, WebM first |
| `featured-treatment-poster.jpg` | same panel | 858 x 1072 | First frame of the clip; shows while it loads, and instead of it when motion is reduced |

## Services stage

These six fill the panel that changes as you scroll the services section.

| Filename | Service | Aspect ratio |
|---|---|---|
| `svc-general.jpg` | General dentistry | 4 : 3 |
| `svc-cosmetic.jpg` | Cosmetic dentistry | 4 : 3 |
| `svc-implants.jpg` | Dental implants | 4 : 3 |
| `svc-invisalign.jpg` | Invisalign | 4 : 3 |
| `svc-whitening.jpg` | Teeth whitening | 4 : 3 |
| `svc-emergency.jpg` | Emergency dentistry | 4 : 3 |

## Team

| Filename | Aspect ratio | Subject |
|---|---|---|
| `dr-emily-carter.jpg` | 1 : 1.02 | Head-and-shoulders, plain background |
| `dr-michael-reed.jpg` | 1 : 1.02 | Head-and-shoulders, plain background |
| `dr-sofia-alvarez.jpg` | 1 : 1.02 | Head-and-shoulders, plain background |

## Before / after

Three draggable comparisons, named by position rather than treatment since the
page no longer labels them. Each pair must be shot at the same angle, distance
and lighting - the slider wipes between them, so any mismatch shows.

| Filename | Position | Aspect ratio |
|---|---|---|
| `case-a-before.jpg` / `case-a-after.jpg` | First slider | 16 : 11 (1120 x 770) |
| `case-b-before.jpg` / `case-b-after.jpg` | Second slider | 16 : 11 |
| `case-c-before.jpg` / `case-c-after.jpg` | Third slider | 16 : 11 |

## Gallery

Five tiles: three upright shots across the top, then the wide chairside scan
beside one more upright shot.

| Filename | Aspect ratio | Subject |
|---|---|---|
| `gallery-treatment-room.jpg` | 0.68 (upright) | Treatment room |
| `gallery-reception.jpg` | 0.68 (upright) | Reception / waiting area |
| `gallery-sterilisation.jpg` | 0.68 (upright) | Sterilisation area |
| `gallery-scanner.jpg` | 1.39 (wide) | Chairside scan on screen — spans two columns |
| `gallery-aligners.jpg` | 0.68 (upright) | Aligner trays |

## Notes

- **Format** — `.jpg` as named above. To use `.webp` or `.png` instead, update
  the `src` on the matching `<img class="photo">` in `index.html`.
- **Size** — export around 1600px on the long edge and compress to roughly
  200–400 KB. Larger files slow the page down without looking better.
- **Consent** — get written patient consent before publishing clinical photos,
  and check your local dental advertising rules on before/after imagery.
