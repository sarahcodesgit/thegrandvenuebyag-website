import { Arrow } from './Arrow';

const directionsUrl = 'https://www.google.com/maps/search/?api=1&query=2103+FM+1960+Rd+W,+Houston,+TX+77090';

export function SiteFooter() {
  return (
    <footer className="site-footer" data-menu-background>
      <div className="footer-top container">
        <div className="footer-brand">
          <a className="brand brand-footer" href="/" aria-label="The AG Grand Venue home">
            <img className="footer-logo-image" src="/media/concept/AGGVLOGOWhite.PNG" alt="The AG Grand Venue" />
          </a>
          <p>A grand setting for the moments that change everything.</p>
        </div>
        <div className="footer-col">
          <span className="footer-label">Visit</span>
          <p>2103 FM 1960 Rd W<br />Houston, TX 77090</p>
          <a href={directionsUrl} target="_blank" rel="noopener">Get directions <Arrow /></a>
        </div>
        <div className="footer-col">
          <span className="footer-label">Inquiries</span>
          <a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a>
          <a href="/contact/#inquiry">Schedule a Tour <Arrow /></a>
        </div>
      </div>
      <div className="footer-bottom container">
        <p>© {new Date().getFullYear()} The AG Grand Venue. All rights reserved.</p>
      </div>
    </footer>
  );
}
