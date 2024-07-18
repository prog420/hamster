### Brain Rot & Hamster = ❤️

---

#### How To Use

1. Obtain **Bearer Token** for Hamster API.
   1. Launch Hamster via Web Telegram.
   2. Override script `clicker/hamstercombatgame.io/default<smth>.js` (check DevTools - `Sources` for Chrome).
   3. Find list of platforms (`[android", "android_x", "ios"]`) and change `android` to `weba`.
   4. Reload page (now you'll be able to play Hamster via Telegram Web).
   5. Go to Network page.
   6. Make some taps and find `taps` requests.
   7. Find headers with token.
2. And your `BEARER_TOKEN` to the Secrets (via Github repo settings or `.env`, whatever).
3. Launch main.py.
