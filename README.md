# The AG Grand Venue website

The AG Grand Venue is a **React + Vite + TypeScript** static website. This architecture preserves the approved luxury editorial experience while making shared UI, route content, interactions, and replaceable media maintainable for future targeted updates.

> The current design is an approved visual baseline. Do not make broad design changes, replace sections, or alter approved typography, motion, spacing, color, responsive behavior, or layouts unless a request explicitly requires it.

## Requirements

- Node.js 22+
- pnpm 10 (the repository pins `pnpm@10.24.0`)

## Install dependencies

```bash
pnpm install
```

## Run locally

```bash
pnpm dev
```

Vite starts the local development server on port `3000` by default. Open `http://localhost:3000`.

## Production build

```bash
pnpm build
```

The build first produces the Vite client bundle and then statically prerenders every public route into `dist/`. This preserves meaningful initial HTML and per-route SEO metadata instead of shipping an empty client-only application shell.

To inspect the production output locally:

```bash
pnpm preview --host 0.0.0.0 --port 3000
```

To run TypeScript checks:

```bash
pnpm typecheck
```

## Project structure

```text
src/
├── components/      # Reusable navigation, footer, media, arrow, and inquiry-form components
├── data/            # Typed route metadata, canonical origin, navigation, and media registry
├── hooks/           # Scroll-reveal interaction hook
├── pages/           # Home, The Venue, Weddings, Events, Gallery, About, Contact, and 404 pages
├── styles/          # Approved visual baseline: typography, responsive layouts, and motion rules
├── App.tsx          # Route-to-page composition and shared layout
├── main.tsx         # React hydration entry
└── ssg.tsx          # Server rendering entry for static page emission

public/
├── media/concept/   # Current concept imagery and the local hero placeholder
├── media/README.md  # Image replacement map
├── manus-routes.json
├── robots.txt
└── sitemap.xml

scripts/prerender.ts # Creates content-bearing HTML for each route after the Vite bundle build
```

## Editing content and media

- **Page content:** edit the relevant `src/pages/*.tsx` component.
- **Shared navigation/footer/form:** edit `src/components/`.
- **Shared presentation and motion:** edit `src/styles/site.css`. Preserve the approved class structure and animation rules unless the requested change requires them.
- **Route metadata, canonical origin, and media references:** edit `src/data/site.ts`.
- **Concept imagery:** replace files in `public/media/concept/`, then retain/update the visible placeholder disclosures and `public/media/README.md` until approved Grand Venue photography is available.
- **Open business details:** remain intentionally documented in `CONTENT-PLACEHOLDERS.md` rather than invented.

## Inquiry form handoff

The form uses stable names: `first_name`, `last_name`, `email`, `phone`, `event_type`, `preferred_event_date`, `estimated_guest_count`, and `message`. It intentionally prevents online lead delivery until an approved GoHighLevel endpoint, authentication method, and field mapping are available. The current React implementation lives in `src/components/InquiryForm.tsx`.

## SEO and static output

Route-specific titles, descriptions, canonical URLs, Open Graph/Twitter values, and the 404 `noindex` directive are defined in `src/data/site.ts` and emitted by `scripts/prerender.ts`. The intended production origin is `https://thegrandbyag.com`; update it only after the real public origin is confirmed, then rebuild and verify all generated metadata, `public/sitemap.xml`, and `public/robots.txt`.

The output directory is `dist/`. No Python generator or generated `site/` directory is part of this architecture.
