(() => {
  const header = document.querySelector('[data-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-site-menu]');
  const darkSurfaceSelector = '.hero, .panel-dark, .image-statement, .page-hero-dark, .page-hero-image, .contact-hero, .not-found, .site-footer';

  const setHeaderTone = () => {
    if (!header || header.classList.contains('is-menu-open')) return;
    const probeY = Math.min(112, Math.round(window.innerHeight * .14));
    const probe = document.elementFromPoint(Math.round(window.innerWidth / 2), probeY);
    header.classList.toggle('is-light-surface', !probe?.closest(darkSurfaceSelector));
  };
  setHeaderTone();
  window.addEventListener('scroll', setHeaderTone, { passive: true });
  window.addEventListener('resize', setHeaderTone);

  if (toggle && menu) {
    const closeMenu = () => {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation');
      toggle.classList.remove('is-active');
      header.classList.remove('is-menu-open');
      menu.classList.remove('is-open');
      menu.hidden = true;
      document.body.style.overflow = '';
      setHeaderTone();
    };
    const openMenu = () => {
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close navigation');
      toggle.classList.add('is-active');
      header.classList.add('is-menu-open');
      menu.hidden = false;
      document.body.style.overflow = 'hidden';
      requestAnimationFrame(() => menu.classList.add('is-open'));
      menu.querySelector('[data-menu-link]')?.focus();
    };
    const menuFocusable = () => [
      toggle,
      ...menu.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])'),
    ].filter((element) => !element.hasAttribute('disabled'));
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      if (open) closeMenu(); else openMenu();
    });
    menu.querySelectorAll('[data-menu-link]').forEach((link) => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu();
        toggle.focus();
      }
      if (event.key === 'Tab' && toggle.getAttribute('aria-expanded') === 'true') {
        const items = menuFocusable();
        const first = items[0];
        const last = items[items.length - 1];
        if (!first || !last) return;
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    });
  }

  const items = document.querySelectorAll('.reveal');
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: .12, rootMargin: '0px 0px -28px' });
    items.forEach((item) => observer.observe(item));
  } else {
    items.forEach((item) => item.classList.add('is-visible'));
  }

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  const form = document.querySelector('[data-inquiry-form]');
  const status = document.querySelector('[data-form-status]');
  const inquiryButton = document.querySelector('[data-inquiry-button]');
  if (form && status) {
    const prepareInquiry = () => {
      const controls = [...form.querySelectorAll('input[required], select[required], textarea[required]')];
      let valid = true;
      controls.forEach((control) => {
        const invalid = !control.checkValidity();
        control.setAttribute('aria-invalid', String(invalid));
        if (invalid) valid = false;
      });
      if (!valid) {
        status.textContent = 'Please complete the required fields before preparing your inquiry.';
        controls.find((control) => !control.checkValidity())?.focus();
        return;
      }
      status.innerHTML = 'Your inquiry details are ready for the future GoHighLevel connection. Online submission is not active in this preview—please email <a href="mailto:info@thegrandbyag.com">info@thegrandbyag.com</a> for time-sensitive planning questions.';
    };
    inquiryButton?.addEventListener('click', prepareInquiry);
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      prepareInquiry();
    });
  }
})();
