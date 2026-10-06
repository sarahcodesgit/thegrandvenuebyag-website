import { useState, type FormEvent } from 'react';
import { Arrow } from './Arrow';

export function InquiryForm() {
  const [status, setStatus] = useState<React.ReactNode>('');

  const prepareInquiry = (event?: FormEvent<HTMLFormElement>) => {
    event?.preventDefault();
    const form = event?.currentTarget ?? document.querySelector<HTMLFormElement>('[data-inquiry-form]');
    if (!form) return;
    const controls = [...form.querySelectorAll<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>('input[required], select[required], textarea[required]')];
    const invalidControl = controls.find((control) => !control.checkValidity());
    controls.forEach((control) => control.setAttribute('aria-invalid', String(!control.checkValidity())));
    if (invalidControl) {
      setStatus('Please complete the required fields before preparing your inquiry.');
      invalidControl.focus();
      return;
    }
    setStatus(<>Your inquiry details are ready for the future GoHighLevel connection. Online submission is not active in this preview—please email <a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a> for time-sensitive planning questions.</>);
  };

  return (
    <form className="inquiry-form reveal" data-inquiry-form noValidate onSubmit={prepareInquiry}>
      <div className="form-grid">
        <label className="form-full">Full Name *<input name="full_name" autoComplete="name" required /></label>
        <label className="form-full">Phone Number *<input type="tel" name="phone" autoComplete="tel" required /></label>
        <label className="form-full">Email Address *<input type="email" name="email" autoComplete="email" required /></label>
        <label className="form-full">Event Type<select name="event_type" defaultValue=""><option value="" disabled>Select an event type</option><option>Wedding</option><option>Quinceañera</option><option>Private Celebration</option><option>Corporate Event or Gala</option><option>Cultural Celebration</option><option>Other</option></select></label>
      </div>
      <div className="form-action">
        <button className="button" type="submit" data-inquiry-button>Prepare My Inquiry <Arrow /></button>
      </div>
      <p className="form-status" data-form-status role="status" aria-live="polite">{status}</p>
    </form>
  );
}
