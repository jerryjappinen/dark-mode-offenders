# pylint: disable=missing-function-docstring
"""Build new README and data.json."""

import os
from utils import build_files

apps_csv_path = os.path.join(os.path.dirname(__file__), "../apps.csv")
updates_csv_path = os.path.join(os.path.dirname(__file__), "../updates.csv")

json_path = os.path.join(os.path.dirname(__file__), "../data.json")
base_readme_path = os.path.join(os.path.dirname(__file__), "readme_base.md")
target_readme_path = os.path.join(os.path.dirname(__file__), "../README.md")

def build_all():
    build_files(
        apps_csv_path,
        updates_csv_path,
        json_path,
        base_readme_path,
        target_readme_path
    )

if __name__ == "__main__":
    print("\n" + "✔️ Generating new README...")
    build_all()
    print(f"✔️ README.md and data.json updated ({ os.path.normpath(target_readme_path)})" + "\n")
