# Dark Mode Offenders

An updated list of services that fail at dark and light theme support.

|App|Web|Mobile app|Desktop app|
|-|:-:|:-:|:-:|
|[Amazon](https://amazon.com)|No dark mode|No dark mode|No dark mode|
|[Contentful](https://ontentful.com/)|No dark mode|-|-|
|[Hygraph](https://hygraph.com/)|No dark mode|-|-|
|[Deepnote](https://deepnote.com/)|No dark mode|-|-|
|[GG.deals](https://deals.gg)|Not synced to OS|-|-|
|[Microsoft Teams](https://teams.microsoft.com/)|Not synced to OS*|✅|✅|
|[Observable](https://observablehq.com)|No dark mode|-|-|
|[Spotify](https://spotify.com/) [[1](https://community.spotify.com/t5/Live-Ideas/All-Platforms-Light-Mode-option/idi-p/730341)]|No light mode|No light mode|No light mode|
|[YouTube](https://www.youtube.com/)|Not synced to OS|✅|-|
|[YouTube Music](https://www.youtube.com/)|No light mode|No light mode|-|


_(*) Requires manual page refresh_

## Rules

Here's what you need for correct implementation of light and dark mode:

- **Light mode**: Your app must be available in light mode
- **Dark mode**: Your app must be available in dark mode
- **Auto switch**: Your app must respect the "dark mode" setting of the user's operating system or browser. If this setting changes while your app is running, the theme must update to match without additional input.

Additional accessibility nice-to-haves: manual override setting, OLED mode, good greyscale experience, high-contrast support.

## Contributing

Leave a [pull request](https://github.com/jerryjappinen/dark-mode-offenders/pulls) with an update to this readme.
