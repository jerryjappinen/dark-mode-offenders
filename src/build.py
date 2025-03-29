# pylint: disable=missing-function-docstring
"""Build new README and data.json."""

import os
from utils import compose_output, build_files

apps_csv_path = os.path.join(os.path.dirname(__file__), "../apps.csv")
updates_csv_path = os.path.join(os.path.dirname(__file__), "../updates.csv")

json_path = os.path.join(os.path.dirname(__file__), "../data.json")
base_readme_path = os.path.join(os.path.dirname(__file__), "readme_base.md")
target_readme_path = os.path.join(os.path.dirname(__file__), "../README.md")

def compose():
    return compose_output(
        apps_csv_path,
        updates_csv_path,
        base_readme_path
    )

def build():
    return build_files(
        apps_csv_path,
        updates_csv_path,
        base_readme_path,
        json_path,
        target_readme_path
    )
