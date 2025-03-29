# pylint: disable=missing-function-docstring
"""Run unit tests on command line."""

import sys
from collections.abc import MutableMapping

from build import compose, build
from tests import test_all

# https://stackoverflow.com/questions/6027558/flatten-nested-dictionaries-compressing-keys
def flatten_dict(dictionary, parent_key='', separator='.'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

def main(command):
    if command == "build":
        print("\n" + "✔️ Generating files...")
        build()
        print("✔️ README.md and data.json updated" + "\n")

    elif command in ["print", "stats"]:
        _apps, _updates, stats, readme = compose()
        if command == "print":
            print(readme + "\n")
        if command == "stats":
            print("\n".join(map(lambda kv: f"{kv[0]}: {kv[1]}", flatten_dict(stats).items())))

    elif command == "test":
        print("\n" + "✔️ Running tests...")
        test_all()
        print("✔️ All tests passed" + "\n")

    else:
        print("Use one of the following commands: build, print, stats, test")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
