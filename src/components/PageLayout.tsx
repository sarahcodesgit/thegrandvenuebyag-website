import type { ReactNode } from 'react';
import type { RouteKey } from '../data/site';
import { SiteFooter } from './SiteFooter';
import { SiteNavigation } from './SiteNavigation';

interface PageLayoutProps {
  currentRoute: RouteKey;
  children: ReactNode;
}

export function PageLayout({ currentRoute, children }: PageLayoutProps) {
  return (
    <>
      <a className="skip-link" href="#main" data-menu-background>Skip to content</a>
      <SiteNavigation currentRoute={currentRoute} />
      <main id="main" data-menu-background>{children}</main>
      <SiteFooter />
    </>
  );
}
