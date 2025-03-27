# Dark Mode Offenders

Many apps and services do a great job with their light and dark mode support. This is a wall of shame for those that do not.

{ apps_output }

_* Fixed_

## Updates

{ updates_output }

## Contributing

Update `data.json` and leave a [pull request](https://github.com/jerryjappinen/dark-mode-offenders/pulls).

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
