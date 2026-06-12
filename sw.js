// Bump CACHE_NAME whenever the precache list or strategy changes.
const CACHE_NAME = 'wwg-v4';

// Relative URLs so the SW works under any base path (e.g. GitHub Pages
// serves this app from /daily-walking/, not the domain root).
const OFFLINE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './bibleData.json'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(OFFLINE_URLS))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    (async () => {
      // cleanup old caches
      const keys = await caches.keys();
      await Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
      await self.clients.claim();
    })()
  );
});

// Network-first for the JSON data file, cache-first (with runtime caching)
// for everything else same-origin.
self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);

  // Only handle same-origin GET requests
  if (url.origin !== location.origin || request.method !== 'GET') return;

  // For the JSON data file, try network first then fall back to cache
  if (url.pathname.endsWith('/bibleData.json') || url.pathname.endsWith('/bibleData_with_tables.json')) {
    event.respondWith(
      fetch(request).then(resp => {
        const copy = resp.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        return resp;
      }).catch(() => caches.match(request))
    );
    return;
  }

  // For navigation and other assets: cache-first, then network, and cache
  // whatever we fetch so the app (incl. the large Bible XML and icons) works
  // fully offline after the first visit.
  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) return cached;
      return fetch(request).then(resp => {
        if (resp.ok) {
          const copy = resp.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        }
        return resp;
      }).catch(() => caches.match('./index.html'));
    })
  );
});
