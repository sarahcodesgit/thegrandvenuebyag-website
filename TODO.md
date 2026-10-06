# Approved Build Outcomes

## 1. Venue-first architecture and editorial homepage

- Convert the supplied luxury-hotel template direction into **The AG Grand Venue**, a premium Houston / North Houston wedding and private-events website without retaining hotel language, rooms, stays, reservations, dining, spa, or accommodation CTAs.
- Provide a conversion-focused homepage with a cinematic hero, The Grand experience, Weddings, Quinceañeras & Celebrations, Private & Corporate Events, an editorial gallery preview, the supplied location, and final Schedule a Tour / Check Availability / Inquire Now pathways.
- Retain a grand, luxurious, modern, architectural, romantic-but-not-overly-feminine, editorial presentation with large imagery, elegant typography, whitespace, smooth but restrained motion, and no generic wedding-template/card-grid treatment.

## 1A. Template-first homepage hero correction

- Preserve the original AURÉLION homepage hero’s full-screen cinematic composition: full-viewport image, dark overlay, centered large serif headline, minimal overlay navigation, and top-left CTA treatment. Do not replace this hero with a new generic composition.
- Replace only the hotel content and imagery with The AG Grand Venue content: a dramatic luxury ballroom/event-venue concept image identified internally and visibly as placeholder imagery; **NORTH HOUSTON · WEDDINGS · PRIVATE EVENTS**; **The Grandest Moments / Deserve a Grand Setting.**; and **Schedule a Tour**.
- Recreate the template’s polished interaction character for the hero: entrance/text reveals, image settling transition, scroll behavior, and hover/focus interactions; honor reduced motion and preserve a visible no-JavaScript reading experience.
- Adapt the original centered AURÉLION logo location to The AG Grand Venue branding and the original minimal overlay navigation to venue-appropriate navigation. Focus this iteration on the hero and first editorial portion of the homepage; do not continue a wider homepage redesign in this correction.

## 1B. Centered full-screen navigation refinement

- Use Mexquite’s full-screen menu only as a UX/layout reference: dark full-screen overlay; The AG Grand Venue branding centered at top; the separate outlined **Schedule a Tour** CTA upper-left; an isolated X/close control upper-right; and understated venue information at the bottom.
- Center the required stacked links both vertically and horizontally: **Home, The Venue, Weddings, Events, Gallery, About, Contact**. Retain The Grand’s elegant serif, make the links luxury-scale but significantly smaller than the existing oversized menu, remove horizontal dividers and decorative arrows, and create generous intentional negative space.
- Keep the new homepage hero and first editorial handoff unchanged. Preserve polished Framer-inspired opening and closing transitions: dark background fade, subtle staggered link reveal, restrained hover/focus opacity/movement/italic treatment, dialog semantics, Escape close, keyboard focus loop, and reduced-motion support.
- Show **2103 FM 1960 Rd W · Houston, TX 77090** near the bottom. Do not invent social profiles; leave an intentional future location for official social links.

## 2. Complete public venue journeys

- Implement Home, The Venue, Weddings, Events, Gallery, About, Contact, and branded 404 pages with simple shared navigation and internal linking.
- Give weddings, quinceañeras, private celebrations, corporate events, and galas meaningful visibility without inventing pricing, capacity, packages, amenities, vendor policies, parking, staffing, catering, alcohol policies, or operating hours.
- Use the supplied address **2103 FM 1960 Rd W, Houston, TX 77090** and **info@thegrandbyag.com**; do not display a phone number.

## 3. Concept imagery and future content handoff

- Reuse only suitable supplied template imagery as clearly disclosed conceptual layout imagery; never present it as The AG Grand Venue photography.
- Organize selected image files under meaningful names and document every future photo replacement slot.
- Document unknown business details as placeholders rather than fabricating them.

## 4. Inquiry form ready for future GoHighLevel integration

- Build an accessible contact/inquiry form UI containing First Name, Last Name, Email, Phone, Event Type, Preferred Event Date, Estimated Guest Count, and Message / Tell Us About Your Event.
- Do not hardcode or simulate a CRM integration. Keep stable markup/field names so the future Grand Venue GoHighLevel sub-account can be connected cleanly.

## 5. Technical SEO, accessibility, and responsiveness

- Replace AURÉLION/hotel metadata with The AG Grand Venue metadata that naturally supports Houston wedding venue, luxury wedding venue Houston, event venue Houston, North Houston wedding venue, quinceañera venue Houston, and private event venue Houston themes.
- Deliver meaningful static HTML, unique title/description pairs, semantic markup, heading hierarchy, descriptive alt text, sensible internal links, canonical structure controlled from the intended domain, robots, sitemap, and a complete route manifest.
- Preserve or improve desktop, tablet, and mobile layouts; include keyboard focus styles and reduced-motion support.

## 6. GitHub feature-branch delivery

- Use `initial-venue-build` for the work in `sarahcodesgit/thegrandvenuebyag-website`.
- Make logical commits as major build parts are completed; push the feature branch only.
- Do not merge, force-push, or otherwise modify `main` without explicit approval.

## 7. Architecture-only React + Vite + TypeScript refactor

**Status: Complete.** TypeScript check and a clean production build pass; `dist/` emits content-bearing HTML for all seven public routes plus a noindex 404. Production-preview checks confirmed every route, route metadata, canonical/OG values, sitemap, robots, media assets, menu focus/close behavior, and the prepared inquiry-form behavior. The approved visual stylesheet is preserved byte-for-byte from the prior baseline; the legacy Python generator and `site/` output are removed.

- Create a dedicated **`react-vite-refactor`** branch from the currently approved visual baseline. Do not make this conversion on `main`, do not merge to `main`, and push the completed refactor to the existing GitHub repository on that branch only.
- Replace the Python `scripts/generate_site.py` workflow and generated `/site` architecture with a clean React + Vite + TypeScript component structure. Organize reusable navigation, footer, buttons, media, and related components under `src/components/`; retain individual public page components under `src/pages/`; retain shared styling under `src/styles/`; centralize replaceable concept photography and future media under `public/media/` where practical.
- This is **not a redesign**. Preserve the approved homepage, typography, colors, spacing, navigation/menu design, all Framer-inspired page/menu/scroll animations and transitions, hover effects, responsive behavior, and all existing pages/routes. Do not simplify or remove any existing interaction solely because it is a refactor.
- Preserve existing SEO behavior: meaningful static HTML for every public route, route-specific titles and descriptions, semantic HTML, sitemap, robots, canonical URLs, and appropriate social metadata. The React/Vite build must emit initial content rather than an empty client-only application shell.
- Before completion, run the TypeScript check and production build; verify the emitted production output provides all routes without errors. Remove the old Python generation source and generated `/site` output only after the React/Vite implementation is verified to reproduce the approved site.
