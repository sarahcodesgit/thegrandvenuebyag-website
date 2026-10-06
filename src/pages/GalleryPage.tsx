import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function GalleryPage() {
  return (
    <>
      <section className="gallery-hero container"><p className="eyebrow reveal">Gallery</p><h1 className="display-hero reveal">The feeling,<br /><em>before the first frame.</em></h1><p className="lead reveal">A visual direction for The AG Grand Venue. These inherited concept images demonstrate the intended rhythm, light, and editorial scale—not the physical venue.</p></section>
      <section className="concept-note"><div className="container reveal"><span className="note-mark">†</span><p><strong>Concept imagery notice.</strong> The complete Grand Venue photography library is forthcoming. The images on this page are placeholders from the supplied template, used only to demonstrate layout and mood direction.</p></div></section>
      <section className="gallery-page-grid container"><div className="gallery-column gallery-column-a reveal"><ConceptImage name="arrival" className="gallery-large" /><ConceptImage name="landscape" className="gallery-medium" /></div><div className="gallery-column gallery-column-b reveal"><ConceptImage name="space" className="gallery-tall" /><ConceptImage name="atmosphere" className="gallery-medium" /></div><div className="gallery-column gallery-column-c reveal"><ConceptImage name="ceremony" className="gallery-medium" /><ConceptImage name="terrace" className="gallery-large" /></div></section>
      <section className="cta-section panel-warm"><div className="container centered-cta reveal"><p className="eyebrow">See the direction in person</p><h2 className="display-lg">Your story belongs<br /><em>at the center of it.</em></h2><a className="button" href="/contact/#inquiry">Schedule a Tour <Arrow /></a></div></section>
    </>
  );
}
