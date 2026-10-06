import { Arrow } from '../components/Arrow';
import { InquiryForm } from '../components/InquiryForm';

const directionsUrl = 'https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090';

export function ContactPage() {
  return (
    <>
      <section id="inquiry" className="inquiry-section section-space container"><div className="inquiry-intro reveal"><p className="eyebrow">Start Planning</p><h1 className="display-lg">Schedule Your<br /><em>Private Tour</em></h1><div className="contact-details inquiry-contact-details"><span className="footer-label">Visit</span><p>2103 FM 1960 Rd W<br />Houston, TX 77090</p><span className="footer-label">Email</span><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a><span className="footer-label">Phone</span><a href="tel:+13465978215">+1 346-597-8215</a></div></div><InquiryForm /></section>
      <section className="location-cta panel-warm"><div className="container location-grid"><div className="reveal"><p className="eyebrow">Plan a visit</p><h2 className="display-lg">The first step is<br /><em>seeing the possibility.</em></h2></div><div className="location-detail reveal"><p>Schedule a private tour or begin a conversation at<br /><a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a></p><a className="text-link" href={directionsUrl} target="_blank" rel="noopener">Get directions <Arrow /></a></div></div></section>
    </>
  );
}
