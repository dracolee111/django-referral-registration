// Define the cache name and files to cache
const CACHE_NAME = 'app-cache-v1';
const FILES_TO_CACHE = [
    '',
    '/static/assets/css/app.css',
    '/static/assets/js/app.js',
];

// Install the service worker and cache all files
self.addEventListener('install', (event) => {
    console.log('ServiceWorker: Installing...');
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('ServiceWorker: Caching app shell');
            return cache.addAll(FILES_TO_CACHE);
        }),
    );
});

// Activate the service worker and delete old caches
self.addEventListener('activate', (event) => {
    console.log('ServiceWorker: Activating...');
    event.waitUntil(
        caches.keys().then((keyList) => {
            return Promise.all(keyList.map((key) => {
                if (key !== CACHE_NAME) {
                    console.log('ServiceWorker: Removing old cache', key);
                    return caches.delete(key);
                }
            }));
        }),
    );
});

// Fetch resources from cache or network
self.addEventListener('fetch', (event) => {
    console.log('ServiceWorker: Fetching ', event.request.url);
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        }).catch(() => {
            if (event.request.mode === 'navigate' && event.request.method === 'GET') {
                return caches.match(FILES_TO_CACHE);
            }
        }),
    );
});

// Listen for the "beforeinstallprompt" event and show the "Add to Home Screen" button
self.addEventListener('beforeinstallprompt', (event) => {
    event.preventDefault();
    const installButton = document.getElementById('install-button');
    installButton.style.display = 'block';
    installButton.addEventListener('click', () => {
        event.prompt();
        event.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('User accepted the A2HS prompt');
            } else {
                console.log('User dismissed the A2HS prompt');
            }
            installButton.style.display = 'none';
        });
    });
});
