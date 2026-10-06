import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function VenuePage() {
  return (
    <>
      <section className="page-hero page-hero-dark">
        <div className="container page-hero-grid"><div className="page-hero-copy"><p className="eyebrow eyebrow-light reveal">The Venue</p><h1 className="display-hero display-light reveal">A setting with<br /><em>its own sense of ceremony.</em></h1><p className="lead lead-light reveal">The AG Grand Venue is being shaped as an architectural canvas for Houston’s most meaningful gatherings.</p></div><div className="page-hero-image reveal"><ConceptImage name="space" className="portrait-image" /></div></div>
      </section>
      <section className="section-space container split-section"><div className="split-media reveal"><ConceptImage name="arrival" className="split-image" /></div><div className="split-copy reveal"><p className="eyebrow">The First Impression</p><h2 className="display-lg">It begins<br /><em>before the first toast.</em></h2><p>There is a difference between a place to host an event and a place that sets the tone for it. The Grand is imagined for the instant guests arrive, the pause before a processional, and the energy that carries a celebration late into the evening.</p><p>As venue details and photography are finalized, this space will become a closer look at the experience, spaces, and possibilities that make the setting distinct.</p></div></section>
      <section className="panel-warm story-band"><div className="container story-grid"><div className="section-index reveal">01 <span>Intentional by design</span></div><div className="reveal"><h2 className="display-lg">Space for a vision.<br /><em>Presence for a memory.</em></h2><p className="lead">A grand venue should feel polished enough to elevate a celebration—and open enough to let it become unmistakably yours.</p></div></div></section>
      <section className="section-space container image-pair"><div className="reveal"><ConceptImage name="light" className="pair-image pair-image-left" /></div><div className="pair-copy reveal"><p className="eyebrow">The Grand Experience</p><h2 className="display-lg">A little more<br /><em>occasion in every detail.</em></h2><p>From romantic weddings to high-energy celebrations and formal gatherings, the strongest event design starts with a point of view. The Grand offers the beginning; your people, traditions, and imagination complete the story.</p><a className="text-link" href="/contact/#inquiry">Schedule a private tour <Arrow /></a></div><div className="reveal"><ConceptImage name="atmosphere" className="pair-image pair-image-right" /></div></section>
      <section className="cta-section panel-dark"><div className="container centered-cta reveal"><p className="eyebrow eyebrow-light">See it in person</p><h2 className="display-lg display-light">Let the setting<br /><em>do the talking.</em></h2><a className="button button-light" href="/contact/#inquiry">Schedule a Tour <Arrow /></a></div></section>
    </>
  );
}
