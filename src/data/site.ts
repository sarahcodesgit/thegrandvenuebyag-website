export const PRODUCTION_ORIGIN = 'https://thegrandbyag.com';

export type RouteKey =
  | 'home'
  | 'venue'
  | 'weddings'
  | 'events'
  | 'gallery'
  | 'about'
  | 'contact'
  | 'notFound';

export interface RouteMeta {
  key: RouteKey;
  path: string;
  bodyClass: string;
  title: string;
  description: string;
  noindex?: boolean;
}

export const routes: Record<RouteKey, RouteMeta> = {
  home: {
    key: 'home', path: '/', bodyClass: 'page page-home',
    title: 'Luxury Wedding Venue in Houston | The AG Grand',
    description: 'The AG Grand Venue is a luxury wedding and private event venue in North Houston for celebrations with a grander point of view.',
  },
  venue: {
    key: 'venue', path: '/the-venue/', bodyClass: 'page page-venue',
    title: 'The Venue | The AG Grand Venue in Houston',
    description: 'Discover the editorial vision behind The AG Grand Venue, a new luxury setting for weddings and private events in North Houston.',
  },
  weddings: {
    key: 'weddings', path: '/weddings/', bodyClass: 'page page-weddings',
    title: 'Houston Wedding Venue | The AG Grand Venue',
    description: 'Plan a wedding with a grander sense of occasion at The AG Grand Venue, a luxury Houston setting for meaningful celebrations.',
  },
  events: {
    key: 'events', path: '/events/', bodyClass: 'page page-events',
    title: 'Private Event Venue Houston | The AG Grand Venue',
    description: 'Explore a new North Houston setting for quinceañeras, private celebrations, corporate events, and gala-worthy occasions.',
  },
  gallery: {
    key: 'gallery', path: '/gallery/', bodyClass: 'page page-gallery',
    title: 'Gallery | The AG Grand Venue, North Houston',
    description: 'Explore the visual direction for The AG Grand Venue through conceptual editorial imagery and a grand celebration point of view.',
  },
  about: {
    key: 'about', path: '/about/', bodyClass: 'page page-about',
    title: 'About The AG Grand Venue | North Houston',
    description: 'Learn about The AG Grand Venue, a new luxury wedding and private-events destination in North Houston, Texas.',
  },
  contact: {
    key: 'contact', path: '/contact/', bodyClass: 'page page-contact',
    title: 'Contact The AG Grand Venue | Schedule a Tour',
    description: 'Schedule a tour or start planning a wedding or private event at The AG Grand Venue in North Houston, Texas.',
  },
  notFound: {
    key: 'notFound', path: '/404.html', bodyClass: 'page page-notfound',
    title: 'Page Not Found | The AG Grand Venue',
    description: 'The page you requested is not available. Return to The AG Grand Venue to explore weddings and private events in North Houston.',
    noindex: true,
  },
};

export const navigation = [
  { label: 'Home', href: '/' },
  { label: 'The Venue', href: '/the-venue/' },
  { label: 'Weddings', href: '/weddings/' },
  { label: 'Events', href: '/events/' },
  { label: 'Gallery', href: '/gallery/' },
  { label: 'About', href: '/about/' },
  { label: 'Contact', href: '/contact/' },
] as const;

export const media = {
  hero: {
    src: '/media/concept/grand-ballroom-hero1.webp',
    alt: 'Conceptual luxury ballroom wedding reception with chandeliers and elegant floral tables; this is not The AG Grand Venue.',
    caption: '',
  },
  arrival: {
    src: '/media/concept/arrival-study.png',
    alt: 'Conceptual editorial image of a floral arrival moment; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  space: {
    src: '/media/concept/space-study.jpg',
    alt: 'Conceptual architectural image of a light-filled gathering space; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  ceremony: {
    src: '/media/concept/ceremony-study.png',
    alt: 'Conceptual ceremony table and floral study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  exterior: {
    src: '/media/concept/grand-ballroom-hero1.webp',
    alt: 'Conceptual exterior and arrival study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  terrace: {
    src: '/media/concept/terrace-study.png',
    alt: 'Conceptual outdoor celebration study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  gathering: {
    src: '/media/concept/gathering-study.png',
    alt: 'Conceptual evening gathering study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  light: {
    src: '/media/concept/light-study.png',
    alt: 'Conceptual interior light and styling study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  atmosphere: {
    src: '/media/concept/atmosphere-study.png',
    alt: 'Conceptual warm architectural atmosphere study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
  landscape: {
    src: '/media/concept/landscape-study.png',
    alt: 'Conceptual open-air landscape study; this is not The AG Grand Venue.',
    caption: 'Concept imagery — layout and mood study only',
  },
} as const;

export type MediaKey = keyof typeof media;

export function routeFromPath(pathname: string): RouteKey {
  const normalized = pathname.endsWith('/') ? pathname : `${pathname}/`;
  const exact = Object.values(routes).find((route) => route.path === pathname || route.path === normalized);
  return exact?.key ?? 'notFound';
}

export function canonicalFor(route: RouteMeta): string {
  return `${PRODUCTION_ORIGIN}${route.path}`;
}
