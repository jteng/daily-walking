const CACHE_NAME = 'wwg-v3';
const OFFLINE_URLS = [
  '/',
  '/index.html',
  '/bibleData.json'
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

// Simple fetch handler: try network first for JSON, otherwise cache-first for assets
self.addEventListener('fetch', event => {
  const request = event.request;
  const url = new URL(request.url);

  // Only handle same-origin requests
  if (url.origin !== location.origin) return;

  // For the JSON data file, try network first then fallback to cache
  if (url.pathname.endsWith('/bibleData.json') || url.pathname.endsWith('/bibleData_with_tables.json')) {
    event.respondWith(
      fetch(request).then(resp => {
        // update cache
        const copy = resp.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        return resp;
      }).catch(() => caches.match(request))
    );
    return;
  }

  // For navigation and other assets, try cache then network
  event.respondWith(
    caches.match(request).then(cached => cached || fetch(request).catch(() => caches.match('/index.html')))
  );
});
