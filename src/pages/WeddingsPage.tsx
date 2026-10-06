import { Arrow } from '../components/Arrow';
import { ConceptImage } from '../components/ConceptImage';

export function WeddingsPage() {
  return (
    <>
      <section className="feature-panel panel-dark">
        <div className="container feature-grid">
          <div className="feature-copy reveal"><p className="eyebrow eyebrow-light">Weddings at The Grand</p><h1 className="display-lg">Make the moment<br /><em>monumental.</em></h1><p>A new North Houston setting for the ceremony, reception, and every unforgettable moment in between.</p><a className="button button-outline-light" href="/contact/#inquiry">Start Planning <Arrow /></a></div>
          <div className="feature-image reveal"><ConceptImage name="ceremony" className="tall-image" eager /></div>
        </div>
      </section>
      <section className="section-space container intro-section intro-section-tight"><div className="section-index reveal">01 <span>Your wedding, in focus</span></div><div className="intro-copy reveal"><p className="eyebrow">A day with a point of view</p><h2 className="display-xl">The best celebrations<br />feel <em>entirely personal.</em></h2><p className="lead">Whether your vision is romantic and candlelit, modern and minimal, or alive with color and tradition, your wedding should reflect the two people at its center. The AG Grand Venue is being created for that kind of possibility.</p></div></section>
      <section className="event-arc panel-warm"><div className="container"><div className="arc-intro reveal"><p className="eyebrow">The wedding journey</p><h2 className="display-lg">From the first look<br /><em>to the last dance.</em></h2></div><div className="arc-grid"><article className="arc-card reveal"><span>01</span><h3>The Arrival</h3><p>The anticipation, the welcome, and the first glimpse of a day that feels different from every other.</p></article><article className="arc-card reveal"><span>02</span><h3>The Ceremony</h3><p>The quiet before the vows, the people closest to you, and a setting worthy of the promise.</p></article><article className="arc-card reveal"><span>03</span><h3>The Celebration</h3><p>A celebration in motion, a full dance floor, and the kind of joy that refuses to be rushed.</p></article></div></div></section>
      <section className="section-space container split-section split-section-reverse"><div className="split-copy reveal"><p className="eyebrow">A new beginning</p><h2 className="display-lg">The story is yours.<br /><em>The setting is The Grand.</em></h2><p>Share the first details of your date and vision, and our team will be ready to begin the conversation. Event details, availability, and tour information will be tailored once they are confirmed.</p><a className="text-link" href="/contact/#inquiry">Inquire about your wedding <Arrow /></a></div><div className="split-media reveal"><ConceptImage name="terrace" className="split-image" /></div></section>
      <section className="cta-section panel-dark"><div className="container centered-cta reveal"><p className="eyebrow eyebrow-light">Your next chapter</p><h2 className="display-lg display-light">Come see what<br /><em>could unfold here.</em></h2><a className="button button-light" href="/contact/#inquiry">Schedule a Tour <Arrow /></a></div></section>
    </>
  );
}
