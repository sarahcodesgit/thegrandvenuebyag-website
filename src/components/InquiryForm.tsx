import { useState, type FormEvent } from 'react';
import { Arrow } from './Arrow';

const webhookUrl = 'https://services.leadconnectorhq.com/hooks/xQD7Uz8Skgy9p1XWz7Mx/webhook-trigger/a3c01691-06d8-4692-abf4-03445987ba10';

export function InquiryForm() {
  const [status, setStatus] = useState<React.ReactNode>('');
  const [submitting, setSubmitting] = useState(false);

  const submitInquiry = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget;
    const controls = [...form.querySelectorAll<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>('input[required], select[required], textarea[required]')];
    const invalidControl = controls.find((control) => !control.checkValidity());
    controls.forEach((control) => control.setAttribute('aria-invalid', String(!control.checkValidity())));

    if (invalidControl) {
      setStatus('Please complete the required fields before submitting your inquiry.');
      invalidControl.focus();
      return;
    }

    const formData = new FormData(form);
    const payload = {
      full_name: String(formData.get('full_name') ?? ''),
      phone: String(formData.get('phone') ?? ''),
      email: String(formData.get('email') ?? ''),
      event_type: String(formData.get('event_type') ?? ''),
      source: window.location.pathname === '/' ? 'Homepage' : 'Contact Page',
    };

    setSubmitting(true);
    setStatus('Submitting your inquiry…');

    try {
      const response = await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!response.ok) throw new Error(`Webhook returned ${response.status}`);

      form.reset();
      controls.forEach((control) => control.removeAttribute('aria-invalid'));
      setStatus('Thank you! Your inquiry has been submitted. Our team will be in touch soon.');
    } catch {
      setStatus(<>We couldn't submit your inquiry right now. Please email <a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a> and our team will help you.</>);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form className="inquiry-form reveal" data-inquiry-form noValidate onSubmit={submitInquiry}>
      <div className="form-grid">
        <label className="form-full">Full Name *<input name="full_name" autoComplete="name" required /></label>
        <label className="form-full">Phone Number *<input type="tel" name="phone" autoComplete="tel" required /></label>
        <label className="form-full">Email Address *<input type="email" name="email" autoComplete="email" required /></label>
        <label className="form-full">Event Type<select name="event_type" defaultValue=""><option value="" disabled>Select an event type</option><option>Wedding</option><option>Quinceañera</option><option>Private Celebration</option><option>Corporate Event or Gala</option><option>Cultural Celebration</option><option>Other</option></select></label>
      </div>
      <div className="form-action">
        <button className="button" type="submit" data-inquiry-button disabled={submitting}>{submitting ? 'Submitting…' : 'Submit My Inquiry'} {!submitting && <Arrow />}</button>
      </div>
      <p className="form-status" data-form-status role="status" aria-live="polite">{status}</p>
    </form>
  );
}
