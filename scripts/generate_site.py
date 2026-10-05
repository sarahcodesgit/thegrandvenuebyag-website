from __future__ import annotations

from pathlib import Path
from shutil import copy2

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ASSETS = SITE / "assets"
CSS = ASSETS / "css"
JS = ASSETS / "js"
IMAGES = ASSETS / "images" / "concept"
TEMPLATE_IMAGES = Path("/home/ubuntu/template-inspect/assets/images")
PRODUCTION_ORIGIN = "https://thegrandbyag.com"

IMAGE_MAP = {
    "arrival-study.png": ("image-0d8c8830.png", "Conceptual editorial image of a floral arrival moment; this is not The AG Grand Venue."),
    "space-study.png": ("image-3be7708e.png", "Conceptual architectural image of a light-filled gathering space; this is not The AG Grand Venue."),
    "ceremony-study.png": ("image-2f40c00a.png", "Conceptual ceremony table and floral study; this is not The AG Grand Venue."),
    "exterior-study.png": ("image-54b7d937.png", "Conceptual exterior and arrival study; this is not The AG Grand Venue."),
    "terrace-study.png": ("image-7077990a.png", "Conceptual outdoor celebration study; this is not The AG Grand Venue."),
    "gathering-study.png": ("image-a1217fa6.png", "Conceptual evening gathering study; this is not The AG Grand Venue."),
    "light-study.png": ("image-36e9a62a.png", "Conceptual interior light and styling study; this is not The AG Grand Venue."),
    "archive-study.png": ("image-a2077?", ""),
    "atmosphere-study.png": ("image-bcb7bcc2.png", "Conceptual warm architectural atmosphere study; this is not The AG Grand Venue."),
    "landscape-study.png": ("image-087a3512.png", "Conceptual open-air landscape study; this is not The AG Grand Venue."),
}

# The source export does not contain image-a2077?. Keep the map intentionally explicit and
# remove that unneeded entry before files are written.
IMAGE_MAP.pop("archive-study.png")

NAV = [
    ("Home", "/"),
    ("The Venue", "/the-venue/"),
    ("Weddings", "/weddings/"),
    ("Events", "/events/"),
    ("Gallery", "/gallery/"),
    ("About", "/about/"),
    ("Contact", "/contact/"),
]

PAGES = {
    "home": {
        "path": "index.html",
        "route": "/",
        "title": "Luxury Wedding Venue in Houston | The AG Grand",
        "description": "The AG Grand Venue is a luxury wedding and private event venue in North Houston for celebrations with a grander point of view.",
    },
    "venue": {
        "path": "the-venue/index.html",
        "route": "/the-venue/",
        "title": "The Venue | The AG Grand Venue in Houston",
        "description": "Discover the editorial vision behind The AG Grand Venue, a new luxury setting for weddings and private events in North Houston.",
    },
    "weddings": {
        "path": "weddings/index.html",
        "route": "/weddings/",
        "title": "Houston Wedding Venue | The AG Grand Venue",
        "description": "Plan a wedding with a grander sense of occasion at The AG Grand Venue, a luxury Houston setting for meaningful celebrations.",
    },
    "events": {
        "path": "events/index.html",
        "route": "/events/",
        "title": "Private Event Venue Houston | The AG Grand Venue",
        "description": "Explore a new North Houston setting for quinceañeras, private celebrations, corporate events, and gala-worthy occasions.",
    },
    "gallery": {
        "path": "gallery/index.html",
        "route": "/gallery/",
        "title": "Gallery | The AG Grand Venue, North Houston",
        "description": "Explore the visual direction for The AG Grand Venue through conceptual editorial imagery and a grand celebration point of view.",
    },
    "about": {
        "path": "about/index.html",
        "route": "/about/",
        "title": "About The AG Grand Venue | North Houston",
        "description": "Learn about The AG Grand Venue, a new luxury wedding and private-events destination in North Houston, Texas.",
    },
    "contact": {
        "path": "contact/index.html",
        "route": "/contact/",
        "title": "Contact The AG Grand Venue | Schedule a Tour",
        "description": "Schedule a tour or start planning a wedding or private event at The AG Grand Venue in North Houston, Texas.",
    },
    "notfound": {
        "path": "404.html",
        "route": "/404.html",
        "title": "Page Not Found | The AG Grand Venue",
        "description": "The page you requested is not available. Return to The AG Grand Venue to explore weddings and private events in North Houston.",
    },
}


def nav(current: str) -> str:
    links = "".join(
        f'<a href="{href}" {"aria-current=\"page\"" if href == current else ""} data-menu-link>{label}</a>'
        for label, href in NAV
    )
    header_class = "site-header"
    return f'''<header class="{header_class}" data-header>
  <div class="header-inner">
    <a class="header-cta" href="/contact/#inquiry">Schedule a Tour</a>
    <a class="header-brand" href="/" aria-label="The AG Grand Venue home">
      <span class="header-brand-name">THE AG GRAND VENUE</span>
      <span class="header-brand-subline">North Houston · Weddings · Private Events</span>
    </a>
    <button class="menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="site-menu" aria-label="Open navigation">
      <span class="sr-only">Open navigation</span><span></span><span></span>
    </button>
  </div>
  <div id="site-menu" class="site-menu" data-site-menu role="dialog" aria-modal="true" aria-label="Site navigation" hidden>
    <div class="site-menu-topbar">
      <a class="site-menu-cta" href="/contact/#inquiry">Schedule a Tour</a>
      <a class="site-menu-brand" href="/" aria-label="The AG Grand Venue home">
        <span class="header-brand-name">THE AG GRAND VENUE</span>
        <span class="header-brand-subline">North Houston · Weddings · Private Events</span>
      </a>
      <button class="site-menu-close" type="button" data-menu-close aria-label="Close navigation">
        <span class="sr-only">Close navigation</span><span></span><span></span>
      </button>
    </div>
    <div class="site-menu-inner container">
      <nav class="site-menu-nav" aria-label="Primary navigation">{links}</nav>
      <div class="site-menu-meta"><span>2103 FM 1960 Rd W · Houston, TX 77090</span></div>
    </div>
  </div>
  <noscript><nav class="noscript-nav" aria-label="Primary navigation">{links}</nav></noscript>
</header>'''


def footer() -> str:
    return '''<footer class="site-footer">
  <div class="footer-top container">
    <div class="footer-brand">
      <a class="brand brand-footer" href="/" aria-label="The AG Grand Venue home">
        <span class="brand-mark">AG</span>
        <span class="brand-copy"><span>THE</span><strong>GRAND VENUE</strong></span>
      </a>
      <p>A grand setting for the moments that change everything.</p>
    </div>
    <div class="footer-col"><span class="footer-label">Visit</span><p>2103 FM 1960 Rd W<br>Houston, TX 77090</p><a href="https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090" target="_blank" rel="noopener">Get directions <span aria-hidden="true">↗</span></a></div>
    <div class="footer-col"><span class="footer-label">Inquiries</span><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a><a href="/contact/#inquiry">Schedule a Tour <span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="footer-bottom container"><p>© <span data-year></span> The AG Grand Venue. All rights reserved.</p><p>Concept imagery is used for layout direction only. Venue photography is forthcoming.</p></div>
</footer>'''


def image(name: str, class_name: str = "", eager: bool = False) -> str:
    _, alt = IMAGE_MAP[name]
    loading = "eager" if eager else "lazy"
    fetch = ' fetchpriority="high"' if eager else ""
    return f'''<figure class="image-frame {class_name}" data-concept-image>
  <img src="/assets/images/concept/{name}" alt="{alt}" loading="{loading}"{fetch}>
  <figcaption>Concept imagery — layout and mood study only</figcaption>
</figure>'''


HERO_CONCEPT_URL = "/manus-storage/async-images/NPJRKZYXpzWdt7lQ9rWtnJ/image-1.webp"


def hero_concept_image() -> str:
    return f'''<figure class="image-frame hero-image hero-concept-image" data-concept-image>
  <img src="{HERO_CONCEPT_URL}" alt="Conceptual luxury ballroom wedding reception with chandeliers and elegant floral tables; this is not The AG Grand Venue." loading="eager" fetchpriority="high">
  <figcaption>Concept imagery — hero layout and mood study only</figcaption>
</figure>'''


def head(page: dict) -> str:
    canonical = f"{PRODUCTION_ORIGIN}{page['route']}"
    robots = '<meta name="robots" content="noindex,follow">' if page["route"] == "/404.html" else ""
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#171513">
  <title>{page['title']}</title>
  <meta name="description" content="{page['description']}">
  {robots}
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['description']}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="The AG Grand Venue">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{page['title']}">
  <meta name="twitter:description" content="{page['description']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
  <script>document.documentElement.classList.add('js')</script>
  <link rel="stylesheet" href="/assets/css/site.css">
  <script src="/assets/js/site.js" defer></script>
</head>'''


def page(key: str, main: str) -> str:
    data = PAGES[key]
    return f'''{head(data)}
<body class="page page-{key}">
  <a class="skip-link" href="#main">Skip to content</a>
  {nav(data['route'])}
  <main id="main">{main}</main>
  {footer()}
</body>
</html>
'''


HOME = f'''
<section class="hero hero-home" aria-labelledby="home-hero-title">
  {hero_concept_image()}
  <div class="hero-overlay"></div>
  <div class="hero-center container">
    <p class="hero-eyebrow">North Houston · Weddings · Private Events</p>
    <h1 id="home-hero-title" class="hero-title hero-title-centered"><span class="hero-line"><span>The Grandest Moments</span></span><span class="hero-line"><em>Deserve a Grand Setting.</em></span></h1>
  </div>
  <a class="hero-scroll" href="#our-point-of-view"><span>Scroll to discover</span><i aria-hidden="true"></i></a>
</section>
<section id="our-point-of-view" class="home-manifesto">
  <div class="container manifesto-grid">
    <div class="manifesto-copy reveal"><p class="eyebrow">The AG Grand Venue</p><h2 class="display-lg">A place for moments<br><em>that ask for more.</em></h2></div>
    <div class="manifesto-detail reveal"><p class="lead">A new North Houston setting for ceremonies, celebrations, and gatherings with a sense of occasion.</p><p>Here, the anticipation of arrival, the meaning of tradition, and the energy of the room all have space to unfold. The Grand is imagined for the memories that deserve to feel singular from the very first moment.</p><a class="text-link" href="/the-venue/">Discover The Venue <span aria-hidden="true">↗</span></a></div>
  </div>
</section>
<section class="feature-panel panel-dark">
  <div class="container feature-grid">
    <div class="feature-copy reveal"><p class="eyebrow eyebrow-light">The Venue Experience</p><h2 class="display-lg">Make an entrance.<br><em>Then make it yours.</em></h2><p>Every unforgettable event begins with a setting that invites possibility. Explore the visual language and intentional atmosphere behind The AG Grand Venue.</p><a class="button button-outline-light" href="/the-venue/">Explore The Venue <span aria-hidden="true">↗</span></a></div>
    <div class="feature-image reveal">{image("space-study.png", "tall-image")}</div>
  </div>
</section>
<section class="section-space container editorial-section">
  <div class="section-index reveal">02 <span>Ways to Gather</span></div>
  <div class="editorial-header reveal"><p class="eyebrow">Every celebration, elevated</p><h2 class="display-xl">Your moment.<br><em>On a grander scale.</em></h2></div>
  <div class="journey-grid">
    <article class="journey-card journey-card-wide reveal">{image("ceremony-study.png", "journey-image")}<div class="journey-content"><span>01</span><h3>Weddings</h3><p>For ceremonies, receptions, and every anticipation-filled moment between.</p><a class="text-link" href="/weddings/">Explore weddings <span aria-hidden="true">↗</span></a></div></article>
    <article class="journey-card reveal">{image("terrace-study.png", "journey-image")}<div class="journey-content"><span>02</span><h3>Celebrations</h3><p>Quinceañeras and milestone occasions with space for personal tradition.</p><a class="text-link" href="/events/#celebrations">Discover celebrations <span aria-hidden="true">↗</span></a></div></article>
    <article class="journey-card journey-card-offset reveal">{image("gathering-study.png", "journey-image")}<div class="journey-content"><span>03</span><h3>Private & Corporate</h3><p>Galas, gatherings, and events designed to leave an impression.</p><a class="text-link" href="/events/#private-events">Explore events <span aria-hidden="true">↗</span></a></div></article>
  </div>
</section>
<section class="image-statement">
  {image("exterior-study.png", "statement-image")}
  <div class="image-statement-overlay"><p class="eyebrow eyebrow-light reveal">A New North Houston Address</p><h2 class="display-xl display-light reveal">Designed for the stories<br><em>still to be told.</em></h2><a class="button button-light reveal" href="/contact/#inquiry">Start Planning <span aria-hidden="true">↗</span></a></div>
</section>
<section class="gallery-preview section-space container">
  <div class="section-topline reveal"><div><p class="eyebrow">Visual Direction</p><h2 class="display-lg">The Grand,<br><em>in every frame.</em></h2></div><a class="text-link" href="/gallery/">View the gallery <span aria-hidden="true">↗</span></a></div>
  <div class="gallery-strip"><div class="reveal">{image("light-study.png", "gallery-tile gallery-tile-a")}</div><div class="reveal">{image("atmosphere-study.png", "gallery-tile gallery-tile-b")}</div><div class="reveal">{image("landscape-study.png", "gallery-tile gallery-tile-c")}</div></div>
</section>
<section class="location-cta panel-warm">
  <div class="container location-grid"><div class="reveal"><p class="eyebrow">Visit The Grand</p><h2 class="display-lg">The next chapter<br><em>starts here.</em></h2></div><div class="location-detail reveal"><p>2103 FM 1960 Rd W<br>Houston, TX 77090</p><div class="location-actions"><a class="button" href="/contact/#inquiry">Schedule a Tour <span aria-hidden="true">↗</span></a><a class="text-link" href="https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090" target="_blank" rel="noopener">Get directions <span aria-hidden="true">↗</span></a></div></div></div>
</section>
'''

VENUE = f'''
<section class="page-hero page-hero-dark">
  <div class="container page-hero-grid"><div class="page-hero-copy"><p class="eyebrow eyebrow-light reveal">The Venue</p><h1 class="display-hero display-light reveal">A setting with<br><em>its own sense of ceremony.</em></h1><p class="lead lead-light reveal">The AG Grand Venue is being shaped as an architectural canvas for Houston’s most meaningful gatherings.</p></div><div class="page-hero-image reveal">{image("space-study.png", "portrait-image")}</div></div>
</section>
<section class="section-space container split-section"><div class="split-media reveal">{image("arrival-study.png", "split-image")}</div><div class="split-copy reveal"><p class="eyebrow">The First Impression</p><h2 class="display-lg">It begins<br><em>before the first toast.</em></h2><p>There is a difference between a place to host an event and a place that sets the tone for it. The Grand is imagined for the instant guests arrive, the pause before a processional, and the energy that carries a celebration late into the evening.</p><p>As venue details and photography are finalized, this space will become a closer look at the experience, spaces, and possibilities that make the setting distinct.</p></div></section>
<section class="panel-warm story-band"><div class="container story-grid"><div class="section-index reveal">01 <span>Intentional by design</span></div><div class="reveal"><h2 class="display-lg">Space for a vision.<br><em>Presence for a memory.</em></h2><p class="lead">A grand venue should feel polished enough to elevate a celebration—and open enough to let it become unmistakably yours.</p></div></div></section>
<section class="section-space container image-pair"><div class="reveal">{image("light-study.png", "pair-image pair-image-left")}</div><div class="pair-copy reveal"><p class="eyebrow">The Grand Experience</p><h2 class="display-lg">A little more<br><em>occasion in every detail.</em></h2><p>From romantic weddings to high-energy celebrations and formal gatherings, the strongest event design starts with a point of view. The Grand offers the beginning; your people, traditions, and imagination complete the story.</p><a class="text-link" href="/contact/#inquiry">Schedule a private tour <span aria-hidden="true">↗</span></a></div><div class="reveal">{image("atmosphere-study.png", "pair-image pair-image-right")}</div></section>
<section class="cta-section panel-dark"><div class="container centered-cta reveal"><p class="eyebrow eyebrow-light">See it in person</p><h2 class="display-lg display-light">Let the setting<br><em>do the talking.</em></h2><a class="button button-light" href="/contact/#inquiry">Schedule a Tour <span aria-hidden="true">↗</span></a></div></section>
'''

WEDDINGS = f'''
<section class="page-hero page-hero-image">
  {image("ceremony-study.png", "hero-image", eager=True)}<div class="hero-overlay"></div><div class="container page-hero-overlay-copy"><p class="eyebrow eyebrow-light reveal">Weddings at The Grand</p><h1 class="display-hero display-light reveal">Make the moment<br><em>monumental.</em></h1><p class="lead lead-light reveal">A new North Houston setting for the ceremony, reception, and every unforgettable moment in between.</p><a class="button button-light reveal" href="/contact/#inquiry">Start Planning <span aria-hidden="true">↗</span></a></div>
</section>
<section class="section-space container intro-section intro-section-tight"><div class="section-index reveal">01 <span>Your wedding, in focus</span></div><div class="intro-copy reveal"><p class="eyebrow">A day with a point of view</p><h2 class="display-xl">The best celebrations<br>feel <em>entirely personal.</em></h2><p class="lead">Whether your vision is romantic and candlelit, modern and minimal, or alive with color and tradition, your wedding should reflect the two people at its center. The AG Grand Venue is being created for that kind of possibility.</p></div></section>
<section class="event-arc panel-warm"><div class="container"><div class="arc-intro reveal"><p class="eyebrow">The wedding journey</p><h2 class="display-lg">From the first look<br><em>to the last dance.</em></h2></div><div class="arc-grid"><article class="arc-card reveal"><span>01</span><h3>The Arrival</h3><p>The anticipation, the welcome, and the first glimpse of a day that feels different from every other.</p></article><article class="arc-card reveal"><span>02</span><h3>The Ceremony</h3><p>The quiet before the vows, the people closest to you, and a setting worthy of the promise.</p></article><article class="arc-card reveal"><span>03</span><h3>The Celebration</h3><p>A celebration in motion, a full dance floor, and the kind of joy that refuses to be rushed.</p></article></div></div></section>
<section class="section-space container split-section split-section-reverse"><div class="split-copy reveal"><p class="eyebrow">A new beginning</p><h2 class="display-lg">The story is yours.<br><em>The setting is The Grand.</em></h2><p>Share the first details of your date and vision, and our team will be ready to begin the conversation. Event details, availability, and tour information will be tailored once they are confirmed.</p><a class="text-link" href="/contact/#inquiry">Inquire about your wedding <span aria-hidden="true">↗</span></a></div><div class="split-media reveal">{image("terrace-study.png", "split-image")}</div></section>
<section class="cta-section panel-dark"><div class="container centered-cta reveal"><p class="eyebrow eyebrow-light">Your next chapter</p><h2 class="display-lg display-light">Come see what<br><em>could unfold here.</em></h2><a class="button button-light" href="/contact/#inquiry">Schedule a Tour <span aria-hidden="true">↗</span></a></div></section>
'''

EVENTS = f'''
<section class="page-hero page-hero-dark">
  <div class="container page-hero-grid"><div class="page-hero-copy"><p class="eyebrow eyebrow-light reveal">Events at The Grand</p><h1 class="display-hero display-light reveal">Celebrate<br><em>without a template.</em></h1><p class="lead lead-light reveal">Milestone moments, cultural traditions, gala evenings, and gatherings designed around your people.</p></div><div class="page-hero-image reveal">{image("gathering-study.png", "portrait-image")}</div></div>
</section>
<section id="celebrations" class="section-space container events-intro"><div class="section-index reveal">01 <span>Ways to gather</span></div><div class="events-intro-copy reveal"><p class="eyebrow">Every occasion, elevated</p><h2 class="display-xl">There is always<br><em>something worth celebrating.</em></h2><p class="lead">The AG Grand Venue is envisioned for celebrations that bring generations together, honor traditions, and turn a once-in-a-lifetime occasion into a lasting memory.</p></div></section>
<section class="event-categories container"><article class="category-row reveal"><span>01</span><div><h3>Quinceañeras</h3><p>A milestone celebration with space for heritage, family, and an entrance to remember.</p></div><a href="/contact/#inquiry" class="text-link">Start planning <span aria-hidden="true">↗</span></a></article><article class="category-row reveal"><span>02</span><div><h3>Private Celebrations</h3><p>Birthdays, anniversaries, and the kind of gathering that deserves a proper sense of occasion.</p></div><a href="/contact/#inquiry" class="text-link">Check availability <span aria-hidden="true">↗</span></a></article><article id="private-events" class="category-row reveal"><span>03</span><div><h3>Galas & Corporate Events</h3><p>Polished settings for annual celebrations, fundraisers, company moments, and formal evenings.</p></div><a href="/contact/#inquiry" class="text-link">Plan an event <span aria-hidden="true">↗</span></a></article><article class="category-row reveal"><span>04</span><div><h3>Cultural Celebrations</h3><p>A versatile starting point for celebrations that honor meaningful customs and personal vision.</p></div><a href="/contact/#inquiry" class="text-link">Start a conversation <span aria-hidden="true">↗</span></a></article></section>
<section class="image-statement image-statement-short">{image("exterior-study.png", "statement-image")}<div class="image-statement-overlay image-statement-overlay-left"><p class="eyebrow eyebrow-light reveal">The Grand Point of View</p><h2 class="display-lg display-light reveal">Big feeling.<br><em>Beautifully considered.</em></h2></div></section>
<section class="section-space container split-section"><div class="split-media reveal">{image("landscape-study.png", "split-image")}</div><div class="split-copy reveal"><p class="eyebrow">Begin with a tour</p><h2 class="display-lg">See what<br><em>your event could become.</em></h2><p>Tell us the occasion you are imagining and the date you have in mind. The inquiry form is ready to help guide the next conversation.</p><a class="button" href="/contact/#inquiry">Inquire Now <span aria-hidden="true">↗</span></a></div></section>
'''

GALLERY = f'''
<section class="gallery-hero container"><p class="eyebrow reveal">Gallery</p><h1 class="display-hero reveal">The feeling,<br><em>before the first frame.</em></h1><p class="lead reveal">A visual direction for The AG Grand Venue. These inherited concept images demonstrate the intended rhythm, light, and editorial scale—not the physical venue.</p></section>
<section class="concept-note"><div class="container reveal"><span class="note-mark">†</span><p><strong>Concept imagery notice.</strong> The complete Grand Venue photography library is forthcoming. The images on this page are placeholders from the supplied template, used only to demonstrate layout and mood direction.</p></div></section>
<section class="gallery-page-grid container"><div class="gallery-column gallery-column-a reveal">{image("arrival-study.png", "gallery-large")}{image("landscape-study.png", "gallery-medium")}</div><div class="gallery-column gallery-column-b reveal">{image("space-study.png", "gallery-tall")}{image("atmosphere-study.png", "gallery-medium")}</div><div class="gallery-column gallery-column-c reveal">{image("ceremony-study.png", "gallery-medium")}{image("terrace-study.png", "gallery-large")}</div></section>
<section class="cta-section panel-warm"><div class="container centered-cta reveal"><p class="eyebrow">See the direction in person</p><h2 class="display-lg">Your story belongs<br><em>at the center of it.</em></h2><a class="button" href="/contact/#inquiry">Schedule a Tour <span aria-hidden="true">↗</span></a></div></section>
'''

ABOUT = f'''
<section class="page-hero page-hero-dark">
  <div class="container page-hero-grid"><div class="page-hero-copy"><p class="eyebrow eyebrow-light reveal">About The Grand</p><h1 class="display-hero display-light reveal">A new point of view<br><em>for North Houston.</em></h1><p class="lead lead-light reveal">The AG Grand Venue is a new destination for people who believe milestone moments deserve meaningful settings.</p></div><div class="page-hero-image reveal">{image("exterior-study.png", "portrait-image")}</div></div>
</section>
<section class="section-space container intro-section intro-section-tight"><div class="section-index reveal">01 <span>The AG point of view</span></div><div class="intro-copy reveal"><p class="eyebrow">More than a backdrop</p><h2 class="display-xl">Made for the moments<br>that <em>bring people together.</em></h2><p class="lead">From the AG family of venues comes a new idea for Houston celebrations: a place imagined with a grander perspective, an editorial sensibility, and space for occasions that are entirely your own.</p><p>It is not a template for someone else’s event. It is a starting point for yours.</p></div></section>
<section class="panel-warm about-location"><div class="container about-location-grid"><div class="reveal"><p class="eyebrow">Located in North Houston</p><h2 class="display-lg">A new address<br><em>for unforgettable occasions.</em></h2></div><div class="address-block reveal"><p>2103 FM 1960 Rd W<br>Houston, TX 77090</p><a class="text-link" href="https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090" target="_blank" rel="noopener">Get directions <span aria-hidden="true">↗</span></a></div></div></section>
<section class="section-space container split-section split-section-reverse"><div class="split-copy reveal"><p class="eyebrow">The next chapter</p><h2 class="display-lg">Be among the first<br><em>to experience The Grand.</em></h2><p>We are looking ahead to the celebrations, traditions, and milestone events this new venue will welcome. Start the conversation with an inquiry or request a private tour.</p><a class="button" href="/contact/#inquiry">Get in Touch <span aria-hidden="true">↗</span></a></div><div class="split-media reveal">{image("light-study.png", "split-image")}</div></section>
'''

CONTACT = '''
<section class="contact-hero panel-dark"><div class="container contact-hero-grid"><div class="contact-heading"><p class="eyebrow eyebrow-light reveal">Contact The Grand</p><h1 class="display-hero display-light reveal">Let’s make space<br><em>for something memorable.</em></h1><p class="lead lead-light reveal">Share a few details about the occasion you are planning, and we’ll be ready to begin the conversation.</p></div><div class="contact-details reveal"><span class="footer-label">Visit</span><p>2103 FM 1960 Rd W<br>Houston, TX 77090</p><span class="footer-label">Email</span><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a></div></div></section>
<section id="inquiry" class="inquiry-section section-space container"><div class="inquiry-intro reveal"><p class="eyebrow">Start Planning</p><h2 class="display-lg">Tell us a little<br><em>about your event.</em></h2><p>This form is prepared for the future Grand Venue GoHighLevel connection. Until online delivery is configured, please use the email address above for time-sensitive inquiries.</p></div><form class="inquiry-form reveal" data-inquiry-form novalidate><div class="form-grid"><label>First Name<input name="first_name" autocomplete="given-name" required></label><label>Last Name<input name="last_name" autocomplete="family-name" required></label><label>Email<input type="email" name="email" autocomplete="email" required></label><label>Phone<input type="tel" name="phone" autocomplete="tel" required></label><label>Event Type<select name="event_type" required><option value="" selected disabled>Select an event type</option><option>Wedding</option><option>Quinceañera</option><option>Private Celebration</option><option>Corporate Event or Gala</option><option>Cultural Celebration</option><option>Other</option></select></label><label>Preferred Event Date<input type="date" name="preferred_event_date" required></label><label>Estimated Guest Count<input type="number" name="estimated_guest_count" inputmode="numeric" min="1" placeholder="Optional"></label><label class="form-full">Tell Us About Your Event<textarea name="message" rows="5" required placeholder="Your vision, occasion, and anything else we should know."></textarea></label></div><div class="form-action"><p class="form-disclosure">No CRM is connected yet. This form will not submit event details online in the current preview.</p><button class="button" type="button" data-inquiry-button>Prepare My Inquiry <span aria-hidden="true">↗</span></button></div><p class="form-status" data-form-status role="status" aria-live="polite"></p></form></section>
<section class="location-cta panel-warm"><div class="container location-grid"><div class="reveal"><p class="eyebrow">Plan a visit</p><h2 class="display-lg">The first step is<br><em>seeing the possibility.</em></h2></div><div class="location-detail reveal"><p>Schedule a private tour or begin a conversation at<br><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a></p><a class="text-link" href="https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090" target="_blank" rel="noopener">Get directions <span aria-hidden="true">↗</span></a></div></div></section>
'''

NOT_FOUND = '''
<section class="not-found panel-dark"><div class="container centered-cta"><p class="eyebrow eyebrow-light">404</p><h1 class="display-hero display-light">This page has<br><em>moved out of frame.</em></h1><p class="lead lead-light">Return to The AG Grand Venue and continue exploring a grander point of view for weddings and celebrations.</p><a class="button button-light" href="/">Return Home <span aria-hidden="true">↗</span></a></div></section>
'''

CSS_TEXT = r'''@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Jost:wght@400;500;600&display=swap');

:root {
  --ink: #171513;
  --ink-soft: #2b2825;
  --ivory: #f3eee6;
  --paper: #e8e0d4;
  --limestone: #c7b8a5;
  --copper: #9a674d;
  --white: #fbf8f3;
  --line: rgba(23, 21, 19, .19);
  --line-light: rgba(255, 255, 255, .28);
  --serif: "Cormorant Garamond", Georgia, serif;
  --sans: "Jost", Arial, sans-serif;
  --container: min(1440px, calc(100vw - 96px));
  --section: clamp(5rem, 9vw, 10rem);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; background: var(--ivory); }
body { margin: 0; color: var(--ink); background: var(--ivory); font-family: var(--sans); font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased; }
img { display: block; width: 100%; height: 100%; object-fit: cover; }
a { color: inherit; text-decoration: none; }
button, input, select, textarea { font: inherit; }
button { cursor: pointer; }
::selection { color: var(--ivory); background: var(--copper); }

.skip-link { position: fixed; top: 1rem; left: 1rem; z-index: 200; transform: translateY(-200%); padding: .65rem 1rem; color: var(--ink); background: var(--white); }
.skip-link:focus { transform: translateY(0); }
.sr-only { position: absolute; overflow: hidden; width: 1px; height: 1px; clip: rect(0, 0, 0, 0); white-space: nowrap; }
.container { width: var(--container); margin: 0 auto; }
.section-space { padding: var(--section) 0; }
.panel-dark { color: var(--white); background: var(--ink); }
.panel-warm { background: var(--paper); }

.site-header { position: fixed; z-index: 30; top: 0; left: 0; width: 100%; color: var(--white); pointer-events: none; transition: color .35s ease; }
.site-header > * { pointer-events: auto; }
.site-header.is-light-surface { color: var(--ink); }
.site-header.is-menu-open { color: var(--white); }
.site-header.is-menu-open .header-inner { visibility: hidden; pointer-events: none; }
.noscript-nav { display: none; }
html:not(.js) .site-header { pointer-events: auto; }
html:not(.js) .noscript-nav { position: fixed; top: 92px; right: 0; left: 0; display: flex; gap: .75rem 1.25rem; align-items: center; justify-content: center; flex-wrap: wrap; padding: .85rem var(--container); color: var(--ink); background: var(--white); border-bottom: 1px solid var(--line); font-size: .58rem; letter-spacing: .14em; text-transform: uppercase; }
.header-inner { position: relative; z-index: 2; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; min-height: 92px; width: var(--container); margin: 0 auto; }
.header-cta, .site-menu-cta { display: inline-flex; justify-self: start; align-items: center; justify-content: center; min-height: 39px; padding: 0 .9rem; border: 1px solid currentColor; font-size: .56rem; font-weight: 500; letter-spacing: .19em; text-transform: uppercase; transition: color .3s ease, background .3s ease, transform .3s ease; }
.header-cta:hover, .site-menu-cta:hover { color: var(--ink); background: var(--white); transform: translateY(-2px); }
.header-brand, .site-menu-brand { display: grid; justify-items: center; gap: .16rem; width: max-content; max-width: 50vw; margin: 0 auto; color: inherit; line-height: 1; text-align: center; }
.header-brand-name { font-family: var(--serif); font-size: clamp(1.25rem, 2.1vw, 1.9rem); font-weight: 600; letter-spacing: .075em; white-space: nowrap; }
.header-brand-subline { overflow: hidden; max-width: 100%; font-size: .43rem; font-weight: 500; letter-spacing: .19em; text-overflow: ellipsis; text-transform: uppercase; white-space: nowrap; }
.menu-toggle { display: grid; justify-self: end; gap: 5px; width: 43px; height: 43px; padding: 0; border: 1px solid currentColor; color: currentColor; background: rgba(255,255,255,.12); place-content: center; transition: color .3s ease, background .3s ease, border-color .3s ease; }
.site-header.is-light-surface .menu-toggle { background: rgba(23,21,19,.05); }
.menu-toggle:hover { color: var(--ink); background: var(--white); }
.menu-toggle span:not(.sr-only) { display: block; width: 18px; height: 1px; background: currentColor; transition: transform .3s cubic-bezier(.2,.7,.2,1); }
.menu-toggle.is-active span:nth-child(2) { transform: translateY(3px) rotate(45deg); }
.menu-toggle.is-active span:nth-child(3) { transform: translateY(-3px) rotate(-45deg); }
.site-header.is-menu-open .menu-toggle { border-color: transparent; color: var(--white); background: transparent; }
.site-menu-close { display: grid; justify-self: end; gap: 5px; width: 43px; height: 43px; padding: 0; border: 0; color: var(--white); background: transparent; place-content: center; transition: opacity .25s ease, transform .25s ease; }
.site-menu-close:hover { opacity: .7; transform: rotate(4deg); }
.site-menu-close span:not(.sr-only) { display: block; width: 18px; height: 1px; background: currentColor; }
.site-menu-close span:nth-child(2) { transform: translateY(3px) rotate(45deg); }
.site-menu-close span:nth-child(3) { transform: translateY(-3px) rotate(-45deg); }
.site-menu { position: fixed; z-index: 1; inset: 0; overflow-y: auto; color: var(--white); background: #0d0c0b; opacity: 0; pointer-events: none; transition: opacity .46s cubic-bezier(.22,.72,.18,1); }
.site-menu[hidden] { display: none !important; }
.site-menu::before { position: absolute; inset: 0; content: ""; opacity: 0; background: radial-gradient(ellipse at 50% 48%, rgba(121,84,62,.13), transparent 48%), linear-gradient(180deg, rgba(255,255,255,.025), transparent 34%); transition: opacity .58s ease; }
.site-menu.is-open { opacity: 1; pointer-events: auto; }
.site-menu.is-open::before { opacity: 1; }
.site-menu.is-closing { opacity: 0; pointer-events: none; }
.site-menu-topbar { position: absolute; z-index: 2; top: 0; right: 0; left: 0; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; min-height: 92px; width: var(--container); margin: 0 auto; }
.site-menu-inner { position: relative; display: grid; grid-template-rows: minmax(0, 1fr) auto minmax(0, 1fr); min-height: 100svh; padding: 6rem 0 2.6rem; }
.site-menu-nav { display: grid; grid-row: 2; gap: clamp(.22rem, .65vh, .55rem); width: max-content; max-width: 100%; margin: 0; justify-self: center; text-align: center; }
.site-menu-nav a { display: block; padding: .1rem .45rem; border: 0; color: var(--white); font-family: var(--serif); font-size: clamp(2.2rem, 4.25vw, 4.35rem); font-weight: 400; letter-spacing: -.028em; line-height: .98; transition: color .28s ease, opacity .28s ease, transform .32s cubic-bezier(.2,.7,.2,1); }
.site-menu-nav a:hover, .site-menu-nav a[aria-current="page"] { color: var(--limestone); font-style: italic; }
.site-menu-nav a:hover { opacity: .72; transform: translateY(-2px); }
.site-menu-nav a:focus-visible { outline: 1px solid var(--copper); outline-offset: .45rem; }
.site-menu-meta { display: grid; grid-row: 3; align-self: end; justify-self: center; margin: 0 0 .2rem; color: rgba(255,255,255,.58); font-size: .58rem; letter-spacing: .14em; text-align: center; text-transform: uppercase; }
.js .site-menu .site-menu-nav a, .js .site-menu .site-menu-meta { opacity: 0; transform: translateY(16px); }
.js .site-menu.is-open .site-menu-nav a { animation: menu-item-in .56s cubic-bezier(.2,.72,.2,1) forwards; }
.js .site-menu.is-open .site-menu-nav a:nth-child(1) { animation-delay: .13s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(2) { animation-delay: .18s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(3) { animation-delay: .23s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(4) { animation-delay: .28s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(5) { animation-delay: .33s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(6) { animation-delay: .38s; }
.js .site-menu.is-open .site-menu-nav a:nth-child(7) { animation-delay: .43s; }
.js .site-menu.is-open .site-menu-meta { animation: menu-item-in .5s .49s cubic-bezier(.2,.72,.2,1) forwards; }
.js .site-menu.is-closing .site-menu-nav a, .js .site-menu.is-closing .site-menu-meta { animation: none; opacity: 0; transform: translateY(-7px); transition: opacity .16s ease, transform .16s ease; }

.brand { display: inline-flex; gap: .65rem; align-items: center; width: max-content; font-size: .64rem; line-height: 1.05; letter-spacing: .22em; }
.brand-mark { display: grid; width: 34px; height: 34px; place-items: center; border: 1px solid currentColor; border-radius: 50%; font-family: var(--serif); font-size: 1rem; letter-spacing: -.1em; }
.brand-copy { display: grid; gap: .18rem; }
.brand-copy span { font-size: .5rem; letter-spacing: .37em; }
.brand-copy strong { font-weight: 500; letter-spacing: .19em; white-space: nowrap; }

.hero { position: relative; display: grid; min-height: 100svh; color: var(--white); overflow: hidden; isolation: isolate; }
.hero-image { position: absolute; z-index: 0; inset: 0; margin: 0; }
.hero-image img { height: 100%; object-position: center center; }
.hero-overlay { position: absolute; z-index: 1; inset: 0; background: linear-gradient(180deg, rgba(7,7,7,.47), rgba(10,9,8,.16) 35%, rgba(8,7,6,.58)), linear-gradient(90deg, rgba(12,10,9,.26), transparent 50%, rgba(12,10,9,.22)); }
.hero-center { position: relative; z-index: 2; display: grid; min-height: 100svh; padding: 8rem 0 5rem; place-content: center; text-align: center; }
.hero-eyebrow { margin: 0 0 1.7rem; color: var(--white); font-size: .61rem; font-weight: 500; letter-spacing: .25em; text-transform: uppercase; }
.hero-title, .display-hero, .display-xl, .display-lg { margin: 0; font-family: var(--serif); font-weight: 500; line-height: .88; letter-spacing: -.052em; }
.hero-title-centered { width: min(1050px, 100%); font-size: clamp(4.2rem, 8.25vw, 9.2rem); text-shadow: 0 5px 27px rgba(0,0,0,.18); }
.hero-line { display: block; overflow: hidden; padding: .03em .07em .13em; }
.hero-line > * { display: block; font-style: normal; }
.hero-line em { font-style: italic; }
.hero-scroll { position: absolute; z-index: 3; bottom: 2rem; left: 50%; display: flex; gap: .8rem; align-items: center; color: var(--white); font-size: .54rem; letter-spacing: .2em; text-transform: uppercase; transform: translateX(-50%); }
.hero-scroll i { display: block; width: 42px; height: 1px; background: currentColor; animation: scroll-line 2.1s ease-in-out infinite; }
.hero-concept-image figcaption { right: 1.2rem; bottom: 1.15rem; left: auto; z-index: 4; }
.js .hero-home .hero-concept-image img { transform: scale(1.12); animation: hero-image-settle 1.8s cubic-bezier(.2,.75,.18,1) .05s forwards; }
.js .page-home .header-cta, .js .page-home .header-brand, .js .page-home .menu-toggle { opacity: 0; transform: translateY(-11px); animation: hero-chrome-in .7s .18s cubic-bezier(.2,.75,.2,1) forwards; }
.js .page-home .header-brand { animation-delay: .31s; }
.js .page-home .menu-toggle { animation-delay: .43s; }
.js .hero-eyebrow { opacity: 0; transform: translateY(15px); animation: hero-chrome-in .65s .53s cubic-bezier(.2,.75,.2,1) forwards; }
.js .hero-line > * { opacity: .001; transform: translateY(115%); animation: hero-line-in 1.05s cubic-bezier(.15,.8,.2,1) forwards; }
.js .hero-line:nth-child(1) > * { animation-delay: .63s; }
.js .hero-line:nth-child(2) > * { animation-delay: .77s; }
@keyframes hero-image-settle { to { transform: scale(1); } }
@keyframes hero-line-in { to { opacity: 1; transform: translateY(0); } }
@keyframes hero-chrome-in { to { opacity: 1; transform: translateY(0); } }
@keyframes menu-item-in { to { opacity: 1; transform: translateY(0); } }
@keyframes scroll-line { 0%, 100% { transform: scaleX(.55); transform-origin: right; } 50% { transform: scaleX(1); transform-origin: left; } }
em { font-weight: 400; }
.hero-bottom { display: flex; gap: 2rem; align-items: flex-end; justify-content: space-between; padding-top: 1.55rem; border-top: 1px solid var(--line-light); }
.hero-bottom p { max-width: 400px; margin: 0; font-size: .9rem; line-height: 1.6; }
.hero-actions { display: flex; gap: 2rem; align-items: center; }
.hero-scroll { position: absolute; right: 3.3rem; bottom: 2.4rem; z-index: 3; display: flex; gap: .7rem; align-items: center; margin: 0; font-size: .56rem; letter-spacing: .2em; text-transform: uppercase; transform: rotate(90deg); transform-origin: right center; }
.hero-scroll span { display: block; width: 45px; height: 1px; background: currentColor; }

.eyebrow, .footer-label { margin: 0 0 1.15rem; color: var(--copper); font-size: .62rem; font-weight: 500; letter-spacing: .2em; text-transform: uppercase; }
.eyebrow-light { color: var(--white); }
.display-hero { max-width: 930px; font-size: clamp(4.2rem, 9vw, 9.3rem); }
.display-xl { max-width: 900px; font-size: clamp(3.5rem, 7.3vw, 7.4rem); }
.display-lg { max-width: 760px; font-size: clamp(3rem, 5.4vw, 5.7rem); }
.display-light { color: var(--white); }
.lead { max-width: 600px; margin: 1.8rem 0 0; color: var(--ink-soft); font-family: var(--serif); font-size: clamp(1.5rem, 2vw, 2rem); line-height: 1.25; }
.lead-light { color: var(--white); }

.button { display: inline-flex; gap: .75rem; align-items: center; justify-content: center; min-height: 49px; padding: 0 1.35rem; border: 1px solid var(--ink); color: var(--ivory); background: var(--ink); font-size: .65rem; font-weight: 500; letter-spacing: .16em; text-transform: uppercase; transition: color .25s ease, background .25s ease, transform .25s ease; }
.button:hover { color: var(--ink); background: transparent; transform: translateY(-2px); }
.button-light { color: var(--ink); border-color: var(--white); background: var(--white); }
.button-light:hover { color: var(--white); background: transparent; }
.button-outline-light { color: var(--white); border-color: var(--line-light); background: transparent; }
.button-outline-light:hover { color: var(--ink); background: var(--white); }
.text-link { display: inline-flex; gap: .65rem; align-items: center; padding-bottom: .22rem; border-bottom: 1px solid var(--ink); font-size: .67rem; font-weight: 500; letter-spacing: .15em; text-transform: uppercase; transition: gap .2s ease; }
.text-link:hover { gap: 1rem; }
.text-link-light { color: var(--white); border-color: rgba(255,255,255,.65); }

.image-frame { position: relative; margin: 0; overflow: hidden; background: #776b60; }
.image-frame img { aspect-ratio: 4 / 3; transition: transform .8s cubic-bezier(.2,.7,.2,1); }
.image-frame:hover img { transform: scale(1.035); }
.image-frame figcaption { position: absolute; bottom: .75rem; left: .75rem; padding: .32rem .5rem; color: var(--white); background: rgba(20,18,16,.7); font-size: .47rem; letter-spacing: .13em; text-transform: uppercase; backdrop-filter: blur(7px); }
.hero .image-frame.hero-image { position: absolute; z-index: 0; inset: 0; margin: 0; }
.hero .image-frame.hero-image img { width: 100%; height: 100%; aspect-ratio: auto; }
.hero-image figcaption { right: 1.25rem; bottom: 1.2rem; left: auto; z-index: 4; }

.intro-section { display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }
.section-index { display: flex; gap: .8rem; align-items: baseline; color: var(--copper); font-family: var(--serif); font-size: 1.45rem; }
.section-index span { color: var(--ink); font-family: var(--sans); font-size: .59rem; letter-spacing: .18em; text-transform: uppercase; }
.intro-copy { max-width: 940px; }
.intro-copy .lead { margin-bottom: 2rem; }
.home-manifesto { padding: clamp(6rem, 10vw, 10.5rem) 0; background: var(--white); }
.manifesto-grid { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(4rem, 10vw, 12rem); align-items: start; }
.manifesto-copy h2 { margin: .4rem 0 0; }
.manifesto-detail { max-width: 530px; padding-left: clamp(2rem, 4vw, 4.5rem); border-left: 1px solid var(--line); }
.manifesto-detail .lead { margin: 0 0 2rem; }
.manifesto-detail > p:not(.lead) { max-width: 470px; margin: 0; color: var(--ink-soft); }
.manifesto-detail .text-link { margin-top: 2.25rem; }
.feature-panel { padding: clamp(4rem, 8vw, 8rem) 0; }
.feature-grid { display: grid; grid-template-columns: .92fr 1.08fr; gap: clamp(3rem, 8vw, 9rem); align-items: center; }
.feature-copy > p:not(.eyebrow) { max-width: 475px; margin: 2rem 0 2.6rem; color: rgba(255,255,255,.72); }
.tall-image img { aspect-ratio: 4 / 5.25; }
.editorial-section { position: relative; }
.editorial-header { display: flex; align-items: end; justify-content: space-between; margin: 0 0 4rem 33.333%; }
.journey-grid { display: grid; grid-template-columns: 1.15fr .85fr .85fr; gap: 1.4rem; align-items: start; }
.journey-card { background: var(--paper); }
.journey-card-wide { margin-top: 0; }
.journey-card-offset { margin-top: 5rem; }
.journey-image img { aspect-ratio: 4 / 4.6; }
.journey-card-wide .journey-image img { aspect-ratio: 1 / 1; }
.journey-content { padding: 1.6rem 1.6rem 1.9rem; }
.journey-content > span { color: var(--copper); font-family: var(--serif); font-size: 1.2rem; }
.journey-content h3 { margin: .35rem 0 .5rem; font-family: var(--serif); font-size: 2.5rem; font-weight: 500; line-height: 1; }
.journey-content p { min-height: 3.1rem; margin: 0 0 1.45rem; font-size: .86rem; }
.image-statement { position: relative; display: grid; min-height: 740px; color: var(--white); overflow: hidden; }
.statement-image { position: absolute; inset: 0; }
.statement-image img { object-position: center; }
.image-statement::after { position: absolute; inset: 0; content: ""; background: linear-gradient(90deg, rgba(13,11,10,.67), rgba(13,11,10,.1)); }
.image-statement-overlay { position: relative; z-index: 1; align-self: center; width: var(--container); margin: 0 auto; }
.image-statement-overlay-left { align-self: end; padding-bottom: 7rem; }
.image-statement-overlay .button { margin-top: 2.2rem; }
.image-statement-short { min-height: 550px; }
.gallery-preview { padding-bottom: calc(var(--section) * .88); }
.section-topline { display: flex; align-items: end; justify-content: space-between; margin-bottom: 3rem; }
.gallery-strip { display: grid; grid-template-columns: 1.05fr .8fr 1.05fr; gap: 1.25rem; align-items: center; }
.gallery-tile img { aspect-ratio: 4 / 5.2; }
.gallery-tile-b { transform: translateY(4rem); }
.gallery-tile-c img { aspect-ratio: 4 / 3.1; }
.location-cta { padding: clamp(4.7rem, 8vw, 8rem) 0; }
.location-grid { display: grid; grid-template-columns: 1.1fr .9fr; gap: 3rem; align-items: end; }
.location-detail { max-width: 400px; }
.location-detail > p { margin: 0 0 2rem; font-family: var(--serif); font-size: 2rem; line-height: 1.25; }
.location-actions { display: flex; gap: 1.4rem; align-items: center; flex-wrap: wrap; }

.page-hero-dark { color: var(--white); background: var(--ink); }
.page-hero { padding: 10.5rem 0 6rem; }
.page-hero-grid { display: grid; grid-template-columns: 1fr .76fr; gap: clamp(3rem, 8vw, 9rem); align-items: end; }
.page-hero-copy .lead { max-width: 540px; margin-top: 2rem; }
.page-hero-image { margin-bottom: -11rem; }
.portrait-image img { aspect-ratio: 4 / 5.15; }
.page-hero-image .image-frame figcaption { display: none; }
.page-hero-image + * { padding-top: 13rem; }
.page-hero-image .portrait-image img { object-position: center; }
.page-hero-image figure { box-shadow: 0 28px 70px rgba(0,0,0,.18); }
.page-hero-image { z-index: 2; }
.page-hero-image .image-frame { background: #61584e; }
.page-hero-image .image-frame img { filter: saturate(.78); }
.page-hero-image .image-frame figcaption { display: block; }
.page-hero-image .portrait-image { max-height: 630px; }
.page-hero-image .portrait-image img { min-height: 450px; }
.page-hero-image .portrait-image figcaption { right: .6rem; bottom: .6rem; left: .6rem; text-align: center; }
.page-hero-image .portrait-image figcaption { display: block; }
.page-hero-image .portrait-image img { object-position: center; }
.page-hero-image .portrait-image { overflow: hidden; }
.page-hero-image .portrait-image > img { height: 100%; }
.page-hero-image .portrait-image figcaption { font-size: .42rem; }
.page-hero-image .portrait-image { margin: 0; }

.split-section { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(3rem, 8vw, 9rem); align-items: center; }
.split-section-reverse .split-copy { order: -1; }
.split-image img { aspect-ratio: 4 / 5; }
.split-copy { max-width: 560px; }
.split-copy h2 { margin-bottom: 1.6rem; }
.split-copy p:not(.eyebrow) { margin: 0 0 1.1rem; color: var(--ink-soft); }
.split-copy .text-link, .split-copy .button { margin-top: 1.15rem; }
.story-band { padding: clamp(4.5rem, 8vw, 8rem) 0; }
.story-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }
.story-grid .lead { margin-top: 1.6rem; }
.image-pair { display: grid; grid-template-columns: 1fr .88fr 1fr; gap: 2.5rem; align-items: center; }
.pair-image img { aspect-ratio: 4 / 5.2; }
.pair-image-right img { aspect-ratio: 4 / 3.15; }
.pair-copy h2 { margin: .4rem 0 1.3rem; }
.pair-copy p:not(.eyebrow) { margin: 0 0 1.5rem; }
.cta-section { padding: clamp(5.5rem, 9vw, 9rem) 0; }
.centered-cta { display: grid; place-items: center; text-align: center; }
.centered-cta .lead { margin-bottom: 2rem; }
.centered-cta .button { margin-top: 2rem; }

.page-hero-image + .intro-section { padding-top: 13rem; }
.intro-section-tight { padding-bottom: calc(var(--section) * .75); }
.page-hero-image + .intro-section-tight { padding-top: 13rem; }
.page-hero-image + .events-intro { padding-top: 13rem; }
.page-hero-image + .section-space { padding-top: 13rem; }
.page-hero-image + .split-section { padding-top: 13rem; }
.page-hero-image + .about-location { padding-top: 13rem; }
.page-hero-image + .event-categories { padding-top: 13rem; }
.page-hero-image + .gallery-page-grid { padding-top: 13rem; }

.page-hero-image { position: relative; min-height: min(825px, 94vh); padding: 0; color: var(--white); overflow: hidden; }
.page-hero-image .hero-image { position: absolute; }
.page-hero-image .hero-image img { object-position: center; }
.page-hero-overlay-copy { position: relative; z-index: 2; display: flex; flex-direction: column; justify-content: end; min-height: min(825px, 94vh); padding-bottom: 6.5rem; }
.page-hero-overlay-copy .display-hero { margin-top: 1rem; }
.page-hero-overlay-copy .button { align-self: start; margin-top: 2rem; }
.event-arc { padding: clamp(4.5rem, 8vw, 8rem) 0; }
.arc-intro { margin-bottom: 4rem; }
.arc-grid { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--line); }
.arc-card { min-height: 280px; padding: 1.6rem 2rem 1rem 0; border-right: 1px solid var(--line); }
.arc-card:not(:first-child) { padding-left: 2rem; }
.arc-card:last-child { border-right: none; }
.arc-card span, .category-row > span { color: var(--copper); font-family: var(--serif); font-size: 1.45rem; }
.arc-card h3 { margin: 2.7rem 0 .65rem; font-family: var(--serif); font-size: 2.55rem; font-weight: 500; line-height: 1; }
.arc-card p { max-width: 275px; margin: 0; font-size: .86rem; }
.events-intro { display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }
.events-intro-copy .lead { margin-bottom: 0; }
.event-categories { margin-bottom: var(--section); border-top: 1px solid var(--line); }
.category-row { display: grid; grid-template-columns: 90px 1fr auto; gap: 2rem; align-items: center; min-height: 180px; border-bottom: 1px solid var(--line); }
.category-row h3 { margin: 0 0 .45rem; font-family: var(--serif); font-size: clamp(2.4rem, 4vw, 4.3rem); font-weight: 500; line-height: .95; }
.category-row p { max-width: 500px; margin: 0; font-size: .88rem; }

.gallery-hero { padding: 10.5rem 0 4.4rem; }
.gallery-hero .lead { max-width: 650px; margin-bottom: 0; }
.concept-note { padding: 1.35rem 0; color: var(--white); background: var(--ink); }
.concept-note .container { display: flex; gap: 1.1rem; align-items: start; max-width: 960px; }
.concept-note p { margin: 0; font-size: .77rem; line-height: 1.55; }
.note-mark { color: var(--limestone); font-family: var(--serif); font-size: 2rem; line-height: .7; }
.gallery-page-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.25rem; align-items: start; padding-top: 4.3rem; padding-bottom: var(--section); }
.gallery-column { display: grid; gap: 1.25rem; }
.gallery-column-b { padding-top: 5.5rem; }
.gallery-large img { aspect-ratio: 4 / 5.3; }
.gallery-tall img { aspect-ratio: 4 / 6.5; }
.gallery-medium img { aspect-ratio: 4 / 3.4; }
.about-location { padding: clamp(4.5rem, 8vw, 8rem) 0; }
.about-location-grid { display: grid; grid-template-columns: 1.3fr .7fr; gap: 4rem; align-items: end; }
.address-block { padding-bottom: .5rem; }
.address-block p { margin: 0 0 1.7rem; font-family: var(--serif); font-size: 2rem; line-height: 1.22; }

.contact-hero { padding: 11rem 0 5.5rem; }
.contact-hero-grid { display: grid; grid-template-columns: 1.25fr .75fr; gap: 4rem; align-items: end; }
.contact-heading .lead { max-width: 630px; }
.contact-details { display: grid; gap: .35rem; padding-bottom: .4rem; }
.contact-details .footer-label:not(:first-child) { margin-top: 1.5rem; }
.contact-details p, .contact-details a { margin: 0; font-family: var(--serif); font-size: 1.4rem; line-height: 1.3; }
.inquiry-section { display: grid; grid-template-columns: .8fr 1.2fr; gap: clamp(3.5rem, 9vw, 10rem); align-items: start; }
.inquiry-intro { position: sticky; top: 110px; }
.inquiry-intro h2 { margin: .4rem 0 1.4rem; }
.inquiry-intro p:not(.eyebrow) { max-width: 385px; margin: 0; font-size: .88rem; }
.inquiry-form { padding: 2.2rem; background: var(--paper); }
.form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem 1.2rem; }
.inquiry-form label { display: grid; gap: .42rem; color: var(--ink-soft); font-size: .62rem; font-weight: 500; letter-spacing: .16em; text-transform: uppercase; }
.inquiry-form input, .inquiry-form select, .inquiry-form textarea { width: 100%; padding: .74rem 0; border: 0; border-bottom: 1px solid rgba(23,21,19,.34); border-radius: 0; outline: 0; color: var(--ink); background: transparent; font-family: var(--sans); font-size: .92rem; letter-spacing: 0; text-transform: none; transition: border-color .2s ease; }
.inquiry-form textarea { min-height: 125px; resize: vertical; }
.inquiry-form select { appearance: none; background-image: linear-gradient(45deg, transparent 50%, var(--ink) 50%), linear-gradient(135deg, var(--ink) 50%, transparent 50%); background-position: calc(100% - 12px) calc(50% - 2px), calc(100% - 8px) calc(50% - 2px); background-size: 4px 4px, 4px 4px; background-repeat: no-repeat; }
.inquiry-form input:focus, .inquiry-form select:focus, .inquiry-form textarea:focus { border-color: var(--copper); }
.inquiry-form input[aria-invalid="true"], .inquiry-form select[aria-invalid="true"], .inquiry-form textarea[aria-invalid="true"] { border-color: #a53325; }
.form-full { grid-column: 1 / -1; }
.form-action { display: flex; gap: 1.8rem; align-items: center; justify-content: space-between; margin-top: 2rem; padding-top: 1.3rem; border-top: 1px solid var(--line); }
.form-disclosure { max-width: 300px; margin: 0; font-size: .68rem; line-height: 1.5; }
.form-status { min-height: 1.5em; margin: 1.2rem 0 0; color: var(--copper); font-size: .78rem; }
.not-found { display: grid; min-height: 100vh; padding: 8rem 0; place-items: center; }

.site-footer { color: var(--white); background: #11100e; }
.footer-top { display: grid; grid-template-columns: 1.3fr .7fr .7fr; gap: 4rem; padding: 5rem 0 4.4rem; }
.footer-brand p { max-width: 290px; margin: 1.6rem 0 0; color: rgba(255,255,255,.68); font-family: var(--serif); font-size: 1.35rem; line-height: 1.22; }
.footer-col { display: grid; align-content: start; gap: .5rem; }
.footer-col .footer-label { color: var(--limestone); }
.footer-col p { margin: 0 0 .3rem; color: rgba(255,255,255,.78); font-size: .84rem; }
.footer-col a { width: max-content; max-width: 100%; border-bottom: 1px solid transparent; font-size: .82rem; transition: border-color .2s ease; }
.footer-col a:hover { border-color: currentColor; }
.footer-bottom { display: flex; gap: 2rem; justify-content: space-between; padding: 1.3rem 0; border-top: 1px solid rgba(255,255,255,.16); color: rgba(255,255,255,.54); font-size: .56rem; letter-spacing: .08em; text-transform: uppercase; }

.reveal { opacity: 1; transform: none; }
.js .reveal { opacity: 0; transform: translateY(22px); transition: opacity .75s cubic-bezier(.2,.65,.2,1), transform .75s cubic-bezier(.2,.65,.2,1); }
.js .reveal.is-visible { opacity: 1; transform: translateY(0); }

@media (max-width: 1000px) {
  :root { --container: min(100% - 56px, 1440px); }
  .journey-grid { grid-template-columns: 1fr 1fr; }
  .journey-card-offset { margin-top: 0; }
  .journey-card-wide { grid-column: span 2; display: grid; grid-template-columns: 1.15fr .85fr; }
  .journey-card-wide .journey-image img { aspect-ratio: 1 / 1; }
  .journey-card-wide .journey-content { display: flex; flex-direction: column; justify-content: center; }
  .image-pair { gap: 1.5rem; }
  .category-row { grid-template-columns: 65px 1fr auto; }
  .footer-top { gap: 2.5rem; }
}

@media (max-width: 760px) {
  :root { --container: min(100% - 36px, 1440px); --section: 4.5rem; }
  body { font-size: 15px; }
  .header-inner { min-height: 76px; }
  html:not(.js) .noscript-nav { top: 76px; gap: .55rem .8rem; font-size: .48rem; }
  .site-menu-topbar { min-height: 76px; }
  .header-cta, .site-menu-cta { min-height: 33px; padding: 0 .47rem; font-size: .4rem; letter-spacing: .14em; }
  .header-brand, .site-menu-brand { max-width: 44vw; }
  .header-brand-name { font-size: clamp(.95rem, 4.5vw, 1.17rem); letter-spacing: .045em; }
  .header-brand-subline { font-size: .3rem; letter-spacing: .12em; }
  .menu-toggle, .site-menu-close { width: 35px; height: 35px; }
  .menu-toggle span:not(.sr-only), .site-menu-close span:not(.sr-only) { width: 15px; }
  .site-menu-inner { min-height: 100svh; padding: 5.5rem 0 1.8rem; }
  .site-menu-nav { gap: .28rem; }
  .site-menu-nav a { padding: .12rem .3rem; font-size: clamp(2rem, 9.7vw, 2.7rem); }
  .site-menu-meta { max-width: 285px; margin-bottom: .1rem; font-size: .48rem; line-height: 1.45; }
  .hero { min-height: 100svh; }
  .hero-center { min-height: 100svh; padding: 7rem 0 4.8rem; }
  .hero-eyebrow { margin-bottom: 1.2rem; font-size: .48rem; letter-spacing: .18em; }
  .hero-title-centered { font-size: clamp(3.35rem, 14.7vw, 5.55rem); line-height: .9; }
  .hero-scroll { bottom: 1.45rem; font-size: .45rem; }
  .hero-scroll i { width: 28px; }
  .hero-concept-image figcaption { right: .65rem; bottom: 4.1rem; font-size: .36rem; }
  .display-hero { font-size: clamp(4.1rem, 18vw, 6rem); }
  .display-xl { font-size: clamp(3.25rem, 15vw, 5rem); }
  .display-lg { font-size: clamp(2.9rem, 13vw, 4rem); }
  .lead { font-size: 1.45rem; }
  .intro-section, .feature-grid, .split-section, .story-grid, .events-intro, .about-location-grid, .contact-hero-grid, .inquiry-section, .manifesto-grid { grid-template-columns: 1fr; gap: 2rem; }
  .section-index { margin-bottom: .3rem; }
  .home-manifesto { padding: 5rem 0; }
  .manifesto-detail { padding-top: 2rem; padding-left: 0; border-top: 1px solid var(--line); border-left: 0; }
  .feature-copy { padding-top: .5rem; }
  .editorial-header { display: block; margin: 0 0 2.4rem; }
  .journey-grid { grid-template-columns: 1fr; gap: 1rem; }
  .journey-card-wide { grid-column: auto; display: block; }
  .journey-card-wide .journey-image img, .journey-image img { aspect-ratio: 4 / 3.3; }
  .journey-content p { min-height: 0; }
  .journey-card-offset { margin-top: 0; }
  .image-statement { min-height: 570px; }
  .image-statement-overlay { align-self: end; padding-bottom: 4.5rem; }
  .image-statement-overlay-left { padding-bottom: 4.5rem; }
  .section-topline { display: grid; gap: 1.5rem; align-items: start; }
  .gallery-strip { grid-template-columns: 1fr 1fr; gap: .8rem; }
  .gallery-tile-c { grid-column: span 2; }
  .gallery-tile-b { transform: translateY(2rem); }
  .location-grid { grid-template-columns: 1fr; gap: 2.2rem; }
  .location-detail > p, .address-block p { font-size: 1.7rem; }
  .page-hero { padding: 8.9rem 0 4.5rem; }
  .page-hero-grid { grid-template-columns: 1fr; gap: 2.8rem; }
  .page-hero-image { margin-bottom: -2.5rem; }
  .page-hero-image + .intro-section, .page-hero-image + .intro-section-tight, .page-hero-image + .events-intro, .page-hero-image + .section-space, .page-hero-image + .split-section, .page-hero-image + .about-location, .page-hero-image + .event-categories, .page-hero-image + .gallery-page-grid { padding-top: 6.5rem; }
  .page-hero-image .portrait-image { max-height: none; }
  .page-hero-image .portrait-image img { min-height: 0; aspect-ratio: 4 / 4; }
  .page-hero-image { min-height: 720px; }
  .page-hero-overlay-copy { min-height: 720px; padding-bottom: 4.5rem; }
  .arc-grid { grid-template-columns: 1fr; }
  .arc-card, .arc-card:not(:first-child) { min-height: auto; padding: 1.5rem 0; border-right: 0; border-bottom: 1px solid var(--line); }
  .arc-card:last-child { border-bottom: 0; }
  .arc-card h3 { margin-top: 1.6rem; }
  .image-pair { grid-template-columns: 1fr; gap: 1.5rem; }
  .pair-copy { padding: 1.8rem 0; }
  .pair-image-right img { aspect-ratio: 4 / 3; }
  .category-row { grid-template-columns: 42px 1fr; gap: 1rem; align-items: start; min-height: auto; padding: 1.7rem 0; }
  .category-row .text-link { grid-column: 2; width: max-content; }
  .category-row h3 { font-size: 2.65rem; }
  .gallery-hero { padding: 8.8rem 0 3.5rem; }
  .gallery-page-grid { grid-template-columns: 1fr 1fr; gap: .8rem; padding-top: 2.7rem; }
  .gallery-column { gap: .8rem; }
  .gallery-column-c { grid-column: span 2; display: grid; grid-template-columns: 1fr 1fr; }
  .gallery-column-b { padding-top: 3rem; }
  .gallery-tall img { aspect-ratio: 4 / 5.7; }
  .contact-hero { padding: 9rem 0 4rem; }
  .inquiry-intro { position: static; }
  .inquiry-form { padding: 1.4rem; }
  .form-grid { grid-template-columns: 1fr; gap: 1.4rem; }
  .form-full { grid-column: auto; }
  .form-action { display: grid; gap: 1.2rem; align-items: start; }
  .footer-top { grid-template-columns: 1fr; gap: 2.5rem; padding: 4rem 0 3rem; }
  .footer-bottom { display: grid; gap: .5rem; justify-content: start; }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { transition-duration: .01ms !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; }
  .js .reveal { opacity: 1; transform: none; }
  .js .hero-home .hero-concept-image img, .js .hero-home .hero-eyebrow, .js .hero-home .hero-line > *, .js .page-home .header-cta, .js .page-home .header-brand, .js .page-home .menu-toggle { opacity: 1; transform: none; animation: none; }
}
'''

JS_TEXT = r'''(() => {
  const header = document.querySelector('[data-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-site-menu]');
  const darkSurfaceSelector = '.hero, .panel-dark, .image-statement, .page-hero-dark, .page-hero-image, .contact-hero, .not-found, .site-footer';

  const setHeaderTone = () => {
    if (!header || header.classList.contains('is-menu-open')) return;
    const probeY = Math.min(112, Math.round(window.innerHeight * .14));
    const probe = document.elementFromPoint(Math.round(window.innerWidth / 2), probeY);
    header.classList.toggle('is-light-surface', !probe?.closest(darkSurfaceSelector));
  };
  setHeaderTone();
  window.addEventListener('scroll', setHeaderTone, { passive: true });
  window.addEventListener('resize', setHeaderTone);

  if (toggle && menu) {
    const menuClose = menu.querySelector('[data-menu-close]');
    const backgroundTargets = [
      document.querySelector('.skip-link'),
      header.querySelector('.header-inner'),
      document.querySelector('main'),
      document.querySelector('footer'),
    ].filter(Boolean);
    const closeDuration = 460;
    let closeTimer;
    let openFrame;
    const setBackgroundInert = (isInert) => {
      backgroundTargets.forEach((element) => {
        element.toggleAttribute('inert', isInert);
        if (isInert) element.setAttribute('aria-hidden', 'true');
        else element.removeAttribute('aria-hidden');
      });
    };
    const closeMenu = () => {
      if (menu.hidden) return;
      window.cancelAnimationFrame(openFrame);
      openFrame = undefined;
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation');
      toggle.classList.remove('is-active');
      menu.classList.remove('is-open');
      menu.classList.add('is-closing');
      document.body.style.overflow = '';
      window.clearTimeout(closeTimer);
      closeTimer = window.setTimeout(() => {
        menu.hidden = true;
        menu.classList.remove('is-closing');
        setBackgroundInert(false);
        header.classList.remove('is-menu-open');
        setHeaderTone();
      }, closeDuration);
    };
    const openMenu = () => {
      window.clearTimeout(closeTimer);
      window.cancelAnimationFrame(openFrame);
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close navigation');
      toggle.classList.add('is-active');
      header.classList.add('is-menu-open');
      setBackgroundInert(true);
      menu.hidden = false;
      menu.classList.remove('is-closing', 'is-open');
      document.body.style.overflow = 'hidden';
      openFrame = requestAnimationFrame(() => {
        if (toggle.getAttribute('aria-expanded') === 'true') menu.classList.add('is-open');
      });
      menu.querySelector('[data-menu-link]')?.focus();
    };
    const menuFocusable = () => [
      ...menu.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'),
    ].filter((element) => element && !element.hasAttribute('disabled'));
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      if (open) closeMenu(); else openMenu();
    });
    menuClose?.addEventListener('click', closeMenu);
    menu.querySelectorAll('[data-menu-link]').forEach((link) => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        window.setTimeout(() => toggle.focus(), closeDuration);
      }
      if (event.key === 'Tab' && toggle.getAttribute('aria-expanded') === 'true') {
        const items = menuFocusable();
        const first = items[0];
        const last = items[items.length - 1];
        if (!first || !last) return;
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    });
  }

  const items = document.querySelectorAll('.reveal');
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .12, rootMargin: '0px 0px -28px' });
    items.forEach((item) => observer.observe(item));
  } else {
    items.forEach((item) => item.classList.add('is-visible'));
  }

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  const form = document.querySelector('[data-inquiry-form]');
  const status = document.querySelector('[data-form-status]');
  const inquiryButton = document.querySelector('[data-inquiry-button]');
  if (form && status) {
    const prepareInquiry = () => {
      const controls = [...form.querySelectorAll('input[required], select[required], textarea[required]')];
      let valid = true;
      controls.forEach((control) => {
        const invalid = !control.checkValidity();
        control.setAttribute('aria-invalid', String(invalid));
        if (invalid) valid = false;
      });
      if (!valid) {
        status.textContent = 'Please complete the required fields before preparing your inquiry.';
        controls.find((control) => !control.checkValidity())?.focus();
        return;
      }
      status.innerHTML = 'Your inquiry details are ready for the future GoHighLevel connection. Online submission is not active in this preview—please email <a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a> for time-sensitive planning questions.';
    };
    inquiryButton?.addEventListener('click', prepareInquiry);
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      prepareInquiry();
    });
  }
})();
'''


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def build() -> None:
    for path in (CSS, JS, IMAGES):
        path.mkdir(parents=True, exist_ok=True)
    for target, (source, _) in IMAGE_MAP.items():
        copy2(TEMPLATE_IMAGES / source, IMAGES / target)

    write(CSS / "site.css", CSS_TEXT)
    write(JS / "site.js", JS_TEXT)
    write(SITE / PAGES["home"]["path"], page("home", HOME))
    write(SITE / PAGES["venue"]["path"], page("venue", VENUE))
    write(SITE / PAGES["weddings"]["path"], page("weddings", WEDDINGS))
    write(SITE / PAGES["events"]["path"], page("events", EVENTS))
    write(SITE / PAGES["gallery"]["path"], page("gallery", GALLERY))
    write(SITE / PAGES["about"]["path"], page("about", ABOUT))
    write(SITE / PAGES["contact"]["path"], page("contact", CONTACT))
    write(SITE / PAGES["notfound"]["path"], page("notfound", NOT_FOUND))

    routes = """{
  \"routes\": [
    {\"path\": \"/\", \"title\": \"Home\"},
    {\"path\": \"/the-venue/\", \"title\": \"The Venue\"},
    {\"path\": \"/weddings/\", \"title\": \"Weddings\"},
    {\"path\": \"/events/\", \"title\": \"Events\"},
    {\"path\": \"/gallery/\", \"title\": \"Gallery\"},
    {\"path\": \"/about/\", \"title\": \"About\"},
    {\"path\": \"/contact/\", \"title\": \"Contact\"}
  ]
}"""
    write(SITE / "manus-routes.json", routes)
    write(SITE / "robots.txt", """User-agent: *
Allow: /
Sitemap: https://thegrandbyag.com/sitemap.xml
""")
    sitemap_urls = "\n".join(f"  <url><loc>{PRODUCTION_ORIGIN}{item['route']}</loc></url>" for key, item in PAGES.items() if key != "notfound")
    write(SITE / "sitemap.xml", f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">
{sitemap_urls}
</urlset>""")
    write(ASSETS / "images" / "README.md", """# Concept imagery replacement map

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
""")
    write(ROOT / "CONTENT-PLACEHOLDERS.md", """# Content inputs still needed

The first pass intentionally avoids making operational claims that have not been provided. Supply the following only when finalized:

- Venue capacities and room/space names
- Package, pricing, and booking information
- Amenities, inclusions, vendor, food, beverage, décor, parking, staffing, accessibility, and policy details
- Dedicated business phone number and business hours
- GoHighLevel endpoint, authentication method, tag/pipeline logic, and field mapping
- Confirmed public domain / deployment URL and official social accounts
- Actual Grand Venue photography, photo usage permissions, and preferred image credits
- A final wide homepage hero photograph of the completed Grand Venue: dramatic ballroom or reception space, tall ceilings, chandeliers, warm lighting, refined tables/florals, and a central text-safe composition. The current hero is a clearly disclosed generated concept placeholder.
- Any legal/privacy text required for a working lead form
""")
    write(ROOT / "README.md", """# The AG Grand Venue website

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
""")
    write(ROOT / ".gitignore", """.DS_Store
__pycache__/
*.pyc
""")


if __name__ == "__main__":
    build()
    print(f"Generated static site at {SITE}")
