import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function VenuePage() {
  return (
    <>
      <section className="home-manifesto">
        <div className="container manifesto-grid">
          <div className="manifesto-copy reveal"><p className="eyebrow">The First Impression</p><h1 className="display-lg">It begins<br /><em>before the first toast.</em></h1></div>
          <div className="manifesto-detail reveal"><p className="lead">There is a difference between a place to host an event and a place that sets the tone for it.</p><p>The Grand is imagined for the instant guests arrive, the pause before a processional, and the energy that carries a celebration late into the evening.</p><p>As venue details and photography are finalized, this space will become a closer look at the experience, spaces, and possibilities that make the setting distinct.</p></div>
        </div>
      </section>
      <section className="section-space container venue-experience-centered">
        <div className="pair-copy reveal"><p className="eyebrow">The Grand Experience</p><h2 className="display-lg">A little more<br /><em>occasion in every detail.</em></h2><p>From romantic weddings to high-energy celebrations and formal gatherings, the strongest event design starts with a point of view. The Grand offers the beginning; your people, traditions, and imagination complete the story.</p><a className="text-link" href="/contact/#inquiry">Schedule a private tour <Arrow /></a></div>
      </section>
      <section className="venue-gallery-marquee" aria-label="Venue gallery preview">
        <div className="venue-gallery-track">
          <img src="/media/gallery/390A0334.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0358.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0380.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0470.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0524.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/asian american-2.png" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-11.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-12.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-14.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-22.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-27.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-40.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-49.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0334.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0358.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0380.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0470.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/390A0524.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/asian american-2.png" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-11.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-12.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-14.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-22.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-27.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-40.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-49.jpg" className="venue-gallery-image" alt="" loading="lazy" />
          <ConceptImage name="ceremony" className="venue-gallery-image" />
          <ConceptImage name="terrace" className="venue-gallery-image" />
          <ConceptImage name="gathering" className="venue-gallery-image" />
          <ConceptImage name="light" className="venue-gallery-image" />
          <ConceptImage name="atmosphere" className="venue-gallery-image" />
          <ConceptImage name="landscape" className="venue-gallery-image" />
        </div>
        <div className="venue-gallery-cta"><a className="text-link" href="/gallery/">Explore the full gallery <Arrow /></a></div>
      </section>
      <section className="cta-section panel-dark"><div className="container centered-cta reveal"><p className="eyebrow eyebrow-light">See it in person</p><h2 className="display-lg display-light">Let the setting<br /><em>do the talking.</em></h2><a className="button button-light" href="/contact/#inquiry">Schedule a Tour <Arrow /></a></div></section>
    </>
  );
}
