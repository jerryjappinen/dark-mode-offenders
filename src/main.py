# pylint: disable=missing-function-docstring
"""Run unit tests on command line."""

import sys
from build import build_all
from tests import test_all

# To keep this running:
#   npx nodemon --exec python3 src/main.py test
def main(command):
    if command == "build":
        print("\n" + "✔️ Generating files...")
        build_all()
        print(f"✔️ README.md and data.json updated" + "\n")

    if command == "test":
        print("\n" + "✔️ Running tests...")
        test_all()
        print("✔️ All tests passed" + "\n")

    else:
        print("Use one of the following commands: build, test")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
