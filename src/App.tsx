import { useEffect } from 'react';
import { PageLayout } from './components/PageLayout';
import { PresalePopup } from './components/PresalePopup';
import { routes, type RouteKey } from './data/site';
import { useSiteEffects } from './hooks/useSiteEffects';
import { ContactPage } from './pages/ContactPage';
import { EventsPage } from './pages/EventsPage';
import { GalleryPage } from './pages/GalleryPage';
import { HomePage } from './pages/HomePage';
import { NotFoundPage } from './pages/NotFoundPage';
import { VenuePage } from './pages/VenuePage';
import { WeddingsPage } from './pages/WeddingsPage';

interface AppProps {
  route: RouteKey;
}

export function App({ route }: AppProps) {
  useSiteEffects();
  const page = routes[route];

  useEffect(() => {
    document.body.className = page.bodyClass;
    document.title = page.title;
  }, [page]);

  const Page = {
    home: HomePage,
    venue: VenuePage,
    weddings: WeddingsPage,
    events: EventsPage,
    gallery: GalleryPage,
    contact: ContactPage,
    notFound: NotFoundPage,
  }[route];

  return <><PageLayout currentRoute={route}><Page /></PageLayout><PresalePopup /></>;
}
