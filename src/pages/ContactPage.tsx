import { Arrow } from '../components/Arrow';
import { InquiryForm } from '../components/InquiryForm';

const directionsUrl = 'https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090';

export function ContactPage() {
  return (
    <>
      <section className="contact-hero panel-dark"><div className="container contact-hero-grid"><div className="contact-heading"><p className="eyebrow eyebrow-light reveal">Contact The Grand</p><h1 className="display-hero display-light reveal">Let’s make space<br /><em>for something memorable.</em></h1><p className="lead lead-light reveal">Share a few details about the occasion you are planning, and we’ll be ready to begin the conversation.</p></div><div className="contact-details reveal"><span className="footer-label">Visit</span><p>2103 FM 1960 Rd W<br />Houston, TX 77090</p><span className="footer-label">Email</span><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a></div></div></section>
      <section id="inquiry" className="inquiry-section section-space container"><div className="inquiry-intro reveal"><p className="eyebrow">Start Planning</p><h2 className="display-lg">Tell us a little<br /><em>about your event.</em></h2><p>This form is prepared for the future Grand Venue GoHighLevel connection. Until online delivery is configured, please use the email address above for time-sensitive inquiries.</p></div><InquiryForm /></section>
      <section className="location-cta panel-warm"><div className="container location-grid"><div className="reveal"><p className="eyebrow">Plan a visit</p><h2 className="display-lg">The first step is<br /><em>seeing the possibility.</em></h2></div><div className="location-detail reveal"><p>Schedule a private tour or begin a conversation at<br /><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a></p><a className="text-link" href={directionsUrl} target="_blank" rel="noopener">Get directions <Arrow /></a></div></div></section>
    </>
  );
}
