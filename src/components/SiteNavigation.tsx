import { useEffect, useRef, useState } from 'react';
import { navigation, routes, type RouteKey } from '../data/site';

const darkSurfaceSelector = '.hero, .panel-dark, .image-statement, .page-hero-dark, .page-hero-image, .contact-hero, .not-found, .site-footer';
const closeDuration = 460;
type MenuState = 'closed' | 'opening' | 'open' | 'closing';

interface SiteNavigationProps {
  currentRoute: RouteKey;
}

function Brand({ className }: { className: string }) {
  return (
    <a className={className} href="/" aria-label="The AG Grand Venue home">
      <span className="header-brand-name">THE AG GRAND VENUE</span>
      <span className="header-brand-subline">North Houston · Weddings · Private Events</span>
    </a>
  );
}

export function SiteNavigation({ currentRoute }: SiteNavigationProps) {
  const headerRef = useRef<HTMLElement>(null);
  const toggleRef = useRef<HTMLButtonElement>(null);
  const dialogRef = useRef<HTMLDivElement>(null);
  const closeTimer = useRef<number | undefined>(undefined);
  const openFrame = useRef<number | undefined>(undefined);
  const restoreFocus = useRef(false);
  const [menuState, setMenuState] = useState<MenuState>('closed');
  const menuIsActive = menuState !== 'closed';
  const cancelPendingOpen = () => {
    if (openFrame.current !== undefined) {
      window.cancelAnimationFrame(openFrame.current);
      openFrame.current = undefined;
    }
  };

  useEffect(() => {
    const header = headerRef.current;
    if (!header) return undefined;

    const setHeaderTone = () => {
      if (menuIsActive) return;
      const probeY = Math.min(112, Math.round(window.innerHeight * 0.14));
      const probe = document.elementFromPoint(Math.round(window.innerWidth / 2), probeY);
      header.classList.toggle('is-light-surface', !probe?.closest(darkSurfaceSelector));
    };

    setHeaderTone();
    window.addEventListener('scroll', setHeaderTone, { passive: true });
    window.addEventListener('resize', setHeaderTone);
    return () => {
      window.removeEventListener('scroll', setHeaderTone);
      window.removeEventListener('resize', setHeaderTone);
    };
  }, [menuIsActive]);

  useEffect(() => {
    const targets = [
      document.querySelector('.skip-link'),
      headerRef.current?.querySelector('.header-inner'),
      document.querySelector('main'),
      document.querySelector('footer'),
    ].filter((element): element is HTMLElement => element instanceof HTMLElement);

    targets.forEach((element) => {
      element.toggleAttribute('inert', menuIsActive);
      if (menuIsActive) element.setAttribute('aria-hidden', 'true');
      else element.removeAttribute('aria-hidden');
    });
    document.body.style.overflow = menuIsActive ? 'hidden' : '';

    return () => {
      targets.forEach((element) => {
        element.removeAttribute('inert');
        element.removeAttribute('aria-hidden');
      });
      document.body.style.overflow = '';
    };
  }, [menuIsActive]);

  useEffect(() => {
    if (menuState !== 'closed' || !restoreFocus.current) return undefined;
    const frame = window.requestAnimationFrame(() => {
      toggleRef.current?.focus();
      restoreFocus.current = false;
    });
    return () => window.cancelAnimationFrame(frame);
  }, [menuState]);

  useEffect(() => {
    if (menuState !== 'opening') return undefined;
    const frame = window.requestAnimationFrame(() => setMenuState('open'));
    openFrame.current = frame;
    window.requestAnimationFrame(() => dialogRef.current?.querySelector<HTMLElement>('[data-menu-link]')?.focus());
    return () => window.cancelAnimationFrame(frame);
  }, [menuState]);

  useEffect(() => {
    if (menuState !== 'closing') return undefined;
    closeTimer.current = window.setTimeout(() => {
      setMenuState('closed');
    }, closeDuration);
    return () => window.clearTimeout(closeTimer.current);
  }, [menuState]);

  useEffect(() => () => {
    window.clearTimeout(closeTimer.current);
    cancelPendingOpen();
  }, []);

  const openMenu = () => {
    window.clearTimeout(closeTimer.current);
    cancelPendingOpen();
    restoreFocus.current = false;
    setMenuState('opening');
  };
  const closeMenu = (shouldRestoreFocus = true) => {
    if (menuState === 'closed' || menuState === 'closing') return;
    cancelPendingOpen();
    restoreFocus.current = shouldRestoreFocus;
    setMenuState('closing');
  };
  const handleToggle = () => (menuIsActive ? closeMenu() : openMenu());

  useEffect(() => {
    if (!menuIsActive) return undefined;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closeMenu();
      if (event.key !== 'Tab') return;
      const controls = [...(dialogRef.current?.querySelectorAll<HTMLElement>('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])') ?? [])];
      const first = controls[0];
      const last = controls.at(-1);
      if (!first || !last) return;
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [menuIsActive, menuState]);

  const menuClassName = [
    'site-menu',
    menuState === 'open' ? 'is-open' : '',
    menuState === 'closing' ? 'is-closing' : '',
  ].filter(Boolean).join(' ');
  const currentPath = routes[currentRoute].path;

  return (
    <header ref={headerRef} className={`site-header${menuIsActive ? ' is-menu-open' : ''}`} data-header>
      <div className="header-inner">
        <a className="header-cta" href="/contact/#inquiry">Schedule a Tour</a>
        <Brand className="header-brand" />
        <button
          ref={toggleRef}
          className={`menu-toggle${menuIsActive ? ' is-active' : ''}`}
          type="button"
          aria-expanded={menuIsActive}
          aria-controls="site-menu"
          aria-label={menuIsActive ? 'Close navigation' : 'Open navigation'}
          onClick={handleToggle}
        >
          <span className="sr-only">{menuIsActive ? 'Close navigation' : 'Open navigation'}</span><span /><span />
        </button>
      </div>
      <div ref={dialogRef} id="site-menu" className={menuClassName} role="dialog" aria-modal="true" aria-label="Site navigation" hidden={menuState === 'closed'}>
        <div className="site-menu-topbar">
          <a className="site-menu-cta" href="/contact/#inquiry" onClick={() => closeMenu(false)}>Schedule a Tour</a>
          <Brand className="site-menu-brand" />
          <button className="site-menu-close" type="button" aria-label="Close navigation" onClick={() => closeMenu()}>
            <span className="sr-only">Close navigation</span><span /><span />
          </button>
        </div>
        <div className="site-menu-inner container">
          <nav className="site-menu-nav" aria-label="Primary navigation">
            {navigation.map((item) => (
              <a key={item.href} href={item.href} aria-current={item.href === currentPath ? 'page' : undefined} data-menu-link onClick={() => closeMenu(false)}>{item.label}</a>
            ))}
          </nav>
          <div className="site-menu-meta"><span>2103 FM 1960 Rd W · Houston, TX 77090</span></div>
        </div>
      </div>
    </header>
  );
}
