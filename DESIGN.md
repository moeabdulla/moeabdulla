# Profile artwork

A visual front door to son.moe: Instrument Sans / Instrument Serif, warm paper, charcoal and the portfolio's red route line. The short Markdown introduction and image alt text keep the content understandable without relying on the artwork.

## Motion and assets

- **Header:** repeating code-to-browser-to-mobile sequence, moving cursor, click ripple, success check and rotating web/mobile/systems captions.
- **Project cards:** real Promote, Shredder and IUoC portfolio captures in animated browser/phone layers. Cards link to full case studies. Promote's front capture contains sample data; Shredder artwork shows the current product, which has expanded beyond the original solo build.
- **DFO:** animated metadata-to-results illustration, preserving the supported minutes-to-seconds result rather than inventing exact timings.
- **Activity:** actual GitHub contribution calendar data with a decorative red animated trail. Snapshot dates are displayed; it does not claim to be a live count or private source-code access.
- **Pengu:** the original, owner-supplied Pengu Focus character with articulated arm/head motion, smiling eyes timed to the wave, blinking and a progress ring.
- Light/dark SVG variants use GitHub's `<picture>` support. All movement is inside `prefers-reduced-motion: no-preference`; a complete static composition is the fallback.
- Text is converted to SVG paths so GitHub does not need to load webfonts. Screenshots are embedded. No JavaScript, remote stats services or API tokens are needed to display the README.

## Rebuilding

```sh
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
.venv/bin/python scripts/build-all.py
```

To refresh contribution data manually using an authenticated GitHub CLI:

```sh
python3 scripts/fetch-activity.py
.venv/bin/python scripts/build-activity.py
```

No scheduled workflow has been enabled. `data/activity.json` is a dated snapshot of aggregate counts; refresh before publishing when needed. Typeface sources and SIL Open Font Licenses are under `assets/fonts/`. Owner-provided screenshots and Pengu artwork are under `assets/source/`.

The ignored `.preview/` directory is local review material and is not profile content. Preview changes locally; commit and push the repository to publish the profile.
