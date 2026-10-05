# The AG Grand Venue website

A static, SEO-forward first-pass website for The AG Grand Venue in North Houston. The design translates the supplied Framer hotel export’s editorial scale, type, spacing, and motion into a wedding and private-events experience.

## Local preview

Run the static server from the project root:

```bash
python3 -m http.server 3000 --directory site
```

Then open `http://localhost:3000`.

## Content editing

- Public pages are in `site/` and its route directories.
- Shared styles are in `site/assets/css/site.css`.
- Navigation, reveal effects, and the non-submitting inquiry-form UI are in `site/assets/js/site.js`.
- The supplied-template image replacement map is in `site/assets/images/README.md`.
- The homepage hero uses a managed concept image declared as `HERO_CONCEPT_URL` in `scripts/generate_site.py`; it remains a placeholder until authentic Grand Venue photography is approved.
- Unknown business details remain documented in `CONTENT-PLACEHOLDERS.md` rather than invented in the site.

## Inquiry form handoff

The form UI uses stable names: `first_name`, `last_name`, `email`, `phone`, `event_type`, `preferred_event_date`, `estimated_guest_count`, and `message`. It intentionally prevents online submission until a GoHighLevel integration is supplied. Replace that UI-only handling in `site/assets/js/site.js` only when the approved GHL endpoint and mapping are available.

## Production metadata

The intended production domain is centralized as `https://thegrandbyag.com` in `scripts/generate_site.py`. Update it only after the real public origin is confirmed, regenerate the static pages, and then verify canonical, Open Graph, sitemap, and robots values.

## Regenerating static pages

This initial build uses `scripts/generate_site.py` to produce the static page files and to copy the selected concept imagery from the supplied template archive. Run:

```bash
python3 scripts/generate_site.py
```

Do not remove the concept-imagery notices or imply that any current placeholder image depicts The AG Grand Venue.
