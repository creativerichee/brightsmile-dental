# Photos

Every illustrated block on the page is also a photo slot. Drop a file in here
with the matching name and it replaces the illustration automatically — no code
changes. Delete a file and the illustration comes back. A missing or broken
image removes itself, so the page never shows a broken-image icon.

| Filename | Where it appears | Aspect ratio | Subject |
|---|---|---|---|
| `hero-smile.jpg` | Hero, right side | 4 : 4.4 (portrait) | A confident patient or dentist, mid-smile |
| `cosmetic-consultation.jpg` | "Smiles you'll love to share" | 5 : 4.6 | Dentist and patient reviewing a treatment plan |
| `technology.jpg` | "Advanced technology" | 5 : 5.2 | Intraoral scanner or chairside monitor in use |
| `dr-emily-carter.jpg` | Team | 1 : 1.02 (square-ish) | Head-and-shoulders, plain background |
| `dr-michael-reed.jpg` | Team | 1 : 1.02 | Head-and-shoulders, plain background |
| `dr-sofia-alvarez.jpg` | Team | 1 : 1.02 | Head-and-shoulders, plain background |
| `veneers-before.jpg` | Transformations slider | 16 : 11 | Close-up smile, before |
| `veneers-after.jpg` | Transformations slider | 16 : 11 | Same smile, after — same angle, same lighting |
| `whitening-before.jpg` | Transformations slider | 16 : 11 | Close-up smile, before |
| `whitening-after.jpg` | Transformations slider | 16 : 11 | Same smile, after |
| `gallery-treatment-room.jpg` | Gallery | 2 : 3 (tall) | Treatment room |
| `gallery-smile.jpg` | Gallery | 4 : 1 (wide) | Smiling patient |
| `gallery-sterilisation.jpg` | Gallery | 2 : 1 | Sterilisation area |
| `gallery-reception.jpg` | Gallery | 2 : 1 | Reception / waiting area |
| `gallery-scanner.jpg` | Gallery | 2 : 1 | Scanner or equipment detail |
| `gallery-aligners.jpg` | Gallery | 2 : 1 | Aligner trays or lab work |

## Notes

- **Format** — `.jpg` as named above. To use `.webp` or `.png` instead, update
  the `src` on the matching `<img class="photo">` in `index.html`.
- **Size** — export around 1600px on the long edge and compress to roughly
  200–400 KB. Larger files slow the page down without looking better.
- **Before/after pairs** — shoot the same angle, distance and lighting for both.
  The slider wipes between them, so any mismatch is very visible.
- **Consent** — get written patient consent before publishing clinical photos,
  and check your local dental advertising rules on before/after imagery.
