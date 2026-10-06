import type { MediaKey } from '../data/site';
import { media } from '../data/site';

interface ConceptImageProps {
  name: MediaKey;
  className?: string;
  eager?: boolean;
}

export function ConceptImage({ name, className = '', eager = false }: ConceptImageProps) {
  const image = media[name];

  return (
    <figure className={`image-frame ${className}`.trim()} data-concept-image>
      <img
        src={image.src}
        alt={image.alt}
        loading={eager ? 'eager' : 'lazy'}
        fetchPriority={eager ? 'high' : undefined}
      />
      <figcaption>{image.caption}</figcaption>
    </figure>
  );
}
