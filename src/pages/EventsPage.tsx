import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function EventsPage() {
  return (
    <>
      <section className="feature-panel panel-dark">
        <div className="container feature-grid">
          <div className="feature-copy reveal"><p className="eyebrow eyebrow-light">Events at The Grand</p><h1 className="display-lg">Celebrate<br /><em>without a template.</em></h1><p>Milestone moments, cultural traditions, gala evenings, and gatherings designed around your people.</p></div>
          <div className="feature-image reveal"><ConceptImage name="gathering" className="tall-image" /></div>
        </div>
      </section>
      <section id="celebrations" className="home-manifesto">
        <div className="container manifesto-grid">
          <div className="manifesto-copy reveal"><p className="eyebrow">Every occasion, elevated</p><h2 className="display-lg">There is always<br /><em>something worth celebrating.</em></h2></div>
          <div className="manifesto-detail reveal"><p className="lead">The AG Grand Venue is envisioned for celebrations that bring generations together, honor traditions, and turn a once-in-a-lifetime occasion into a lasting memory.</p></div>
        </div>
      </section>
      <section className="event-categories container"><article className="category-row reveal"><span>01</span><div><h3>Quinceañeras</h3><p>A milestone celebration with space for heritage, family, and an entrance to remember.</p></div><a href="/contact/#inquiry" className="text-link">Start planning <Arrow /></a></article><article className="category-row reveal"><span>02</span><div><h3>Private Celebrations</h3><p>Birthdays, anniversaries, and the kind of gathering that deserves a proper sense of occasion.</p></div><a href="/contact/#inquiry" className="text-link">Check availability <Arrow /></a></article><article id="private-events" className="category-row reveal"><span>03</span><div><h3>Galas &amp; Corporate Events</h3><p>Polished settings for annual celebrations, fundraisers, company moments, and formal evenings.</p></div><a href="/contact/#inquiry" className="text-link">Plan an event <Arrow /></a></article><article className="category-row reveal"><span>04</span><div><h3>Cultural Celebrations</h3><p>A versatile starting point for celebrations that honor meaningful customs and personal vision.</p></div><a href="/contact/#inquiry" className="text-link">Start a conversation <Arrow /></a></article></section>
      <section className="image-statement image-statement-short"><ConceptImage name="exterior" className="statement-image" /><div className="image-statement-overlay image-statement-overlay-left"><p className="eyebrow eyebrow-light reveal">The Grand Point of View</p><h2 className="display-lg display-light reveal">Big feeling.<br /><em>Beautifully considered.</em></h2></div></section>
      <section className="section-space container split-section"><div className="split-media reveal"><img src="/media/gallery/B+P-40.jpg" className="split-image" alt="" loading="lazy" /></div><div className="split-copy reveal"><p className="eyebrow">Begin with a tour</p><h2 className="display-lg">See what<br /><em>your event could become.</em></h2><p>Tell us the occasion you are imagining and the date you have in mind. The inquiry form is ready to help guide the next conversation.</p><a className="button" href="/contact/#inquiry">Inquire Now <Arrow /></a></div></section>
    </>
  );
}
