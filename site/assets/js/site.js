(() => {
  const header = document.querySelector('[data-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-mobile-menu]');

  const setHeaderState = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 24);
  };
  setHeaderState();
  window.addEventListener('scroll', setHeaderState, { passive: true });

  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      toggle.classList.toggle('is-active', !open);
      menu.hidden = open;
      document.body.style.overflow = open ? '' : 'hidden';
    });
    menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.classList.remove('is-active');
      menu.hidden = true;
      document.body.style.overflow = '';
    }));
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
