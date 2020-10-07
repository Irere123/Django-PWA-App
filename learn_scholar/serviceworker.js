var staticCacheName = "static-site-v1" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/bootstrap.css',
    '/static/js/boostrap.js',
    '/static/images/icons/72x72.png',
    '/static/images/icons/96x96.png',
    '/static/images/icons/128x128.png',
    '/static/images/icons/144x144.png',
    '/static/images/icons/152x152.png',
    '/static/images/icons/192x192.png',
    '/static/images/icons/384x384.png',
    '/static/images/icons/512x512.png',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});