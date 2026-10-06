import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function GalleryPage() {
  return (
    <>
      <section className="home-manifesto">
        <div className="container manifesto-grid">
          <div className="manifesto-copy reveal"><p className="eyebrow">Gallery</p><h1 className="display-lg">The feeling,<br /><em>before the first frame.</em></h1></div>
          <div className="manifesto-detail reveal"><p className="lead">A visual direction for The AG Grand Venue. These inherited concept images demonstrate the intended rhythm, light, and editorial scale—not the physical venue.</p></div>
        </div>
      </section>
      <section className="gallery-page-grid container">
        <div className="gallery-column gallery-column-a reveal">
          <img src="/media/gallery/390A0334.jpg" className="gallery-large" alt="" loading="lazy" />
          <img src="/media/gallery/390A0470.jpg" className="gallery-medium" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-11.jpg" className="gallery-large" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-27.jpg" className="gallery-medium" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-49.jpg" className="gallery-large" alt="" loading="lazy" />
        </div>
        <div className="gallery-column gallery-column-b reveal">
          <img src="/media/gallery/390A0358.jpg" className="gallery-tall" alt="" loading="lazy" />
          <img src="/media/gallery/390A0524.jpg" className="gallery-medium" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-12.jpg" className="gallery-tall" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-40.jpg" className="gallery-medium" alt="" loading="lazy" />
        </div>
        <div className="gallery-column gallery-column-c reveal">
          <img src="/media/gallery/390A0380.jpg" className="gallery-medium" alt="" loading="lazy" />
          <img src="/media/gallery/asian american-2.png" className="gallery-large" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-14.jpg" className="gallery-medium" alt="" loading="lazy" />
          <img src="/media/gallery/B+P-22.jpg" className="gallery-large" alt="" loading="lazy" />
        </div>
      </section>
      <section className="cta-section panel-warm"><div className="container centered-cta reveal"><p className="eyebrow">See the direction in person</p><h2 className="display-lg">Your story belongs<br /><em>at the center of it.</em></h2><a className="button" href="/contact/#inquiry">Schedule a Tour <Arrow /></a></div></section>
    </>
  );
}
