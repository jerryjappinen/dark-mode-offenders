"""Configuration for validation and the README build script."""

# pylint: disable-next=invalid-name
csv_delimiter = ","

# pylint: disable-next=invalid-name
default_group = "General"

platforms = ["web", "mobile", "desktop"]

verdicts = {

    # Implemented correctly
    "done": "✅",

    # App not available on this platform
    "no_release": "-",

    # App is available on this platform, but dark and light theme support is unknown
    "unknown": "?",

    # No dark version available (always light)
    "no_dark_mode": "No dark mode",

    # No light version available (always dark)
    "no_light_mode": "No light mode",

    # Dark and light themes implemented, but must be manually set
    "no_os_sync": "Not synced with OS",

    # Dark and light themes respect OS setting, but do not update in real time
    "requires_refresh": "Requires page refresh",
    # "requires_refresh_multiple": "Requires multiple page refreshes",

    # Features are there, but they don't work correctly
    "buggy": "Buggy"
}
