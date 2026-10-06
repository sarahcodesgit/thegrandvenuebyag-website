import { createRoot, hydrateRoot } from 'react-dom/client';
import { App } from './App';
import { routeFromPath } from './data/site';
import './styles/site.css';

document.documentElement.classList.add('js');

const root = document.getElementById('root');
if (!root) throw new Error('React root element was not found.');

const app = <App route={routeFromPath(window.location.pathname)} />;
if (root.hasChildNodes()) hydrateRoot(root, app);
else createRoot(root).render(app);
