# Dark Mode Offenders

An updated list of apps and services that fail at dark and light theme support.

|App|Web|Mobile app|Desktop app|
|-|:-:|:-:|:-:|
|[Amazon](https://amazon.com)|No dark mode|No dark mode|-|
|[Amazon Prime Gaming](https://gaming.amazon.com/)|No light mode|-|No light mode|
|[Booking.com](https://booking.com/)|No dark mode|No dark mode|-|
|[CodeSandbox](https://codesandbox.io/)|No light mode|-|-|
|[Contentful](https://ontentful.com/)|No dark mode|-|-|
|[Deepnote](https://deepnote.com/)|No dark mode|-|-|
|[Epic Games Store](https://store.epicgames.com/)|No light mode|-|No light mode|
|[GG.deals](https://deals.gg)|Not synced with OS|-|-|
|GameMaker editor|-|-|Not synced with OS|
|[Gmail](http://mail.google.com/)|Not synced with OS|✅|-|
|[Godot editor](https://godotengine.org/)|-|-|Not synced with OS|
|[GOG.com](https://gog.com)|No dark mode|-|No light mode|
|Google|Requires page refresh|✅|-|
|Google Docs|No dark mode|✅|-|
|[Google Gemini](https://gemini.google.com/app)|Requires page refresh|?|-|
|Google Maps|No dark mode|✅|-|
|Google Sheets|No dark mode|✅|-|
|Google Slides|No dark mode|✅|-|
|[Hacker News](http://news.ycombinator.com/)|No dark mode|-|-|
|[Hygraph](https://hygraph.com/)|No dark mode|-|-|
|[Microsoft Teams](https://teams.microsoft.com/)|Requires page refresh|✅|✅|
|[Muzli](https://muz.li/)|Not synced with OS|-|-|
|[Netflix](https://www.netflix.com/)|No light mode|No light mode|-|
|[Observable](https://observablehq.com)|No dark mode|-|-|
|[PayPal](https://www.paypal.com/de/home)|No dark mode|No dark mode|-|
|[Product Hunt](https://www.producthunt.com/notifications)|No dark mode|-|-|
|[Spotify](https://spotify.com/) ([1](https://community.spotify.com/t5/Live-Ideas/All-Platforms-Light-Mode-option/idi-p/730341))|No light mode|No light mode|No light mode|
|[Steam](https://store.steampowered.com/)|No light mode|No light mode|No light mode|
|[Wolfram Alpha](https://www.wolframalpha.com/)|Requires page refresh|-|-|
|[Xbox](https://www.xbox.com/en-US/play)|No light mode|No light mode|No light mode|
|[YouTube](https://www.youtube.com/)|Not synced with OS|✅|-|
|[YouTube Music](https://www.youtube.com/)|No light mode|No light mode|-|

## Rules

Here's what you need for correct implementation of light and dark mode:

- **Light mode**: Your app must be available in light mode
- **Dark mode**: Your app must be available in dark mode
- **Auto switch**: Your app must respect the "dark mode" setting of the user's operating system or browser.
  - If this setting changes while your app is running, your app must match the theme without user input.
  - You can optionally provide a way for users to force their preferred team regardless of the OS setting, as long as they have a way to change it back later.
  - Auto switch should be the default behavior for new users, even if you have other options.

Additional nice-to-haves: manual theme selection, OLED mode, good greyscale experience, high-contrast support.

## Contributing

Leave a [pull request](https://github.com/jerryjappinen/dark-mode-offenders/pulls) with an update to this readme.
