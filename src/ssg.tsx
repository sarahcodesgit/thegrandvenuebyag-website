import { renderToStaticMarkup } from 'react-dom/server';
import { App } from './App';
import type { RouteKey } from './data/site';

export function renderRoute(route: RouteKey): string {
  return renderToStaticMarkup(<App route={route} />);
}
