import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';
import { InquiryForm } from '../components/InquiryForm';

export function HomePage() {
  return (
    <>
      <section className="hero hero-home" aria-labelledby="home-hero-title">
        <ConceptImage name="hero" className="hero-image hero-concept-image" eager />
        <div className="hero-overlay" />
        <div className="hero-center container">
          <p className="hero-eyebrow">North Houston · Weddings · Private Events</p>
          <h1 id="home-hero-title" className="hero-title hero-title-centered"><span className="hero-line"><span>Grand Moments</span></span><span className="hero-line"><em>Deserve a Grand Setting.</em></span></h1>
        </div>
      </section>
      <section id="our-point-of-view" className="home-manifesto">
        <div className="container manifesto-grid">
          <div className="manifesto-copy reveal"><p className="eyebrow">The AG Grand Venue</p><h2 className="display-lg">A place for moments<br /><em>that ask for more.</em></h2></div>
          <div className="manifesto-detail reveal"><p className="lead">A new North Houston setting for ceremonies, celebrations, and gatherings with a sense of occasion.</p><p>Here, the anticipation of arrival, the meaning of tradition, and the energy of the room all have space to unfold. The Grand is imagined for the memories that deserve to feel singular from the very first moment.</p><a className="text-link" href="/the-venue/">Discover The Venue <Arrow /></a></div>
        </div>
      </section>
      <section className="feature-panel panel-dark">
        <div className="container feature-grid">
          <div className="feature-copy reveal"><p className="eyebrow eyebrow-light">The Venue Experience</p><h2 className="display-lg">Make an entrance.<br /><em>Then make it yours.</em></h2><p>Every unforgettable event begins with a setting that invites possibility. Explore the visual language and intentional atmosphere behind The AG Grand Venue.</p><a className="button button-outline-light" href="/the-venue/">Explore The Venue <Arrow /></a></div>
          <div className="feature-image reveal"><ConceptImage name="space" className="tall-image" /></div>
        </div>
      </section>
      <section className="section-space container editorial-section">
        <p className="eyebrow reveal">Every celebration, elevated.</p>
        <div className="editorial-header editorial-header-centered reveal"><h2 className="display-xl home-single-line-heading">Your moment. <em>On a grander scale.</em></h2></div>
        <div className="journey-grid">
          <article className="journey-card reveal"><ConceptImage name="ceremony" className="journey-image" /><div className="journey-content"><span>01</span><h3>Weddings</h3><p>For ceremonies, receptions, and every anticipation-filled moment between.</p><a className="text-link" href="/weddings/">Explore weddings <Arrow /></a></div></article>
          <article className="journey-card reveal"><ConceptImage name="terrace" className="journey-image" /><div className="journey-content"><span>02</span><h3>Celebrations</h3><p>Quinceañeras and milestone occasions with space for personal tradition.</p><a className="text-link" href="/events/#celebrations">Discover celebrations <Arrow /></a></div></article>
          <article className="journey-card reveal"><ConceptImage name="gathering" className="journey-image" /><div className="journey-content"><span>03</span><h3>Private &amp; Corporate</h3><p>Galas, gatherings, and events designed to leave an impression.</p><a className="text-link" href="/events/#private-events">Explore events <Arrow /></a></div></article>
        </div>
      </section>
      <section id="home-inquiry" className="inquiry-section section-space container">
        <div className="inquiry-intro reveal"><p className="eyebrow">Start Planning</p><h2 className="display-lg">Schedule Your<br /><em>Private Tour</em></h2><div className="contact-details inquiry-contact-details"><span className="footer-label">Visit</span><p>2103 FM 1960 Rd W<br />Houston, TX 77090</p><span className="footer-label">Email</span><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a><span className="footer-label">Phone</span><a href="tel:+13465978215">+1 346-597-8215</a></div></div>
        <InquiryForm />
      </section>
      <section className="location-cta panel-warm">
        <div className="container reveal"><p className="eyebrow">Visit The Grand</p><h2 className="display-lg">The next chapter <em>starts here.</em></h2></div>
      </section>
    </>
  );
}
