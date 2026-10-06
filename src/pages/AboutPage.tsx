import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

const directionsUrl = 'https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090';

export function AboutPage() {
  return (
    <>
      <section className="page-hero page-hero-dark"><div className="container page-hero-grid"><div className="page-hero-copy"><p className="eyebrow eyebrow-light reveal">About The Grand</p><h1 className="display-hero display-light reveal">A new point of view<br /><em>for North Houston.</em></h1><p className="lead lead-light reveal">The AG Grand Venue is a new destination for people who believe milestone moments deserve meaningful settings.</p></div><div className="page-hero-image reveal"><ConceptImage name="exterior" className="portrait-image" /></div></div></section>
      <section className="section-space container intro-section intro-section-tight"><div className="section-index reveal">01 <span>The AG point of view</span></div><div className="intro-copy reveal"><p className="eyebrow">More than a backdrop</p><h2 className="display-xl">Made for the moments<br />that <em>bring people together.</em></h2><p className="lead">From the AG family of venues comes a new idea for Houston celebrations: a place imagined with a grander perspective, an editorial sensibility, and space for occasions that are entirely your own.</p><p>It is not a template for someone else’s event. It is a starting point for yours.</p></div></section>
      <section className="panel-warm about-location"><div className="container about-location-grid"><div className="reveal"><p className="eyebrow">Located in North Houston</p><h2 className="display-lg">A new address<br /><em>for unforgettable occasions.</em></h2></div><div className="address-block reveal"><p>2103 FM 1960 Rd W<br />Houston, TX 77090</p><a className="text-link" href={directionsUrl} target="_blank" rel="noopener">Get directions <Arrow /></a></div></div></section>
      <section className="section-space container split-section split-section-reverse"><div className="split-copy reveal"><p className="eyebrow">The next chapter</p><h2 className="display-lg">Be among the first<br /><em>to experience The Grand.</em></h2><p>We are looking ahead to the celebrations, traditions, and milestone events this new venue will welcome. Start the conversation with an inquiry or request a private tour.</p><a className="button" href="/contact/#inquiry">Get in Touch <Arrow /></a></div><div className="split-media reveal"><ConceptImage name="light" className="split-image" /></div></section>
    </>
  );
}
