# Concept imagery replacement map

The initial site deliberately uses selected images from the supplied AURÉLION hotel export only as visual layout studies. They **do not depict The AG Grand Venue** and must be replaced before photography-led public marketing.

| Current site filename | Current purpose | Replace with |
| --- | --- | --- |
| Managed concept URL `image-1.webp` | Full-screen homepage hero — generated luxury-ballroom layout, motion, and mood study | Authentic wide Grand Venue ballroom or reception photography with a central text-safe area |
| `arrival-study.png` | Arrival atmosphere | Grand Venue exterior, arrival, or architectural entrance photography |
| `space-study.png` | Venue-space layout demonstration | Primary Grand Venue interior or architectural space photograph |
| `ceremony-study.png` | Wedding editorial composition | Actual ceremony or reception photography at The AG Grand Venue |
| `exterior-study.png` | Full-width location / arrival layout | Actual venue exterior or branded architectural photography |
| `terrace-study.png` | Celebration and wedding section image | Actual celebration, reception, or outdoor venue image |
| `gathering-study.png` | Private-events layout image | Actual gala, corporate, or celebration photography |
| `light-study.png` | Editorial detail image | Grand Venue material, light, or décor detail photography |
| `atmosphere-study.png` | Warm architectural gallery composition | Actual atmospheric interior / event detail photograph |
| `landscape-study.png` | Open-air event layout image | Actual Grand Venue exterior, event, or Houston-context photograph |

The generated homepage hero is served from Manus managed storage rather than a local source file. It is **concept/placeholder imagery**, not a photo of The AG Grand Venue. When authentic hero photography is ready, replace the `HERO_CONCEPT_URL` value in `scripts/generate_site.py`, update the associated alt text, and remove the hero-specific concept notice only after the selected file is confirmed to be authentic Grand Venue photography.

When replacing an image, keep the filename and crop intent where possible so that the layout requires no code changes. Update every relevant `alt` attribute and remove the concept-imagery notices only when the selected file is confirmed to be an authentic Grand Venue photo.
