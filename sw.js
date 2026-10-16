// Service worker minimal: membuat BST OS bisa dipasang di HP/tablet. Selalu pakai jaringan agar data selalu terbaru.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", () => {});
