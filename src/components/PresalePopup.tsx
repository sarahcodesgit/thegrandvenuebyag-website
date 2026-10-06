import { useEffect, useState } from 'react';

const STORAGE_KEY = 'ag-grand-2027-presale-dismissed';

export function PresalePopup() {
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    try {
      if (window.sessionStorage.getItem(STORAGE_KEY) !== 'true') {
        const timer = window.setTimeout(() => setIsOpen(true), 900);
        return () => window.clearTimeout(timer);
      }
    } catch {
      const timer = window.setTimeout(() => setIsOpen(true), 900);
      return () => window.clearTimeout(timer);
    }
  }, []);

  useEffect(() => {
    if (!isOpen) return;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') dismiss();
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [isOpen]);

  const dismiss = () => {
    setIsOpen(false);
    try {
      window.sessionStorage.setItem(STORAGE_KEY, 'true');
    } catch {
      // The popup can still close when storage is unavailable.
    }
  };

  if (!isOpen) return null;

  return (
    <div className="presale-popup-backdrop" role="presentation" onMouseDown={(event) => {
      if (event.target === event.currentTarget) dismiss();
    }}>
      <section className="presale-popup" role="dialog" aria-modal="true" aria-labelledby="presale-popup-title">
        <button className="presale-popup-close" type="button" onClick={dismiss} aria-label="Close presale offer">×</button>
        <p className="presale-popup-eyebrow">2027 Presale Now Open</p>
        <h2 id="presale-popup-title">Any Available 2027 Date<br /><em>Only $7,900</em></h2>
        <p className="presale-popup-copy">Celebrate your wedding, quinceañera, or special event at The AG Grand Venue with exclusive presale pricing.</p>
        <div className="presale-popup-proof" aria-label="Presale bookings now available">
          <span aria-hidden="true">★★★★★</span>
          <strong>Presale bookings now available</strong>
        </div>
        <a className="button presale-popup-cta" href="https://tour.thegrandbyag.com/book-a-tour">Check Availability</a>
        <button className="presale-popup-dismiss" type="button" onClick={dismiss}>I’m still exploring</button>
      </section>
    </div>
  );
}
