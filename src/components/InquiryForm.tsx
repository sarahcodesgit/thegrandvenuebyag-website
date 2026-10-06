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
        <label>First Name<input name="first_name" autoComplete="given-name" required /></label>
        <label>Last Name<input name="last_name" autoComplete="family-name" required /></label>
        <label>Email<input type="email" name="email" autoComplete="email" required /></label>
        <label>Phone<input type="tel" name="phone" autoComplete="tel" required /></label>
        <label>Event Type<select name="event_type" required defaultValue=""><option value="" disabled>Select an event type</option><option>Wedding</option><option>Quinceañera</option><option>Private Celebration</option><option>Corporate Event or Gala</option><option>Cultural Celebration</option><option>Other</option></select></label>
        <label>Preferred Event Date<input type="date" name="preferred_event_date" required /></label>
        <label>Estimated Guest Count<input type="number" name="estimated_guest_count" inputMode="numeric" min="1" placeholder="Optional" /></label>
        <label className="form-full">Tell Us About Your Event<textarea name="message" rows={5} required placeholder="Your vision, occasion, and anything else we should know." /></label>
      </div>
      <div className="form-action">
        <p className="form-disclosure">No CRM is connected yet. This form will not submit event details online in the current preview.</p>
        <button className="button" type="submit" data-inquiry-button>Prepare My Inquiry <Arrow /></button>
      </div>
      <p className="form-status" data-form-status role="status" aria-live="polite">{status}</p>
    </form>
  );
}
