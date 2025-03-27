# Dark Mode Offenders

Many apps and services do a great job with their light and dark mode support. This is a wall of shame for those that do not.

|App|Web|Mobile app|Desktop app|
|-|:-:|:-:|:-:|
|[Amazon](https://amazon.com)|No dark mode|No dark mode|-|
|[Amazon Prime Gaming](https://gaming.amazon.com/)|No light mode|-|No light mode|
|[Booking.com](https://booking.com/)|No dark mode|No dark mode|-|
|[CodeSandbox](https://codesandbox.io/)|No light mode|-|-|
|[Contentful](https://ontentful.com/)|No dark mode|-|-|
|[Deepnote](https://deepnote.com/)|No dark mode|-|-|
|eBay|No dark mode|✅|-|
|[Epic Games Store](https://store.epicgames.com/)|No light mode|-|No light mode|
|[GG.deals](https://deals.gg)|Not synced with OS|-|-|
|GameMaker editor|-|-|Not synced with OS|
|[Gmail](http://mail.google.com/)|Not synced with OS|✅|-|
|[Godot editor](https://godotengine.org/)|-|-|Not synced with OS|
|[GOG.com](https://gog.com)|No dark mode|-|No light mode|
|Google|Requires multiple page refreshes|✅|-|
|Google Docs|No dark mode|✅|-|
|[Google Gemini](https://gemini.google.com/app)|Requires page refresh|?|-|
|Google Maps|No dark mode|✅|-|
|Google Sheets|No dark mode|✅|-|
|Google Slides|No dark mode|✅|-|
|[Hacker News](http://news.ycombinator.com/)|No dark mode|-|-|
|[Hygraph](https://hygraph.com/)|No dark mode|-|-|
|[Marimo](https://marimo.io)|Buggy|-|-|
|~~[Microsoft Teams](https://teams.microsoft.com/)~~ *|✅|✅|✅|
|[Muzli](https://muz.li/)|Not synced with OS|-|-|
|MotherDuck|No dark mode|-|-|
|[Netflix](https://www.netflix.com/)|No light mode|No light mode|-|
|[Observable](https://observablehq.com)|No dark mode|-|-|
|[PayPal](https://www.paypal.com/de/home)|No dark mode|No dark mode|-|
|[Product Hunt](https://www.producthunt.com/notifications)|No dark mode|-|-|
|[Spline](https://spline.design/)|No light mode|-|-|
|[Spotify](https://spotify.com/) ([1](https://community.spotify.com/t5/Live-Ideas/All-Platforms-Light-Mode-option/idi-p/730341))|No light mode|No light mode|No light mode|
|[Steam](https://store.steampowered.com/)|No light mode|No light mode|No light mode|
|[Wolfram Alpha](https://www.wolframalpha.com/)|Requires page refresh|-|-|
|[Xbox](https://www.xbox.com/en-US/play)|No light mode|No light mode|No light mode|
|[YouTube](https://www.youtube.com/)|Requires page refresh|✅|-|
|[YouTube Music](https://www.youtube.com/)|No light mode|No light mode|-|

_* Fixed_

## Updates

- March 26, 2025: Teams (web) no longer requires a page refresh for the theme to update.

## Contributing

Leave a [pull request](https://github.com/jerryjappinen/dark-mode-offenders/pulls) with an update to this readme.

## Rules

Here's what you need for correct implementation of light and dark mode:

- **Light mode**: App must be available in light mode.
- **Dark mode**: App must be available in dark mode.
- **Sync with OS**: App must respect the _dark mode_ setting of the user’s OS or browser.
  - If this setting changes, the app must match its theme without user input.
  - Optionally allows users to force their preferred theme regardless of OS setting (as long as they have a way to change it back later).
  - Auto switch should be the default behavior for new users, even if other options are available.

#### Nice-to-haves

Additional nice-to-haves: manual theme selection, OLED mode, good greyscale experience, high-contrast support.

#### Operating systems

Operating systems should allow users to conveniently switch between light and dark mode, and optionally set the mode based on a schedule (such as sunrise/sunset). They should allow the wallpaper to be changed or adjusted based on which mode is in use. Unfortunately, there is still work to be done on this front.
