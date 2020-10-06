const staticCacheName = 'site-static-v1';
const dynamicCacheName = 'site-dynamic-v1';

const assets = [
    '/',
    '/static/js/bootstrap.js',
    '/static/js/bootstrap.js.map',
    '/static/js/bootstrap.min.js',
    '/static/js/bootstrap.min.js.map',
    '/static/js/bootstrap.bundle.js',
    '/static/js/bootstrap.bundle.js.map',
    '/static/js/bootstrap.bundle.min.js',
    '/static/js/bootstrap.bundle.min.js.map',
    '/static/css/login.css',
    '/static/css/pass_reset.css',
    '/static/css/sign_up.css',
    '/static/css/bootstrap.css',
    '/static/css/bootstrap.css.map',
    '/static/css/bootstrap.min.css',
    '/static/css/bootstrap.min.css.map',
    '/static/css/bootstrap.css',
    '/static/css/bootstrap-grid.css',
    '/static/css/bootstrap-grid.min.css',
    '/static/css/bootstrap-grid.css.map',
    '/static/css/bootstrap-grid.min.css.map',
    '/static/css/bootstrap-reboot.css',
    '/static/css/bootstrap-reboot.css.map',
    '/static/css/bootstrap-reboot.min.css',
    '/static/css/bootstrap-reboot.min.css.map',
    '/static/images/72x72.png',
    '/static/images/144x144.png',
    '/static/images/192x192.png',
    '/static/images/512x512.png',
    '/static/images/instagram.svg',
    '/static/images/favicon-32x32.png',
    '/static/images/facebook.svg',
    '/static/images/twitter.svg',
    'https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@1,300&display=swap',
    'https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap',
    'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d50482.22492548014!2d-122.42403531959755!3d37.739881787218685!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80859a6d00690021%3A0x4a501367f076adff!2sSan%20Francisco%2C%20CA%2C%20USA!5e0!3m2!1sen!2srw!4v1600580066902!5m2!1sen!2srw',
];

// Install a Service worker 
self.addEventListener('install', evt => {
    // console.log('service worker has been installed');
    evt.waitUntil(
        caches.open(staticCacheName).then(cache => {
            console.log('caching shell assets');
            cache.addAll(assets);
        })
    );
});

// Activate Event
self.addEventListener('activate', evt => {
    // console.log('service worker has been activated');
    evt.waitUntil(
        caches.keys().then( keys => {
            // console.log(keys);
            return Promise.all(keys
                .filter(key => key !== staticCacheName && key !== dynamicCacheName)
                .map(key => caches.delete(key))
                
            )
        })
    );
});

// fetch event
self.addEventListener('fetch', evt => {
  //  console.log('fetch event', evt);
  evt.respondWith(
      caches.match(evt.request).then(cacheRes => {
         return cacheRes || fetch(evt.request).then(fetchRes => {
             return caches.open(dynamicCacheName).then(cache => {
                 cache.put(evt.request.url, fetchRes.clone());
                 limitCacheSize(dynamicCacheName, 20);
                 return fetchRes;
             })
         });
      }).catch(() => caches.match('/offline/'))
  );
});

// cache size limit function
const limitCacheSize = (name, size) => {
    caches.open(name).then(cache => {
        cache.keys().then(keys => {
            if(keys.length > size){
                cache.delete(keys[0]).then(limitCacheSize(name, size));
            }
        })
    })

};